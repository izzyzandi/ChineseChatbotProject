import nltk
from hyphen import Hyphenator
import jieba


def NumberOfSyllables(text):
    text = text.lower()
    total = 0
    for words in text.split():
        for i in range(0, len(words)):
            if words[i] == 'a' or words[i] == 'e' or words[i] == 'i' or words[i] == 'o' or words[i] == 'u' or words[i] == 'y':
                if words[i-1] != 'a' and words[i-1] != 'e' and words[i-1] != 'i' and words[i-1] != 'o' and words[i-1] != 'u' and words[i-1] != 'y':
                    total = total + 1
                    print(words)
                    print(total)
        if (words.endswith('e') and len(words) > 4) or (words.endswith('ed') and not words.endswith('led')):
            total = total - 1
    return total



def NumberOfWords(text):
    return len(text.split())


def NumberOfSentences(text):
    return len(nltk.sent_tokenize(text))

def FleschKincaidScore(numberOfSyllables, numberOfWords, numberOfSentences):
    return 206.835 - 1.015 * (numberOfWords / numberOfSentences) - 84.6 * (numberOfSyllables / numberOfWords)


text = ("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, "
        "his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through "
        "the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust "
        "from entering along with him.")
#text = input("INPUT: ")
#text = "我 叫 舒諾妍，我 今 年 二十 歲。我 喜歡 藍色 ，我 不 喜歡 紅色。我 喜歡 吃 麵，我 不 喜歡 吃 飯。"
r = FleschKincaidScore(NumberOfSyllables(text), NumberOfWords(text), NumberOfSentences(text))
x = NumberOfWords(text)
y = NumberOfSentences(text)
z = NumberOfSyllables(text)
# print(x)
# print(y)
# print(z)
print(r)
print("Number of syllables:", z)

#GUI fs 22 3 36
# GUI 20 3 36
# this 23 3 33


# import random
#
# # Chinese vocabulary for quizzing
# chinese_vocabulary = {
#     "你好": "hello",
#     "谢谢": "thank you",
#     "学习": "study",
#     "水果": "fruit",
#     "动物": "animal",
#     # Add more vocabulary as needed
# }
#
# # Function to quiz the user on Chinese vocabulary with biased incorrect answers
# def chinese_vocabulary_quiz():
#     question = random.choice(list(chinese_vocabulary.keys()))
#     correct_answer = chinese_vocabulary[question]
#
#     # Create a list of incorrect answers (excluding the correct answer)
#     incorrect_answers = [v for k, v in chinese_vocabulary.items() if k != question]
#
#     # Bias towards incorrect answers by selecting a random incorrect answer
#     biased_incorrect_answer = random.choice(incorrect_answers)
#
#     # Shuffle the answers so the correct answer is not always in the same position
#     answers = random.sample([correct_answer, biased_incorrect_answer], k=2)
#
#     # Ask the question
#     print(f"Translate the Chinese word: {question}")
#
#     # Present the shuffled answers to the user
#     for i, answer in enumerate(answers, start=1):
#         print(f"{i}. {answer}")
#
#     # Get user input
#     user_choice = input("Your Answer (Enter the number): ")
#
#     # Check the answer
#     user_answer = answers[int(user_choice) - 1]
#     if user_answer == correct_answer:
#         print("Correct! Great job!")
#     else:
#         print(f"Sorry, the correct answer is: {correct_answer}")
#
# # Example usage
# print("Chinese Vocabulary Quiz Bot: 你好！Let's test your Chinese vocabulary. Type 'exit' to end the quiz.")
# while True:
#     chinese_vocabulary_quiz()
#
#     # Check if the user wants to exit
#     exit_command = input("Type 'exit' to end the quiz or press Enter to continue: ")
#     if exit_command.lower() == 'exit':
#         print("Chinese Vocabulary Quiz Bot: 谢谢参与！Goodbye!")
#         break
#
#






# # Example rules for the Chinese language learning chatbot
# chat_rules = {
#     "greetings": ["你好", "您好", "Hi", "Hello"],
#     "introduction": ["介绍一下你自己", "你是谁", "你叫什么名字"],
#     "study_tips": ["如何学好中文", "学习中文的技巧", "怎么提高中文水平"],
#     "practice_methods": ["如何练习中文", "提高中文口语", "学中文的有效方法"],
#     "resources": ["好的中文学习资源", "推荐学中文的网站", "中文学习书籍"],
#     "farewell": ["再见", "拜拜", "Goodbye"],
# }
#
# # Function to process user input and generate a response
# def process_chinese_revision(input_text):
#     input_text_lower = input_text.lower()
#
#     # Check for greetings
#     if any(greeting in input_text_lower for greeting in chat_rules["greetings"]):
#         return "你好！有什么我可以帮助你的吗？"
#
#     # Check for introductions
#     elif any(keyword in input_text_lower for keyword in chat_rules["introduction"]):
#         return "我是一个中文学习助手。如果你有任何关于学中文的问题，都可以问我哦！"
#
#     # Check for study tips
#     elif any(keyword in input_text_lower for keyword in chat_rules["study_tips"]):
#         return "学好中文需要坚持，多听多读多练，可以参加语言交换，还可以用中文阅读材料。"
#
#     # Check for practice methods
#     elif any(keyword in input_text_lower for keyword in chat_rules["practice_methods"]):
#         return "练习中文口语可以找语伴，多说多练。阅读中文文章、听中文音频也是提高水平的好方法。"
#
#     # Check for resources
#     elif any(keyword in input_text_lower for keyword in chat_rules["resources"]):
#         return "一些好的中文学习资源包括：汉语水平考试教材、中文学习网站（如Duolingo、HelloChinese）以及中文新闻和博客。"
#
#     # Check for farewell
#     elif any(keyword in input_text_lower for keyword in chat_rules["farewell"]):
#         return "再见！如果有问题，随时来找我。祝你学习愉快！"
#
#     # Default response
#     else:
#         return "抱歉，我不太明白你的问题。可以问我关于学中文的任何问题哦！"
#
# # Example usage
# print("Chinese Study Bot: 你好！我是中文学习助手。有什么我可以帮助你的吗？")
# while True:
#     user_input = input("你: ")
#     if user_input.lower() == '再见':
#         print("Chinese Study Bot: 再见！祝你学习愉快。")
#         break
#
#     response = process_chinese_revision(user_input)
#     print("Chinese Study Bot:", response)
