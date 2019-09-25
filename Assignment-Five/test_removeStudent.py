import removeStudent

def test_addStudent():
    print("\n Testing removing student from a class")
    result = removeStudent.checkStudent(23456)
    assert result == True

def test_addStudent_fail():
    print("\n Testing failure removing student from a class")
    result = removeStudent.checkStudent(6079)
    assert result == True