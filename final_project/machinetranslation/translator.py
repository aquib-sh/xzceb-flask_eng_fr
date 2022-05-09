"""Author: Shaikh Aquib
Provides translation services with the help of IBM Language Translator
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

class LanguageTranslator:
    """Translates text into another language using the help of IBM Language Translator"""
    def __init__(self):
        apikey = os.environ['apikey']
        url = os.environ['url']

        self.__authenticator = IAMAuthenticator(apikey)
        self.__language_translator = LanguageTranslatorV3(
                version='2018-05-01',
                authenticator=self.__authenticator
        )
        self.__language_translator.set_service_url(url)

    def __translate(self, text, model_id="en-es"):
        """Base function for implementating translation"""
        translation = self.__language_translator.translate(
                text=text,
                model_id=model_id).get_result()
        return translation["translations"][0]["translation"]

    def englishToFrench(self, englishText):
        """Translates English text to French"""
        return self.__translate(englishText, model_id="en-fr")

    def frenchToEnglish(self, frenchText):
        """Translates French text to English"""
        return self.__translate(frenchText, model_id="fr-en")
