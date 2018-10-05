import pytest
from actions import *

#All movement functions tested
def test_right():
    assert next_pos((0,0),RIGHT) == (1, 0)

def test_left():
    assert next_pos((0,0),LEFT) == (-1, 0)

def test_up():
    assert next_pos((0,0),UP) == (0, 1)

def test_down():
    assert next_pos((0,0),DOWN) == (0, -1)

#No movement expected when non-existent direction specified 
def test_nonexistent_direction():
    assert next_pos((10,10),-1) == (10,10)