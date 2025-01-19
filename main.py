from api.polls import PollApp


def main():
    user_input = -1
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
                break


        break

    print("Thanks for playing!")


main()
