import requests
from django.contrib.auth.models import User

def ec_auth(ecid, password):
    url = 'https://legacy.countway.harvard.edu/ws/ecommonsauth.cgi'
    params = {'user': ecid, 'pass': password}
    r = requests.get(url, params=params)
    resp = r.content.decode("utf-8")
    if r.status_code == 200 and resp != 'null':
        userInfo = {'username' : ecid}
        return userInfo
    else:
        return None


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False
