import re


#Define variables for pass value as global variable

threat_win_1 =''
threat_win_2 =''
threat_edge_1 =''
threat_edge_2 =''

area_win_1 =''
area_win_2 =''
area_edge_1 =''
area_edge_2 =''

platform =''

error=''

"""

   >>>> :::: Call functions & Check threat level according pattern dataset


   """

def windows(str,str2):
    print("Inside the function")

    global platform
    platform = 'Windows'


    platfrom = str
    exploit = str2
    threatHigh = ['constrained impersonation capability privilege escalation exploit','remote code execution exploit','security feature bypass','mount point arbitrary device open privilege escalation ex'
                  'file system metadata disclosures exploit','memory disclosure vulnerability','bypass exploit',
                  'pool overflow exploit','stack memory disclosure exploit',]
    threatMedium = []

    try:
        threatData = re.findall(
            r'constrained impersonation capability privilege escalation exploit|security feature bypass|mount point arbitrary device open privilege escalation ex|remote code execution exploit|'
            r'file system metadata disclosures exploit|memory disclosure vulnerability|bypass exploit|pool overflow exploit|stack memory disclosure exploit',
            exploit)

        print(threatData[0])
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global area_win_1
                    area_win_1 = threatData[0]
                    global threat_win_1
                    threat_win_1 = 'High'


        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global area_win_2
                    area_win_2 = threatData[0]
                    global threat_win_2
                    threat_win_2 = 'High'



    except:
        global error
        error ='Not found in database'
        print(error)

    return


def edge(str,str2):
    print("Inside the function")

    global platform
    platform = 'Windows'


    platfrom = str
    exploit = str2
    threatHigh = ['serverfreeallocation vulnerability','incorrectly parses object patterns exploit']
    threatMedium = ['bailoutontaggedvalue bailouts exploit','incorrect function declaration scope exploit','opttagchecks property consideration exploit','leafinterpreterframe vulnerability','incorrect function declaration scope exploit','inlinecallapplytarget_shared failed return exploit']

    try:
        threatData = re.findall(
            r'incorrect function declaration scope exploit|serverfreeallocation vulnerability|leafinterpreterframe vulnerability|incorrect function declaration scope exploit|inlinecallapplytarget_shared failed return exploit'
            r'opttagchecks property consideration exploit|bailoutontaggedvalue bailouts exploit|incorrectly parses object patterns exploit' , exploit)

        print(threatData[0])
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global area_edge_1
                    area_edge_1 = threatData[0]
                    global threat_win_1
                    threat_win_1 = 'High'


        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global area_edge_2
                    area_edge_2 = threatData[0]
                    global threat_edge_2
                    threat_edge_2 = 'Medium'



    except:
        global error
        error ='Not found in database'
        print(error)

    return