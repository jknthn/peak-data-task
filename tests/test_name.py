import pytest

from src.name import Name


def test_init_none():
    with pytest.raises(ValueError):
        _ = Name(full=None, initial=None)


def test_wrong_initials():
    with pytest.raises(ValueError):
        _ = Name(full="jeremi", initial="k")


def test_only_full():
    name = Name(full="jeremi")
    assert name.full == "jeremi"
    assert name.initial == "j"


def test_only_initial():
    name = Name(full=None, initial="j")
    assert name.full is None
    assert name.initial == "j"


def test_good_initial():
    name = Name(full="jeremi", initial="j")
    assert name.full == "jeremi"
    assert name.initial == "j"


def test_is_dash_equal():
    assert Name.is_dash_equal("jeremi", "j")
    assert Name.is_dash_equal("jeremi-tomasz", "j-t")
    assert Name.is_dash_equal("jeremi-tomasz-jeremi", "j-t-j")
    assert not Name.is_dash_equal("jeremi", "t")
    assert not Name.is_dash_equal("jeremi-tomasz", "j-j")
    assert not Name.is_dash_equal("jeremi-tomasz-jeremi", "j-t")


def test_to_initial():
    assert Name.to_initial("jeremi") == "j"
    assert Name.to_initial("jeremi-tomasz") == "j-t"
    assert Name.to_initial("jeremi-tomasz-jeremi") == "j-t-j"


def test_only_full_dashed():
    name = Name(full="jeremi-tomasz")
    assert name.full == "jeremi-tomasz"
    assert name.initial == "j-t"


def test_only_initial_dashed():
    name = Name(full=None, initial="j-t")
    assert name.full is None
    assert name.initial == "j-t"


def test_good_initial_dashed():
    name = Name(full="jeremi-tomasz", initial="j-t")
    assert name.full == "jeremi-tomasz"
    assert name.initial == "j-t"


def test_wrong_initials_dashed():
    with pytest.raises(ValueError):
        _ = Name(full="jeremi-tomasz", initial="k")
    with pytest.raises(ValueError):
        _ = Name(full="jeremi-tomasz", initial="j-b")
    with pytest.raises(ValueError):
        _ = Name(full="jeremi-tomasz", initial="b-t")
    with pytest.raises(ValueError):
        _ = Name(full="jeremi-tomasz", initial="b-b")
