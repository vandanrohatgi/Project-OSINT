modules=['portScanModule','emailModule','subDomainsModule','publicIpModule','sslModule']
from modules.sslModule import getSSL

def start(data):
    if len(data) < 3:
        return("Please select at least one module")
    else:
        return("starting...")