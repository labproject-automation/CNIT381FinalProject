### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
### Utilities Libraries
import routers
import useless_skills as useless
import useful_skills as useful

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'namlab@webex.bot'
teams_token = 'ZmNkNDllYTEtZDBlZi00NGYyLWI5NzItNDdmNzI3M2MwZTc1ZTM0MDUyOTMtZmRj_P0A1_da087be3-a5c4-42e0-91c2-0fc6d3da3fdb'
bot_url = "https://02de-144-13-254-66.ngrok.io"
bot_app_name = 'Charles'

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm Charles, please let me prove to you that I can be useful.  ".format(
        sender.firstName
    )
    response.markdown += "\n\nSee what I can do with **/help**."
    return response
    
#RESTCONF skill
def sys_info(incoming_msg):
    """Return the system info
    """
    response = Response()
    info = useful.system_info_restconf(url_base, headers,device_username,device_password)

    if len(info) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the device system information I know. \n\n"
        response.markdown += "Device type: {}.\nSerial-number: {}.\nCPU Type:{}\n\nSoftware Version:{}\n" .format(
            info['device-inventory'][0]['hw-description'], info['device-inventory'][0]["serial-number"], 
            info['device-inventory'][4]["hw-description"],info['device-system-data']['software-version'])

    return response

# Netmiko skill demostrating show ip route on router to chatbot
def netmiko(incoming_msg):
    response = Response()
    response.markdown = "These are Branch routes"
    response.markdown += useful.showRouteNetmiko()
    return response
    
#ansible skill for show ip int br
def ansible_skill(incoming_msg):
    response = Response()
    response.markdown = "Here is the show ip int br command:\n"
    response.markdown += useful.ansibleskill()
    return response
    
#monitor
def monitor(incoming_msg):
        useful.monitorskill()
        
def isakmp(incoming_msg):
    response = Response()
    response.markdown = "These are the new VPN configurations on branch and HQ routers\n"
    response.markdown += useful.show_isakmp()
    return response

# Set the bot greeting.
bot.set_greeting(greeting)

# Add Bot's Commmands
bot.add_command("show ip route", "Look at the routes on Branch router with Netmiko", netmiko)
bot.add_command("show ip int br", "Show Interfaces with Ansible", ansible_skill)
bot.add_command("show sys info", "Show System Info with RESTCONF", sys_info)
bot.add_command("show monitor", "Starts monitor... check with show crypto isakmp policy", monitor)
bot.add_command("show crypto isakmp policy", "Check Isakmp Policy", isakmp)
# Every bot includes a default "/echo" command.  You can remove it, or any
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)

