import pytest
from spongemock import spongemock

def test_easy_peasy():
    expected = "tEsT"
    actual = spongemock.mock("test")
    assert(expected == actual)

def test_easy_i_word():
    expected = "rYaN eAtS tiNy DoNg"
    actual = spongemock.mock("ryan eats tiny dong")
    assert(expected == actual)

def test_special_chars():
    actual = spongemock.mock("Lick my penis-fuck\\")
    expected = "LiCk My PeNiS-fUcK\\"
    assert(expected == actual)

def test_is_aint_easy():
    expected = "iLLiNoiS"
    actual = spongemock.mock("illinois")
    assert(expected == actual)

def test_lowercase_i():
    expected = "rYaN i Do NoT LiKe ThiS rULe"
    actual = spongemock.mock("ryan I do not like this rule")
    assert(expected == actual)