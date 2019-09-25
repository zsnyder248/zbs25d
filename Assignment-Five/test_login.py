import login

def test_login():
    print("\n Testing Login")
    result = login.logIn("zbs25d", "password")
    assert result == True

def test_login_fail():
    print("\n Testing Fail Login")
    result = login.logIn("zbs25d", "pass")
    assert result == True