# Minecraft Server Discord Hook
Notify a Discord Server when you start or stop your Minecraft Server.

# Installation
* Download the latest release and extract all files into your Minecraft Server directory.

# Configuration
* Create a webhook to your desired Discord Server chat channel in `Server Settings > Integrations > Webhooks > New Webhook` and copy its URL for configuration.
* Obtain the role ID of the role you would like to \@mention when the server is notified by typing `\@<your_role_here>` in any chat channel.

In `run.json`
```
{
  "server_jar":"server.jar",
  "jvm_args":"-Xms1G -Xmx4G",
  "webhook_url":"your_url_here",
  "role_id":"your_role_here"
}
```
* Modify `server_jar` with the name of your Minecraft Server jar file.
* Modify `jvm_args` with your desired Java Runtime Environment arguments.
* Modify `webhook_url` with the URL to your Discord Server webhook.
* Modify `role_id` with the ID of the role you would like to \@mention.

# Starting and stopping your server
* Start your server by opening `run.bat`. Your Discord Server will receive an online notification.
* Stop your server by typing `stop` in the console. Your Discord Server will receive an offline notification.
