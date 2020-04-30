from baseAPITester import login, deactivateuser
import IATtestvariable

user_details = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'userid': IATtestvariable.newusr['userid']
}

if __name__ == '__main__':
    login(user_details)
    deactivateuser(user_details)
