import threading
from bitcoinrpc.authproxy import AuthServiceProxy
import sched, time
import numpy as np

scheduler = sched.scheduler(time.time, time.sleep)
access = AuthServiceProxy("http://valval:beamap@172.17.0.3:18332")
def new_timed_call(calls_per_second, callback, *args, **kw):
    period = 1.0 / (np.random.lognormal(np.log(2.8432803665655411), 0.29731261148742899)*1000)
    def reload():
        callback(*args, **kw)
        period = 1.0 / (np.random.lognormal(np.log(2.8432803665655411), 0.29731261148742899)*1000)
        print period
        scheduler.enter(period, 0, reload, ())
    scheduler.enter(period, 0, reload, ())

#### example code ####

def p():
    t=1
    #access.sendtoaddress(access.getnewaddress(), 0.00001)
new_timed_call(np.random.lognormal((np.log(2.8432803665655411), 0.29731261148742899)*1000), p)  # print '3' three times per second
scheduler.run()