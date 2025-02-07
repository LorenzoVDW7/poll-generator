"""In this module, the tests for API communication about the categories reside"""
from api.polls import PollApp

def test_categories():
    app = PollApp()
    categories = app.get_categories()
    assert type(categories) is list
    assert categories is not None
    for category in categories:
        assert type(category) is dict
