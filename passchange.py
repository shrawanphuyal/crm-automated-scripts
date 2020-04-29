from baseAPITester import login, passchange
import IATtestvariable

user_details = {
    'uemail': IATtestvariable.newusr['email'],
    'upassword': IATtestvariable.newusr['password'],
    'newpass': IATtestvariable.newusr['newpass']
}

if __name__ == '__main__':
    login(user_details)
    passchange(user_details)
