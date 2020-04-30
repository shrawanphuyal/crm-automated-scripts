from baseAPITester import login, passchange
import IATtestvariable

user_details = {
    'email': IATtestvariable.newusr['email'],
    'password': IATtestvariable.newusr['password'],
    'newpass': IATtestvariable.newusr['newpass']
}

if __name__ == '__main__':
    login(user_details)
    print(user_details)
    passchange(user_details)
