from django.shortcuts import render, redirect

from django.urls import reverse

from django.views.generic import TemplateView
from estudiante.models import Estudiante, Evaluacion
from sesion.models import Peluche, Sesion, JuegoTopos, JuegoRompeC, JuegoLetras, JuegoLaberinto, JuegoColorear
from django.db.models import Count
from collections import Counter

import random
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from recomendacion.models import RecoJuegosS, RecoPeluche, RecoTablero, RecoVarita


# Create your views here.

class EstuChartView(TemplateView):
    template_name ="dashboard/GraphEstu.html"
    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            estudiantes = Estudiante.objects.all()
            uni_edu = Estudiante.objects.values("unidad_edu").annotate(count=Count("unidad_edu")).order_by("unidad_edu")       
            num_ses= Sesion.objects.values("Estudiante").annotate(countE=Count("Estudiante")).order_by("Estudiante")
            sesiones = Sesion.objects.all()
            peluche = Peluche.objects.all()

            nombre = kwargs['nombre']

            vPel=0
            vVar=0
            vJuS=0
            vTMofi=0
            vTMope=0

            for sesH in sesiones:
                if sesH.Estudiante.nombre == nombre:
                    if sesH.Herramienta =='Peluche MoFi':
                        vPel=vPel+1
                    if sesH.Herramienta =='Juegos Serios':
                        vJuS=vJuS+1
                    if sesH.Herramienta =='Tablero Mofi':
                        vTMofi=vTMofi+1
                    if sesH.Herramienta =='Tablero MoPe':
                        vTMope=vTMope+1
                    if sesH.Herramienta =='Varita':
                        vVar=vVar+1

            ses_her=[vPel,vJuS,vVar,vTMofi,vTMope]

            estAct=[]
            Act=['Sombrero','Zapatos','Manos','Cierres','Broches']
            valA=[0,0,0,0,0]

            estudianteF=Estudiante.objects.all()
            for estu in estudiantes:
                if estu.nombre==nombre:
                    estudianteF=estu


            for Pel in peluche:
                if Pel.Sesion.Estudiante.nombre==nombre:
                    aux=0
                    for ac in Act:
                        if ac == Pel.Tipo:
                            valA[aux]=valA[aux]+1
                        aux=aux+1
            
            ValJue=[0,0,0,0,0]
            JuTo = JuegoTopos.objects.all()
            contJueTo=0
            for jue in JuTo:
                for Ses in sesiones:
                    if Ses.id == jue.Sesion.id:
                        if Ses.Estudiante.nombre==nombre:
                            contJueTo=contJueTo+1
            #print(contJueTo)

            JuLa = JuegoLaberinto.objects.all()
            contJueLa=0
            for jue in JuLa:
                for Ses in sesiones:
                    if Ses.id == jue.Sesion.id:
                        if Ses.Estudiante.nombre==nombre:
                            contJueLa=contJueLa+1
            #print(contJueLa)

            JuRo = JuegoRompeC.objects.all()
            contJueRo=0
            for jue in JuRo:
                for Ses in sesiones:
                    if Ses.id == jue.Sesion.id:
                        if Ses.Estudiante.nombre==nombre:
                            contJueRo=contJueRo+1
            #print(contJueRo)

            JuCo = JuegoColorear.objects.all()
            contJueCo=0
            for jue in JuCo:
                for Ses in sesiones:
                    if Ses.id == jue.Sesion.id:
                        if Ses.Estudiante.nombre==nombre:
                            contJueCo=contJueCo+1
            #print(contJueCo)

            JuLe = JuegoLetras.objects.all()
            contJueLe=0
            for jue in JuLe:
                for Ses in sesiones:
                    if Ses.id == jue.Sesion.id:
                        if Ses.Estudiante.nombre==nombre:
                            contJueLe=contJueLe+1
            #print(contJueLe)

            ValJue=[contJueTo, contJueLa, contJueCo, contJueRo, contJueLe]

            RecoPelu=RecoPeluche.objects.all()
            RecoVal=[0,0,0,0,0]
            for Pel in RecoPelu:
                if Pel.Estudiante.nombre==nombre:
                    Sem=Pel.Semanas
                    Fre=Pel.FrecuenciaS   
                    RecoVal[0]=Pel.Sombrero
                    RecoVal[1]=Pel.Cordon 
                    RecoVal[2]=Pel.Velcro
                    RecoVal[3]=Pel.Cierre
                    RecoVal[4]=Pel.Broches

            RecoJue=RecoJuegosS.objects.all()
            RecoJuVal=[0,0,0,0,0]
            for Pel in RecoJue:
                if Pel.Estudiante.nombre==nombre:  
                    RecoJuVal[0]=Pel.Topos
                    RecoJuVal[1]=Pel.Laberinto 
                    RecoJuVal[2]=Pel.RompeC
                    RecoJuVal[3]=Pel.Colorear
                    RecoJuVal[4]=Pel.Letras
            
            Recotab=RecoTablero.objects.all()
            RecoTabVal=[0,0,0]
            for tab in Recotab:
                if tab.Estudiante.nombre==nombre:  
                    RecoTabVal[0]=tab.Trazos
                    RecoTabVal[1]=tab.Pinzas 
                    RecoTabVal[2]=tab.Precision
                    


            nombresE=[]
            for nom in estudiantes:
                for item in num_ses:
                    if nom.id==item['Estudiante']:
                        nombresE.append(nom.nombre)
                       # print (estudianteF[0].edad_cron_mes)

            colorV = [ ]
            for item in uni_edu:
                r = lambda: random.randint(0,255)
                color = ('#%02X%02X%02X' % (r(),r(),r()))
                colorV.append(color)

            context={
                "qs":estudiantes,
                "qsq":uni_edu,
                "colorV":colorV,
                "num_ses":num_ses,
                "nom_est_ses":nombresE,
                "numA":valA,
                "acti":Act,
                "est":nombre,
                "Estu":estudianteF,
                "PelReco":RecoVal,
                "Sem":Sem,
                "Fre": Fre,
                "ValJue": ValJue,
                "RecoValJu":RecoJuVal,
                "RecoTab":RecoTabVal,
                "SesHer":ses_her
                }
            
            return context

def graficas(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request,"dashboard/charts.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

class EstChartView(TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            uni_edu = Estudiante.objects.values("unidad_edu").annotate(count=Count("unidad_edu")).order_by("unidad_edu")
            estudiantes = Estudiante.objects.all()      
            num_ses= Sesion.objects.values("Estudiante").annotate(countE=Count("Estudiante")).order_by("Estudiante")
            nombresE=[]
            for nom in estudiantes:
                for item in num_ses:
                    if nom.id==item['Estudiante']:
                        nombresE.append(nom.nombre)

            colorV = [ ]
            for item in uni_edu:
                r = lambda: random.randint(0,255)
                color = ('#%02X%02X%02X' % (r(),r(),r()))
                colorV.append(color)

            context={
                "qs":estudiantes,
                "qsq":uni_edu,
                "colorV":colorV,
                "num_ses":num_ses,
                "nom_est_ses":nombresE}
            return context      

class EstuTableView(TemplateView):
    template_name = 'dashboard/estudiantes.html'
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context["qs"]=Estudiante.objects.all()
            return context

class EvalTableView(TemplateView):
    template_name = 'dashboard/eval.html'
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context["qs"]=Evaluacion.objects.all()
            return context

class SesiTableView(TemplateView):
    template_name = 'dashboard/sesiones.html'
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context["qs"]=Sesion.objects.all()
            return context

class PelTableView(TemplateView):
    template_name = 'dashboard/peluche.html'
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context["qs"]=Peluche.objects.all()
            return context

##############################

class PeluChartView(TemplateView):
    template_name ="dashboard/GraphPel.html"
    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            estudiantes = Estudiante.objects.all()     
            num_ses= Sesion.objects.values("Estudiante").annotate(countE=Count("Estudiante")).order_by("Estudiante")
            sesiones = Sesion.objects.all()
            peluche = Peluche.objects.all()

            nombre = kwargs['nombre']           
            estAct=[]
            Act=['Sombrero','Zapatos','Manos','Cierres','Broches']
            valA=[0,0,0,0,0]

            estudianteF=Estudiante.objects.all()
            for estu in estudiantes:
                if estu.nombre==nombre:
                    estudianteF=estu

            for Pel in peluche:
                if Pel.Sesion.Estudiante.nombre==nombre:
                    aux=0
                    for ac in Act:
                        if ac == Pel.Tipo:
                            valA[aux]=valA[aux]+1
                        aux=aux+1
            
            RepSon=[]
            FeSon=[]
            RepBro=[]
            FeBro=[]
            RepCor=[]
            FeCor=[]
            RepCie=[]
            FeCie=[]
            Repvel=[]
            Fevel=[]
            for Pelu in peluche:
                if Pelu.Sesion.Estudiante.nombre==nombre:
                    if 'Sombrero' == Pelu.Tipo:
                        auxSt=Pelu.Tiempo
                        auxVec=auxSt.split(":")
                        RepSon.append(int(auxVec[1]))
                        fe = str(Pelu.Sesion.fecha)
                        x = fe.split(" ", 1)
                        FeSon.append(x[0])

                    if 'Zapatos' == Pelu.Tipo:
                        auxSt=Pelu.Tiempo
                        auxVec=auxSt.split(":")
                        RepCor.append(int(auxVec[1]))
                        fe = str(Pelu.Sesion.fecha)
                        x=fe.split(" ", 1)
                        FeCor.append(x[0])

                    if 'Manos' == Pelu.Tipo:
                        auxSt=Pelu.Tiempo
                        auxVec=auxSt.split(":")
                        Repvel.append(int(auxVec[1]))
                        fe = str(Pelu.Sesion.fecha)
                        x=fe.split(" ", 1)
                        Fevel.append(x[0])

                    if 'Cierres' == Pelu.Tipo:
                        auxSt=Pelu.Tiempo
                        auxVec=auxSt.split(":")
                        RepCie.append(int(auxVec[1]))
                        fe = str(Pelu.Sesion.fecha)
                        x=fe.split(" ", 1)
                        FeCie.append(x[0])
                        

                    if 'Broches' == Pelu.Tipo:
                        auxSt=Pelu.Tiempo
                        auxVec=auxSt.split(":")
                        RepBro.append(int(auxVec[1]))
                        fe = str(Pelu.Sesion.fecha)
                        x=fe.split(" ", 1)
                        FeBro.append(x[0])
        
            nombresE=[]
            for nom in estudiantes:
                for item in num_ses:
                    if nom.id==item['Estudiante']:
                        nombresE.append(nom.nombre)
                       # print (estudianteF[0].edad_cron_mes)

            context={
                "qs":estudiantes,
                "num_ses":num_ses,
                "nom_est_ses":nombresE,
                "numA":valA,
                "acti":Act,
                "est":nombre,
                "Estu":estudianteF,
                "NumSon":RepSon,
                "NumBro":RepBro,
                "NumCor":RepCor,
                "NumCie":RepCie,
                "NumVel":Repvel,
                "FeSon":FeSon,
                "FeBro":FeBro,
                "FeCor":FeCor,
                "FeCie":FeCie,
                "FeVel":Fevel
                }
            
            return context
