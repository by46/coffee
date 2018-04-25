import os

from pymongo import MongoClient

import gridfs

fs = gridfs.GridFS(None)
fs.put()
client = MongoClient()
db = client['demo']
db.
def worker():
    print os.getcwd()
    pid = os.fork()
    if pid == 0:
        print 'children'
        return
    print 'parent', pid

if __name__ == '__main__':
    worker()
