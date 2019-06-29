import requests
import subprocess
import os
import io
import shlex
import time
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
    if iface or os.environ.get('IFACE'):
        ping_cmd = "ping -I {} -c 1 {}".format(os.environ.get('IFACE', iface), hostname)
    else:
        ping_cmd = "ping -c 1 {}".format(hostname)
    ping_args = shlex.split(ping_cmd)
    while True:
        with io.open(os.devnull, 'wb') as devnull:
            try:
                subprocess.check_call(
                    ping_args,
                    stdout=devnull, stderr=devnull)
            except subprocess.CalledProcessError:
                time.sleep(10)
            else:
                return True
