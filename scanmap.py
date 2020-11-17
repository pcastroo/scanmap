import os
import nmap3
nm = nmap3.Nmap()

target = input("TARGET: ") #input the target
ping = os.system("ping -c 1 " + target) #server up or down

results = nm.nmap_version_detection(target) #nmap -sV dict

print ('####################\n')
print ('[+]HOST : ' + target)

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