from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band ,Musician,Guitarist,Bassist,Drummer
import pytest

def test_version():
    assert __version__ == '0.1.0'



## preparing the data

mike = Guitarist('mike') 
carlos = Drummer('carlos')
john = Bassist('john')   


maroon5 = Band('maroon5')
maroon5.add_members(mike)
maroon5.add_members(carlos)
maroon5.add_members(john)

#########################################################################
########## Tests ###############
#########################################################################

def test_to_list(cls):
    expected = [mike,carlos,john]
    actual = maroon5.to_list()
    assert  actual == expected

def test_play_solo():
    expected = 'mike Play solo'
    actual = mike.play_solo()
    assert actual == expected

def test_play_solos():
    expected = "mike Play solo\ncarlos Play solo\njohn Play solo\n"
    actual = maroon5.play_solos()
    assert actual == expected

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
