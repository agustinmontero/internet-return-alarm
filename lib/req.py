import requests
import os
from requests.exceptions import HTTPError, Timeout, ConnectionError


def check_request(url_check='http://www.google.com.ar'):
    try:
        r = requests.get(url_check, timeout=10)
        r.raise_for_status()
    except (HTTPError, Timeout, ConnectionError):
        # print('Error en la conexion.')
        return False
    else:
        print(r.url, 'downloaded successfully', url_check)
        return True


def do_ping(hostname='8.8.8.8', iface=None):
    if iface:
        ping_cmd = "ping -I {} -c 1 {} &> /dev/null".format(iface, hostname)
    else:
        ping_cmd = "ping -c 1 {} &> /dev/null".format(hostname)
    response = os.system(ping_cmd)
    if response == 0:
        return True
    else:
        return False
