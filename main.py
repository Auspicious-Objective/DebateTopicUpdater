from bs4 import BeautifulSoup
import telebot
import requests
import datetime
import threading

token = ""
chatID = ""
link = "https://www.speechanddebate.org/topics/"
bot = telebot.TeleBot(token)


def getTopic(link):
    global topic
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    resolved_paragraph = paragraphs[9]
    topic = resolved_paragraph.text

def getMonth():
    global month
    month = datetime.datetime.now().strftime("%B")

def sendTopic(message):
    bot.send_message(chatID, message)

def main():
    topicThread = threading.Thread(target=getTopic(link=link,))
    topicThread.start()

    dateThread = threading.Thread(target=getMonth)
    dateThread.start()

    topicThread.join()
    dateThread.join()
    message = f'The public forum topic for the month of {month} is "{topic}".'
    sendTopic(message)

main()
