import json
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    url = f"{url}/v3/translate?source=en&target=fr&text={englishText}&version=2018-05-01"
    headers = {'Content-Type': 'application/json', 'Authorization': f"Bearer {apikey}"}
    response = requests.get(url, headers=headers)
    frenchText = json.loads(response.text)['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    url = f"{url}/v3/translate?source=fr&target=en&text={frenchText}&version=2018-05-01"
    headers = {'Content-Type': 'application/json', 'Authorization': f"Bearer {apikey}"}
    response = requests.get(url, headers=headers)
    englishText = json.loads(response.text)['translations'][0]['translation']
    return englishText
