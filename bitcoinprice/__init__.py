from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'dmp1ce'
LOGGER = getLogger(__name__)

class BitcoinPriceSkill(MycroftSkill):
    def __init__(self):
        super(BitcoinPriceSkill, self).__init__(name="BitcoinPriceSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        intent = IntentBuilder("BitcoinPriceIntent").require("BitcoinPriceKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:
            r = requests.get("http://apiv2.bitcoinaverage.com/indices/local/ticker/btcusd")
            self.speak_dialog("bitcoin.price", data={'price': str(r.json()['averages']['day'])})
        except:
            self.speak_dialog("not.found")

    def stop(self):
        pass

def create_skill():
    return BitcoinPriceSkill()
