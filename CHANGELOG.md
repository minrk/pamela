# Changes in pamela

## 1.1.0

- Add OTP support in `authenticate` by accepting a list for password.

## 1.0.0

- Add environment methods to PAMHandle: get_env, put_env, del_env, get_envlist
- Add item methods to PAMHandle: get_item, set_item
- Add session methods to PAMHandle: open_session, close_session
- Allow leaving transactions open with `close=False` argument to `authenticate`,
  in which case the PAMHandle object is returned

## 0.3.0

- Support setcred flags besides reinitialize
- Allow change_password to be noninteractive

## 0.2.0

- Rename PamException to PAMError

## 0.1.0 - first release
