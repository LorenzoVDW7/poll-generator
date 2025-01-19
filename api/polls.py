import json

import requests


class PollApp():
    def __init__(self):
        self.token = self.get_session_token()
        self.categories = self.get_categories()

    @staticmethod
    def get_categories() -> list:
        url = "https://opentdb.com/api_category.php"
        req = ""
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
        finally:
            response = json.loads(req.text)
            category_list = [category["name"] for category in response["trivia_categories"]]
        return category_list

    def get_session_token(self) -> str:
        url = "https://opentdb.com/api_token.php?command=request"
        req = requests.get(url)
        return req.json()['token']

    def get_polls(self, amount: int = 10, difficulty: str = "medium",
                  category: int = None, question_type: str = None) -> list:
        req = ""
        url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}"
        if category:
            url += f"&category={category}"
        if question_type:
            url += f"&question_type={question_type}"

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
        finally:
            response = req.json()
            if response["response_code"] == 0:
                polls_list = [poll for poll in response["results"]]
                return polls_list

