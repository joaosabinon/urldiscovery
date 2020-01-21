#!/usr/bin/python
import webbrowser
import pyscreenshot as ImageGrab
import time

url = "https://google.com.br"

if __name__ == "__main__":

    web = webbrowser.open(url, new=0, autoraise=True)
    time.sleep(4)
    im = ImageGrab.grab(backend='gnome-screenshot')  # X1,Y1,X2,Y2
    im.show()

#webbrowser.cle()