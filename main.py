import sys
from ib_insync import *
import pandas as pd

ib = IB()

# IB Gateway
# ib.connect('127.0.0.1', 4002, clientId=1)

# TWS
ib.connect('127.0.0.1', 7497, clientId=5)

try:

except Exception as e:
  print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
  print(e)