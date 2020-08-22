from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band
import pytest

def test_version():
    assert __version__ == '0.1.0'



## preparing the data

mike = Band.Guitarist('mike') 
carlos = Band.Drummer('carlos')
john = Band.Bassist('john')   


def test_play_solo():
    expected = 'play drummer'
    actual = carlos.play_solo()
    assert actual == expected

def test_play_solos():
    expected = "mike play a solos\ncarlos play a solos\njohn play a solos\n"
    actual = mike.play_solos()
    assert actual == expected

def test_to_list():
    expected = ['mike','carlos','john']
    actual = mike.to_list()
    assert  actual == expected

def test_str():
    expected = "Guitarist <mike>"
    actual = mike.__str__()
    assert actual == expected

def test_rper():
    expected = " 'john' "
    actual = john.__repr__()
    assert actual == expected

def test_get_instrument():
    expected = "Drummer"
    actual = carlos.get_instrument()
    assert actual == expected