import os
import sys
import io
import filecmp
import pytest

from pykoa.koa import Koa 
from astropy.table import Table,Column

userdict = {
   "koaadmin_zuxbor10":"Successfully login as koaadmin",
   "xxkoaadmin_zuxbor10":"Failed to login: userid [xxkoaadmin] is invalid.",
   "koaadmin_xxzuxbor10":"Failed to login: Incorrect password [xxzuxbor10] for userid [koaadmin]"
}

#server = "http://vmkoatest.ipac.caltech.edu:8000/"

#
#    test login method: correctly, wrong userid, and wrong password
#
@pytest.mark.parametrize ("user, expected", list(userdict.items()), ids=list(userdict.keys()))  
 
def test_login_success (user, expected, capsys):
    
    ind = user.index('_')
    userid = user[0:ind]
    password = user[ind+1:]
    
    Koa.login ('./tapcookie.txt', \
        userid=userid, \
        password=password)
        
        #password=password, \
        #server=server)
    
    out, err = capsys.readouterr()
    assert out.startswith (expected)


#
#   Test query_datetime method for all instruments; returns ipac format tables. 
#   Pass if the returned IPAC table is identical to the truth data.
#
#fmtdict = {
#    "ipac":".tbl",
#    "votable":".xml",
#    "csv":".csv",
#    "tsv":".tsv"
#}

datetimedict = {
    "hires":"2019-01-01 00:00:00/2019-01-10 23:59:59",
    "deimos":"2019-01-01 00:00:00/2019-02-28 23:59:59",
    "osiris":"2019-05-28 00:00:00/2019-05-31 23:59:59",
    "esi":"2015-09-01 00:00:00/2015-09-30 23:59:59"
}

@pytest.mark.parametrize ("instr,datetime", list(datetimedict.items()), \
    ids=list(datetimedict.keys()))
 
def test_query_datetime (instr, datetime, capsys):

    outpath = './datetime.' + instr + '.tbl'
    datapath = './truthdata/datetime.' + instr + '.tbl'
 
    Koa.query_datetime (instr, \
        datetime, \
        outpath, \
        cookiepath='./tapcookie.txt')
        
        #cookiepath='./tapcookie.txt', \
        #server=server)
    
    assert os.path.exists(outpath), \
        f'Result not downloaded to file [{outpath:s}]'
    assert (filecmp.cmp (outpath, datapath, shallow=False))


