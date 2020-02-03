import os
import sys
import socket
from pymongo import MongoClient
import ConfigParser


class connector():

    conf_file = 'rpcoh_conf.ini'
    connection = None
    db = None
    db_account = None
    db_secretkey=None
    db_name = 'rpcoh'
    db_host='localhost'
    db_port=27017
    mode_debug = False

    mHBList = []

    def __init__(self):
        self.readConfig()


    def readConfig(self):
        config = ConfigParser.ConfigParser()
        config.read(self.conf_file)
        debug = config.get('settings', 'debug')
        self.db_name = config.get('db', 'db_name')
        self.db_port = config.get('db', 'db_port')
        if(debug == 'true'):
            self.mode_debug = True
            self.db_account = config.get('settings', 'db_account')
            self.db_secretkey = config.get('settings', 'db_secretkey')
            self.db_host = config.get('db', 'db_d_host')
        else :
            self.db_account = config.get('settings', 'db_account')
            self.db_secretkey = config.get('settings', 'db_secretkey')
            self.db_host = config.get('db', 'db_r_host')

    def connectDB(self):

        self.connection = MongoClient(self.db_host, self.db_port)
        db = self.connection[self.db_name]
        db.authenticate(self.db_account, self.db_secretkey)
        collection = db['epg']
        collection.find()

if __name__=='__main__':
    con = connector()





