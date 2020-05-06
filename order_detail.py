from baseAPITester import login, order_details
import IATtestvariable

order = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'orderid': IATtestvariable.order['id']
}

if __name__ == '__main__':
    login(order)
    order_details(order)
