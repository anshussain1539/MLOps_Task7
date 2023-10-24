from main import Bulb

bulb = Bulb()

def test_bulb_status():
    assert bulb.getStatus() == "Bulb is not glowing"


def test_bulb_on():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"

def test_bulb_off():
    bulb.isOff()
    assert bulb.getStatus() == "Bulb is glowing"


