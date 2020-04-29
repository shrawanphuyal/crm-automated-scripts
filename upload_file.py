import IATtestvariable
from baseAPITester import upload_file, login

file = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'file': IATtestvariable.file['name']
}

if __name__ == '__main__':
    login(file)
    upload_file(file)
