from lib.req import do_ping
from lib.sounds import play_sound


if __name__ == '__main__':
    try:
        state = do_ping()
        play_sound()
    except KeyboardInterrupt as e:
        print('Exiting...')
        exit(0)
