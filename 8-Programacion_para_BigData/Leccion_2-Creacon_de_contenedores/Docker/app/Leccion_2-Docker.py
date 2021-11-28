'''
  Author: Python_Elidas
  Email: Pyro.elidas@gmail.com
  Python Version: 3.6.9
  Date: 2021-09-09T09:57:31.080Z
  Version: 0.0.1
'''

# __LIBRARIES__ #
from fastapi import FastAPI


# __MAIN CODE__ #
app = FastAPI()

@app.get('/')
async def root():
    return {'Message': 'Welcome to FastAPI'}


# __NOTES__ #
'''
  >
'''


# __BIBLIOGRAPHY__
'''
  >
'''
