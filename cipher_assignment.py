# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:15:22 2019

@author: sapangha
"""

"""
5) Write a program in Python with one class called Cipher. Within the constructor of this class, ask user for a string and store
it. Use a static variable, key to store a randomly generated integer between 1 and 50 inclusive. Implement two methods,
encrypt and decrypt within this class. Encrypt generates and prints a cipher text using the user-entered string and the key and
decrypt generates decrypted string from ciphertext. The cipher only encrypts alpha and numeric (A-Z, a-z, 0-9). All Symbols,
such as - , ; %, remain unencrypted. The cipher text can have special characters. Use generator expression to filter out alpha
and numeric characters of the input string and to generate cipher text. Create an instance of this class, encrypt and decrypt
back the user entered string.


"""




import numpy as np
class Cipher2:
    encrpt_key =  np.random.randint(1,51)
    def __init__(self):
        
        self.userInput = input("Enter a String")
    def filterdata(self,inputtext):
        for char1 in inputtext:
            
            finalLetter = char1
            if char1.isalnum():
                result = ord(char1) + Cipher2.encrpt_key
                finalLetter = chr(result)
            yield finalLetter
    def encrypt(self,*args):
        if len(args)>0:
            self.userInput = args[0]
        cipherText = ""
            
        text = self.filterdata(self.userInput)
        for i in text:
            cipherText += i
        #print ("Your encrpyted text is: ", cipherText)
        return cipherText
    
    def decrypte(self,*args):
        if len(args)>0:
            self.userInput = args[0]
        
        encrypt_str = self.encrypt(self.userInput)
        decypt_str = ""
        for i in range(len(self.userInput)):
            finalLetter1 = self.userInput[i]
            if self.userInput[i].isalnum():
               result1 = ord(encrypt_str[i]) - Cipher2.encrpt_key 
               finalLetter1 = chr(result1)
            decypt_str += finalLetter1
        
        return decypt_str
        
cip = Cipher2()
print ("Your encrypted text is :",cip.encrypt())
print ("Your decrypted text is :",cip.decrypte())
