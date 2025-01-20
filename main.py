import random
from api.polls import PollApp
from helper.formatting import single_poll_from_list, format_categories
from helper.answering import parse_answer, format_int_in_range, format_difficulty


def main():
    # TODO: Add exception handling for user input.
    # TODO: Add documentation
    # TODO: Cleaning up main loop by breaking up code into smaller methods
    # TODO: Fix token getting reset every time the game is restarted
    app = PollApp()
    user_input = None
    user_category = None
    poll_ids = [category['id'] for category in app.categories]
    active = True

    print("Welcome to the Poll-Generator!")

    while active:
        print("Here's a list of categories to choose from: ")
        format_categories(app)

        while user_input != 69:
            try:
                user_input = parse_answer("\nPlease choose a category based on the numbers per category: ", poll_ids)
            except ValueError:
                print("Please enter a valid number")
                continue
            finally:
                for category in app.categories:
                    if user_input == category['id']:
                        print(f"You chose {category['name']}")
                        user_category = category['id']
                break

        user_difficulty_answer = format_difficulty("Please select a difficulty level: ")
        user_amount_answer = format_int_in_range("Please enter the amount of poll questions you'd like to answer: ")
        print("\nA random poll will now be generated for you...")

        polls_response = app.get_polls(category=user_category,
                                       difficulty=user_difficulty_answer, amount=user_amount_answer)
        while polls_response:
            single_poll = single_poll_from_list(polls_response)
            print(f"Your question is: {single_poll['question']}")
            print("The answers are: ")
            for answer in single_poll['answers']:
                print(f"\t{answer}")
            user_answer = ""
            while True:
                user_answer = input("Choose wisely, what do you think the right answer is? ")
                if user_answer not in single_poll['answers']:
                    print("Please enter a valid answer from the list of answers.")
                else:
                    if user_answer == single_poll['correct_answer']:
                        print(f"You chose {single_poll['correct_answer']}, this was correct!")
                        break
                    else:
                        print(f"You chose {user_answer}, this was incorrect!")
                        continue
        active = False

    print("Thanks for playing!")


main()
