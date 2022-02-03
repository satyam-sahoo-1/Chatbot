from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")

convo=[
    'hello',
    'hi there !',
    'what is your name',
    'my name is Bot, I am created by satyam',
    'how are you',
    'I am fine',
    'where do you live',
    'I live in lukhnau',
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

print("Talk to bot")
while True:
    query = input()
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("bot : ", answer)