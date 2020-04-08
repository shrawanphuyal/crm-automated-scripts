from baseAPITester import login, passchange
import IATtestvariable
user_details = {}

if __name__ == '__main__':
    user_details['uemail'] = IATtestvariable.newusr['email']
    user_details['upassword'] = IATtestvariable.newusr['password']
    user_details['newpass'] = IATtestvariable.newusr['newpass']
    login(user_details)
    passchange(user_details)
