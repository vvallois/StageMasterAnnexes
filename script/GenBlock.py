from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://valval:beamap@172.17.0.3:18332")
#Genere 2000 blocks
access.generate(2000)


