#https://www.bing.com/videos/riverview/relatedvideo?q=how%20to%20make%20ai%20chatbot%20in%20python%20that%20speaks%20chinese&mid=FDD1713E3F89FD8007CDFDD1713E3F89FD8007CD&ajaxhist=0
import jieba
import numpy
import tflearn
import tensorflow
import random
import json

words = []
labels = []
training_words = []
training_tags = []

with open("intents.json",  encoding='utf-8') as file:
    data = json.load(file)

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

net = tflearn.input_data(shape=[None,len(training[0])])
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]),activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000,batch_size=8,show_metric=True)

model.save("model.tflearn")

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
    while True:
        inp = input("YOU: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.7:

            for tag_ in data["intents"]:
                if tag_["tag"] == tag:
                    responses = tag_["responses"]

            print(random.choice(responses))

        else:
            print("我不懂。")

def initial_prompt():
    inp = input("INITIAL INPUT")  # replace with a quiz input of what the user got incorrect

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]


    for tag_ in data["intents"]:
        if tag_["tag"] == tag:
            responses = tag_["responses"]

    print(random.choice(responses))


initial_prompt()
chat()