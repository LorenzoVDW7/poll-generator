import random
from api.polls import PollApp
from helper.formatting import single_poll_from_list


def main():
    user_input = -1
    user_category = -1
    poll_ids = []
    app = PollApp()
    print("Welcome to the Poll-Generator!")

    while True:
        print("Here's a list of categories to choose from: ")
        for count, category in enumerate(app.categories):
            if count % 4 == 0:
                print("")
            print(f"{category['id']}: {category['name']} ", end="")
            poll_ids.append(category['id'])

        while user_input != 69:
            try:
                user_input = int(input("\nPlease choose a category based on the numbers per category "
                                       "or type '69' to quit: "))
            except ValueError:
                print("Please enter a valid number.")
            finally:
                if user_input not in poll_ids:
                    print("Please enter a valid number from the list of options.")
                    continue
                for category in app.categories:
                    if user_input == category['id']:
                        print(f"You chose {category['name']}")
                        user_category = category['id']
                break

        user_difficulty_answer = input(
            "Please choose a difficulty level or leave empty for a random difficulty level: ")
        user_amount_answer = int(input("Please choose a amount of questions, this number can be between 1 and 50: "))
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

        break

    print("Thanks for playing!")


main()
