from subprocess import Popen, STDOUT, PIPE, check_output
from time import sleep
import keyboard
import re
import playsound
import os
import pyttsx3

def playino(mytext):
    playsound.playsound(os.path.join(os.getcwd(), 'tempaud', mytext + '.mp3'))

def connect2wifi(wifi_name,passwordy):
    handle = Popen('netsh wlan connect '+wifi_name, stdout=PIPE, stdin=PIPE, shell=True,  stderr=STDOUT)

    sleep(10)

    handle.stdin.write((passwordy+'\n').encode())
    while handle.poll() == None:
        print(handle.stdout.readline().strip())

    playino('fini')

def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        return False


def scanforwifi():

    results = check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii")  # needed in python 3
    results = results.replace("\r", "")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    ssids.remove('')
    return ssids


def getpass():
    playino('passkey')
    bol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
    i = 0
    not_selected = True
    closer = True
    keyphrase = None
    difty = False


    while not_selected:

        if len(bol)-1 < i:
            playino(bol[len(bol)-1])
            i = len(bol)-1
            difty = True
            sleep(0.4)


        else:
            playino(bol[i])
            sleep(0.4)

        while True:

            if keyboard.is_pressed('a'):
                i+=1
                break
            elif keyboard.is_pressed('s'):

                if keyphrase == None:
                    keyphrase = bol[i]
                    playino('beep')
                else:
                    keyphrase = keyphrase + bol[i]
                    playino('beep')

                i = 0
                break
            elif keyboard.is_pressed('d'):
                i+=5
                break
            elif keyboard.is_pressed('o'):
                not_selected = False
                break

            if difty == False:
                pass

            else:
                i = 0
                difty = False


    return keyphrase

def casing_check(keyphrase):
    playino('casing')
    termi = False
    fin_phrase = []
    for l in keyphrase:
        print(l)
        sleep(0.15)
        while True:
            if l.isdigit():
                fin_phrase.append(l)
                break
            else:
                if keyboard.is_pressed('a'):
                    fin_phrase.append(l.upper())
                    break
                elif keyboard.is_pressed('s'):
                    fin_phrase.append(l.lower())
                    break
                elif keyboard.is_pressed('d'):
                    termi = True
                    break

        if termi == True:
            break
        else:
            pass
    return ''.join(fin_phrase)

def ssidsnatch():
    playino('ssidsn')
    termi = False

    while not termi:
        for i in scanforwifi():
            ssid_main = i.split(re.findall(r'\w+\s\d+\s:\s',i)[0])[1]
            nonetsay(ssid_main)
            sleep(0.15)
            while True:
                if keyboard.is_pressed('a'):
                    break
                elif keyboard.is_pressed('s'):
                    playino('beep')
                    return ssid_main
                elif keyboard.is_pressed('d'):
                    termi = True
                    break

            if termi == True:
                break
            else:
                pass

def nonetsay(text):
    try:
        something = pyttsx3.init()
        something.setProperty('rate', 160)
        something.say(text)
        something.runAndWait()

    except Exception as e:
        print(e)

def main():

    wifiname = ssidsnatch()
    pass_fina = casing_check(getpass())
    connect2wifi(wifi_name=wifiname,passwordy=pass_fina)
    if internet():
        nonetsay('successfully connected to the internet')
    else:
        nonetsay('process failed')

