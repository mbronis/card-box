def test_match_all_str(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_all(**{"name": "foo"})
    assert c1.matches_all(**{"name": "FOO"})
    assert not c1.matches_all(**{"name": ""})
    assert not c1.matches_all(**{"name": "foobar"})


def test_match_all_int(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_all(**{"hp": 1})
    assert c1.matches_all(**{"hp": 1.0})
    assert not c1.matches_all(**{"hp": 2})


def test_match_all_tuple(get_test_cards):
    c1, c2, c3 = get_test_cards

    assert c1.matches_all(**{"powers": ["foo"]})
    assert not c1.matches_all(**{"powers": ["foo", "bar"]})
    assert not c1.matches_all(**{"powers": []})

    assert c2.matches_all(**{"powers": ["foo", "bar"]})
    assert not c2.matches_all(**{"powers": ["foo"]})

    assert not c3.matches_all(**{"powers": []})


def test_match_all_multiple(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_all(**{"name": "foo", "hp": 1, "powers": ["foo"]})
    assert c1.matches_all(**{"name": "foo", "hp": 1})
    assert not c1.matches_all(**{"name": "foo", "hp": 1, "powers": ["bar"]})


def test_match_any_str(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_any(**{"name": "foo"})
    assert c1.matches_any(**{"name": "FOO"})
    assert c1.matches_any(**{"name": "fo"})
    assert not c1.matches_any(**{"name": ""})
    assert not c1.matches_any(**{"name": "bar"})


def test_match_any_int(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_any(**{"hp": 1})
    assert c1.matches_any(**{"hp": 1.0})
    assert c1.matches_any(**{"hp": 2})
    assert not c1.matches_any(**{"hp": 0})


def test_match_any_tuple(get_test_cards):
    c1, c2, c3 = get_test_cards

    assert c1.matches_any(**{"powers": ["foo"]})
    assert c1.matches_any(**{"powers": ["foo", "bar"]})
    assert not c1.matches_any(**{"powers": []})
    assert not c1.matches_any(**{"powers": ["baz"]})

    assert c2.matches_any(**{"powers": ["foo"]})
    assert c2.matches_any(**{"powers": ["bar"]})
    assert c2.matches_any(**{"powers": ["foo", "bar"]})

    assert not c3.matches_any(**{"powers": []})


def test_match_any_multiple(get_test_cards):
    c1, *_ = get_test_cards

    assert c1.matches_any(**{"name": "foo", "hp": 1, "powers": ["foo"]})
    assert c1.matches_any(**{"name": "foo", "hp": 1})
    assert c1.matches_any(**{"name": "f", "hp": 0, "powers": ["bar"]})
    assert c1.matches_any(**{"name": "baz", "hp": 5, "powers": ["bar"]})
    assert c1.matches_any(**{"name": "baz", "hp": 0, "powers": ["foo"]})

    assert not c1.matches_any(**{"name": "baz", "hp": 0, "powers": ["baz"]})
