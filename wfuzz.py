import wfuzz

def directory_scan():
    """
    Directory scan using Wfuzz - Directory brute-forcing to discover hidden files and directories
    """
    protocol = 'http://'
    target = input('Add target IP/URL: ')
    fuzzext = '/FUZZ'
    urltarget = protocol + target + fuzzext
    
    path = input("Add required wordlist: ")
    
    for r in wfuzz.fuzz(url=urltarget, hc=[404], payloads=[("file", dict(fn=path))]):
        print(r)

#Defining POST parameters for "fuzzing" function
def fuzzing_Postparams():
    """
    POST parameter fuzzing using Wfuzz
    """
    print('POST parameters can be found in browser inspect mode or via Burp Suite\n')
    
    #Defining the protocol
    webprotocol = 'http://'
    #Variable where the user-added URL/IP is stored
    target = input('Add target IP/URL:')
    #Adding the protocol to the URL
    urltarget = webprotocol + target
    #Variable where the path to the wordlist is stored
    path = input("Add required wordlist: ")
    param1 = input("Add first parameter: ")
    param2 = input("Add second parameter: ")
    cookie = input("Please, add the 'Cookie' including PHPSESSID: ")
    
    print("Do you know any user data for the target?")
    print("1: Yes")
    print("2: No")
    option = input("Please, choose an option: ")
    
    if option == "1":
        #Adding username from the user
        user = input("Add username: ")
        finalparam = param1 + "=" + user + "&" + param2 + "=" + "FUZZ"
        
        with wfuzz.get_session("-b " + cookie + " -c -z file," + path + " " + "--hs Invalid -d " + finalparam + " " + urltarget) as s:
            for r in s.fuzz():
                print(r)
    
    elif option == "2":
        #If the user does not know user data for the target, Wfuzz function will be used to find them using the added wordlist
        finalparam = param1 + "=" + "FUZZ" + "&" + param2 + "=" + "FUZZZ"
        
        with wfuzz.get_session("-b " + cookie + " -c -z file," + path + " " + "-z file," + path + " " + "--hs Invalid -d " + finalparam + " " + "-u " + urltarget) as s:
            for r in s.fuzz():
                print(r)
