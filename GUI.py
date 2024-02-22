import math
import tkinter

import startupProgram.startupProgram


def add_newline(message):
    num_of_loops = math.ceil(len(message)/70)+1
    for i in range(1, num_of_loops):
        upper_bound = i*70
        lower_bound = (i-1)*70
        messages.insert(tkinter.END, "User: " + message[lower_bound:upper_bound])

def send(event=None):
    message = userMsg.get()
    if len(message) > 70:
        add_newline(message)
    else:
        messages.insert(tkinter.END, "User: " + message)
    if z == 1:
        messages.insert(tkinter.END, startupProgram.startupProgram.Startup(message))
        userMsg.set("")
    # message = userMsg.get()
    # messages.insert(tkinter.END, "User: " + message)
    # if z == 1:
    #     messages.insert(tkinter.END, startupProgram.startupProgram.Startup(message))
    # userMsg.set("")


def startupGUI():
    messages.insert(tkinter.END,
                    "Chatbot: Hi. I am a Chinese teaching chatbot. Before we can begin any lessons, I need to know your level.",
                    "Chatbot: Please type up to 10 sentences in Chinese. When typing, please separate words with spaces. 谢谢!\n")


z = 0
x = tkinter.Tk()
x.title("Chinese Teaching Chatbot")
messageWindow = tkinter.Frame(x)

userMsg = tkinter.StringVar()
scroll = tkinter.Scrollbar(messageWindow)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
messages = tkinter.Listbox(messageWindow, height=40, width=120, yscrollcommand=scroll.set)
messages.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages.pack()
messageWindow.pack()
userMsg.set("")

z = z + 1

inputbar = tkinter.Entry(x, width=120, textvariable=userMsg)
inputbar.bind("<Return>", send)
inputbar.pack()
sendButton = tkinter.Button(x, text="Send", command=send)
sendButton.pack()


startupGUI()

tkinter.mainloop()
