def parse_answer(prompt: str, valid_choices: list) -> int:
    """Method to validate the user input, making sure only valid answers are provided.
    :param prompt: The prompt to be displayed.
    :param valid_choices: A list of valid choices for the end user to choose from.
    :return: The validated choice made by the user, based on displayed prompt.
    :rtype: int"""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid number.")


def format_int_in_range(prompt: str, min_amount: int = 1, max_amount: int = 50) -> int:
    """Method to format a prompt into a valid range, making sure the user doesn't pass the limit of poll questions.
    :param prompt: The prompt to be displayed.
    :param min_amount: The minimum amount of questions to show. The default is at least 1 question.
    :param max_amount: The maximum amount of questions to show, which is 50 questions according to API documentation.
    :return: The validated amount of questions a user would like to receive.
    :rtype: int"""
    while True:
        try:
            choice = int(input(prompt))
            if min_amount <= choice <= max_amount:
                return choice
            print("Please enter a valid number within the specified range.")
        except ValueError:
            print("Please enter a valid number.")


def format_difficulty(prompt: str) -> str | None:
    """Method specifies a range of difficulty options. If the user doesn't pick one of the provided options,
    the default option, which is specified in api/polls, will be used.
    :param prompt: The prompt to be displayed.
    :return: Either the validated chosen difficulty or None.
    :rtype: str | None"""
    difficulty_options = ["easy", "medium", "hard"]
    print("The difficulty levels are: ")
    for option in difficulty_options:
        print(f"\t{option}".title())
    while True:
        choice = input(prompt)
        if choice.lower() in difficulty_options:
            return choice
        print("You didn't enter a valid option, the default will be used. (Medium)")
        return None

def poll_handler(poll: dict) -> bool:
    print(f"Your question is: {poll['question']}")
    print("The answers are:")
    for answer in poll['answers']:
        print(f"\t{answer}")

    while True:
        user_answer = input("Choose wisely, what do you think the right answer is? ")
        if user_answer not in poll['answers']:
            print("You didn't enter a valid answer.")
        elif user_answer == poll['correct_answer']:
            print("You entered the correct answer.")
            return True
        else:
            print("You entered the wrong answer.")

