import telebot
import ctypes
import os

bot = telebot.TeleBot('Token from @BotFather')
main_user = 'Username without @'
#telebot.apihelper.proxy = {'Proxy'}

@bot.message_handler(content_types=['text'])
def commands(message):
    if message.from_user.username == main_user:
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('LOCK', 'SIGN OUT')
        user_markup.row('SLEEP')
        user_markup.row('SHUTDOWN')
        user_markup.row('RESTART')
        bot.send_message(message.from_user.id, 'Select command:', reply_markup = user_markup)
        if (message.text == 'LOCK'):
            ctypes.windll.user32.LockWorkStation()
        if (message.text == 'SIGN OUT'):
            os.system("shutdown -l")
        elif (message.text == 'SLEEP'):
            os.system("shutdown /h")
        elif (message.text == 'SHUTDOWN'):
            os.system("shutdown /s")
        elif (message.text == 'RESTART'):
            os.system("shutdown /r")

if __name__ == '__main__':
     bot.polling(none_stop=True)