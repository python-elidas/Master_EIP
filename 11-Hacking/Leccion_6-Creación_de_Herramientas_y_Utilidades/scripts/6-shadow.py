#!/usr/bin/python 
 
import os,sys 
import crypt 
import codecs 
import argparse 
 
def bruteForce(cryptPass,user): 
    dicFile = open ('/tmp/passes','r') 
    hashtype = cryptPass.split("$")[1] 
    if hashtype == '6': 
        print("[+] Hash type SHA-512 ...") 
        salt = cryptPass.split("$")[2] 
        salt = "$" + hashtype + "$" + salt + "$" 
        for passwd in dicFile.readlines(): 
            passwd=passwd.strip('\n') 
            cryptWord = crypt.crypt(passwd,salt) 
            if (cryptWord == cryptPass): 
                print("[+] Found password %s for the user %s " %(user, passwd)) 
    print("Finished attack!") 
 
if __name__=="__main__": 
    parse = argparse.ArgumentParser(description='Simple brute force /etc/shadow .') 
    parse.add_argument('-f', dest='shadowFile', help='Shadow file location, example: \'/etc/shadow\'') 
    argus=parse.parse_args() 
    if argus.shadowFile == None: 
       parse.print_help() 
       exit 
    else: 
        passFile = open (argus.shadowFile,'r') 
        for line in passFile.readlines(): 
            line = line.replace("\n","").split(":") 
            if  not line[1] in [ 'x', '*','!' ]: 
                user = line[0] 
                cryptPass = line[1] 
                bruteForce(cryptPass,user) 
