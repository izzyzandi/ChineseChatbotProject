def NumberOfSyllables(text):
    counter = 0
    for c in text:
        if c != '!' and c != '.' and c != '?' and c != '。':
            if ord(c) > 123:
                counter = counter + 1
    return counter

def NumberOfSentences(text):
    counter = 0
    for c in text:
        if c == '!' or c == '.' or c == '?' or c == '。':
            counter = counter + 1
    return counter

def FleschKincaidScore(numberOfSyllables, numberOfWords, numberOfSentences):
    return 206.835 - 1.015 * (numberOfWords / numberOfSentences) - 84.6 * (numberOfSyllables / numberOfWords)

def NumberOfWords(text):
    return len(text.split())


print("Hi. I am a Chinese teaching chatbot. Before we can begin any lessons, I need to know your level.\nPlease type"
      "up to 10 sentences in Chinese. When typing, please separate words with spaces. 谢谢!\n")

text = input()


#text = "hello there is a lovely place over there. Thank you"
#text = "我 要 一 杯 水. 你 喜欢 吃 面?"

r = FleschKincaidScore(NumberOfSyllables(text), NumberOfWords(text), NumberOfSentences(text))
x = NumberOfSyllables(text)
y = NumberOfSentences(text)
z = NumberOfWords(text)
print(x)
print(y)
print(z)
print(r)
