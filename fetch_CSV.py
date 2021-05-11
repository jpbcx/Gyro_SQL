import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

srvhost = "102.37.101.111"
svruser = "azureuser"
svrkey = "C:\\Users\\jonathanp\\Documents\\Bidvest CSV-SQL\\SSH-keys\\GyroSFTP_key_0426.pem"
lpath = "C:\\Users\\jonathanp\\Documents\\Bidvest CSV-SQL\\Work\\Sandbox\\"

def fetch_file(filename)
filename = filename+".csv"
with pysftp.Connection(srvhost, username=svruser, private_key=svrkey, cnopts=cnopts) as sftp:
    sftp.chdir("/data/bidvest/upload") # This is the remote path.
    sftp.get(filename, localpath=lpath+filename) # This is the particular file that you are after.
# Reinhartd wants a copy of the DB files.