def logIn(username, password):
    if (username):
        if(password == "password"):
            return True
        else:
            return False

def main():
    print(logIn("zbs25d", "password"))

if __name__ == "__main__":
    main()