from stomp import Connection, PrintingListener
import time

c = Connection([('127.0.0.1', 61613)])
c.set_listener('', PrintingListener())
c.start()

c.connect('emmet', 'masterbuilder', wait=True)
c.subscribe('/queue/test01', 123)
# c.send('queue/test01', 'a test message')
time.sleep(60)

