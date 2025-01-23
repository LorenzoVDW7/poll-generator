"""This module is meant for helper functions regarding the formatting of input/output"""
import random

from api.polls import PollApp


def single_poll_from_list(poll_list: list) -> dict:
    """Formats an incoming list of poll questions into a single poll.
    :rtype: dict
    :returns: A dictionary containing the poll question and it's answers.
    :param poll_list: A list of incoming poll questions."""

    random.shuffle(poll_list)
    single_poll = poll_list.pop()
    poll_dict = {"question": single_poll['question']}

    # Creates list consisting of both correct and incorrect answers, so answers can be shuffled properly.
    # If not, the correct answer will always be in the same location.
    answers = [single_poll['correct_answer']]
    for incorrect_answer in single_poll['incorrect_answers']:
        answers.append(incorrect_answer)
    random.shuffle(answers)

    poll_dict['answers'] = answers
    poll_dict['correct_answer'] = single_poll['correct_answer']
    return poll_dict

def format_categories(app: PollApp) -> None:
    for count, category in enumerate(app.categories):
        if count % 4 == 0:
            print("")
        print(f"{category['id']}: {category['name']} ", end="")



