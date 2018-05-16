import re


#Define variables for pass value as global variable
platform=''
threat_linker_1 =''
threat_linker_2 =''
area_linker_1=''
area_linker_2=''
threat_lindis_1=''
threat_lindis_2=''
area_lindis_1=''
area_lindis_2=''
threat_linother_1=''
threat_linother_2=''
area_linother_1=''
area_linother_2=''

error = ''

"""

   >>>> :::: Call functions & Check threat level according pattern dataset


   """

def linuxKernel(str,str2):

    print("Inside the function")
    global platform
    platform = 'Linux'

    platfrom = str
    exploit = str2
    print(":: "+exploit)
    try:
       threatHigh = ['local privilege escalation exploit', 'kaslr address leak exploit',
                     'memory corruption bugs vulnerability', 'socket use-after-free exploit',
                     'local denial of service exploit', 'race condition vulnerability']
       threatMedium = ['off-by-one (poc) exploit', 'overwriting the huge zero page', 'amit',
                       'the huge dirty cow overwriting the huge zero page']

       threatData = re.findall(
           r'local privilege escalation exploit|amit|kaslr address leak exploit|'
           r'overwriting the huge zero page|the huge dirty cow overwriting the huge zero page|memory corruption bugs vulnerability',
           exploit)

       print('END')
       print(threatData[0])
       print("final")
       for i in range(threatHigh.__len__()):
           if threatHigh:

               if (threatData[0] == threatHigh[i]):
                   print('--------------------------')
                   print(":: Threat Level is High ::")
                   print('--------------------------')
                   global threat_linker_1
                   threat_linker_1 = 'High'
                   global area_linker_1
                   area_linker_1 = threatData[0]

       for i in range(threatMedium.__len__()):

           if threatMedium:
               if (threatData[0] == threatMedium[i]):
                   print('--------------------------')
                   print('::: Area : ' ' :::')
                   print(":: Threat Level is Medium ::")
                   global threat_linker_2
                   threat_linker_2 = 'Medium'
                   global area_linker_2
                   area_linker_2 = threatData[0]

    except:
       global error
       error = 'Not found is database'
       print(error)
    return


#For linux distro

def linux_distro(str,str2):
    print("Inside the function")
    global platform
    platform = 'Linux distro'

    platfrom = str
    exploit = str2

    threatHigh = ['multiple persistent web vulnerabilities','denial of service exploit','cross site scripting vulnerabilities','stack corruption vulnerability']


    try:
        threatData = re.findall(
            'multiple persistent web vulnerabilities|denial of service exploit|cross site scripting vulnerabilities|stack corruption vulnerability',
            exploit)
        print("final")
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_lindis_1
                    threat_lindis_1 = 'High'
                    global area_lindis_1
                    area_lindis_1 = threatData[0]
    except:
        global error
        error = 'Not found is database'
        print(error)
    return



#For others eg. remote code

def others(str,str2):

    print("Inside the function")
    global platform
    platform = 'Linux'

    platfrom = str
    exploit = str2
    threatHigh = ['command execution Vulnerability']
    threatMedium = ['denial of service poc']

    try:

        threatData = re.findall(r'denial of service poc' , exploit)


        print('END')
        print(threatData[0])
        print("final")
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_linother_1
                    threat_linother_1 = 'High'
                    global area_linother_1
                    area_linother_1 = threatData[0]

        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global threat_linother_2
                    threat_linother_2 = 'Medium'
                    global area_linother_2
                    area_linother_2 = threatData[0]
    except:
        global error
        error = 'Not found is database'
        print(error)


    return
