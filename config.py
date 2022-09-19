import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    RPC_SOCKET = os.environ.get('RPC_SOCKET') or 'you-will-never-guess'
    CONNECT_INFO = os.environ.get('CONNECT_INFO') or 'you-will-never-guess'