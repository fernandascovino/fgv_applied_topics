from datetime import datetime as dt
from pandas import to_datetime

# LEGISLATURAS
# i = round((dt.now().year - 2003)/4+0.5)
# period = list(range(0,i))
# legislaturas = {}

# for x in period:
#     t = ('{}-01-31'.format(2003+4*x), '{}-02-01'.format(2007+4*x))
#     legislaturas[t] = 52+x

anos = round((dt.now().year - 2003)/4+0.5)
periodo = list(range(0,anos))
legislaturas = {to_datetime('{}-01-31'.format(2003+4*x)): 52+x for x in periodo}
    
    