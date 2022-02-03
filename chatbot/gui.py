import tkinter
from tkinter import *
from PIL import ImageTk, Image






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