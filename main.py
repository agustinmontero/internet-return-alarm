from lib.req import do_ping
from lib.sounds import play_sound


if __name__ == '__main__':
    from time import sleep
    state = 0
    try:
        while not state:
            sleep(10)
            # state = check_request()
            state = do_ping(iface='enp1s0')
        play_sound()
    except KeyboardInterrupt as e:
        print('Saliendo de la aplicacion...')
        exit(0)
