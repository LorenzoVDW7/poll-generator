"""The tests for the API token reside in this module.
TODO: Add tests when token is being stored inside of a database."""
from api.polls import PollApp


def test_token():
    app = PollApp()
    token = app.token
    assert token