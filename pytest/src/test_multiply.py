from multiply import multiply
import pytest

@pytest.mark.parametrize(
    "a  , b  , expected", [
    (-1 , 5  , -5),
    (0  ,10  , 0),
    (-2 ,-3  , 6)             ]
    
    )
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.skip(reason="لسه مش جاهز للاختبار")
def test_multiply_with_unable_values():
    a, b = 7, 0  # Example values
    with pytest.raises(ZeroDivisionError):
        multiply(a, b)

@pytest.mark.xfail(reason="الميزة دي لسه ما خلصتش")
def test_future_feature():
    assert 1 + 1 == 3