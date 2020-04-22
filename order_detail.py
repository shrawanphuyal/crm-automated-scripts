from baseAPITester import login, order_details
import IATtestvariable
order = {}
user_details = {}
if __name__ == '__main__':
    order['email'] = IATtestvariable.superadmin['email']
    order['password'] = IATtestvariable.superadmin['password']
    login(order)
    user_details['access'] = order['access']
    order['id'] = IATtestvariable.order['id']
    order_details(order)
