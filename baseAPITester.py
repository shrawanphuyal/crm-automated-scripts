import requests
import json
import bs4
import os
import IATtestvariable


def login(user_details):
    login_url = IATtestvariable.server_url + '/api/token/'
    data = {
        'email': user_details['email'],
        'password': user_details['password']
    }
    login = requests.post(login_url, data)
    access = json.loads(login.text)['access']
    user_details['access'] = access
    return user_details


def passchange(user_details):
    passchange_url = IATtestvariable.server_url + '/api/accounts/password/change/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'password': user_details['newpass']
    }
    passchange = requests.post(url=passchange_url, data=data, headers=headers)
    print(passchange.text)
    return user_details


def userdetails(user_details):
    userdetails_url = IATtestvariable.server_url + '/api/accounts/users-me/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    userdetails = requests.get(url=userdetails_url, headers=headers)
    print(userdetails.text)
    return user_details


def otheruserdetails(user_details):
    otheruserdetails_url = IATtestvariable.server_url + '/api/accounts/users/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    otheruserdetails = requests.get(url=otheruserdetails_url, headers=headers)
    print(otheruserdetails.text)
    return user_details


def updateuser(user_details):
    updateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'email': user_details['uemail'],
        'firstname': user_details['fname'],
        'lastname': user_details['lname'],
        'password': user_details['upassword'],
        'role': user_details['role']
    }
    updateuser = requests.put(url=updateuser_url.format(user_details['userid']), data=data, headers=headers)
    print(updateuser.text)
    return user_details


def deactivateuser(user_details):
    deactivateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'is_active': 'False'
    }
    deactivateuser = requests.put(url=deactivateuser_url.format(user_details['userid']), data=data, headers=headers)
    print(deactivateuser.text)
    return user_details


def createuser(user_details):
    createuser_url = IATtestvariable.server_url + '/api/accounts/createuser/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'email': user_details['uemail'],
        'firstname': user_details['fname'],
        'lastname': user_details['lname'],
        'password': user_details['upassword'],
        'role': user_details['role']
    }
    createuser = requests.post(url=createuser_url, data=data, headers=headers)
    print(createuser.text)
    user_details['userid'] = json.loads(createuser.text)['id']
    print(createuser.text)
    return user_details


def audittrail(user_details):
    audittrail_url = IATtestvariable.server_url + '/audittrial/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    audittrail = requests.get(url=audittrail_url, headers=headers)
    print(audittrail.text)
    return user_details


def allorder(order):
    order_url = IATtestvariable.server_url + '/orders/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    order = requests.get(url=order_url, headers=headers)
    print(order.text)
    return order


def order_details(order):
    order_details_url = IATtestvariable.server_url + '/order-detail/{0}/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    order_details = requests.get(url=order_details_url.format(order['id']), headers=headers)
    print(order_details.text)
    return order


def order_modify(order):
    order_modify_url = IATtestvariable.server_url + '/order-detail/{0}/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        "locked": order['locked'],
    }
    order_details = requests.put(url=order_modify_url.format(order['id']), data=data, headers=headers)
    print(order_details.text)
    return order


def order_locked(order):
    order_locked_url = IATtestvariable.server_url + '/getorder/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        'id': order['id']
    }
    order_details = requests.post(url=order_locked_url, data=data, headers=headers)
    print(order_details.text)
    return order


def margincal(margin):
    margin_url = IATtestvariable.server_url + '/margincalculator/'
    headers = {
        'Authorization': 'Bearer ' + margin['access']
    }
    data = {
        'merchant_name': margin['merchant'],
        'department_name': margin['department']
    }
    margincal = requests.get(url=margin_url, data=data, headers=headers)
    print(margincal.text)
    return margin


def redemption_detail(redemption):
    redemption_url = IATtestvariable.server_url + '/order/{0}/'
    headers = {
        'Authorization': 'Bearer ' + redemption['access']
    }
    redemption_detail = requests.get(url=redemption_url.format(redemption['id']), headers=headers)
    print(redemption_detail.text)
    return redemption


def create_refund(refund):
    refund_url = IATtestvariable.server_url + '/create-refund/'
    headers = {
        'Authorization': 'Bearer ' + refund['access']
    }
    data = {
        'orders': IATtestvariable.refund['orders'],
        'product': IATtestvariable.refund['product'],
        'refundReason': IATtestvariable.refund['reason'],
        'refundAdditionalInfo': IATtestvariable.refund['addinfo'],
        'refundAttachment1': IATtestvariable.refund['attach1'],
        'refundAttachment2': IATtestvariable.refund['attach2'],
        'refundAttachment3': IATtestvariable.refund['attach3'],
        'zendeskID': IATtestvariable.refund['zendeskID']
    }
    create_refund = requests.post(url=refund_url, data=data, headers=headers)
    print(create_refund.text)
    return refund


def update_refund(refund):
    refund_url = IATtestvariable.server_url + '/update-refund/'
    headers = {
        'Authorization': 'Bearer ' + refund['access']
    }
    data = {
        'orders': refund['orders'],
        'product': refund['product'],
        'refundAdditionalInfo': refund['addinfo'],
        'refundAttachment1': refund['attach1'],
        'refundAttachment2': refund['attach2'],
        'refundAttachment3': refund['attach3'],
        'zendeskID': refund['zendeskID']
    }
    update_refund = requests.post(url=refund_url, data=data, headers=headers)
    print(update_refund.text)
    return refund


def upload_file(file):
    file_upload_url = IATtestvariable.server_url + '/file1/'
    headers = {
        'Authorization': 'Bearer ' + file['access']
    }
    file1 = {
        'file': file['file']
    }
    upload_file = requests.post(url=file_upload_url, files=file1, headers=headers)
    print(upload_file.text)
    return file

