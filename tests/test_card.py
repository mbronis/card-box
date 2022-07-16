from tests.fixtures import get_test_cards


def test_match_all_str(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_all(**{"name": "foo"})
    assert c1.matches_all(**{"name": "FOO"})
    assert not c1.matches_all(**{"name": "foobar"})


def test_match_all_int(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_all(**{"hp": 1})
    assert c1.matches_all(**{"hp": 1.0})
    assert not c1.matches_all(**{"hp": 2})
    assert not c1.matches_all(**{"hp": None})


def test_match_all_tuple(get_test_cards):
    c1, c2, c3 = get_test_cards

    assert c1.matches_all(**{"powers": ["foo"]})
    assert c2.matches_all(**{"powers": ["foo", "bar"]})
    assert c3.matches_all(**{"powers": []})
    assert not c1.matches_all(**{"powers": []})
    assert not c1.matches_all(**{"powers": ["foo", "bar"]})
    assert not c2.matches_all(**{"powers": ["foo"]})
