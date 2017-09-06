from bitcoinrpc.authproxy import AuthServiceProxy

#Génère un block depuis chaque noeud
for x in range(1, 4):
    access = AuthServiceProxy("http://valval:beamap@172.17.0."+str(x+1)+":18332")
    access.generate(1)
