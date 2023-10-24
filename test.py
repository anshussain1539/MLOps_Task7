from main import Bulb

bulb = Bulb()

#Test case-1
def test_bulb_status():
    assert bulb.getStatus() == "Bulb is not glowing"


#Test case-2
def test_bulb_on():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"

#Test case-3
def test_bulb_off():
    bulb.isOff()
    assert bulb.getStatus() == "Bulb is glowing"


