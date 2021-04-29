#Minecraft server start script with discord notify
#Author: John Yorke

#imports
import subprocess
import requests
import json
from discord import Webhook, RequestsWebhookAdapter
from datetime import datetime

#load config
with open("run.json", "r") as file:
    config = json.load(file)

jar = config["server_jar"]
args = config["jvm_args"]
url = config["webhook_url"]
role = config["role_id"]

#get webhook
webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

#sends the server online message to the discord channel
def sendUpMessage():
    time = datetime.now().strftime("(%Y-%m-%d @ %H:%M:%S)")
    webhook.send(role + " Server is now online " + time)

#sends the server offline message to the discord channel
def sendDownMessage():
    time = datetime.now().strftime("(%Y-%m-%d @ %H:%M:%S)")
    webhook.send(role + " Server is now offline " + time)

#send a server online message and start the server
sendUpMessage()
subprocess.call("java " + args + " -jar " + jar + " nogui")
#after the server is stopped, send a server offline message
sendDownMessage()
#pause
input("\nPress any key to continue...")
