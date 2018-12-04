from pygame import mixer, error
from time import sleep


def play_sound():
    try:
        mixer.init()
        mixer.music.load('./lib/alarm.mp3')
        mixer.music.play()
        sleep(15)
        mixer.music.stop()
    except (KeyboardInterrupt, error) as message:
        print("No se pudo reproducir el sonido")
        raise SystemExit(message)