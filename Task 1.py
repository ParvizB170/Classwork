username = input("Enter your username:")
username=username.strip()
if username is None or username == "":
    print("Invalid username") 
elif not username[0].isalpha() or len(username)<4:
    print("Username not allowed")
else:
    print("username allowed")