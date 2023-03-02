# # import telebot

# # bot = telebot.TeleBot('1929975195:AAH7CcZxBFrs4SxYNqAQ60_0uNTszPUg9JQ')

# # @bot.message_handler(commands='start')
# # def menu_principal(message):
# #     markup = telebot.types.InlineKeyboardMarkup()
# #     markup.add(telebot.types.InlineKeyboardButton('Opção 1', callback_data='1'))
# #     markup.add(telebot.types.InlineKeyboardButton('Opção 2', callback_data='2'))
# #     markup.add(telebot.types.InlineKeyboardButton('Opção 3', callback_data='3'))
# #     bot.send_message(message.chat.id, 'Menu principal:', reply_markup=markup)

# # def submenu_1(message):
# #     markup = telebot.types.InlineKeyboardMarkup()
# #     markup.add(telebot.types.InlineKeyboardButton('Subopção 1.1', callback_data='1.1'))
# #     markup.add(telebot.types.InlineKeyboardButton('Subopção 1.2', callback_data='1.2'))
# #     markup.add(telebot.types.InlineKeyboardButton('Voltar', callback_data='voltar'))
# #     bot.send_message(message.chat.id, 'Submenu 1:', reply_markup=markup)

# # @bot.callback_query_handler(func=lambda call: True)
# # def callback_query(call):
# #     if call.data == '1':
# #         submenu_1(call.message)
# #     elif call.data == 'voltar':
# #         menu_principal(call.message)

# # bot.polling()

# import telebot

# bot = telebot.TeleBot('1929975195:AAH7CcZxBFrs4SxYNqAQ60_0uNTszPUg9JQ')

# @bot.message_handler(commands='start')
# def menu_principal(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.row(telebot.types.InlineKeyboardButton('Botão 1', callback_data='1'),
#             telebot.types.InlineKeyboardButton('Botão 2', callback_data='2'))
#     markup.row(telebot.types.InlineKeyboardButton('Botão 3', callback_data='3'),
#             telebot.types.InlineKeyboardButton('Botão 4', callback_data='4'))
#     bot.send_message(message.chat.id, 'Escolha um botão:', reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == '1':
#         bot.send_message(call.message.chat.id, 'Você escolheu o botão 1')
#     elif call.data == '2':
#         bot.send_message(call.message.chat.id, 'Você escolheu o botão 2')
#     elif call.data == '3':
#         bot.send_message(call.message.chat.id, 'Você escolheu o botão 3')
#     elif call.data == '4':
#         bot.send_message(call.message.chat.id, 'Você escolheu o botão 4')

# bot.polling()

import telebot

bot = telebot.TeleBot('1929975195:AAH7CcZxBFrs4SxYNqAQ60_0uNTszPUg9JQ')

@bot.message_handler(commands='formulario')
def formulario(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Enviar formulário', callback_data='formulario'))
    bot.send_message(message.chat.id, 'Por favor, preencha o formulário:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'formulario':
        bot.send_message(call.message.chat.id, 'Nome:')
        bot.register_next_step_handler(call.message, processar_nome)

def processar_nome(message):
    nome = message.text
    bot.send_message(message.chat.id, 'Endereço:')
    bot.register_next_step_handler(message, processar_endereco)

def processar_endereco(message):
    endereco = message.text
    bot.send_message(message.chat.id, 'Obrigado pelo seu tempo, o formulário foi enviado com sucesso!')

bot.polling()
