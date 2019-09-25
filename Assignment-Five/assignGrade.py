def grade(pawPrint, grd):
    if(grd < 0 or grd > 100):
        return False
    else:
        return checkStudent(pawPrint, grd)

def checkStudent(pawPrint, grd):
    #Check if student ID is valid
    count = 0
    paw = pawPrint
    while(pawPrint>0):
        count = count+1
        pawPrint = pawPrint//10

    if(count<3):
        return False
    else:
        return assignGrade(paw, grd)

def assignGrade(pawPrint, grd):
    #Assign the valid grade to the valid pawPrint in a database
    return True

def main():
    print(grade(12345, 95))

if __name__ == "__main__":
    main()