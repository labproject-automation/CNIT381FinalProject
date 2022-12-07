# CNIT381FinalProject
For This project we will be building a Webex automated Chatbox that will communicate with our two routers (CSR1000v). 

## Setup
### Step 1
You will need to install these packages before we begin
```
sudo snap install ngrok 
pip3 install webexteamssdk 
pip3 install webexteamsbot 
```
### Step 2
Now to create an account for the bot to use. Go to https://developer.webex.com and either login or create an account. After logining in click on "Start Building Apps" then on the next page click on "Create a Bot." Here you will fill out the following info: Bot name, Bot username, select/upload an Icon, App Hub Description. Then click Add Bot at the bottom of the page after filling it all out.

### Step 3
You will now want to save the Bot Access Token in a text file, you will need this for a later step. Here is an example what what it'll look like.

![image](https://user-images.githubusercontent.com/119529085/206284448-687ca637-011f-4b89-980c-bbb223e49044.png)

### Step 4
Download The following: 381Bot.py, BotSkills.py, ansible.cfg, inventory.txt, and routers.py to a folder directory on your machine. For the program to run successfully on the machine you are running the program make sure you have python 3.8.15 or later installed. 
For the two routers (HQ and Branch) you will follow the configuration listed in CSR1.txt and CSR2.txt, this will create the VPN connection. (Note that CSR1 is HQ router)

### Step 5
Open a terminal and enter the following command:
```
 ngrok http 5000
 ```
This will create a connection so Webex and python can communicate to each other. Once it's run you will want to copy the forwarding address so you can paste it in the 381bot.py file. Do not close the terminal or end the process, this would cause the bot to no longer work. Here is an example of what the forwarding address will look like.
 
![image](https://user-images.githubusercontent.com/119529085/206284569-bf45715b-7d63-489c-801e-229096fc6f7b.png)

 ### Step 6
 

 

