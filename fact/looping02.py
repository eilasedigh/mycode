#! //usr/bin/env python3
#Open File
dnsfile = open("dnsserver.txt")
#Create list of lines
dnslist= dnsfile.readlines()
#Loop over Lines
for svr in dnslist:
    print(svr, end="")
dnsfile.close()
