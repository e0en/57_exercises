#!/usr/bin/env python
import json
import random


FILENAME_PREFIX = '57_trivia'


def load_game_data():
    try:
        with open(f'{FILENAME_PREFIX}.json') as fp:
            return json.loads(fp.read())
    except:
        return []

def save_game_data(data):
    with open(f'{FILENAME_PREFIX}.json', 'w') as fp:
        fp.write(json.dumps(data))



def show_question(problem):
    print(problem['question'])
    answers = random.sample(problem['answers'], len(problem['answers']))
    correct_choices = set()
    for i, a in enumerate(answers):
        print(f' {i + 1}. {a["content"]}')
        if a['is_correct']:
            correct_choices.add(i + 1)

    valid_choices = set(range(1, len(answers) + 1))
    user_choice = input('Answer?: ')
    user_choice = int(user_choice)
    while user_choice not in valid_choices:
        user_choice = input('Invalid input.\nAnswer?: ')

    return user_choice in correct_choices


def add_problems():
    problems = []
    while True:
        question = input('Question?: ')
        if not question:
            print('Ok. Finishing adding problems.\n')
            break

        choices = []
        while True:
            choice = input('Answer choice: ')
            if not choice:
                print('Ok. Moving on to the next problem.\n')
                break
            is_correct = input('Is the answer above correct? (y/N): ')
            is_correct = is_correct.lower() == 'y'

            if is_correct:
                print(f'{choice} is a correct answer to {question}')

            choices += [{'content': choice, 'is_correct': is_correct}]
        problems += [{'question': question, 'answers': choices}]
    return problems


if __name__ == '__main__':
    problems = load_game_data()
    if not problems:
        new_problems = add_problems()
        save_game_data(problems + new_problems)
        exit(0)

    n_correct = 0
    while True:
        problem = random.choice(problems)
        is_correct = show_question(problem)
        if is_correct:
            n_correct += 1
        else:
            print(f'You got {n_correct} in a row. Finishing.')
            break

    add_new = input('Want to add new problems? (y/N): ')
    add_new = add_new.lower() == 'y'
    if add_new:
        new_problems = add_problems()
        save_game_data(problems + new_problems)
