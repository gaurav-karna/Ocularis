import time
import requests
from xml.etree import ElementTree
import os
import playsound
import datetime
import multiprocessing
import keyboard


def playerasync(uid):

    playsound.playsound(os.path.join(os.getcwd(), 'majortempaud', uid + '.wav'),False)

def checker():

    while 1:
        if keyboard.is_pressed('d'):
            break


class TextToSpeech(object):
    def __init__(self, subscription_key,texty):
        self.subscription_key = subscription_key
        self.tts = texty
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None


def get_token(self):
    fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    headers = {
        'Ocp-Apim-Subscription-Key': self.subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    self.access_token = str(response.text)


def save_audio(self,uid):
    base_url = 'https://westus.tts.speech.microsoft.com/'
    path = 'cognitiveservices/v1'
    constructed_url = base_url + path
    headers = {
        'Authorization': 'Bearer ' + self.access_token,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'User-Agent': 'Ocularis_TTS'
    }
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
    voice.text = self.tts
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)
    if response.status_code == 200:
        with open(os.path.join(os.getcwd(), 'majortempaud', uid + '.wav'), 'wb') as audio:
            audio.write(response.content)
            print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")




def modular_speech(text):
    try:
        subscription_key = "51140fb620194c33b1e60d3df44bfd1f"
        now = datetime.datetime.now()
        uid = str(now.date()) + str(now.hour) + str(now.minute) + str(now.second)
        app = TextToSpeech(subscription_key,text)
        get_token(app)
        save_audio(app,uid)
        p1 = multiprocessing.Process(target=checker)
        p2 = multiprocessing.Process(target=playerasync(uid))
        p1.start()
        p2.start()
        # p.join()
        p2.terminate()
        if p2.is_alive():
            p2.terminate()

    except Exception as e:
        print(e)




if __name__ == '__main__':
    # creating processes
    modular_speech('hey there macha how are you,its been a great pleasure talking to you, do you know how happy iam at this point of time')

    # both processes finished
    print("Done!")

