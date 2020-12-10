import json
import time 
from threading import*
class CRD:
    def __init__(self):
        self.data = '{}'
        self.z = json.loads(self.data) #loads is used to take in a string and return a json object
    def create(self,key,value,timeout=0):
            d = json.loads(self.data)#local variable
            if key in self.z:
                print("Key already exist in the data store") 
            else:
                if(key.isalpha()):
                    if (self.z.__sizeof__())<(1024*1024*1024) and value<=(16*1024*1024): #checking size of file and JSON object
                        if timeout==0:
                            value_time=[value,timeout]#array to store the value and time to live of a key
                        else:
                            value_time=[value,time.time()+timeout]#array to store the value and time to live a key
                        if len(key)<=32: 
                            d[key]=value_time
                            self.z.update(d)
                    else:
                        
                        print("Memory exceeded!!Size has crossed the threshold values")
                else:
                    print("Invalid!!!Key must only be a string ")
    def read(self,key):
            try:
                a=self.z[key]
            except KeyError:
                    print("Please enter a valid key") 
            else:
                b=self.z[key]
                if b[1]!=0:
                    if time.time()<b[1]: #comparing the present time with expiry time
                        string=str(key)+":"+str(b[0]) #to return the value in the format of JSONObject i.e.,"key_name:value"
                        return string
                    else:
                        print("Time-to-live of",key,"has expired") 
                else:
                    string=str(key)+":"+str(b[0])
                    return string
    def delete(self,key):
            try:
                a=self.z[key]
            except KeyError:
                print("Please enter a valid key") 
            else:
                b=self.z[key]
                if b[1]!=0:
                    if time.time()<b[1]: #comparing the current time with expiry time
                        del self.z[key]
                        print("Key is deleted successfully ")
                    else:
                        print("Time-to-live of",key,"has expired") 
                else:
                    del self.z[key]
                    print("Key is deleted successfully ")


