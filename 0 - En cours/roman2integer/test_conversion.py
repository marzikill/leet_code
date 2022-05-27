from conversion import roman2integer, integer2roman


print(integer2roman(3))
def test_conversion1():
    # Example 1:
    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3.
    assert roman2integer('III') == 3
    # Example 2:
    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V= 5, III = 3.
    assert roman2integer('LVIII') == 58
    # Example 3:
    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    assert roman2integer('MCMXCIV') == 1994

    # Personnal tests
    assert roman2integer('I') == 1
    assert roman2integer('IVXCM') == 1094


def test_conversion2():
    # Example 1:
    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3.
    assert integer2roman(3) == 'III'
    # Example 2:
    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V= 5, III = 3.
    assert integer2roman(58) == 'LVIII'
    # Example 3:
    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    assert integer2roman(1994) == 'MCMXCIV'

    # Personnal tests
    assert integer2roman(1) == 'I'
    assert integer2roman(1094) == 'MXCIV'
