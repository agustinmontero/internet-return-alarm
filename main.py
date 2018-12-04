from lib.req import hacer_ping
from lib.sounds import play_sound


if __name__ == '__main__':
    from time import sleep
    state = 0
    try:
        while state == 0:
            sleep(10)
            state = hacer_ping()
        play_sound()
    except KeyboardInterrupt as e:
        print('Saliendo de la aplicacion...')
        exit(0)
