def find_test():
    r = tab2bintree([1, 2, 3, 4, 5, 6, 7])
    assert find(r, 1)
    assert find(r, 4)
    assert find(r, 7)
    assert not find(r, 0)
    assert not find(r, 9)
    assert not find(r, 0.5)
    return True


def count_elt_test():
    for i in range(10):
        assert count_elt(tab2bintree(list(range(i)))) == i
    return True
