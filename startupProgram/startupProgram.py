import jieba


def NumberOfSyllables(text):
    counter = 0
    for c in text:
        if c != '!' and c != '.' and c != '?' and c != '。' and c != '，' and c != ',':
        #    if ord(c) > 123:
                counter = counter + 1
    return counter


def NumberOfSentences(text):
    counter = 0
    for c in text:
        if c == '!' or c == '.' or c == '?' or c == '。':
            counter = counter + 1
    return counter


def FleschKincaidScoreCalculation(numberOfSyllables, numberOfWords, numberOfSentences):
    return 206.835 - 1.015 * (numberOfWords / numberOfSentences) - 84.6 * (numberOfSyllables / numberOfWords)


def NumberOfWords(text):
    counter = 0
    text = list(jieba.cut(text))
    for c in text:
        if c != '!' and c != '.' and c != '?' and c != '。' and c != ',' and c != '，':
            counter = counter + 1
    return counter


def Startup(text):
#    print(
#        "Hi. I am a Chinese teaching chatbot. Before we can begin any lessons, I need to know your level.\nPlease type"
#        "up to 10 sentences in Chinese. When typing, please separate words with spaces. 谢谢!\n")

#    text = input()
    r = FleschKincaidScoreCalculation(NumberOfSyllables(text), NumberOfWords(text), NumberOfSentences(text))

    # x = NumberOfWords(text)
    # y = NumberOfSentences(text)
    # z = NumberOfSyllables(text)
    # print(x)
    # print(z)
    # print(r)

    if r >= 69:
        return ("Chatbot: You are a beginner")
    elif 55 < r < 69:
        return("Chatbot: You are intermediate")
    else:
        return("Chatbot: You are fluent!")
