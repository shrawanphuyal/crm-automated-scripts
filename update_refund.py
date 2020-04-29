import IATtestvariable
from baseAPITester import update_refund, login

refund = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'orders': IATtestvariable.refund['orders'],
    'product': IATtestvariable.refund['product'],
    'addinfo': IATtestvariable.refund['addinfo'],
    'attach1': IATtestvariable.refund['attach1'],
    'attach2': IATtestvariable.refund['attach2'],
    'attach3': IATtestvariable.refund['attach3'],
    'zendeskID': IATtestvariable.refund['zendeskID']
}

if __name__ == '__main__':
    login(refund)
    update_refund(refund)
