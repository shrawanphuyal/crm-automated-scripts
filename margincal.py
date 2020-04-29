import IATtestvariable
from baseAPITester import margincal, login

margin = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'merchant': IATtestvariable.margin['merchant_name'],
    'department': IATtestvariable.margin['department_name'],
}

if __name__ == '__main__':
    login(margin)
    margincal(margin)