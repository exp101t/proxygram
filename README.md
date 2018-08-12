# Proxygram – Pseudo-proxy for pyTelegramBotApi
## Installing proxy
Proxy is optimised for Heroku. So:
1. Edit `servers.json` (add your tokens, server IPs and ports with bots)
2. Create repository in Proxy folder
```
$ git init
```
3. Log in Heroku and create app
```
$ heroku login
$ heroku create <app_name>
```
4. Push the project
```
$ git add *
$ git commit -m 'First commit'
$ git push heroku master
```
## Starting the bot
1. Edit `config.py` (add your token and proxy IP)
2. Write and start your bot
