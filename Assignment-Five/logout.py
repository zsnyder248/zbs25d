def logout(username, log):
    if (username):
        if(log == 1):
            #1 means the student has clicked the logout button
            return True
        else:
            return False

def main():
    print(logout("zbs25d", 1))

if __name__ == "__main__":
    main()