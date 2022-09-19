import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', "whocares")
    RPC_SOCKET = os.environ.get('RPC_SOCKET')
    CONNECT_INFO = os.environ.get('CONNECT_STRING')