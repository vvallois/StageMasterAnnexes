from subprocess import call
from bitcoinrpc.authproxy import AuthServiceProxy
import docker
import time

#Deploit les images dockers et connecte les noeuds Bitcoin entre eux 
print("************************DEPLOY************************")
client = docker.from_env()
for x in range(1, 4):
    client.containers.run("bitcoin-template", "bitcoind -regtest  -zmqpubrawblock=tcp://0.0.0.0:2833"+str(x)+" -zmqpubrawtx=tcp://0.0.0.0:2833"+str(x), detach=True, name="bit"+str(x), mem_limit="256m", ports={'2833'+str(x)+'/tcp': ('0.0.0.0', 28330+x)})
    time.sleep(5)

accessip = AuthServiceProxy("http://valval:beamap@172.17.0.4:18332")    
for y in range(1, 4):
       accessip.addnode("172.17.0."+str(y+1), "onetry")
       print 1

accessip = AuthServiceProxy("http://valval:beamap@172.17.0.3:18332")    
for y in range(1, 4):
       accessip.addnode("172.17.0."+str(y+1), "onetry")
       print 2

accessip = AuthServiceProxy("http://valval:beamap@172.17.0.2:18332")    
for y in range(1, 4):
        accessip.addnode("172.17.0."+str(y+1), "onetry")
        print 3

print("*************************DONE************************")
