#!/usr/bin/python
import os, sys
with open("/dev/shm/ttt.txt", "w") as fd:
	fd.write("hola")
	fd.write(os.name)
