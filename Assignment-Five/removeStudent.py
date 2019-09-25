classList = [12345, 23456]
def removeStudent(pawPrint):
    if (pawPrint in classList):
        classList.remove(pawPrint)
        return True

def checkStudent(pawPrint):
    #Check if student ID is valid
    count = 0
    paw = pawPrint
    while(pawPrint>0):
        count = count+1
        pawPrint = pawPrint//10

    if(count<3):
        return False
    else:
        result = removeStudent(paw)
    return result

def main():
    print(checkStudent(12345))

if __name__ == "__main__":
    main()