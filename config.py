import os


class Config(object):
    JSON_AS_ASCII = os.environ.get('JSON_AS_ASCII')
    SUBSCRIPTION_KEY = os.environ.get('SUBSCRIPTION_KEY')
