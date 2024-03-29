import cPickle 
import sys, os
import zlib


def checkdir(path):
  if not os.path.exists(path): 
    os.makedirs(path)

def tex(x):
  return r'$\mathrm{'+x+'}$'

def save(data,name):  
  compressed=zlib.compress(cPickle.dumps(data))
  f=open(name,"wb")
  f.writelines(compressed)
  f.close()

def load(name): 
  compressed=open(name,"rb").read()
  data=cPickle.loads(zlib.decompress(compressed))
  return data

def load2(name): 
  compressed=open(name,"rb").read()
  data=cPickle.loads(compressed)
  return data

def isnumeric(value):
  try:
    int(value)
    return True
  except:
    return False

  return r'$\mathrm{'+x+'}$'

def ERR(msg):
  print msg
  sys.exit()

def lprint(msg):
  sys.stdout.write('\r')
  sys.stdout.write(msg)
  sys.stdout.flush()



