
    
import os
import optparse
import sys
import nmap3
import time
nm = nmap3.Nmap()
parse = optparse.OptionParser()

parse.add_option("-?", action="help",help="show the options")
parse.add_option("-t", help="the target", dest="target")

(options, args) = parse.parse_args()

ping = os.system("ping -c 1 " + options.target) #server up or down

os.system("clear")
os.system("figlet ScaNmap")

results = nm.nmap_version_detection(options.target) #nmap -sV dict

print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)

print ('\n####################\n')
print ('[+]HOST: ' + options.target)
#server up or down
if ping == 0:
    print ('[+]STATE : UP')
    
else:
    print ('[+]STATE : DOWN')
    sys.exit()
    
#search ports and services
for dict in results:
    print ('\n####################\n')
    print ('[+]PROTOCOL:', dict['protocol'])
    print ('[+]PORT:', dict['port'],'| STATE:',dict['state'])
    try:
        print ('[+]SERVICE:', dict['service']['name'], '| VERSION:'+ dict['service']['product'] + dict['service']['version'])
    except NameError:
        print ('[+]SERVICE:', dict['service']['name'], '| VERSION:'+ dict['service']['product'])
    except NameError:
        print ('[+]SERVICE:', dict['service']['name'], '| VERSION:'+ dict['service']['version'])
    except:
        print ('[+]SERVICE:', dict['service']['name'])

print('MAIN PORTS: 20, 21, 22, 23, 25(587), 53, 80, 443, 8080, 43')
print ('\n####################\n')
    
    
    
