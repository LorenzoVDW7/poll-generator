def parse_answer(prompt: str, valid_choices: list) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid number.")

def format_int_in_range(prompt: str, min: int = 1, max: int = 50) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if min <= choice <= max:
                return choice
            print("Please enter a valid number within the specified range.")
        except ValueError:
            print("Please enter a valid number.")

def format_difficulty(prompt: str) -> str | None:
    difficulty_options = ["easy", "medium", "hard"]
    print(f"The difficulty levels are: ")
    for option in difficulty_options:
        print(f"\t{option}".title())
    while True:
        choice = input(prompt)
        if choice.lower() in difficulty_options:
            return choice
        print("You didn't enter a valid option, the default will be used. (Medium)")
        return None
