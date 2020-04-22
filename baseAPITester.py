import requests
import json
import bs4
import lxml
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
    audittrail_url = IATtestvariable.server_url + '/autittrail'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    audittrail = requests.get(url=audittrail_url, headers=headers)
    print(audittrail.text)
    return user_details


def order(order):
    order_url = IATtestvariable.server_url + '/orders/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        'to': order['to'],
        'from': order['from'],
        'redemptionid': order['redemptionid'],
        'uuid': order['uuid'],
        'email': order['email'],
        'status': order['status'],
        'merchant': order['merchant'],
        'sort': order['sort']
    }
    order = requests.post(url=order_url, data=data, headers=headers)
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
    order_details_url = IATtestvariable.server_url + '/order-detail/{0}/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        "locked": order['locked'],
    }
    order_details = requests.put(url=order_details_url.format(order['id']), data=data, headers=headers)
    print(order_details.text)
    return order


def order_locked(order):
    order_details_url = IATtestvariable.server_url + '/getorder/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        'id': order['id']
    }
    order_details = requests.post(url=order_details_url, data=data, headers=headers)
    print(order_details.text)
    return order

