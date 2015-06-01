#!/usr/bin/python
import sys,getopt

def subnets(argv):
	CIDR = 30
	NETCOUNT = 32

	NETBLOCK = ["netaddress","host1","host2","broadcast"]
	BLOCKLEN = (2**(32-CIDR))
	

	try:
		opts,args=getopt.getopt(argv,None,['base='])

		if not opts:
			print 'Usage Error:<filename> --base=<ipaddress>'
			sys.exit(2)

		for opt,arg in opts:
			if opt == "--base":
				inp=arg
				#print "IP address:"+inp
				#print BLOCKLEN
		#inp = ' inp/NETCOUNT'
		x= inp.split("/")
		inp =x[0]
		NETCOUNT =int(x[1])
		mask = netmask(CIDR)
		for i in range(2**(32-NETCOUNT)):
			NETBLOCK[0] = inp
			for j in range(1,BLOCKLEN):
				inp = address_inc(inp,1)
				NETBLOCK[j] = inp
			print str(i+1)+' - ip block : '+NETBLOCK[0]+'/'+str(CIDR)+', IPs '+NETBLOCK[1]+' : '+NETBLOCK[2]+', netmask '+mask+' (cidr /'+str(CIDR)+')' 
			inp = address_inc(inp,1)

	except getopt.GetoptError:
		print 'Usage Error:<filename> --base=<ipaddress>'
		sys.exit(2)

def address_inc(ip,step):
	flag = 0
	octet=ip.split('.')

	if len(octet) != 4 :
		print 'Error: Invalid IP Address.'
		sys.exit(2)

	for i in range(4):
		octet[i] = int(octet[i])
		if octet[i] >= 256:
			flag = 1

	if flag == 1:
		print 'Error: Invalid IP Address.'
		sys.exit(2)


	for i in range(step):
		octet[3] += 1

		for j in range(3,-1,-1):
			if octet[j] == 256:
				octet[j-1] += 1
				octet[j] = 0
	return str(octet[0])+'.'+str(octet[1])+'.'+str(octet[2])+'.'+str(octet[3])

def netmask(cidr):
	mask = [255,255,255,255]

	mask[0] = int(256-(2**(32-cidr-24)))
	mask[1] = int(256-(2**(32-cidr-16)))
	mask[2] = int(256-(2**(32-cidr-8)))
	mask[3] = int(256-(2**(32-cidr)))

	for i in range(4):
		if mask[i] < 0:
			mask[i] = 0
	return str(mask[0])+'.'+str(mask[1])+'.'+str(mask[2])+'.'+str(mask[3])

if __name__ == "__main__":
	  subnets(sys.argv[1:])



