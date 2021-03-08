import pytest
from Bird import Bird


#def test_update():

def test_get_image_path():
    TestBird = Bird(0, 0, 'images/flappy_bird.png')
    assert TestBird.get_image_path() == 'images/flappy_bird.png'

'''
def test_get_size():
    TestBird = Bird(0, 0, 'test_path/image.png')


def test_get_edges():

def test_get_corners():
'''