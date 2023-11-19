import tkinter


def send():
    message = userMsg.get()
    userMsg.set("")
    messages.insert(tkinter.END,"User: "+message)


x = tkinter.Tk()
x.title("Chinese Teaching Chatbot")
messageWindow = tkinter.Frame(x)

userMsg = tkinter.StringVar()
scroll = tkinter.Scrollbar(messageWindow)

messages = tkinter.Listbox(messageWindow, height=20, width=60, yscrollcommand=scroll.set)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
messages.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages.pack()
messageWindow.pack()

inputbar = tkinter.Entry(x, width=60, textvariable=userMsg)
inputbar.bind("<Return>", send)
inputbar.pack()
sendButton = tkinter.Button(x, text="Send", command=send)
sendButton.pack()

tkinter.mainloop()