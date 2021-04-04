# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 06:54:38 2021
GCYCZFMLYLEIM
@author: md_Rila_
"""
def key_fill(key,len_pt):
    while(len_pt!=len(key)):
        for i in range(0,len(key)):
            if(len_pt!=len(key)):
                key+=key[i]
    return(key)
pt=input("Enter the plain text to be encrypted : ")
pt=list(pt.upper())
key=input("Enter the key : ")
key=list(key.upper())
key=key_fill(key,len(pt))
ct=""
for i in range(0,len(pt)):
    c=(ord(pt[i])+ord(key[i]))%26
    c+=ord('A')
    ct+=chr(c)
print("The Cipher text :",ct)
gt=""
for i in range(0,len(ct)):
    p=(ord(ct[i])-ord(key[i])+26)%26
    p+=ord('A')
    gt+=chr(p)
print("The Plain text :",gt)
    
    