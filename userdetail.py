from baseAPITester import login, userdetails
import IATtestvariable

user_details = {}

if __name__ == '__main__':
    user_details['email'] = IATtestvariable.superadmin['email']
    user_details['password'] = IATtestvariable.superadmin['password']
    login(user_details)
    userdetails(user_details)
