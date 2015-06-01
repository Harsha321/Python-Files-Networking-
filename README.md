# Python-Files-Networking-
This repo consists of python files which are related to networking
1.Conversion of IPaddress to Integer using command line tool
2.Conversion of Integer to IP address using command line tool
3.Tool that takes a subnet as an input and output a list of 16 /30 subnets
4.Tool that makes the number of subnets configurable
5.Tool that automatically output the maximum possible number of subnets based on the base entry and its CIDR

Description of how to Implement above programs:

1. To calculate the integer from an IP address, we have to perform the following calculation.
	(first octet * 256^3) + (second octet * 256^2) + (third octet * 256) + (fourth octet)
      =	(first octet * 16777216) + (second octet * 65536) + (third octet * 256) + (fourth octet)
 
Example: Given IP address: 192.168.10.1 and now it will be converted as below according to above process
      =	(192 * 16777216) + (168 * 65536) + (10 * 256) + (1)
      =	3232238081

2. To calculate the IP address from given integer take the argument divide with 253^3(16777216) and 
   perform modulo division and store it as octet1. Again take the argument divide with 256^2(65536)
   perform modulo division and store it as octet2. Again take the argument divide with 256 and 
   perform modulo division and store it as octet3. Again take the argument and perform modulo division
   and store it in octet4. Finally take string of each octet and concatenate with '.' between them

3.  CIDR and NETCOUNT values are initialized
NETBLOCK contains netaddress, host1, host2, broadcast address that are to be printed on output
BLOCKLEN is calculated as (2^(32-CIDR))
Given --base as options and args are to be passed to those options.
Args are now passed into inp value.
netmask of CIDR is passed into mask.
Inp value now will be store into NETBLOCK[0], which means it will be stored into first element of array of NETBLOCK which is netaddress.
Now the addresses of inp value will be incremented as address_inc(inp,1)  and will again be stored into inp value. The incremented inp value will now be fed into NETBLOCK. 
Now we can print   the output according to our desired format.
address_inc  and netmask functions are created.

4.In this program NETCOUNT = 30 and one more option --nb_subnet is to be taken. 
In try block in for loop we have to pass  --nb_subnet into options and integer value of arguments is then passed into NETCOUNT. 
The rest of the program will be same as the above program.

5.In this program for calculating base entry and its CIDR we have to use split function for splitting base address and its CIDR.  
Now the split function should be applied to the arg so that base entry and CIDR gets split by '/'. The IPBASE gets stored in 1st element of NETBLOCK. When the BLOCKLEN gets incremented, IPBASE value also gets incemented. Here we define to functions ip2int(ip) and int2ip(int_value) to print the correct ip value. 

