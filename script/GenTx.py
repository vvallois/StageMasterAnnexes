from bitcoinrpc.authproxy import AuthServiceProxy

access = AuthServiceProxy("http://valval:beamap@172.17.0.3:18332")
print access.getbalance()
#Envoie 0,001 bitcoin a une nouvelle adresse
access.sendtoaddress(access.getnewaddress(), 0.001)