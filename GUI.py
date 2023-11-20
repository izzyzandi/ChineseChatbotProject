import tkinter

import startupProgram.startupProgram


def send(event=None):
    message = userMsg.get()
    messages.insert(tkinter.END, "User: " + message)
    if z == 1:
        messages.insert(tkinter.END, startupProgram.startupProgram.Startup(message))
    userMsg.set("")


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
