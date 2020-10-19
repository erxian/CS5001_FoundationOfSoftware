from upc import is_valid_upc


def test_is_valid_upc():
    assert(is_valid_upc("9780128053904") is True)
    assert(is_valid_upc("56248745972626") is False)
    assert(is_valid_upc("a7665391") is False)
