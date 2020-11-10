from recipes import convert_name
from recipes import write_recipe


def test_convert_name():
    assert(convert_name("Egg and Soldiers") == "egg_and_soldiers.txt")
    assert(convert_name(" Nine piz$za") == "nine_pizza.txt")
    assert(convert_name(" ") == ".txt")
    assert(convert_name("!!!") == ".txt")
