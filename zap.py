import time
import os
from pprint import pprint
import subprocess
from zapv2 import ZAPv2
import logging

#clear function to clear the terminal after each choice
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_zap():
    """Starting OWASP ZAP in Daemon mode"""
    print('Starting ZAP ...')
    subprocess.Popen(['/usr/share/zaproxy/zap.sh', '-daemon', '-config', 'api.key=hello'], 
                     stdout=open(os.devnull, 'w'))
    #Starting OWASP Zap in Daemon mode
    print('Please wait 10 seconds for ZAP to load...')
    time.sleep(10)

def spider_scan():
    """
    Spider scan - Automatic discovery of new resources (URL) on a specific site
    """
    protocol = 'http://'
    target = input('Enter target URL: ')
    urlTarget = protocol + target
    apiKey = "hello"
    
    zap = ZAPv2(apikey=apiKey)
    
    print('Accessing target {}'.format(urlTarget))
    zap.urlopen(urlTarget)
    time.sleep(2)
    
    print('"Spider" scanning {}'.format(urlTarget))
    scanid = zap.spider.scan(urlTarget)
    
    #Loop until the scan finishes
    while (int(zap.spider.status(scanid)) < 100):
        print('Progress %: {}'.format(zap.spider.status(scanid)))
        time.sleep(5)
    
    print('Scanning is complete!')
    
    # Generate reports
    with open('report.html', 'w') as f:
        f.write(zap.core.htmlreport(apikey=apiKey))
    
    with open('report.xml', 'w') as f:
        f.write(zap.core.xmlreport(apikey=apiKey))
    
    print('Reports have been saved as report.html and report.xml')

def active_scan():
    """
    Active scan - Active search for potential vulnerabilities, using known methods
    """
    protocol = 'http://'
    target = input('Enter target URL: ')
    urlTarget = protocol + target
    apiKey = "hello"
    
    zap = ZAPv2(apikey=apiKey)
    
    print('Accessing target {}'.format(urlTarget))
    zap.urlopen(urlTarget)
    time.sleep(2)
    
    print('"Active" scanning {}'.format(urlTarget))
    scanid = zap.ascan.scan(urlTarget)
    
    #Loop until the scan finishes
    while (int(zap.ascan.status(scanid)) < 100):
        print('Progress %: {}'.format(zap.ascan.status(scanid)))
        time.sleep(5)
    
    print('Scanning is complete!')
    
    # Generate reports
    with open('report.html', 'w') as f:
        f.write(zap.core.htmlreport(apikey=apiKey))
    
    with open('report.xml', 'w') as f:
        f.write(zap.core.xmlreport(apikey=apiKey))
    
    print('Reports have been saved as report.html and report.xml')
