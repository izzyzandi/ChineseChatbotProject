

























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


