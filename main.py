import math
import tkinter
import jieba
import numpy
import tflearn
import tensorflow
import json
import startupProgram.startupProgram
import random


vocabulary = {
    "人": "people",
    "妈妈": "mother",
    "爸爸": "father",
    "老师": "teacher",
    "学生": "student",
    "水": "water",
    "茶": "tea",
    "米饭": "rice",
    "鸡蛋": "egg",
    "书": "book",
    "水果": "fruit",
    "苹果": "apple",
    "被子": "cup",
    "飞机": "plane",
    "猫": "cat",
    "狗": "dog",
    "天气": "weather",
    "中国": "China",
    "英国": "England",
    "家": "home",
    "学校": "school",
    "饭馆": "restaurant",
    "商店": "shop",
    "火车站": "train station",
    "住": "to live",
    "去": "to go",
    "喝": "to drink",
    "听": "to listen",
    "读": "to read",
    "热": "hot",
    "冷": "cold",
    "吃": "to eat",
    "你好": "hello"
}

incorrect_vocabulary = list()


def quiz():
    for j in range(5):
        global button
        chinese_q = random.choice(list(vocabulary.keys()))
        english_a = vocabulary[chinese_q]
        fake_answer1 = vocabulary[random.choice(list(vocabulary.keys()))]
        fake_answer2 = vocabulary[random.choice(list(vocabulary.keys()))]

        while fake_answer1 == english_a or fake_answer2 == english_a or fake_answer1 == fake_answer2:
            fake_answer1 = vocabulary[random.choice(list(vocabulary.keys()))]
            fake_answer2 = vocabulary[random.choice(list(vocabulary.keys()))]

        messages.insert(tkinter.END, "Chatbot: " + f"What is the correct translation of {chinese_q}?")
        # print(f"What is the correct translation of {chinese_q}?")
        answers = random.sample([english_a, fake_answer1, fake_answer2], k=3)

        for i, x in enumerate(answers):
            messages.insert(tkinter.END, "Chatbot: " + f"{i + 1}. {x}")
            # print(f"{i+1}. {x}")

        messages.insert(tkinter.END, "Chatbot: " + "Please enter the number of the correct answer")
        messages.see(tkinter.END)

        global message
        # button = False
        sendButton.wait_variable(button)
        # sendButton.wait_variable(button)
        # while not button:
        #     x = 0
            # user_answer = int(input("Please enter the number of the correct answer: "))
        user_answer = int(message)
        user_answer = answers[int(user_answer - 1)]

        if user_answer == english_a:
            messages.insert(tkinter.END, "Chatbot: " + "Correct answer!")
            # print("Correct answer!")
        else:
            messages.insert(tkinter.END, "Chatbot: " + f"Incorrect. The correct answer is \"{english_a}\"")
            # print(f"Incorrect. The correct answer is \"{english_a}\"")
            incorrect_vocabulary.append(chinese_q)

    if len(incorrect_vocabulary) == 0:
        incorrect_vocabulary.append(chinese_q)

    #    print(incorrect_vocabulary)
    return random.choice(incorrect_vocabulary)


words = []
labels = []
training_words = []
training_tags = []

with open("intents.json", encoding='utf-8') as file:
    data = json.load(file)


def setup():
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            words_tokenised = list(jieba.cut(pattern))
            words.extend(words_tokenised)
            training_words.append(words_tokenised)
            training_tags.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(training_words):
        bag = []

        for w in words:
            if w in doc:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(training_tags[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    tensorflow.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)

    model.save("model.tflearn")

    return model


# PREDICTIONS


def bag_of_words(user_input, words):
    bag = [0 for _ in range(len(words))]
    s_words = list(jieba.cut(user_input))

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def chat():
    model = setup()
    initial_prompt(model)
    while True:
        sendButton.wait_variable(button)
        inp = message
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.7:

            for tag_ in data["intents"]:
                if tag_["tag"] == tag:
                    responses = tag_["responses"]

            # return random.choice(responses)
            messages.insert(tkinter.END, "Chatbot: " + random.choice(responses))
            messages.see(tkinter.END)
            # print(random.choice(responses))

        else:
            # return "我不懂。"
            messages.insert(tkinter.END, "Chatbot: " + "我不懂。")
            messages.see(tkinter.END)
            # print("我不懂。")


def initial_prompt(model):
    inp = quiz()
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tag_ in data["intents"]:
        if tag_["tag"] == tag:
            responses = tag_["responses"]

    # print(random.choice(responses))
    messages.insert(tkinter.END, "Chatbot: " + random.choice(responses))


def add_newline(message):
    lineLength = 55
    num_of_loops = math.ceil(len(message) / lineLength) + 1
    for i in range(1, num_of_loops):
        upper_bound = i * lineLength
        lower_bound = (i - 1) * lineLength
        messages.insert(tkinter.END, "User: " + message[lower_bound:upper_bound])


def send(event=None):
    global z
    global button
    global message
    button.set(not button)
    message = userMsg.get()
    if len(message) > 55:
        add_newline(message)
    else:
        messages.insert(tkinter.END, "User: " + message)
    if z % 15 == 0:
        userMsg.set("")
        z += 1
        chat()
    if z > 1:
        userMsg.set("")
        z += 1
    if z == 1:
        messages.insert(tkinter.END, startupProgram.startupProgram.Startup(message))
        userMsg.set("")
        z += 1
        chat()
    messages.see(tkinter.END)


def startupGUI():
    messages.insert(tkinter.END,
                    "Chatbot: Hi. I am a Chinese teaching chatbot. Before we can begin, I need to know your level.",
                    "Chatbot: Please type up to 5 sentences in Chinese. 谢谢!\n")


global message
z = 0
x = tkinter.Tk()
x.title("Chinese Teaching Chatbot")
messageWindow = tkinter.Frame(x)

button = tkinter.BooleanVar()
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
