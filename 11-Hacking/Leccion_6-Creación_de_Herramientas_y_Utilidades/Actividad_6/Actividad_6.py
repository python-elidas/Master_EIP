#__BIBLIOTECAS__#
import os, sys
import crypt, codecs
import binascii, hashlib
import argparse

from attr import has

#__MAIN FUNCTIONS__#
def win(hash, psswrd): # si es un sistema windows:
    ntlm_hash = binascii.hexlify(
        hashlib.new(
            'md4',
            psswrd.encode('utf-16le')
        ).digest()
    )
    return hash.split(':')[0], ntlm_hash

def unix(hash, psswrd): # SI es un sistema linux
    methods = {
        '1': '[-] Hash type MD5 ...',
        '2a': '[-] Hash type BLOWFISH ...',
        '2y': '[-] Hash type BLOWFISH ...',
        'y': '[-] Hash type BLOWFISH ...',
        '5': '[-] Hash type SHA256 ...',
        '6': '[-] Hash type SHA512 ...'
    }
    usr = hash.split(':')[0]
    hash = hash.split(':')[1]
    #print(methods[hash.split('$')[1]])
    salt = '$'+'$'.join(hash.split('$')[1:3])+'$' # cadena de encriptación
    return usr, crypt.crypt(psswrd, salt)
            
def bruteForce(syst, hashFile, psswrds='passFile.txt'):
    hashes = open(hashFile, 'r') # abrimos el archivo con los hashes
    dictFile = open(psswrds, 'r').readlines() # leemos el archivo con las posibles contraseñas
    for account in hashes.readlines():
        for line in dictFile:
            line = line.replace("\n","")
            if syst == 'windows':
                psswrd = account.split(':')[3]
                print('[-] Hash type NTLM ...')
                user, hash = win(account, line)
            elif syst == 'unix':
                psswrd = account.split(':')[1]
                user, hash = unix(account, line)
            if hash == psswrd:
                print('[*] Hash Found!\n[*]\tUsername: %s\n[*]\tPassword: %s'%(user, line))

#__DEFAULT RUN__#
if __name__ == '__main__':
    # parseamos argumentos para que resulte mas comodo de lanzar
    parse = argparse.ArgumentParser(description='Brute force routine for system passwords')
    parse.add_argument(
        '-os', '--OperatinSystem',
        required=True,
        help='Select Windows type OS or Unix type OS'
    )
    parse.add_argument(
        '-uf', '--unixFile',
        default='/etc/shadow',
        required=False,
        help='Directory & name of the file with the hashes in Unix OS'
    )
    parse.add_argument(
        '-wf', '--winFile',
        default='hashes.txt',
        required=False,
        help='Name of the file with the hashes in Windows OS'
    )
    parse.add_argument(
        '-pf', '--psswrdFile',
        default='passFile.txt',
        required=False,
        help='Name of the file with the passwords to test'
    )
    args = parse.parse_args()
    systm = args.OperatinSystem
    psswrds = args.psswrdFile
    if str(systm).lower() == 'windows':
        file = args.winFile
    elif str(systm).lower() == 'unix':
        file = args.unixFile
    #try:
    bruteForce(systm, file, psswrds)
    #except Exception:
    #    print('[!] Somethong went wrong. Please, verify the parameters. ')