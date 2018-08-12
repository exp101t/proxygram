import telebot, config, flask, os

bot    = telebot.TeleBot(config.token)
server = flask.Flask(__name__)

@server.route("/" + config.token, methods = ['POST'])
def getUpdates():
    bot.process_new_updates([
        telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))
    ])
    return "!", 200

if __name__ == '__main__':
    # Trick to change base_url default value
    telebot.apihelper._make_request.__defaults__ = ('get', None, None, config.proxy)
    
    # Setting webhook to our proxy
    bot.remove_webhook()
    bot.set_webhook(url = config.proxy.format(config.token, ''))
    
    # And starting server
    server.run(host = "0.0.0.0", port = os.environ.get('PORT', 5000))