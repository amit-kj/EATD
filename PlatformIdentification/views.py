from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import post
from .forms import explit_search
from CoreFiles import ioio
from CoreFiles import phpsSignature as php
from CoreFiles import windowsSingnature as  win
from CoreFiles import linuxSignature as lin

from django.http import HttpResponse


import test as t
# Create your views here.


def index(request):


    return  render(request,"home.html")

def create(request):

    print("start form")

    name = explit_search(request.POST or None)

    if name.is_valid():
        print("button clicked")
        #initialize

        #Windows
        win.area_edge_1=''
        win.area_edge_2=''
        win.area_win_1=''
        win.area_win_2=''
        win.threat_edge_1=''
        win.threat_edge_2=''
        win.threat_win_1=''
        win.threat_win_2=''
        win.error=''
        win.platform=''

        #Php
        php.area_joomla_1=''
        php.area_joomla_2=''
        php.area_wordpress_1=''
        php.area_wordpress_2=''
        php.threat_wordpress_1=''
        php.threat_wordpress_2=''
        php.threat_joomla_1=''
        php.threat_joomla_2=''
        php.threat_drupal_1=''
        php.threat_drupal_2=''
        php.area_drupal_1=''
        php.area_drupal_2=''
        php.threat_webapp_1=''
        php.threat_webapp_2=''
        php.area_webapp_1=''
        php.area_webapp_2=''
        php.error=''
        php.platform=''



        #Linux

        lin.threat_linker_1 = ''
        lin.threat_linker_2 = ''
        lin.area_linker_1 = ''
        lin.area_linker_2 = ''
        lin.threat_lindis_1 = ''
        lin.threat_lindis_2 = ''
        lin.area_lindis_1 = ''
        lin.area_lindis_2 = ''
        lin.threat_linother_1 = ''
        lin.threat_linother_2 = ''
        lin.area_linother_1 = ''
        lin.area_linother_2 = ''
        lin.error=''
        lin.platform=''

        explit_name = request.POST['exploit']
        print("Name : "+explit_name)



        ioio.explitName(explit_name)
        ioio.passName(explit_name)

        #get form ioio(for php exploits)

        name = str(explit_name)





    #Define variable to pass through html
    e_name = name
    e_threat = (win.threat_win_1+win.threat_win_2+win.threat_edge_1+win.threat_edge_2+php.threat_joomla_1+php.threat_joomla_2+php.threat_wordpress_1+php.threat_wordpress_2+
                lin.threat_linker_1+lin.threat_linker_2+lin.threat_lindis_1+lin.threat_lindis_2+php.threat_drupal_1+php.threat_drupal_2+php.threat_webapp_1+
                php.threat_webapp_2+lin.threat_linother_1+lin.threat_linother_2)

    e_platform = (win.platform+php.platform+lin.platform)

    e_area = (win.area_win_1+win.area_win_2+win.area_edge_1+win.area_edge_2+php.area_wordpress_1+php.area_wordpress_2+php.area_joomla_1+php.area_joomla_2+
              lin.area_linker_1+lin.area_linker_2+lin.area_lindis_1+lin.area_lindis_2+php.area_drupal_1+php.area_drupal_2+php.area_webapp_1+php.area_webapp_2+
              lin.area_linother_1+lin.area_linother_2)


    e_error=(win.error+php.error+lin.error)

    # set threat and area if not found in dataset

    if(e_threat == ''):
        e_threat ='N\A'
        e_area ='N\A'



    return render(request,'form.html',{'name':e_name,'e_name':e_threat,'platform':e_platform,'area':e_area,'error':e_error})



def chart(request):

    return render(request, 'chart.html')



def about(request):

    return render(request, 'about.html')



def pchart(request):





    return render(request, 'pchart.html')




