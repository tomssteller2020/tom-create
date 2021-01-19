import databasing.py, mining.py, networks.py, eccs.py, encodings.py, networks.py, threads.py
from hashlib import sha256

db 				= databasing.crackDB()
miner			= mining.crackcoinMiner()
network 		= networks.crackcoinNetwork()

ecc 			= eccs.ellipticCurve()
hasher 			= sha256
encoder 		= encodings.b58encoder()
threader 		= threads.crackcoinThreader()


from os.path import isfile
if not isfile(db.dbFile):
	db.createDB()
