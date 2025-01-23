import pytest
from helper.answering import format_difficulty, poll_handler

def test_format_difficulty_correct(monkeypatch):
    """Test for passing a 'Correct' value to the method"""
    inputs = iter(["easy", "medium", "hard"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    choice_easy = format_difficulty("Select a difficulty between easy, medium and hard: ")
    choice_medium = format_difficulty("Select a difficulty between easy, medium and hard: ")
    choice_hard = format_difficulty("Select a difficulty between easy, medium and hard: ")
    assert choice_easy == 'easy'
    assert choice_medium == 'medium'
    assert choice_hard == 'hard'

def test_format_difficulty_incorrect(monkeypatch):
    """Test for passing an 'Incorrect' value to the method"""
    monkeypatch.setattr('builtins.input', lambda _: 'incorrect')
    incorrect_choice = format_difficulty("Incorrect choice: ")
    assert incorrect_choice is None
