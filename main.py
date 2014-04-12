import asyncore
import socket
import threading
import robot


class HTTPClient(asyncore.dispatcher):
    def __init__(self, host):
        print "we are gonna connect!"
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 1338))
        self.delim = "\r\n"
        self.recv_message = ""
        # message = {"c": 0, "b": 0, "a": 0}
        self.buffer = ""
        self.robot = robot.Robot()

    def handle_connect(self):
        print "Handle connect triggered"
        pass

    def handle_close(self):
        print "Handle close triggered"
        self.close()

    def handle_read(self):
        message = self.recv(1024)
        print message
        self.recv_message = self.recv_message + message
        if self.recv_message.find(self.delim) > 0:
            self.recv_message = self.recv_message.strip(self.delim)
            if self.recv_message=="@":
                self.send("@"+self.delim)
                self.recv_message = ""
            else:
                print self.recv_message
                self.buffer = "ok" + self.delim
                self.robot.doCommand(self.recv_message)
                self.recv_message = ""



    def writable(self):
        return self.buffer is not None

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

ip = '10.17.0.38'
#qip = '192.168.0.32'
client = HTTPClient(ip)
t = threading.Thread(target=asyncore.loop)
t.start()
while 1:
    a = raw_input()
    if a == "q":
        client.close()
        t.join()
        break
