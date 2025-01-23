"""In this module, the tests for API communication about the categories reside"""


def test_categories(app):
    categories = app.get_categories()
    assert type(categories) == list
    assert categories is not None
    for category in categories:
        assert type(category) == dict
