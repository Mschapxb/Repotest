from inc_dec import increment, decrement

def test_increment():
    assert increment(3) == 4
    assert increment(-1) == 0

def test_decrement():
    assert decrement(3) == 2
    assert decrement(0) == -1
