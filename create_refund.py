import IATtestvariable
from baseAPITester import create_refund, login

refund = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'orders': IATtestvariable.refund['orders'],
    'product': IATtestvariable.refund['product'],
    'refundReason': IATtestvariable.refund['reason'],
    'addinfo': IATtestvariable.refund['addinfo'],
    'attach1': IATtestvariable.refund['attach1'],
    'attach2': IATtestvariable.refund['attach2'],
    'attach3': IATtestvariable.refund['attach3'],
    'zendeskID': IATtestvariable.refund['zendeskID']
}

if __name__ == '__main__':
    login(refund)
    create_refund(refund)