import pytest
from project import temp, weight, longitud, volumen


def test_temp():
    with pytest.raises(SystemExit):
        temp("32 F")
        temp("-10 C")
        temp("-459.67 F")

def test_weight():
    with pytest.raises(SystemExit):
        weight("10 lb")
        weight("5 kg")
        weight("0 lb")

def test_longitud():
    with pytest.raises(SystemExit):
        longitud("10 mi")
        longitud("100 m")
        longitud("0.1 in")

def test_volumen():
    with pytest.raises(SystemExit):
        volumen("2 gal")
        volumen("3 pt")
        volumen("0.1 fl oz")


