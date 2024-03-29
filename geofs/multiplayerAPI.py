import requests
import json

class multiplayerAPI:
    def __init__(self, sessionID, accountID):
        self.sessionID = sessionID
        self.accountID = accountID
        self.myID = None,
        self.lastMsgID = None,
    
    def handshake(self): # initializes connection and gains mandatory variables from server.
        # initializes server connection and gets details from server.
        body = {
            "origin": "https://www.geo-fs.com",
            "acid": self.accountID,
            "sid": self.sessionID,
            "id": "",
            "ac": "1",
            "co": [42.36021568682466,-70.98767598755524,4.589746820023676,-103.04273973572526,-15.919583740307557,-0.376840533503692],
            "ve": [2.7011560632672626e-10,7.436167948071671e-11,0.000004503549489433212,0,0,0],
            "st": {"gr":True,"as":0},
            "ti": 1678751444055,
            "m": "", 
            "ci": 0
        }
        try:
            response = requests.post(
                "https://mps.geo-fs.com/update",
                json = body,
                cookies = {"PHPSESSID": self.sessionID}
            )
            print("Successfully connect to server.")
            response_body = json.loads(response.text)
            self.myID = response_body["myId"]


            body2 = {
                "origin": "https://www.geo-fs.com",
                "acid": self.accountID,
                "sid": self.sessionID,
                "id": self.myID,
                "ac": "1",
                "co": [42.36021568682466,-70.98767598755524,4.589746820023676,-103.04273973572526,-15.919583740307557,-0.376840533503692],
                "ve": [2.7011560632672626e-10,7.436167948071671e-11,0.000004503549489433212,0,0,0],
                "st": {"gr":True,"as":0},
                "ti": 1678751444055,
                "m": "", 
                "ci": self.lastMsgID
            }
            response = requests.post(
                "https://mps.geo-fs.com/update",
                json = body2,
                cookies = {"PHPSESSID": self.sessionID}
            )
            response_body = json.loads(response.text)
            self.myID = response_body["myId"]
            self.lastMsgID = response_body["lastMsgId"]
        except:
            print("Unable to connect to GeoFS. Check your connection and restart the application.")

    def sendMsg(self, msg):
        body = {
            "origin": "https://www.geo-fs.com",
            "acid": self.accountID,
            "sid": self.sessionID,
            "id": self.myID,
            "ac": "1",
            "co": [42.36021568682466,-70.98767598755524,4.589746820023676,-103.04273973572526,-15.919583740307557,-0.376840533503692],
            "ve": [2.7011560632672626e-10,7.436167948071671e-11,0.000004503549489433212,0,0,0],
            "st": {"gr":True,"as":0},
            "ti": None,
            "m": msg,
            "ci": 0
        }
        try:
            response = requests.post(
                "https://mps.geo-fs.com/update",
                json = body,
                cookies = {"PHPSESSID": self.sessionID}
            )
            response_body = json.loads(response.text)
            self.myID = response_body["myId"]
        except:
            print("Unable to connect to GeoFS. Check your connection and restart the application.")

    def getMessages(self):
        body = {
            "origin": "https://www.geo-fs.com",
            "acid": self.accountID,
            "sid": self.sessionID,
            "id": self.myID,
            "ac": "1",
            "co": [42.36021568682466,-70.98767598755524,4.589746820023676,-103.04273973572526,-15.919583740307557,-0.376840533503692],
            "ve": [2.7011560632672626e-10,7.436167948071671e-11,0.000004503549489433212,0,0,0],
            "st": {"gr":True,"as":0},
            "ti": None,
            "m": "",
            "ci": self.lastMsgID
        }
        try:
            response = requests.post(
                "https://mps.geo-fs.com/update",
                json = body,
                cookies = {"PHPSESSID": self.sessionID}
            )
            print(response)
            response_body = json.loads(response.text)
            self.myID = response_body["myId"]
            self.lastMsgID = response_body["lastMsgId"]

            return response_body["chatMessages"]
        except:
            print("Unable to connect to GeoFS. Check your connection and restart the application.")
