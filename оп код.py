import telebot
from telebot import types
import random
ALL_p = {}

with open('token.txt', 'r') as file:
    token = file.read()
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["fight"])
def repeat_all_messages(message):
    #print(bot.get_chat(message.chat_id))
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Ударить в голову🙍‍♂️", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Ударить в ногу🦵", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Ударить в руку🤚", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="Ударить в тело👕", callback_data="button4")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)

    bot.send_message(message.chat.id, "Выберите куда бить!", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ALL_p
    if call.message:
        defense = random.randint(1, 4)
        if call.data == "button1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            if defense == 1:
                bot.send_message(call.message.chat.id, "Попадание в блок.")
                ALL_p[call.message.chat.id][1] -= ALL_p[call.message.chat.id][1]
                
            else:
                bot.send_message(call.message.chat.id, "Попадание в голову.")
                ALL_p[call.message.chat.id][1] += 0.5
                ALL_p[call.message.chat.id][3] += ALL_p[call.message.chat.id][0]
                if (ALL_p[call.message.chat.id][3] >= ALL_p[call.message.chat.id][4]):
                    bot.send_message(call.message.chat.id, "Победа.")
                    ALL_p[call.message.chat.id][0] += ALL_p[call.message.chat.id][2]
                    ALL_p[call.message.chat.id][3] = 0  
        if call.data == "button2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            if defense == 2:
                bot.send_message(call.message.chat.id, "Попадание в блок.")
                ALL_p[call.message.chat.id][1] -= 3
            else:
                bot.send_message(call.message.chat.id, "Попадание в ногу.")
                ALL_p[call.message.chat.id][1] += 0.5
                ALL_p[call.message.chat.id][3] += ALL_p[call.message.chat.id][0]
                if (ALL_p[call.message.chat.id][3] >= ALL_p[call.message.chat.id][4]):
                    bot.send_message(call.message.chat.id, "Победа.")
                    ALL_p[call.message.chat.id][0] += ALL_p[call.message.chat.id][2]
                    ALL_p[call.message.chat.id][3] = 0
                    ALL_p[call.message.chat.id][1] = 10
        if call.data == "button3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            if defense == 3:
                bot.send_message(call.message.chat.id, "Попадание в блок.")
                ALL_p[call.message.chat.id][1] -= 3
            else:
                bot.send_message(call.message.chat.id, "Попадание в руку.")
                ALL_p[call.message.chat.id][1] += 0.5
                ALL_p[call.message.chat.id][3] += ALL_p[call.message.chat.id][0]
                if (ALL_p[call.message.chat.id][3] >= ALL_p[call.message.chat.id][4]):
                    bot.send_message(call.message.chat.id, "Победа.")
                    ALL_p[call.message.chat.id][0] += ALL_p[call.message.chat.id][2]
                    ALL_p[call.message.chat.id][3] = 0
                    ALL_p[call.message.chat.id][1] = 10
        if call.data == "button4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            if defense == 4:
                bot.send_message(call.message.chat.id, "Попадание в блок.")
                ALL_p[call.message.chat.id][1] -= 3
            else:
                bot.send_message(call.message.chat.id, "Попадание в тело.")
                ALL_p[call.message.chat.id][1] += 0.5
                ALL_p[call.message.chat.id][3] += ALL_p[call.message.chat.id][0]
                if (ALL_p[call.message.chat.id][3] >= ALL_p[call.message.chat.id][4]):
                    bot.send_message(call.message.chat.id, "Победа.")
                    ALL_p[call.message.chat.id][0] += ALL_p[call.message.chat.id][2]
                    ALL_p[call.message.chat.id][3] = 0
                    ALL_p[call.message.chat.id][0] = 10
        if (ALL_p[call.message.chat.id][1] <= 0):
            bot.send_message(call.message.chat.id, "Ты умер")
            ALL_p[call.message.chat.id][0] -= 1
            ALL_p[call.message.chat.id][1] = 10
        bot.send_message(call.message.chat.id, 'У тебя ' + str(ALL_p[call.message.chat.id][1]) + ' ХП')
        repeat_all_messages(call.message)

@bot.message_handler(commands=["fl1"])
def lvl(message):
    global ALL_p
    ALL_p[message.chat.id][4] = 10
@bot.message_handler(commands=["fl2"])
def lvl(message):
    global ALL_p
    ALL_p[message.chat.id][2] = 5
    ALL_p[message.chat.id][4] = 50
    
@bot.message_handler(commands=["fl3"])
def lvl(message):
    global ALL_p 
    ALL_p[message.chat.id][2] = 10
    ALL_p[message.chat.id][4] = 100
@bot.message_handler(commands=["fl4"])
def lvl(message):
    global ALL_p
    ALL_p[message.chat.id][2] = 100
    ALL_p[message.chat.id][4] = 10000
@bot.message_handler(commands=["HPboss"])
def HPboss(message):
    global ALL_p
    bot.send_message(message.chat.id, 'У босса осталось ' + str(ALL_p[message.chat.id][4] - ALL_p[message.chat.id][3]) + ' ХП')    


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Это бот война, здейсь ты можешь биться с боссами и увеличивать силу.\nЧтобы начать бой напиши - /fight.\nЧтобы узнать своё здоровье напиши - /HP\nЧтобы узнать свой урон напиши - /damage\nИспользуй /fl[от 1 до 4], чтобы установить здоровье босса. 1 - 10, 2-50, 3-100, 4-10000\nЧтобы узнать здоровье босса напиши - /HPboss ")
@bot.message_handler(commands=["start"])
def start(message):
    global ALL_p
    ALL_p[message.chat.id] = [0, 0, 0, 0, 0]
    ALL_p[message.chat.id][0] = 1
    ALL_p[message.chat.id][1] = 10
    ALL_p[message.chat.id][2] = 1
    ALL_p[message.chat.id][3] = 0
    ALL_p[message.chat.id][4] = 10
    bot.send_message(message.chat.id, "Если хочешь узнать больше напиши - /help")    
@bot.message_handler(commands=["HP"])
def HP(message):
    global ALL_p
    bot.send_message(message.chat.id, 'У тебя ' + str(ALL_p[message.chat.id][1]) + ' ХП')
@bot.message_handler(commands=["damage"])
def damage(message):
    global ALL_p
    bot.send_message(message.chat.id,'У тебя '+ str(ALL_p[message.chat.id][0])+' урона')
bot.polling(none_stop=True)
