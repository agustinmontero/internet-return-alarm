import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError


def hacer_ping(url_check='http://www.google.com.ar'):
    try:
        r = requests.get(url_check, timeout=10)
        r.raise_for_status()
    except (HTTPError, Timeout, ConnectionError):
        # print('Error en la conexion.')
        return 0
    else:
        print(r.url, 'downloaded successfully', url_check)
        return 1