from bitcoinrpc.authproxy import AuthServiceProxy
import simplejson as json

for x in range(1, 4):
    access = AuthServiceProxy("http://valval:beamap@172.17.0."+str(x+1)+":18332")
    blockbesthash = access.getbestblockhash()
    blockbest = access.getblock(blockbesthash)
    #Affiche la hauteur du dernier block présent dans chaque noeuds
    print ("node n:"+str(x)+" "+str(blockbest["height"]))

#Affichage des informations du dernier noeud
print json.dumps(access.getmininginfo(), indent=4, separators=(',', ': '))
print json.dumps(access.getpeerinfo(), indent=4, separators=(',', ': '))
print json.dumps(access.getnetworkinfo(), indent=4, separators=(',', ': '))
print json.dumps(access.getblockchaininfo(), indent=4, separators=(',', ': '))
print json.dumps(access.getrawmempool(), indent=4, separators=(',', ': '))
