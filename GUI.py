# import math
# import tkinter
#
# import startupProgram.startupProgram
# import chatbot
#
#
# def add_newline(message):
#     lineLength = 55
#     num_of_loops = math.ceil(len(message)/lineLength)+1
#     for i in range(1, num_of_loops):
#         upper_bound = i*lineLength
#         lower_bound = (i-1)*lineLength
#         messages.insert(tkinter.END, "User: " + message[lower_bound:upper_bound])
#
#
# def send(event=None):
#     global z
#     message = userMsg.get()
#     if len(message) > 55:
#         add_newline(message)
#     else:
#         messages.insert(tkinter.END, "User: " + message)
#     if z == 2:
#
#         # messages.insert(tkinter.END, "Chatbot: " + chatbot.chat(message))
#         chatbot.chat(message)
#         userMsg.set("")
#     if z == 1:
#         messages.insert(tkinter.END, startupProgram.startupProgram.Startup(message))
#         userMsg.set("")
#         z += 1
#
#
# def startupGUI():
#     messages.insert(tkinter.END,
#                     "Chatbot: Hi. I am a Chinese teaching chatbot. Before we can begin, I need to know your level.",
#                     "Chatbot: Please type up to 10 sentences in Chinese. 谢谢!\n")
#
#
# z = 0
# x = tkinter.Tk()
# x.title("Chinese Teaching Chatbot")
# messageWindow = tkinter.Frame(x)
#
# userMsg = tkinter.StringVar()
# scroll = tkinter.Scrollbar(messageWindow)
# scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# messages = tkinter.Listbox(messageWindow, height=40, width=120, yscrollcommand=scroll.set)
# messages.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# messages.pack()
# messageWindow.pack()
# userMsg.set("")
#
# z = z + 1
#
# inputbar = tkinter.Entry(x, width=120, textvariable=userMsg)
# inputbar.bind("<Return>", send)
# inputbar.pack()
# sendButton = tkinter.Button(x, text="Send", command=send)
# sendButton.pack()
#
#
# startupGUI()
#
# tkinter.mainloop()
