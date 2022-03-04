from spongebobify.main import aye_aye

def test_aye_aye_non_alpha_no_change():
    assert aye_aye("111111!") == "111111!"


def test_aye_aye_text_not_altered():
    assert aye_aye("Are ya ready kids").lower() == "Are ya ready kids".lower()


def test_aye_aye_unicode_symbols():
    assert aye_aye("˙˙∂∂∂∂∂˚¥∑∑®") == "˙˙∂∂∂∂∂˚¥∑∑®"


def test_aye_aye_alters_text():
    assert aye_aye("Are ya ready kids") != "Are ya ready kids"
