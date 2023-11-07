import nltk
def NumberOfWords(text):
    return len(text.split())

def NumberOfSentences(text):
    return len(nltk.sent_tokenize(text))
def FleschKincaidScore(numberOfSyllables, numberOfWords, numberOfSentences):

    return 206.835 - 1.015 * (numberOfWords / numberOfSentences) - 84.6 * (numberOfSyllables / numberOfWords)


text = "hello there is a lovely place over there. Thank you"
r = FleschKincaidScore(13, NumberOfWords(text), NumberOfSentences(text))
x = NumberOfWords(text)
y = NumberOfSentences(text)
print(r)