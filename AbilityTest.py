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
        chinese_q = random.choice(list(vocabulary.keys()))
        english_a = vocabulary[chinese_q]
        fake_answer1 = vocabulary[random.choice(list(vocabulary.keys()))]
        fake_answer2 = vocabulary[random.choice(list(vocabulary.keys()))]

        while fake_answer1 == english_a or fake_answer2 == english_a or fake_answer1 == fake_answer2:
            fake_answer1 = vocabulary[random.choice(list(vocabulary.keys()))]
            fake_answer2 = vocabulary[random.choice(list(vocabulary.keys()))]

        print(f"What is the correct translation of {chinese_q}?")

        answers = random.sample([english_a, fake_answer1, fake_answer2], k=3)

        for i, x in enumerate(answers):
            print(f"{i+1}. {x}")

        user_answer = int(input("Please enter the number of the correct answer: "))
        user_answer = answers[int(user_answer - 1)]

        if user_answer == english_a:
            print("Correct answer!")
        else:
            print(f"Incorrect. The correct answer is \"{english_a}\"")
            incorrect_vocabulary.append(chinese_q)

        if len(incorrect_vocabulary) == 0:
            incorrect_vocabulary.append(chinese_q)

    print(incorrect_vocabulary)
    return random.choice(incorrect_vocabulary)