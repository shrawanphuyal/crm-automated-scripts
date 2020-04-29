from baseAPITester import login, order_modify
import IATtestvariable

order = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'id': IATtestvariable.order['id'],
    'locked': IATtestvariable.order['locked']
}

if __name__ == '__main__':
    login(order)
    order_modify(order)
