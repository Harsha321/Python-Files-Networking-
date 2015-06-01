#!/usr/bin/python
import sys,getopt

def subnet_generator(argv):
	CIDR = 30
	try:
		opts,args = getopt.getopt(argv,None,["base="])

		for opt,arg in opts:
			if opt == "--base":
				IPBASE,COUNT = arg.split('/')
				COUNT = int(COUNT)

		mask = netmask(CIDR)
		NETCOUNT = 2**(30-COUNT)
		IPBASE = ip2int(IPBASE)
		BLOCKLEN = (2**(32-CIDR))
		NETBLOCK = [0,0,0,0]

		for i in range(NETCOUNT):
			NETBLOCK[0] = IPBASE
			for j in range(1,BLOCKLEN):
				IPBASE += 1
				NETBLOCK[j] = IPBASE

			print str(i+1)+' - ip block: '+int2ip(NETBLOCK[0])+'/'+str(CIDR)+', IPs '+int2ip(NETBLOCK[1])+' : '+int2ip(NETBLOCK[2])+', netmask '+mask+' (cidr /'+str(CIDR)+')'
			IPBASE += 1

	except getopt.GetoptError:
		print 'Usage Error: <filename> --base=<IP address/MASK>'
		sys.exit(2)
	except ValueError:
		print 'Data Error: Invalid argument value.'


def ip2int(ip):
	try:
		ipaddr=ip.split('.')

		if (len(ipaddr) != 4):
			sys.exit("Data Error: Invalid IP address.")

		result = 0
		for i in range(4):
			ipaddr[i] = int(ipaddr[i])
			
			if (ipaddr[i] <0) or (ipaddr[i] >255):
				sys.exit("Data Error: Invalid IP address.")

			result <<= 8
			result |= (ipaddr[i] & 0xff)
		return result

	except AttributeError:
		print 'Data Error: Invalid IP address.'
		sys.exit(2)


def int2ip(int_value):
	try:
		int_value = int(int_value)

		o1 = ((int_value >> 24)&0xff)
		o2 = ((int_value >> 16)&0xff)
		o3 = ((int_value >> 8)&0xff)
		o4 = ((int_value)&0xff)
		return str(o1)+'.'+str(o2)+'.'+str(o3)+'.'+str(o4)

	except ValueError:
		print 'Data Error: Invalid integer value.'
		sys.exit(2)

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
	if len(sys.argv) >=2:
		subnet_generator(sys.argv[1:])
	else:
		print 'Usage Error: <filename> --base=<IP address/MASK>'
		sys.exit(2)
