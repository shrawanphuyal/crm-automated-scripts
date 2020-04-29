from baseAPITester import login, order_locked
import IATtestvariable

order = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'id': IATtestvariable.order['id']
}

if __name__ == '__main__':
    login(order)
    order_locked(order)
