from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import tinify
import datetime
import multiprocessing
from xml.etree import ElementTree
from azure.cognitiveservices.search.newssearch import NewsSearchAPI
import re
from azure.cognitiveservices.vision.computervision import ComputerVisionAPI
from msrest.authentication import CognitiveServicesCredentials
from urllib.parse import parse_qs
from urllib.parse import urlparse
from builtins import input
from utils import create_uber_client
from utils import fail_print
from utils import import_oauth2_credentials
from utils import paragraph_print
from utils import response_print
from utils import success_print
from uber_rides.client import SurgeError
from uber_rides.errors import ClientError
from uber_rides.errors import ServerError
import face_recognition
import os
import shutil
from time import sleep
import urllib.request
import pyap
import playsound
import azure.cognitiveservices.speech as speechsdk
import requests
import json
from PIL import Image
import cv2
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
import keyboard
import time
import subprocess
import soundfile as sf
import pyttsx3

if os.path.exists(os.path.join(os.getcwd(), 'folder_images')):
    pass
else:
    os.mkdir(os.path.join(os.getcwd(), 'folder_images'))

if os.path.exists(os.path.join(os.getcwd(), 'tempimages')):
    pass
else:
    os.mkdir(os.path.join(os.getcwd(), 'tempimages'))

if os.path.exists(os.path.join(os.getcwd(), 'majortempaud')):
    # os.rmdir(os.path.join(os.getcwd(), 'majortempaud'))
    shutil.rmtree(os.path.join(os.getcwd(), 'majortempaud'))
    os.mkdir(os.path.join(os.getcwd(), 'majortempaud'))
else:
    os.mkdir(os.path.join(os.getcwd(), 'majortempaud'))

if os.path.exists(os.path.join(os.getcwd(), 'temp.mp3')):
    os.remove('temp.mp3')

bingMapsKey = 'Ar_sR9YDasSzQx0unCEyCqmb9cqIivEp4qHFYCCfuAYJfiZriQcMuYFt_IRzvR3b '
tinify.key = "XhGGcrKhVkpTLSr7m7ZdRsz18DCgxdww"
cameraResolution = (1024, 768)


def playerasync():
    # playsound.playsound(os.path.join(os.getcwd(), 'majortempaud', '2019-03-0725129' + '.wav'),False)
    # print('j')
    subprocess.run(['python', 'speech_init.py'])


def checker():
    time_start = time.time()
    while sound_dur > (time.time() - time_start) :
        if keyboard.is_pressed('d'):
            break


class TextToSpeech(object):
    def __init__(self, subscription_key, texty):
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


def save_audio(self, uid):
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

    else:
        print("\nStatus code: " + str(
            response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

def clock():
    try:
        something = pyttsx3.init()
        something.setProperty('rate', 160)
        something.say(datetime.datetime.now().strftime('today is %d    %m, the time is %H %M'))
        something.runAndWait()

    except Exception:
        pass


def modular_speech(text):
    try:
        global sound_dur
        subscription_key = "51140fb620194c33b1e60d3df44bfd1f"
        now = datetime.datetime.now()
        uid = str(now.date()) + str(now.hour) + str(now.minute) + str(now.second)
        app = TextToSpeech(subscription_key, text)
        get_token(app)
        save_audio(app, uid)
        sound_template = sf.SoundFile(os.path.join(os.getcwd(), 'majortempaud', uid + '.wav'))
        sound_dur = len(sound_template) / sound_template.samplerate
        # p1 = multiprocessing.Process(target=checker)
        # p2 = multiprocessing.Process(target=playerasync())
        # p1.start()
        # p2.start()
        # p2.join()
        # p2.terminate()
        # p1.terminate()
        proc = subprocess.Popen(['python', 'speech_init.py', uid])
        checker()
        proc.kill()
        sleep(1)


    except Exception as e:
        print(e)


def speak_label(mytext):
    playsound.playsound(os.path.join(os.getcwd(), 'tempaud', mytext + '.mp3'))
    # speak
    while True:

        if keyboard.is_pressed('a'):
            break
        if keyboard.is_pressed('s'):
            global opener
            opener = True
            break
        if keyboard.is_pressed('q'):
            speak_label('goodbye')
            quit()


def naviagtor(mlon, mlat, loc):
    prevlen = 0

    while 1:

        # input information
        longitude = mlon
        latitude = mlat
        destination = str(loc)

        encodedDest = urllib.parse.quote(destination, safe='')

        routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(latitude) + "," + str(
            longitude) + "&wp.1=" + encodedDest + "&key=" + bingMapsKey

        request = urllib.request.Request(routeUrl)
        response = urllib.request.urlopen(request)

        r = response.read().decode(encoding="utf-8")
        result = json.loads(r)

        itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
        route_distance = result["resourceSets"][0]["resources"][0]["travelDistance"]

        directions = []
        main_dist = []

        # pprint.pprint(result)
        for item in itineraryItems:
            if float(item["travelDistance"]) < 1:
                org_distance = str(float(item["travelDistance"]) * 1000) + ' metre '
            else:
                org_distance = str(item["travelDistance"]) + 'kilometre'

            directions.append(item["instruction"]["text"] + ' in ' + org_distance)
            main_dist.append(float(item["travelDistance"] * 1000))

        # print(main_dist)
        if int(main_dist[0]) < 10:
            modular_speech(directions[1])

        if len(directions) - prevlen == 0:
            pass
        else:
            modular_speech(directions[0])

        # print(directions)

        prevlen = len(directions)

        if keyboard.is_pressed('s') == 0:
            if int(main_dist[0]) < 10:
                modular_speech(directions[1])
            else:
                modular_speech(directions[0])

        if keyboard.is_pressed('d') == 0:
            break

        num = 4

        # since average human walking speed is 1.6m per second
        start = time.time()
        while 1:
            if (time.time() - start) > num:
                break
            if keyboard.is_pressed('s') == 0:
                if int(main_dist[0]) < 10:
                    modular_speech(directions[1])
                else:
                    modular_speech(directions[0])

            if keyboard.is_pressed('d') == 0:
                break


def location(address):
    addresses = pyap.parse(address, country='US')
    return addresses[0]


# location('can you direct me to 1394 Woodridge Lane Memphis Tennessee')

def speech2text():
    speech_key, service_region = "30bf61e9604041eba9e79231abfa89af", "westus"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return 'error please try again'
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
        return 'error please try again'


def find_loc_address(address):
    encoded_dest = urllib.parse.quote(address, safe='')
    endpoint = 'http://dev.virtualearth.net/REST/v1/Locations?q=' + encoded_dest + '&key=' + bingMapsKey
    request = urllib.request.Request(endpoint)
    response = urllib.request.urlopen(request)

    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)
    res_Check = result["resourceSets"][0]["resources"][0]['geocodePoints'][1]['coordinates']
    return res_Check
    # print(json.dumps(res_Check, indent=2))


def currentad_seletest():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait

    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude, longitude)


def save_speech(mytext):
    playsound.playsound(os.path.join(os.getcwd(), 'tempaud', mytext + '.mp3'))


def currentad():
    send_url = "http://api.ipstack.com/check?access_key=c687e4498fc801d7a66e9b42fb2f6e50"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    return [latitude, longitude]


def directions():
    try:
        # lat,lon = find_loc_address('1427 Alderbrook Ln San Jose CA 95129')
        save_speech('whereDoYouWantToGo')
        speech = speech2text()
        mlat, mlon = currentad()
        try:
            loc = location(speech)
        except IndexError:
            loc = speech
        naviagtor(mlon, mlat, loc)
    except Exception:
        save_speech('error')


def weather():
    latt, long = currentad()
    endpoint = 'http://api.openweathermap.org/data/2.5/forecast?'
    api_key = 'e33c84cc9eb1157c533611a494f638a3'
    nav_request = 'lat={}&lon={}&APPID={}'.format(latt, long, api_key)
    request = endpoint + nav_request
    # Sends the request and reads the response.
    response = urllib.request.urlopen(request).read().decode('utf-8')
    # Loads response as JSON
    weather = json.loads(response)
    current_temp = weather['list'][0]['main']['temp']
    temp_c = current_temp - 273.15
    temp_c_str = str(int(temp_c)) + ' degree Celsius '
    descript_place = weather['list'][0]['weather'][0]['main']
    modular_speech(descript_place + ' ' + temp_c_str)


def uber():
    UFP_PRODUCT_ID = '26546650-e557-4a7b-86e7-6a3942445247'

    SURGE_PRODUCT_ID = 'd4abaae7-f4d6-4152-91cc-77523e8165a4'

    save_speech('whereDoYouWantToGo')
    speech = speech2text()
    START_LAT, START_LNG = currentad()
    try:
        loc = location(speech)
    except IndexError:
        loc = speech

    END_LAT, END_LNG = find_loc_address(loc)

    def estimate_ride(api_client):

        try:
            estimate = api_client.estimate_ride(
                product_id=SURGE_PRODUCT_ID,
                start_latitude=START_LAT,
                start_longitude=START_LNG,
                end_latitude=END_LAT,
                end_longitude=END_LNG,
                seat_count=2
            )

        except (ClientError, ServerError) as error:
            fail_print(error)

        else:
            success_print(estimate.json)

    def update_surge(api_client, surge_multiplier):

        try:
            update_surge = api_client.update_sandbox_product(
                SURGE_PRODUCT_ID,
                surge_multiplier=surge_multiplier,
            )

        except (ClientError, ServerError) as error:
            fail_print(error)

        else:
            success_print(update_surge.status_code)

    def update_ride(api_client, ride_status, ride_id):

        try:
            update_product = api_client.update_sandbox_ride(ride_id, ride_status)

        except (ClientError, ServerError) as error:
            fail_print(error)

        else:
            message = '{} New status: {}'
            message = message.format(update_product.status_code, ride_status)
            success_print(message)

    def request_ufp_ride(api_client):

        try:

            estimate = api_client.estimate_ride(
                product_id=UFP_PRODUCT_ID,
                start_latitude=START_LAT,
                start_longitude=START_LNG,
                end_latitude=END_LAT,
                end_longitude=END_LNG,
                seat_count=2
            )
            fare = estimate.json.get('fare')

            request = api_client.request_ride(
                product_id=UFP_PRODUCT_ID,
                start_latitude=START_LAT,
                start_longitude=START_LNG,
                end_latitude=END_LAT,
                end_longitude=END_LNG,
                seat_count=2,
                fare_id=fare['fare_id']
            )

        except (ClientError, ServerError) as error:
            fail_print(error)
            return

        else:
            success_print(estimate.json)
            success_print(request.json)
            return request.json.get('request_id')

    def request_surge_ride(api_client, surge_confirmation_id=None):

        try:
            request = api_client.request_ride(
                product_id=SURGE_PRODUCT_ID,
                start_latitude=START_LAT,
                start_longitude=START_LNG,
                end_latitude=END_LAT,
                end_longitude=END_LNG,
                surge_confirmation_id=surge_confirmation_id,
                seat_count=2
            )

        except SurgeError as e:
            surge_message = 'Confirm surge by visiting: \n{}\n'
            surge_message = surge_message.format(e.surge_confirmation_href)
            response_print(surge_message)

            confirm_url = 'Copy the URL you are redirected to and paste here: \n'
            result = input(confirm_url).strip()

            querystring = urlparse(result).query
            query_params = parse_qs(querystring)
            surge_id = query_params.get('surge_confirmation_id')[0]

            # automatically try request again
            return request_surge_ride(api_client, surge_id)

        except (ClientError, ServerError) as error:
            fail_print(error)
            return

        else:
            success_print(request.json)
            return request.json.get('request_id')

    def get_ride_details(api_client, ride_id):

        try:
            ride_details = api_client.get_ride_details(ride_id)

        except (ClientError, ServerError) as error:
            fail_print(error)

        else:
            success_print(ride_details.json)

    if __name__ == '__main__':
        credentials = import_oauth2_credentials()
        api_client = create_uber_client(credentials)

        # ride request with upfront pricing flow

        modular_speech("Request a ride with upfront pricing product.")
        ride_id = request_ufp_ride(api_client)

        modular_speech("Update ride status to accepted.")
        update_ride(api_client, 'accepted', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)
        update_ride(api_client, 'in_progress', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)

        modular_speech("Update ride status to completed.")
        update_ride(api_client, 'completed', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)

        # ride request with surge flow

        modular_speech("Ride estimates before surge.")
        estimate_ride(api_client)

        modular_speech("Activate surge.")
        update_surge(api_client, 2.0)

        modular_speech("Ride estimates after surge.")
        estimate_ride(api_client)

        modular_speech("Request a ride with surging product.")
        ride_id = request_surge_ride(api_client)

        modular_speech("Update ride status to accepted.")
        update_ride(api_client, 'accepted', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)
        update_ride(api_client, 'in_progress', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)

        modular_speech("Update ride status to completed.")
        update_ride(api_client, 'completed', ride_id)

        modular_speech("Updated ride details.")
        get_ride_details(api_client, ride_id)

        modular_speech("Deactivate surge.")
        update_surge(api_client, 1.0)


def whatsthat():
    try:
        now = datetime.datetime.now()
        timer = str(now.date()) + str(now.hour) + str(now.minute) + str(now.second)

        name_docu = os.path.join(os.getcwd(), 'tempimages', timer + '.jpeg')
        cap = cv2.VideoCapture(0)
        r, image = cap.read()
        cv2.imwrite(name_docu, image)
        cap.release()

        # import cv2
        # img = cv2.imread('makeharvard.png')
        # cv2.imwrite(timer+'.jpeg',img)

        source = tinify.from_file(os.path.join(os.getcwd(), 'tempimages', timer + '.jpeg'))
        url = source.url

        # Get region and key from environment variables

        region = 'westcentralus'
        key = '3202352b4d3e49678aa066c513ae0ef2'

        # Set credentials
        credentials = CognitiveServicesCredentials(key)

        # Create client
        client = ComputerVisionAPI(region, credentials=credentials)
        # url = "http://www.public-domain-photos.com/free-stock-photos-4/travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg"
        language = "en"
        max_descriptions = str(3)

        analysis = client.describe_image(url, max_descriptions, language)

        if len(analysis.captions) > 0:
            captionn = analysis.captions[0].text
            print(captionn)
            modular_speech(captionn)

        else:
            save_speech('unknownError')

    except Exception as e:
        print(e)


def remember():
    # set camera resolution
    name_docu = 'tempface.jpeg'
    cap = cv2.VideoCapture(0)
    r, image = cap.read()
    cv2.imwrite(name_docu, image)
    cap.release()

    image_port = face_recognition.load_image_file(name_docu)
    face_locations = face_recognition.face_locations(image_port)
    # from PIL import Image
    # image = Image.open(name_docu)

    if len(face_locations) > 0:
        # face_location = face_locations = face_recognition.face_locations(image_port)

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            save_speech('nameOfPerson')
            name_person = speech2text()
            pil_image.save(os.path.join(os.getcwd(), 'folder_images', name_person + '.jpeg'))

    else:

        save_speech('noFaces')


def whoisthat():
    try:

        known_face_encodings = []
        known_face_names = []

        for i in os.listdir(os.path.join(os.getcwd(), 'folder_images')):
            shaaran_image = face_recognition.load_image_file(os.path.join(os.getcwd(), 'folder_images', i))
            shaaran_encoding = face_recognition.face_encodings(shaaran_image)[0]
            known_face_encodings.append(shaaran_encoding)
            known_face_names.append(os.path.splitext(i)[0])

        cameraResolution = (1024, 768)

        name_docu = 'tempface.jpeg'
        cap = cv2.VideoCapture(0)
        r, image = cap.read()
        cv2.imwrite(name_docu, image)
        cap.release()

        rgb_small_frame = cv2.imread("tempface.jpeg")
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

        for faces in face_names:
            modular_speech(faces)

        if len(face_names) == 0:
            modular_speech('noFaces')

    except Exception:
        pass


def facts():
    subscription_key = '600ab55597bb4bf08c1878e935ead82c'
    from azure.cognitiveservices.search.entitysearch import EntitySearchAPI
    from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
    from msrest.authentication import CognitiveServicesCredentials

    client = EntitySearchAPI(CognitiveServicesCredentials(subscription_key))
    save_speech('answer')
    speech = speech2text()
    try:

        entity_data = client.entities.search(query=speech)
        if entity_data.entities.value:

            main_entities = [entity for entity in entity_data.entities.value
                             if entity.entity_presentation_info.entity_scenario == "DominantEntity"]

            if main_entities:
                main_string = main_entities[0].description
                # sent_token = main_string.split('.')
                #
                # for sente in sent_token:
                #     modular_speech(sente)
                #     if keyboard.is_pressed('d'):
                #         break
                modular_speech(main_string)

    except AttributeError:
        save_speech('unknownError')


def readit():
    region = 'westcentralus'
    key = '3202352b4d3e49678aa066c513ae0ef2'

    # Set credentials
    credentials = CognitiveServicesCredentials(key)

    # Create client
    client = ComputerVisionAPI(region, credentials=credentials)

    name_docu = 'tempread.jpeg'
    cap = cv2.VideoCapture(0)
    r, image = cap.read()
    cv2.imwrite(name_docu, image)
    cap.release()

    source = tinify.from_file(os.path.join(os.getcwd(), name_docu))
    url = source.url
    mode = TextRecognitionMode.handwritten
    raw = True
    custom_headers = None
    numberOfCharsInOperationId = 36

    save_speech('waitForText')

    # Async SDK call
    rawHttpResponse = client.recognize_text(url, mode, custom_headers, raw)

    # Get ID from returned headers
    operationLocation = rawHttpResponse.headers["Operation-Location"]
    idLocation = len(operationLocation) - numberOfCharsInOperationId
    operationId = operationLocation[idLocation:]

    result = client.get_text_operation_result(operationId)

    # SDK call
    while result.status in ['NotStarted', 'Running']:
        time.sleep(1)
        result = client.get_text_operation_result(operationId)

    # Get data
    main_string = ''

    if result.status == TextOperationStatusCodes.succeeded:

        for line in result.recognition_result.lines:
            main_string = main_string + ' ' + line.text

        main_string = re.sub("!|/|;|:|-", "", main_string)
        main_string = main_string.replace('|', '')
        main_string = main_string.replace('*', '')

        modular_speech(main_string)

        # sent_token = main_string.split('.')
        #
        # for sente in sent_token:
        #     modular_speech(sente)
        #     if keyboard.is_pressed('d'):
        #         break
    else:
        save_speech('unknownError')


def check(text_inlet):
    text_key = 'c592c263a5b0440392ef655eda344e00'
    text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"
    documents = {'documents': [
        {'id': '1', 'language': 'en',
         'text': text_inlet}
    ]}
    headers = {'Ocp-Apim-Subscription-Key': text_key}
    response = requests.post(key_phrase_api_url, headers=headers, json=documents)
    key_phrases = response.json()
    stringy = ''
    for i in key_phrases['documents'][0]['keyPhrases']:
        stringy = stringy + ' ' + i
    return stringy


def news(search_term=None):
    subscription_key = "a05456788ad8447d8039b0e1d75f012a"

    if search_term == None:
        save_speech('newsspeak')
        speech = speech2text()
        search_term = check(speech)

    client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
    news_result = client.news.search(query=search_term, market="en-us", count=10, freshness='Week')
    closer = False

    if news_result.value:
        for k in news_result.value:
            modular_speech(k.name)

            while True:
                if keyboard.is_pressed('a'):
                    break

                if keyboard.is_pressed('s'):
                    modular_speech(k.description)
                    sleep(1)
                    break

                if keyboard.is_pressed('d'):
                    closer = True
                    break

                if keyboard.is_pressed('q'):
                    speak_label('goodbye')
                    quit()

            if closer == True:
                break

            else:
                pass

        # first_news_result = news_result.value[0]
        # print("Total estimated matches value: {}".format(news_result.total_estimated_matches))
        # print("News result count: {}".format(len(news_result.value)))
        # print("First news name: {}".format(first_news_result.name))
        # print("First news url: {}".format(first_news_result.url))
        # print("First news description: {}".format(first_news_result.description))
        # print("First published time: {}".format(first_news_result.date_published))
        # print("First news provider: {}".format(first_news_result.provider[0].name))
    else:
        save_speech("nonews")


def main():
    global opener
    opener = False
    count_main = 0
    try:
        while True:

            if count_main == 0:
                # save_speech('Welcome to Ocularis, the blind assistant')
                save_speech('welcome')
                sleep(3)
                count_main = 1


            # button_next = a
            # button_ok   = s
            # button_back = d

            speak_label('weather')
            if opener == True:
                weather()
                opener = False
            else:
                pass

            speak_label('clock')
            if opener == True:
                clock()
                opener = False
            else:
                pass

            speak_label('directions')
            if opener == True:
                directions()
                opener = False
            else:
                pass

            speak_label('uber')
            if opener == True:
                uber()
                opener = False
            else:
                pass

            speak_label('whatsthat')
            if opener == True:
                whatsthat()
                opener = False
            else:
                pass

            speak_label('remember')
            if opener == True:
                remember()
                opener = False
            else:
                pass

            speak_label('whosthat')
            if opener == True:
                whoisthat()
                opener = False
            else:
                pass

            speak_label('facts')
            if opener == True:
                facts()
                opener = False
            else:
                pass

            speak_label('readIt')
            if opener == True:
                readit()
                opener = False
            else:
                pass

            speak_label('news')
            if opener == True:
                news()
                opener = False
            else:
                pass

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        # device = get_device()
        main()
    except KeyboardInterrupt:
        pass
