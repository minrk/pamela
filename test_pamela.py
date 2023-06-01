import getpass

import pytest

import pamela


def test_pam_error_noargs():
    e = pamela.PAMError()
    s = str(e)
    r = repr(e)
    assert 'Unknown' in s
    assert 'Unknown' in r


def test_pam_error_errno():
    en = 2
    e = pamela.PAMError(errno=en)
    assert str(en) in str(e)
    assert 'Unknown' not in str(e)


def test_auth_nouser():
    with pytest.raises(pamela.PAMError) as exc_info:
        pamela.authenticate('userdoesntexist', 'wrongpassword')

    e = exc_info.value
    assert 'Unknown' not in str(e)


def test_auth_badpassword():
    with pytest.raises(pamela.PAMError) as exc_info:
        pamela.authenticate(getpass.getuser(), 'wrongpassword')

    e = exc_info.value
    assert 'Unknown' not in str(e)


def test_all():
    for name in pamela.__all__:
        getattr(pamela, name)


def test_environment():
    handle = pamela.pam_start(getpass.getuser(), 'login')

    k1, v1 = 'A', 'hat'
    handle.put_env(k1, v1)
    assert v1 == handle.get_env(k1)

    k2, v2 = 'B', 'dog'
    handle.put_env(k2, v2)
    assert v2 == handle.get_env(k2)

    assert handle.get_envlist() == {k1: v1, k2: v2}

    with pytest.raises(pamela.PAMError):
        handle.get_env("doesn't exist")

    handle.del_env(k2)

    with pytest.raises(pamela.PAMError):
        handle.get_env(k2)

    assert handle.get_envlist() == {k1: v1}

    # test set_item / get_item
    handle.set_item(pamela.PAM_RHOST, '127.0.0.1')

    assert handle.get_item(pamela.PAM_RHOST) == '127.0.0.1'
    assert handle.get_item(pamela.PAM_RUSER) == None


@pytest.mark.skip(reason="doesn't work on CI")
def test_session():
    handle = pamela.pam_start(getpass.getuser(), 'login')
    handle.open_session()
    handle.close_session()
