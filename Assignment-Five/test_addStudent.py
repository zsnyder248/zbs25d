import addStudent

def test_addStudent():
    print("\n Testing adding student to class")
    result = addStudent.checkStudent(45678)
    assert result == True

def test_addStudent_fail():
    print("\n Testing failure adding student to class")
    result = addStudent.checkStudent(12)
    assert result == True