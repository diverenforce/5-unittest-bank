from bank import value
import pytest

def test_value_caps():
    assert value('JOKING HAHAHA') == 100
    assert value('WHATDOYOUMEAN????') == 100
    assert value('HOWIS THIS POSSIBLE?!!') == 20
    assert value('HELLO TO THE UNKNOWN') == 0

def test_value_small():
    assert value('joking hahahaha') == 100
    assert value('whatdoyoumean????') == 100
    assert value('howis this possible?!!') == 20
    assert value('hello to the unknown') == 0