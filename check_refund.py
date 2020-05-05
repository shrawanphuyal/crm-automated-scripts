import IATtestvariable
from baseAPITester import check_refund, login

check = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
}

if __name__ == '__main__':
    login(check)
    check_refund(check)
