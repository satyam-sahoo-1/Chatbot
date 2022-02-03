import tkinter
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image
import ChatTrainer

bot = ChatBot("My Bot")

# convo=[
#     'hello',
#     'hi there !',
#     'what is your name',
#     'my name is Bot, I am created by satyam',
#     'how are you',
#     'I am fine',
#     'where do you live',
#     'I live in lukhnau',
# ]

convo = ChatTrainer.convo

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)


main = Tk()

main.geometry("500x650")

main.title("MY CHAT BOT")
img = Image.open("xub.png")
# img = PhotoImage(file ="xub.png")
img = img.resize((100, 100), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)

photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0, END)



frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

#creating text field

textF=Entry(main, font = ("verdena", 20))
textF.pack(fill=X, pady=1)

#button
btn = Button(main, text = "Ask from Bot", font=("Verdena",20), command = ask_from_bot)
btn.pack()


main.mainloop()