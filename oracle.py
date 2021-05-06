from tkinter import StringVar


def register_user():


    print("Enter email address:")
    Email = StringVar()
    print("Enter Password:")
    Password = StringVar()


if Email == "Emre@gmail.com" or Password == "JavaProgram":
    print("Welcome Emre!")

else:
    print("Wrong Email address or Password please try again!")
