from baseAPITester import login, audittrail
import IATtestvariable

order = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password']
}

if __name__ == '__main__':
    login(order)
    audittrail(order)
