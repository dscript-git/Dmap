import os
#colors
yellow = '\033[93m'
green = '\033[92m'

class Root:
    def root_check(self):
        os.system('clear')
        if os.getuid() == 0:
            print ("")
            print (green," [Good, You Are Rooted]")
            print ("  [You'll have the Full Option]")
            return (' [+] === ROOTED MODE ===')
        else:
            print ("")
            print (yellow," [Sorry, You Aren't Rooted]")
            print ("  [You'll have Limited Option]")
            return (' [!] === NON-ROOTED MODE ===')
