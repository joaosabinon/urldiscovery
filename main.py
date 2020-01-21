#!/usr/bin/python
import webbrowser
import pyscreenshot as ImageGrab
import time
import datetime
import hashlib
import re

url = "https://google.com.br"

# take the archive name
def archiveName(string):
    cleanString = re.sub('[^A-Za-z0-9]+', '', string)
    stringCipher = hashlib.md5(cleanString.encode())
    return str(stringCipher.hexdigest())

def discovery():
    if __name__ == "__main__":
        #open the site
        webbrowser.open(url, new=0, autoraise=True)
        time.sleep(4)

        #take the screenshot
        im = ImageGrab.grab(backend='gnome-screenshot')  # X1,Y1,X2,Y2

        #save the screenshot
        now = datetime.datetime.now()
        archive = archiveName(str(now))
        path = '/tmp/'+archive+'.png'
        im.save(path)

        #return the path
        return str(path)

discovery()



