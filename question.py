question = input()
question = question.lower()
answers =  {'hi':'hi there!', 'how are you?':'fine, and you?', 'bye':'see you'}
def get_answer(question, answers):
    return answers.get(question)
test = get_answer(question, answers)
print(test)