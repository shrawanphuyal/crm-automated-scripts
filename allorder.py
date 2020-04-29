from baseAPITester import login, allorder
import IATtestvariable

order = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password']
}

if __name__ == '__main__':
    login(order)
    allorder(order)
