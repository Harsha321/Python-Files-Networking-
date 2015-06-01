#!/usr/bin/python
import getopt, sys

def ip(argv):
	output = ['o1', 'o2', 'o3', 'o4']
	try:
	 	opts,args = getopt.getopt(argv, "i:")
		if not opts:
			print 'Usage Error:<filename>'
			sys.exit(2)
		for opt,arg in opts:
			if opt == "-i":
				ip = arg

	 			o1 = (int(ip)/ 16777216) % 256
    	 			o2 = (int(ip) / 65536) % 256
    	 			o3 = (int(ip) / 256) % 256
    	 			o4 = int(ip) % 256

    			print "integer to IP : "+str(o1)+'.'+str(o2)+'.'+str(o3)+'.'+str(o4)
    
	except getopt.GetoptError:
		print 'Usage Error:<filename>'
		sys.exit(2)	

if __name__ == "__main__":
    ip(sys.argv[1:])
