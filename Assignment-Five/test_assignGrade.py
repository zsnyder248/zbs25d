import assignGrade

def test_assignGrade():
    print("\n Testing assigning grade")
    result = assignGrade.grade(12345, 80)
    assert result == True

def test_assignGrade_fail():
    print("\n Testing Fail assign grade")
    result = assignGrade.grade(34567, 200)
    assert result == True