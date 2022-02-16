import binascii, hashlib, sys

if len(sys.argv) != 3:
	print("[-] usage ntlmCracker.py <hashes_file> <dict_file>")
	exit()

hashes = open(sys.argv[1])
dictFile = open(sys.argv[2], 'r')
for account in hashes:
	for line in dictFile.readlines():
		line = line.replace("\n","")
		hash_account = account.split(':')[3]
		ntlm_hash = binascii.hexlify(hashlib.new('md4', line.encode('utf-16le')).digest())
		if ntlm_hash.decode("utf-8") == hash_account:
			print("[+] Hash found! Username: %s Password: %s " %(account.split(':')[0] , line))
