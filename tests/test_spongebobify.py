from spongebobify.main import aye_aye


def test_aye_aye_non_alpha_no_change():
    assert aye_aye("111111!") == "111111!"


def test_aye_aye_text_not_altered():
    assert aye_aye("Are ya ready kids").lower() == "Are ya ready kids".lower()


def test_aye_aye_unicode_symbols():
    assert aye_aye("˙˙∂∂∂∂∂˚¥∑∑®") == "˙˙∂∂∂∂∂˚¥∑∑®"


def test_aye_aye_length_and_content():
    input_text = "Are ya ready kids"
    result = aye_aye(input_text)
    assert len(result) == len(input_text)
    assert result.lower() == input_text.lower()
    # Check that it's not JUST lowercase or JUST uppercase (statistically safe)
    if any(c.isalpha() for c in input_text):
        assert not result.isupper()
        assert not result.islower()
