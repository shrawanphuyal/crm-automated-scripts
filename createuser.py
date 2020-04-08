from baseAPITester import login, createuser
import IATtestvariable

user_details = {}

if __name__ == '__main__':
    user_details['email'] = IATtestvariable.superadmin['email']
    user_details['password'] = IATtestvariable.superadmin['password']
    login(user_details)
    user_details['uemail'] = IATtestvariable.newusr['email']
    user_details['upassword'] = IATtestvariable.newusr['password']
    user_details['fname'] = IATtestvariable.newusr['fname']
    user_details['lname'] = IATtestvariable.newusr['lname']
    user_details['role'] = IATtestvariable.newusr['role']
    createuser(user_details)
