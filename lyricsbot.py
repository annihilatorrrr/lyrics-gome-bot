from config import bot_token, genius_token
import telebot
from telebot import types
from telebot import util
from lyricsgenius import Genius

bot = telebot.TeleBot(bot_token)
genius = Genius(genius_token)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    start = types.ReplyKeyboardRemove('start')
    username = message.from_user.username
    name = message.from_user.first_name
    
    if username != None:
        bot.send_message(message.chat.id, f"Hello, {username}.\n\nI'm a lyrics finder bot.\nSend the song name and I'll try my best to find the song lyrics for you!", reply_markup=start)
    else:
        bot.send_message(message.chat.id, f"Hello, {name}.\n\nI'm a lyrics finder bot.\nSend the song name and I'll try my best to find the song lyrics for you!", reply_markup=start)

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    start = types.ReplyKeyboardRemove('help')
    bot.send_message(message.chat.id, 'Click /start to activate the bot. If you write the name of the song or the name of the artist, you can see the lyrics of the song.\n\nYou can also support the developer by clicking /donate.')

@bot.message_handler(commands=['donate'])
def handle_start_help(message):
    start = types.ReplyKeyboardRemove('donate')
    bot.send_message(message.chat.id, 'You can send any amount through the payment system: \n\n' + '<a href="https://yoomoney.ru/to/4100116813383560">ЮMoney</a>', parse_mode='html')

@bot.message_handler(content_types=['text'])
def songs_text(message):
    search_songs = genius.search_songs(message.text)
    markup = types.InlineKeyboardMarkup(row_width=1)

    for item in search_songs['hits']:
        result = item['result']['title']
        name = item['result']['primary_artist']['name']
        result_id = item['result']['id']
        i = types.InlineKeyboardButton(result + ' - ' + name, callback_data=result_id)
        markup.add(i)

    bot.send_message(message.chat.id, 'Please select a song:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == call.message.json['reply_markup']['inline_keyboard'][0][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][0][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][1][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][1][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][2][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][2][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][3][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][3][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][4][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][4][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][5][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][5][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][6][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][6][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][7][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][7][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][8][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][8][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
        elif call.data == call.message.json['reply_markup']['inline_keyboard'][9][0]['callback_data']:
            text_song = genius.song(call.message.json['reply_markup']['inline_keyboard'][9][0]['callback_data'])
            lyrics_title = text_song['song']['title']
            lyrics_name = text_song['song']['primary_artist']['name']
            lyrics_image = text_song['song']['header_image_url']
            search_song = genius.search_song( lyrics_title + lyrics_name)
            text = search_song.lyrics
            text_output = '<b>Title:</b> ' + text_song['song']['full_title'] + '\n' + '<b>Artist:</b> ' + lyrics_name + '\n'
            bot.send_photo(call.message.chat.id, lyrics_image, text_output, parse_mode='html')
            splitted_text = util.split_string(text, 4000)
            for text in splitted_text:
                bot.send_message(call.message.chat.id, text)
            pass
               
bot.polling(timeout=60, long_polling_timeout=60)