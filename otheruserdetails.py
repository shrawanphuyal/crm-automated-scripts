from baseAPITester import login, otheruserdetails
import IATtestvariable

user_details = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password']
}

if __name__ == '__main__':
    login(user_details)
    otheruserdetails(user_details)
