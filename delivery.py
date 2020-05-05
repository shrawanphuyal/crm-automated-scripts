import IATtestvariable
from baseAPITester import delivery_fund, login

check = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'value': 20,
    'order_id': IATtestvariable.refund['orders'],
}

if __name__ == '__main__':
    login(check)
    delivery_fund(check)