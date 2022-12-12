# CNIT381FinalProject
For This project we will be building a Webex automated Chatbox that will communicate with our two routers (CSR1000v).
For our Netmiko skill we will have the Chatbox show ip route and show crypto isakmp policy
For our RESCONF skill we will have the Chatbox show system info
For our Ansible skill we will have the Chatbox show ip int br

## Setup Instructions 
### Step 1
You will need to install these packages before we begin
```
sudo snap install ngrok 
pip3 install webexteamssdk 
pip3 install webexteamsbot 
```
### Step 2
Now to create an account for the bot to use. Go to https://developer.webex.com and either login or create an account. After logging in click on "Start Building Apps" then on the next page click on "Create a Bot." Here you will fill out the following info: Bot name, Bot username, select/upload an Icon, App Hub Description. Then click Add Bot at the bottom of the page after filling it all out.

### Step 3
You will now want to save the Bot Access Token in a text file, you will need this for a later step. Here is an example what it'll look like.

![image](https://user-images.githubusercontent.com/119529085/206284448-687ca637-011f-4b89-980c-bbb223e49044.png)

### Step 4
Download The following: 381Bot.py, useful_skils.py, useless_skills.py, myparamiko.py, inventory.txt, ansible.cfg and routers.py to a folder directory on your machine. For the program to run successfully on the machine you are running the program make sure you have python 3.8.15 or later installed. 
For the two routers (HQ and Branch) you will follow the configuration listed in CSR1.txt and CSR2.txt, this will create the VPN connection. (Note that CSR1 is HQ router)

### Step 5
Open a terminal and enter the following command:
```
 ngrok http 5000
 ```
This will create a connection so Webex and python can communicate to each other. Once it's run you will want to copy the forwarding address so you can paste it in the 381bot.py file. Do not close the terminal or end the process, this would cause the bot to no longer work. Here is an example of what the forwarding address will look like.
 
![image](https://user-images.githubusercontent.com/119529085/206284569-bf45715b-7d63-489c-801e-229096fc6f7b.png)

 ### Step 6
 Now open 381bot.py in a text editor, you will change the bot_email, teams_token, bot_url and the bot_app_name. For the bot_email you will change this to the email address that was assigned to your bot when you made it in the Webex developer page, it should end with a @webex.bot address. With the teams_token you will be using the token you got after creating the box. The bot_url will be the forwarding address you just got by running the ngrok http 5000 command. And lastly, you will Change the bot_app_name to what you named the bot while creating it.
 
![image](https://user-images.githubusercontent.com/119529085/206804500-65fc7bb1-cfd4-4211-9280-1e6a552854e1.png)

### Step 7
Make sure the router addresses are the same as the addresses used in our python files. You may need to change the ip addresses in the routers.py, inventory.txt, and useful_skills.py. This will all depend on what addresses your routers have obtained. 

### Step 8
Finally, make sure you have saved all relevant files and run the 381Bot.py on a terminal, follow the command below to run it. The bot should now be running, now go to https://teams.webex.com and message the bot, you should receive a reply.
```
 python3 381bot.py
 ```

## Congrats you are now done!!! 
You should now be able to successfully be able to talk with the bot. If you followed our code, it should look like the picture below.

![image](https://user-images.githubusercontent.com/119529085/206818715-eed42d0d-46a3-4dff-8fc6-8c4a5ab50014.png)


 

