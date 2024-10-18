from exceptions import RegistrationError

class NewUser():

    def __init__ (self):
        self.username = input("Please enter your username:")
        self.password = input("Please enter your password:")
        self.registration(self.username, self.password)
        
    def registration(self, username, password):
        if not(isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha()):
            raise RegistrationError("Incorrect username")
            
        if not(isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum()):
            raise RegistrationError("Incorrect password")

        print("Регистрация прошла успешно!")

while True:
    try:
        user = NewUser()
        break
    except RegistrationError:
        print("Ошибка регистрации!")