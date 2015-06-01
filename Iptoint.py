#!/usr/bin/python
import getopt, sys

def ip(argv):
	try:
		#opts, args = getopt.getopt(argv, None)
		if not argv:	
			print 'Usage Error:<filename>'
			sys.exit(2)
		#print argv[0]
		"""for opt,arg in opts:
			if opt== :"""
		o = argv[0]
		octect = map(int, o.split('.'))
    		print "IP to integer : "+ str((16777216 * octect[0]) + (65536 * octect[1]) + (256 * octect[2]) + octect[3])
    			

	except getopt.GetoptError:
		print 'Usage Error:<filename>'
		sys.exit(2)
	
if __name__ == "__main__":
    	ip(sys.argv[1:])
