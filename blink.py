from liblo import *
import sys
import time
import requests
import getpass

class MuseServer(ServerThread):
    #listen for messages on port 5001
    def __init__(self, user, password):
        ServerThread.__init__(self, 5001)
        self.user = user
        self.password = password
        y = {"user":user,"password":password}
        requests.post("http://104.236.236.222:3001/login",y)

    #receive accelrometer data
    @make_method('/muse/elements/blink', 'i')
    def acc_callback(self, path, args):
        blink = args[0]
        print "%d" % (blink)
        if blink == 1:
            x = {"blink":"1"}
            requests.post("http://104.236.236.222:3001/blink",x)

    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        a =1

try:
    user = "XXXXXXXX" #str(raw_input("Username: "))
    password = "XXXXXXXX" #str(raw_input("Password: "))
    #password = str(getpass.getpass())
    server = MuseServer(user, password)
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
