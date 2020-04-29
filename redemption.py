import IATtestvariable
from baseAPITester import redemption_detail, login

redemption = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'id': IATtestvariable.redemption['id']
}

if __name__ == '__main__':
    login(redemption)
    redemption_detail(redemption)