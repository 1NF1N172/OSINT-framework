import nmap3
import json

def serviceSCan():
    """
    Service version detection scan using Nmap
    """
    target = input("Please, enter target IP/URL: ")
    #User adds target URL/IP
    print("Please, wait a few seconds...")
    nmap = nmap3.Nmap()
    #Execution of service version detection
    version_result = nmap.nmap_version_detection(target)
    #Output of the result
    print(version_result)

def topPortScan():
    """
    Top port scan with service version detection using Nmap
    """
    target = input("Please, enter target IP/URL: ")
    #Defining the Nmap variable
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(target, args="-sV")
    #Output of the result
    print(results)
