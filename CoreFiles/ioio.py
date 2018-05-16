import re
from CoreFiles import phpsSignature as ps
from CoreFiles import windowsSingnature as win
from CoreFiles import linuxSignature as lin



print('----------------------')
print('   Exploit filter   ')
print('----------------------')

print()

print("Input Any String : ")
#st1 = input().lower()

def passName(str1):

    ex_name = str1
    return ex_name

def explitName(str1):

    exploit_name =str(str1)
    print('Showing from corefiles')
    print('Exolit name is : '+exploit_name)

    st1 = exploit_name.lower()

    """

       >>>> :::: call specfic function to determine the threat 


       """
    def findTheatPHP(str):
        print('----- Indentifying threat for PHP exploit -------')
        print()
        part = str
        print("Function Called")

        if (part == 'wordpress'):
            ps.wordpress(part, st1)

        elif (part == 'joomla'):
            ps.joomla(part, st1)

        elif (part == 'drupal'):
            ps.drupal(part,st1)

        else:
            ps.webApplication(part, st1)
            print("Php > from other")

    def findThreatWindows(str):
        print('----- Indentifying threat for Windows exploit -------')
        print()
        part = str
        print("Function Called")

        if (part == 'microsoft windows'):
            win.windows(part, st1)

        elif(part == 'microsoft edge chakra'):
            win.edge(part,st1)

        else:
            print("Not match for windows ")

    def findThreatLinux(str):
        print('----- Indentifying threat for Linux exploit -------')
        print()
        part = str
        print("Function Called")

        if (part == 'linux kernel'):
            lin.linuxKernel(part, st1)

        elif (part == 'centos' or part == 'ubuntu' or part == 'backbox os'):
            lin.linux_distro(part, st1)



        else:
            lin.others(part,st1)

    """

    >>>> :::: Start main functions "Identify platform


    """

    def identifyPlatform():

        print('inside indenfity function')
        strn = st1


        try:
            keyPlatfromPhp = re.findall(r'wordpress|mybb|xenforo'
                                        r'php|drupal|joomla|wordpress|amit|playsms|icewarp|wuzhi', strn)
            php = keyPlatfromPhp[0]

        except IndexError:
            php = 'null'

        try:
            keyPlatfromWindows = re.findall(r'microsoft edge chakra|firefox|microsoft office|microsoft windows', strn)
            windows = keyPlatfromWindows[0]

        except IndexError:
            windows = 'null'

        try:
            print('ckl')
            keyPlatfromLinux = re.findall(r'linux kernel|centos|mikrotik|libreoffice|solarwinds lem|apache'
                                          r'ubuntu|linux xfburn|backbox os|ponyos|ettercap '
                                          r'barracuda waf|alienvault|unitrends ueb'
                                          r'rubygems|ucopia|solarwinds lem |tcpreplay', strn)

            linux = keyPlatfromLinux[0]
            print('Key lin :'+linux)

        except IndexError:
            linux = 'null'

        print("++++++++++++++++++++++++++++++++++++++++++")

        if keyPlatfromPhp:

            phpDataSetForPhp = ['joomla', 'wordpress', 'xenforo','icewarp','php', 'drupal','wuzhi','playsms','amit']
            for i in range(phpDataSetForPhp.__len__()):
                if (keyPlatfromPhp[0] == phpDataSetForPhp[i]):
                    print('Match found')
                    platfrom = 'PHP'
                    print("Platfrom : " + platfrom)
                    print("Part : " + keyPlatfromPhp[0].upper())
                    findTheatPHP(keyPlatfromPhp[0])

        elif keyPlatfromWindows:
            print("key is Widows")

            windowsDataSet = ['microsoft windows', 'firefox', 'microsoft office','microsoft edge chakra']
            for i in range(windowsDataSet.__len__()):
                if (keyPlatfromWindows[0] == windowsDataSet[i]):
                    print('Match Found')
                    platfrom = 'Windows'
                    print('Platfrom : ' + platfrom.upper())
                    findThreatWindows(keyPlatfromWindows[0])



        elif keyPlatfromLinux:

            linuxDataSet = ['linux kernel','mikrotik','centos', 'libreoffice', 'solarwinds lEM', 'apache', 'ubuntu',
                            'linux xfburn', 'backbox os', 'ponyos', 'ettercap', 'barracuda waf', 'alienvault',
                            'unitrends ueb', 'shadowsocks',
                            'rubygems', 'ucopia', 'solarwinds lem', 'tcpreplay']

            for i in range(linuxDataSet.__len__()):
                if (keyPlatfromLinux[0] == linuxDataSet[i]):
                    print('Match Found')
                    platfrom = 'Linux'
                    print('Platfrom : ' + platfrom.upper())
                    print('Area : ' + keyPlatfromLinux[0].upper())
                    findThreatLinux(keyPlatfromLinux[0])

        """"



        //   ::::::  END OF METHOD ::::::::: ///




        """

    identifyPlatform()


    """"
    //   Identifying Threat Level for particular exploit ///
    """










