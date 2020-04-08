from baseAPITester import login, deactivateuser
import IATtestvariable

user_details = {}

if __name__ == '__main__':
    user_details['email'] = IATtestvariable.superadmin['email']
    user_details['password'] = IATtestvariable.superadmin['password']
    login(user_details)
    user_details['userid'] = '12'
    deactivateuser(user_details)
