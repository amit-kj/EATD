"""
Here stores all php exploits signature & Theat level
data
"""
import re


#Define variables for pass value as global variable

platform=''
threat_wordpress_1 =''
threat_wordpress_2 =''
threat_joomla_1 =''
threat_joomla_2 =''
area_wordpress_1=''
area_wordpress_2=''
area_joomla_1=''
area_joomla_2=''
threat_drupal_1 =''
threat_drupal_2 =''
area_drupal_1=''
area_drupal_2=''
threat_webapp_1=''
threat_webapp_2=''
area_webapp_1=''
area_webapp_2=''

error = ''
"""

   >>>> :::: Call functions & Check threat level according pattern dataset


   """
def wordpress(str,str2):

    print("Inside the function")
    global platform
    platform = 'PHP'

    platfrom = str
    exploit = str2
    threatHigh = ['remote code execution vulnerability','remote file inclusion','privilege escalation exploit','remote file upload exploit','shell upload exploit','php code upload exploit','authenticated file upload exploit']
    threatMedium = ['cross site request forgery', 'csv injection vulnerability','cross site scripting vulnerability','cookie consent authenticated persistent cross-site scriptit']

    try:
        threatData = re.findall(
            r'cross site scripting vulnerability|remote code execution vulnerability|remote file inclusion|privilege escalation exploit|remote file upload exploit|csv injection vulnerability|cross site request forgery'
            r'cookie consent authenticated persistent cross-site scriptit|shell upload exploit|php code upload exploit|authenticated file upload exploit',
            exploit)

        print(threatData[0])
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_wordpress_1
                    threat_wordpress_1 = 'High'
                    global area_wordpress_1
                    area_wordpress_1=threatData[0]


        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global threat_wordpress_2
                    threat_wordpress_2 = 'Medium'
                    global area_wordpress_2
                    area_wordpress_2 = threatData[0]



    except:
        global error
        error='Not found is database'
        print(error)

    return



def joomla(str,str2):
    print("Inside the function")

    global platform
    platform = 'PHP'


    platfrom = str
    exploit = str2

    threatHigh=['sql injection vulnerability','arbitrary file download vulnerability','property injection exploit','authenticated remote code exploit',
                'file upload vulnerability','sessionid sql injection vulnerability']
    threatMedium=['cross-site request forgery' , 'csv macro injection vulnerability','backup file download vulnerability']

    try:
        threatData = re.findall(
            r'|cross-site request forgery|property injection exploit|csv injection vulnerability|'
            r'sql injection vulnerability|authenticated remote code exploit|'
            r'|csv macro injection vulnerability|arbitrary file download vulnerability|file upload vulnerability|sessionid sql injection vulnerability|backup file download vulnerability|',
            exploit)
        print(threatData[0])
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print('<<< Area : ' + platfrom + ' >>>')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_joomla_1
                    threat_joomla_1 = 'High'
                    global area_joomla_1
                    area_joomla_1 = threatData[0]

        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global threat_joomla_2
                    threat_joomla_2 = 'Medium'
                    global area_joomla_2
                    area_joomla_2 = threatData[0]

        return
    except:
        global error
        error='Not found is database'
        print(error)





def drupal(str,str2):
    print("Inside the function")

    global platform
    platform = 'PHP'


    platfrom = str
    exploit = str2
    threatHigh=['sql injection vulnerability','property injection exploit','sql injection','authenticated remote code exploit']
    threatMedium=['pp']

    try:
        threatData = re.findall(
            r'cross site scripting vulnerability |property injection exploit|csv injection vulnerability|cross site request forgery|sql injection|sql injection vulnerability|authenticated remote code exploit|',
            exploit)
        print(threatData[0])

        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print('<<< Area : ' + platfrom + ' >>>')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_drupal_1
                    threat_drupal_1 = 'High'
                    global area_drupal_1
                    area_drupal_1 = threatData[0]

        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global threat_drupal_2
                    threat_drupal_2 = 'Medium'
                    global area_drupal_2
                    area_drupal_2 = threatData[0]

        return
    except:
        global error
        error='Not found is database'
        print(error)


def others(str,str2):

    print("Inside the function")

    platfrom = str
    exploit = str2

    threatHigh = ['database backup download vulnerability', 'cross-site scripting vulnerabilities', 'sql injection',
                  'code execution vulnerability', 'remote code execution exploit'
        , 'file upload exploit', 'local file disclosure exploit']
    threatMedium = ['physical path leakage vulnerability', 'request forgery vulnerability',
                    'open redirection vulnerabilities']


    try:

        threatData = re.findall(
            r'database backup download vulnerability|cross-site scripting vulnerabilities|sql injection|code execution vulnerability|remote code execution exploit|file upload exploit|local file disclosure exploit|physical path leakage vulnerability|'
            r'request forgery vulnerability|open redirection vulnerabilities', exploit)

        print(threatData[0])

        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print('<<<< Area : ' + platfrom + ' >>>>')
                    print(":: Threat Level is High ::")
                    print('--------------------------')

        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('<<<< Area : ' + platfrom + ' >>>>')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')

        return
    except:

        global error
        error = 'Not found is database'
        print(error)





def webApplication(str,str2):
    print("Inside the function")

    global platform
    platform = 'PHP'


    platfrom = str
    exploit = str2

    threatHigh=['sql injection vulnerability','filename authenticated code execution exploit','directory traversal vulnerability','cross site scripting vulnerability',
                'directory traversal vulnerability']
    threatMedium=['cross site request forgery']

    try:
        threatData = re.findall(
            r'cross site scripting vulnerability |directory traversal vulnerability|csv injection vulnerability|cross site request forgery|sql injection|sql injection vulnerability|pp'
            r'filename authenticated code execution exploit|directory traversal vulnerability',
            exploit)
        print(threatData[0])
        for i in range(threatHigh.__len__()):
            if threatHigh:

                if (threatData[0] == threatHigh[i]):
                    print('--------------------------')
                    print('<<< Area : ' + platfrom + ' >>>')
                    print(":: Threat Level is High ::")
                    print('--------------------------')
                    global threat_webapp_1
                    threat_webapp_1 = 'High'
                    global area_webapp_1
                    area_webapp_1 = threatData[0]

        for i in range(threatMedium.__len__()):

            if threatMedium:
                if (threatData[0] == threatMedium[i]):
                    print('--------------------------')
                    print('::: Area : ' + platfrom + ' :::')
                    print(":: Threat Level is Medium ::")
                    print('--------------------------')
                    global threat_webapp_2
                    threat_webapp_2 = 'Medium'
                    global area_webapp_2
                    area_webapp_2 = threatData[0]


    except:
        global error
        error='Not found is database'
        print(error)
    return


