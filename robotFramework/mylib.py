#encoding: utf-8
import hashlib

def gen_sign(*args):
	m = hashlib.md5()  
	m.update(''.join(args).encode('utf-8'))  
	return m.hexdigest()