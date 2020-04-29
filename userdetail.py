from baseAPITester import login, userdetails
import IATtestvariable

user_details = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password']
}

if __name__ == '__main__':
    login(user_details)
    userdetails(user_details)
