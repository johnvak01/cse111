'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''
from pytest import approx
import pytest
import random

# import functions to test
from prosody_analyzer import calculate_stresses, calculate_foot_pattern, match_metrical_pattern

def test_basic_foot_pattern():
    '''
    FOR:    x 
    PARAM:  x
    RETURN: x
    '''
    # text basic feet
    assert calculate_foot_pattern("00") == ["dibrach"]
    assert calculate_foot_pattern("01") == ["iamb"]
    assert calculate_foot_pattern("10") == ["trochee"]
    assert calculate_foot_pattern("11") == ["spondee"]
    assert calculate_foot_pattern("001") == ["anapest"]
    assert calculate_foot_pattern("100") == ["dactyl"]

def test_joined_foot_patterns():
    # test doubles
    assert calculate_foot_pattern("0000") == ["dibrach","dibrach"]
    assert calculate_foot_pattern("0101") == ["iamb","iamb"]
    assert calculate_foot_pattern("1010") == ["trochee","trochee"]
    assert calculate_foot_pattern("1111") == ["spondee","spondee"]
    assert calculate_foot_pattern("001001") == ["anapest","anapest"]
    assert calculate_foot_pattern("100100") == ["dactyl","dactyl"]
    
    # test permutations of two

    # assert calculate_foot_pattern("0000") == [" py"," "]

def test_random_patterns():
    pattern = ""
    try:
        for x in range(500):
            pattern = "".join(random.choices(["0","1"], k=random.randint(2,100)))
            print(pattern)
            assert calculate_foot_pattern(pattern)
    except Exception as e:
        pytest.fail(f"Random Patterns failed to produce coherent results. The Error: {e}")
        

def test_foot_pattern_matching():
    assert match_metrical_pattern(["iamb"]) == "iambic monometer"
    assert match_metrical_pattern(["iamb","dactyle"]) == "dimeter"
    assert match_metrical_pattern(["iamb","iamb","iamb","iamb","iamb"]) == "iambic pentameter"
# Main call
pytest.main(["-v", "--tb=line", "-rN", __file__])