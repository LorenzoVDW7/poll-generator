"""This module contains the functionality for consuming the Open Trivia Database API"""
import json
import requests


class PollApp:
    def __init__(self):
        self.token = self.get_session_token()
        self.categories = self.get_categories()

    @staticmethod
    def get_categories() -> list:
        """Retrieves categories from API and returns them in a list.
        :rtype: list
        :return: The list of categories"""
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
        """Retrieves session token from the API, with a lifetime of 6 hours when inactive.
        :rtype: str
        :return: Session token
        """
        url = "https://opentdb.com/api_token.php?command=request"
        req = requests.get(url)
        return req.json()['token']

    @staticmethod
    def get_polls(amount: int = 10, difficulty: str = "medium",
                  category: int = None, question_type: str = None) -> list:
        """Retrieves polls based on multiple optional factors.
        :param amount: The amount of polls to return.
        :param difficulty: The difficulty of the poll questions.
        :param category: The category of the poll questions.
        :param question_type: The type of the poll questions. Can either be boolean (true/false), or multiple choice.
        :rtype: list
        :return: The list of polls"""
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

