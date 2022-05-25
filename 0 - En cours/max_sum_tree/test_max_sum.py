from max_sum import stupid, tab2bintree


def test_single_value():
    assert stupid(tab2bintree([-1])) == -1
    assert stupid(tab2bintree([0])) == 0
    assert stupid(tab2bintree([1])) == 1
    assert stupid(tab2bintree([-5])) == -5


def test_double_values():
    assert stupid(tab2bintree([-1, -2])) == -1
    assert stupid(tab2bintree([-1, 3])) == 3
    assert stupid(tab2bintree([1, 3])) == 4
    assert stupid(tab2bintree([3, -1])) == 3
    assert stupid(tab2bintree([-3, -1])) == -1


def test_triple_values():
    assert stupid(tab2bintree([-1, -2, -5])) == -1
    assert stupid(tab2bintree([-2, -1, -5])) == -1
    assert stupid(tab2bintree([-2, -5, -1])) == -1
    assert stupid(tab2bintree([2, -5, -1])) == 2
    assert stupid(tab2bintree([2, 3, -1])) == 5
    assert stupid(tab2bintree([-1, 3, 2])) == 4
    assert stupid(tab2bintree([-1, 2, 3])) == 4
    assert stupid(tab2bintree([-3, 2, 3])) == 3
    assert stupid(tab2bintree([5, 2, 3])) == 10
