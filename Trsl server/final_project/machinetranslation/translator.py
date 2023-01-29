"""
In this file I build a translator from english to french and vis versa
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def englishToFrench(englishText):
    """
    function which handles english input and translate it to french
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(
        text=englishText,
        # model_id = 'en-fr'
        source='en',
        target='fr'
    ).get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    """
    function which handles french input and translate it to english
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(
        text=frenchText,
        # model_id = 'fr-en'
        source='fr',
        target='en'
    ).get_result()
    englishText = translation['translations'][0]['translation']
    return englishText

