## Table of contents
* [General info](#general-info)
* [Things to be done](#things-to-be-done)
* [Workflow](#workflow)

## General info
* This project is a simple Key-Value based datastore that supports the basic CRD(Create,Read and Delete) operations.
* Additional functionalities include a Time-to-live property (optional usage) where the user can set an expiry limit before which we must perform read and delete operations on the key. Basically, **Snapchat for CRD operations**. 
* Project does not have any additional dependencies apart from those packaged within the standard Python 3.7 x64 executable variant. 

## Usage
```
from key_value import *

#Create an object 
x = CRD()

#Add a key-value to the JSON

x.create("Varun", 21)

#Read values 

x.read("Varun")

#Delete Values

x.delete("Varun")
```


## Workflow
* The package provides a simple functions the user can import to perform CRD operations on a single process, locally. 
* The create operation is used to add a new key-value pair and to the data store. This occurs if and only if each key is unique, and if the key is a string capped at 32 characters.
* It also makes sure that the size of the data store is less than 1 GB.
* The read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object, It only returns the value if the time to live of the key is within the specified time(in seconds). 
* Finally, the delete operation can also be performed by providing the key and if the key exists it deletes the key from the datastore, and raises an error otherwise. It also verifies that the time to live of the key is within the specified time(in seconds)
