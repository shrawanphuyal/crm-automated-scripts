import baseAPITester
import IATtestvariable

user_details = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'uemail': IATtestvariable.newusr['email'],
    'upassword': IATtestvariable.newusr['newpass'],
    'fname': IATtestvariable.newusr['fname'],
    'lname': IATtestvariable.newusr['lname'],
    'role': IATtestvariable.newusr['role'],
    'value': 20,
    'order_id': IATtestvariable.refund['orders'],
    'orders': IATtestvariable.refund['orders'],
    'product': IATtestvariable.refund['product'],
    'refundReason': IATtestvariable.refund['reason'],
    'addinfo': IATtestvariable.refund['addinfo'],
    'attach1': IATtestvariable.refund['attach1'],
    'attach2': IATtestvariable.refund['attach2'],
    'attach3': IATtestvariable.refund['attach3'],
    'zendeskID': IATtestvariable.refund['zendeskID'],
    'merchant': IATtestvariable.margin['merchant_name'],
    'department': IATtestvariable.margin['department_name'],
    'orderid': IATtestvariable.order['id'],
    'locked': IATtestvariable.order['locked'],
    'redem_id': IATtestvariable.redemption['id'],
    'file': IATtestvariable.file['name']
}

if __name__ == '__main__':

    baseAPITester.login(user_details)
    baseAPITester.createuser(user_details)
    baseAPITester.otheruserdetails(user_details)
    baseAPITester.userdetails(user_details)
    baseAPITester.updateuser(user_details)
    baseAPITester.audittrail(user_details)
    baseAPITester.allorder(user_details)
    baseAPITester.order_details(user_details)
    baseAPITester.order_modify(user_details)
    baseAPITester.order_locked(user_details)
    baseAPITester.create_refund(user_details)
    baseAPITester.update_refund(user_details)
    #baseAPITester.check_refund(user_details)
    baseAPITester.delivery_fund(user_details)
    baseAPITester.redemption_detail(user_details)
    baseAPITester.update_refund(user_details)
    baseAPITester.margincal(user_details)
    baseAPITester.user_delete(user_details)
    print(user_details['userid'])

