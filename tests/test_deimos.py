import sys
import io
from pykoa.koa import Koa 
from astropy.table import Table,Column

def test_login():
    
    try:
        Koa.login ('./tapcookie.txt', \
            userid='koaadmin', \
            password='zuxbor10', \
            debugfile='./pytest.debug')

    except Exception as e:
        print (f'Koa.login exception: {str(e):s}')

#
#    search by datetime: result file all found records
#
def test_datetime_query():

    status = ''
 
    try:
        Koa.query_datetime ('deimos', \
            '2020-09-01 00:00:00/2020-09-30 23:59:59', \
            './datetime.tbl', \
            cookiepath='./tapcookie.txt')
    
        status == 'ok'
 
    except Exception as e:
        print (f'query_datetime exception: {str(e):s}')
        
    if (status == 'ok'):

        try:
            astropytbl = Table.read ('./datetime.tbl', format='ascii.ipac')
            nrec = len (astropytbl)
            print (f'astropytbl exception: {str(e):s}')

      
        except Exception as e:
            print (f'astropytbl exception: {str(e):s}')

        print (f'datetime.tbl contains {nrec:d} recs')

