from pymongo import MongoClient
import logging


class CreditCard():
    logger = logging.getLogger(__name__)
    app = None

    @staticmethod
    def init_db(app):
        CreditCard.app = app

        CreditCard.client = MongoClient(app.config['DB_URI'])  # type: pymongo.MongoClient
        CreditCard.db = CreditCard.client[app.config['DB_NAME']]  # type: pymongo.collection
        CreditCard.collection = CreditCard.db['card']  # type: pymongo.collection

