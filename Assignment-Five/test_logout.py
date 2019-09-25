import logout

def test_logout():
    print("\n Testing Logout")
    result = logout.logout("zbs25d", 1)
    assert result == True

def test_logout_fail():
    print("\n Testing Fail Logout")
    result = logout.logout("zbs25d", 0)
    assert result == True