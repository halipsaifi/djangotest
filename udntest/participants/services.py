import requests
import ast
from django.contrib.auth.models import User

def ec_auth(ecid, password):
    url = 'https://legacy.countway.harvard.edu/ws/ecommonsauth.cgi'
    params = {'user': ecid, 'pass': password}
    r = requests.get(url, params=params)
    resp = r.content.decode("utf-8")
    if r.status_code == 200 and resp != 'null':
        data = "{'username':'"+ecid+"',\
        'firstname':'"+resp.split(' ')[0]+"',\
        'lastname':'"+resp.replace('\t', ' ').split(' ')[1]+"',\
        'email':'"+resp.replace('\t', ' ').split(' ')[2]+"'}"
        userInfo = ast.literal_eval(data)
        print(userInfo)
        return userInfo
    else:
        return None


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False
