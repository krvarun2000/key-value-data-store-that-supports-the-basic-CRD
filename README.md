## Table of contents
* [General info](#general-info)
* [Things to be done](#things-to-be-done)
* [Walkthrough](#walkthrough)

## General info
* This project is a simple Key value datastore that supports the basic CRD(Create,read and delete) operations
* We also have Time to live property which is optional and it gives us the time(in seconds) expiry limit before which we can read or delete the key

## Things to be done
* We first have to import the necessary packages such as json,time and threading
* Need  to have a basic idea on how key-value pair works 

## Walkthrough
* We have a class inside which the CRD(Create,read and delete) operations exists
* The create operation is used to create a new key-value pair and add it to the data store only if each key are unique and the key should only be a string capped at 32 characters
* It also makes sure that the size of the data store is less than 1 GB 
* The read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object, It only returns the value if the time to live of the key is within the specified time(in seconds)
* If the key does not exist in the data store it raises an KeyError
* Finally the delete operation can also be performed by providing the key and if the key exist it deletes the key from the datastore if not raises an error, It also verifies that the time to live of the key is within the specified time(in seconds)
