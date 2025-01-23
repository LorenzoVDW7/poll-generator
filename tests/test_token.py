"""The tests for the API token reside in this module.
TODO: Add tests when token is being stored inside of a database."""


def test_token(app):
    token = app.token
    assert token