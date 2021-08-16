import json
import zmq

context = zmq.Context()

sock_typ = zmq.SUB
client = context.socket(sock_typ)
client.connect("tcp://127.0.0.1:5556")

class subscriber():
    def __init__(self, request:str, debug_mode:bool=False):
        self.request = request
        self.debug_mode = debug_mode

    def get_data(self):
        client.subscribe("")
        msg= client.recv_json()
        if self.debug_mode:
            print(msg)
        try:
            msg_rtn = msg[self.request]
        except KeyError:
            pass
        return msg_rtn
