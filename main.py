from api.polls import PollApp
from helper.formatting import single_poll_from_list, format_categories
from helper.answering import parse_answer, format_int_in_range, format_difficulty, poll_handler


def main():
    # TODO: Add exception handling for user input.
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

        user_difficulty_answer = format_difficulty("Please select a difficulty level: ").lower()
        user_amount_answer = format_int_in_range("Please enter the amount of poll questions you'd like to answer: ")
        print("\nA random poll will now be generated for you...")

        polls_response = app.get_polls(category=user_category,
                                       difficulty=user_difficulty_answer, amount=user_amount_answer)
        while polls_response:
            poll_details = single_poll_from_list(polls_response)
            poll_handler(poll_details)

        while True:
            user_continue_answer = input("\nWould you like to continue? (y/n): ").lower()
            if user_continue_answer == "y":
                active = True
                break
            elif user_continue_answer == "n":
                active = False
                break
            else:
                print("Please enter either 'y' or 'n': ")
                continue

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
