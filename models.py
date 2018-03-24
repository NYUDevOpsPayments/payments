from pymongo import MongoClient
import logging


class CreditCard():
    logger = logging.getLogger(__name__)
    app = None

    def __init__(self, name, card, exp, cvv, card_id = None):
        # type: (string, string, (number, number), number, number) -> None
        self.name = name
        self.card = card
        self.exp = exp
        self.cvv = cvv
        self.card_id = card_id


    @staticmethod
    def init_db(app):
        CreditCard.app = app

        CreditCard.client = MongoClient(app.config['DB_URI'])  # type: pymongo.MongoClient
        CreditCard.db = CreditCard.client[app.config['DB_NAME']]  # type: pymongo.collection
        CreditCard.collection = CreditCard.db['card']  # type: pymongo.collection
