import os

#Function that will "clear" the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n" + "-" * 500)

#Welcome message and ASCII art
print("\n\n\n" + "-" * 500)
print("Welcome, this script contains a set of tools for detecting vulnerabilities in WEB applications!")
print("\n")
print("""
██╗███╗   ██╗███████╗
██║████╗  ██║██╔════╝
██║██╔██╗ ██║█████╗  
██║██║╚██╗██║██╔══╝  
██║██║ ╚████║██║     
╚═╝╚═╝  ╚═══╝╚═╝     
""")

def main_menu():
    print("Choose a tool to start\n")
    print("1: OWASP ZAP")
    print("2: Wfuzz")
    print("3: Nmap")
    #Displaying the 3 possible tools
    tool = input("\nPlease, enter your chosen tool: ")
    clear()  #Clearing the terminal

    if tool == "1":  #If the user chooses OWASP ZAP, a submenu will be shown where they need to choose the scan type
        print("What type of scan do you want to perform?\n")
        print("1: Spider scan (Automatic discovery of new resources (URL) on a specific site)")
        print("2: Active scan (Active search for potential vulnerabilities, using known methods)")
        print("3: Return to main menu")
        option = input("\nPlease, enter your chosen option: ")
        clear()

        if option == "1":
            from zap import spider_scan  #If the user chooses option 1, Spider scan will be executed
            spider_scan()
        elif option == "2":
            from zap import active_scan  #If the user chooses option 2, Active scan will be executed
            active_scan()
        elif option == "3":  #If the user chooses option 3, it will return to the main menu
            main_menu()
    
    elif tool == "2":  #If the user chooses Wfuzz
        print("What type of scan do you want to perform?\n")
        print("1: Directory scan (Directory scanning)")
        print("2: POST parameter fuzzing (Fuzzing POST parameters)")
        print("3: Return to main menu")
        option = input("\nPlease, enter your chosen option: ")
        clear()
        
        if option == "1":
            from wfuzz import directory_scan
            directory_scan()
        elif option == "2":
            from wfuzz import fuzzing_Postparams
            fuzzing_Postparams()
        elif option == "3":
            main_menu()
    
    elif tool == "3":  #If the user chooses Nmap
        print("What type of scan do you want to perform?\n")
        print("1: Service version detection (Service version detection)")
        print("2: Top ports scan (Top ports scanning)")
        print("3: Return to main menu")
        option = input("\nPlease, enter your chosen option: ")
        clear()
        
        if option == "1":
            from nmap import serviceSCan
            serviceSCan()
        elif option == "2":
            from nmap import topPortScan
            topPortScan()
        elif option == "3":
            main_menu()

if __name__ == "__main__":
    main_menu()
