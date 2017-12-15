#!/usr/bin/python2
"""\n
RoXor Project.

Usage:
  roxor [-H] <message> [-H] <key> [-o OUTPUT] [-hv]
  roxor -F <filename> [-H] <key> [-o OUTPUT] [-hv]
  roxor -F <filename1> -F <filename2> [-o OUTPUT] [-hv]

Arguments:
  message		      the message to be xored
  key			      the key used for xoring

Options:
  -h --help        	      Show this screen.
  -v --version		      Show version.
  -F --file	   	      Specify a file.
  -H --hex		      Use Hex format.
  -o OUTPUT --out=OUTPUT      specify the result filename.
"""

from itertools import cycle,islice
from docopt import docopt
import sys


####### Useful Functions #########
def is_file(name):
    return True if args["--file"] and __import__('os').path.isfile(name) else False

def encrypt(message,key):
    key=''.join(islice(cycle(key),len(message)))
    res=''.join([chr(ord(message[i]) ^ ord(key[i])) for i in range(len(message))])
    return res

########## Main Function ##########

if __name__ == '__main__':

  args = docopt(__doc__,version="RoXor v0.1\nBy Abderraouf\nTh3-Jackers Team")
  a_output=args["--out"] if args["--out"] else "roxor_output"
  a_key=args["<key>"]
  a_hex=args["--hex"]
  a_files=args["--file"]
  a_filename=args["<filename>"]
  a_filename1=args["<filename1>"]
  a_filename2=args["<filename2>"]

  if not a_files:
      a_msg=args["<message>"]
      if a_hex > 0:
        if sys.argv[1] in ["-H","--hex"]:
	  a_msg=a_msg.decode("hex")
	if sys.argv[3] in ["-H","--hex"]:
	  a_key=a_key.decode("hex")

  elif a_files==1:
      ##### Check if the fils is valid #####
      if not is_file(a_filename):
        print("\nNO SUCH FILE ----> "+a_filename)
        sys.exit(1)
      ##### Grab the file content and the key ######
      a_msg=open(args["<filename>"],"rb").read()
      if args["--hex"]==1:	a_key=args["<key>"].decode("hex")
      else:	a_key=args["<key>"]

  elif a_files==2:
	##### Check if the files are valid ##############
      if (not is_file(a_filename1)) or (not is_file(a_filename2)):
        print("\nNO SUCH FILE ----> "+a_filename1+" and/or "+a_filename2)
        sys.exit(1)
      ########## Grap files content ###############
      a_msg=open(args["<filename1>"],"rb").read()
      a_key=open(args["<filename2>"],"rb").read()

  res = encrypt(a_msg,a_key)
  print res
