import os
import sys
import nmap3
nm = nmap3.Nmap()

ping = os.system("ping -c 1 " + sys.argv[1]) #server up or down

results = nm.nmap_version_detection(sys.argv[1]) #nmap -sV dict

print ('####################\n')
print ('[+]HOST: ' + sys.argv[1])

#server up or down
if ping == 0:
    print ('[+]STATE : UP')
    
else:
    print ('[+]STATE : DOWN')
    
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
    
    
