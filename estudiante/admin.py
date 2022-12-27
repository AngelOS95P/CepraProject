from django.contrib import admin
from .models import Estudiante, Evaluacion
from clips import Environment, Symbol
import clips
from multiprocessing import Process, Queue

from recomendacion.models import RecoJuegosS, RecoPeluche, RecoTablero, RecoVarita


# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    pass
    list_display=('id','nombre','sexo','edad_cron_mes','edad_eval_mes','puntuacion','puntuacionMF','puntuacionMP','lateralidad','nivel','unidad_edu','ciudad')

admin.site.register(Estudiante, EstudianteAdmin)

class EvaluacionAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','M52','M53','M54','M55','M56','M57','M58','M59','M60','M61','M62','M66','M67','M68','M69','M70','M71','M72','M73','M74','M75','M76','M77')

    def save_model(self, request, obj, form, change):
        recomendacionEst(obj, obj.Estudiante)
        print("llamado")

        #queue = Queue()
        #p = Process(target=recomendacionEst, args=(queue, obj, obj.Estudiante))
        #p.start()
        #p.join() # this blocks until the process terminates
        #result = queue.get()
        #print (result)

admin.site.register(Evaluacion, EvaluacionAdmin)


def recomendacionEst(Eval, Est):
    print("Entra")
    idEvalEst=Est.id
    nom=Est.nombre
    puntuacion=Est.puntuacion
    PMF=Est.puntuacionMF
    PMP=Est.puntuacionMP
    edadEst=Est.edad_eval_mes
    
    clp = Environment()
    clp.load('SE.clp')

    clp.eval("(assert  (Edad "+str(edadEst)+"))")
    clp.eval("(assert  (PMF "+str(PMF)+"))")
    clp.eval("(assert  (PMP "+str(PMP)+"))")
    
    M52  =  Eval.M52
    if M52 == "Adquirido": val=2
    if M52 == "En proceso": val=1
    if M52 == "No adquirido": val=0
    sAuxF = "(assert  (M52 "+ str(val) +"))"
    clp.eval(sAuxF)
    
    M53  =  Eval.M53
    if M53 == "Adquirido": val=2
    if M53 == "En proceso": val=1
    if M53 == "No adquirido": val=0
    sAuxF = "(assert  (M53 "+ str(val) +"))"
    clp.eval(sAuxF)

    M54  =  Eval.M54
    if M54 == "Adquirido": val=2
    if M54 == "En proceso": val=1
    if M54 == "No adquirido": val=0
    sAuxF = "(assert  (M54 "+ str(val) +"))"
    clp.eval(sAuxF)

    M55  =  Eval.M55
    if M55 == "Adquirido": val=2
    if M55 == "En proceso": val=1
    if M55 == "No adquirido": val=0
    sAuxF = "(assert  (M55 "+ str(val) +"))"
    clp.eval(sAuxF)

    M56  =  Eval.M56
    if M56 == "Adquirido": val=2
    if M56 == "En proceso": val=1
    if M56 == "No adquirido": val=0
    sAuxF = "(assert  (M56 "+ str(val) +"))"
    clp.eval(sAuxF)

    M57  =  Eval.M57
    if M57 == "Adquirido": val=2
    if M57 == "En proceso": val=1
    if M57 == "No adquirido": val=0
    sAuxF = "(assert  (M57 "+ str(val) +"))"
    clp.eval(sAuxF)

    M58  =  Eval.M58
    if M58 == "Adquirido": val=2
    if M58 == "En proceso": val=1
    if M58 == "No adquirido": val=0
    sAuxF = "(assert  (M58 "+ str(val) +"))"
    clp.eval(sAuxF)

    M59  =  Eval.M59
    if M59 == "Adquirido": val=2
    if M59 == "En proceso": val=1
    if M59 == "No adquirido": val=0
    sAuxF = "(assert  (M59 "+ str(val) +"))"
    clp.eval(sAuxF)

    M66  =  Eval.M66
    if M66 == "Adquirido": val=2
    if M66 == "En proceso": val=1
    if M66 == "No adquirido": val=0
    sAuxF = "(assert  (M66 "+ str(val) +"))"
    clp.eval(sAuxF)

    M67  =  Eval.M67
    if M67 == "Adquirido": val=2
    if M67 == "En proceso": val=1
    if M67 == "No adquirido": val=0
    sAuxF = "(assert  (M67 "+ str(val) +"))"
    clp.eval(sAuxF)

    M68  =  Eval.M68
    if M68 == "Adquirido": val=2
    if M68 == "En proceso": val=1
    if M68 == "No adquirido": val=0
    sAuxF = "(assert  (M68 "+ str(val) +"))"
    clp.eval(sAuxF)

    M69  =  Eval.M69
    if M69 == "Adquirido": val=2
    if M69 == "En proceso": val=1
    if M69 == "No adquirido": val=0
    sAuxF = "(assert  (M69 "+ str(val) +"))"
    clp.eval(sAuxF)

    M70  =  Eval.M70
    if M70 == "Adquirido": val=2
    if M70 == "En proceso": val=1
    if M70 == "No adquirido": val=0
    sAuxF = "(assert  (M70 "+ str(val) +"))"
    clp.eval(sAuxF)

    M71  =  Eval.M71
    if M71 == "Adquirido": val=2
    if M71 == "En proceso": val=1
    if M71 == "No adquirido": val=0
    sAuxF = "(assert  (M71 "+ str(val) +"))"
    clp.eval(sAuxF)

    M72  =  Eval.M72
    if M72 == "Adquirido": val=2
    if M72 == "En proceso": val=1
    if M72 == "No adquirido": val=0
    sAuxF = "(assert  (M72 "+ str(val) +"))"
    clp.eval(sAuxF)

    M73  =  Eval.M73
    if M73 == "Adquirido": val=2
    if M73 == "En proceso": val=1
    if M73 == "No adquirido": val=0
    sAuxF = "(assert  (M73 "+ str(val) +"))"
    clp.eval(sAuxF)
    print("Run")
    clp.run()
    #print("Runeado")
    #------ Recommendation Peluche ---------------------------------------
    evaluar1 = "(find-all-facts ((?x recommendationPeluche )) TRUE)"
    value1  =  clp.eval(evaluar1)
    if(len(value1)>0):
        valF=dict(value1[0])
        Fs = valF.get("Frecuencia_Semanal")
        So = valF.get("Sombrero")
        Br = valF.get("Broches")
        Ci = valF.get("Cierre")
        Ma = valF.get("Velcro")
        Za = valF.get("Cordones")
        Se = valF.get("Semanas")
        print (nom+" Frecuencia Semanal Peluche: "+ str(Fs)+" Sombrero: "+str(So)+" Broches: "+ str(Br)+" Cierre: "+str(Ci)+" Velcro: "+ str(Ma)+" Cordones: "+str(Za)+" Semanas: "+ str(Se) )
        #Metodo editar  base de datos Peluche

        try:
            reco = RecoPeluche.objects.get(Estudiante=idEvalEst)
            #print("Encontrado")
            #print(reco.id)
            reco.FrecuenciaS=   Fs
            reco.Sombrero   =   So
            reco.Broches    =   Br
            reco.Cierre     =   Ci
            reco.Velcro     =   Ma
            reco.Cordon     =   Za
            reco.Semanas    =   Se
            reco.save()
            #print("Actualizado")

        except RecoPeluche.DoesNotExist:
            #print("No encontrado")
            p = RecoPeluche(
                Estudiante  =   Est,
                FrecuenciaS =   Fs,
                Sombrero    =   So,
                Broches     =   Br,
                Cierre      =   Ci,
                Velcro      =   Ma,
                Cordon      =   Za,
                Semanas     =   Se)
            p.save()

            pass
        except RecoPeluche.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass

    #------ Recommendation Juegos Serios ---------------------------------
    evaluarJS = "(find-all-facts ((?x recommendationJuegoS )) TRUE)"
    valueJS =  clp.eval(evaluarJS)
    if(len(valueJS)>0):
        valJ=dict(valueJS[0])
        Fs = valJ.get("Frecuencia_Semanal")
        To = valJ.get("Topos")
        La = valJ.get("Laberinto")
        Ro = valJ.get("RompeC")
        Co = valJ.get("Colorear")
        Le = valJ.get("Letras")
        Se = valJ.get("Semanas")
        print (nom+" Frecuencia Semanal Juegos S: "+str(Fs)+" Topos: "+ str(To)+" Laberinto: "+str(La)+" RompeC: "+ str(Ro)+" Colorear: "+str(Co)+" Letras: "+ str(Le)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Juego Serios
        try:
            reco = RecoJuegosS.objects.get(Estudiante=idEvalEst)
            #print("Encontrado")
            #print(reco.id)
            reco.FrecuenciaS=   Fs
            reco.Topos      =   To
            reco.Laberinto  =   La
            reco.RompeC     =   Ro
            reco.Colorear   =   Co
            reco.Letras     =   Le
            reco.Semanas    =   Se
            reco.save()

        except RecoJuegosS.DoesNotExist:
            #print("No encontrado")
            p = RecoJuegosS(
                Estudiante  =   Est,
                FrecuenciaS =   Fs,
                Topos       =   To,
                Laberinto   =   La,
                RompeC      =   Ro,
                Colorear    =   Co,
                Letras      =   Le,
                Semanas     =   Se)
            p.save()

            pass
        except RecoJuegosS.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass

        
    #------ Recommendation Varita ---------------------------------
    evaluarTA = "(find-all-facts ((?x recommendationTablero )) TRUE)"
    valueTA =  clp.eval(evaluarTA)
    if(len(valueTA)>0):
        valT=dict(valueTA[0])
        Fs = valT.get("Frecuencia_Semanal")
        Tr = valT.get("Trazos")
        Pi = valT.get("Pinzas")
        Pr = valT.get("Precision")
        Se = valT.get("Semanas")
        print (nom+" Frecuencia Semanal Tablero: "+str(Fs)+" Trazos: "+ str(Tr)+" Pinzas: "+str(Pi)+" Precision: "+ str(Pr)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Tablero
        try:
            reco = RecoTablero.objects.get(Estudiante=idEvalEst)
            #print("Encontrado")
            #print(reco.id)
            reco.FrecuenciaS=   Fs
            reco.Trazos     =   Tr
            reco.Pinzas     =   Pi
            reco.Precision  =   Pr
            reco.Semanas    =   Se
            reco.save()

        except RecoTablero.DoesNotExist:
            #print("No encontrado")
            p = RecoTablero(
                Estudiante  =   Est,
                FrecuenciaS =   Fs,
                Trazos      =   Tr,
                Pinzas      =   Pi,
                Precision   =   Pr,
                Semanas     =   Se)
            p.save()

            pass
        except RecoTablero.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass


    #------ Recommendation Varita ---------------------------------
    evaluarVA = "(find-all-facts ((?x recommendationVarita )) TRUE)"
    valueVA =  clp.eval(evaluarVA)
    if(len(valueVA)>0):
        valV=dict(valueVA[0])
        Fs = valV.get("Frecuencia_Semanal")
        Ho = valV.get("horizontal")
        Ve = valV.get("vertical")
        Ob = valV.get("oblicuas")
        Se = valV.get("Semanas")
        print (nom+" Frecuencia Semanal Varita: "+str(Fs)+" horizontal: "+ str(Ho)+" vertical: "+str(Ve)+" oblicuas: "+ str(Ob)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Tablero
        try:
            reco = RecoVarita.objects.get(Estudiante=idEvalEst)
            #print("Encontrado")
            #print(reco.id)
            reco.FrecuenciaS=   Fs
            reco.Horizontal =   Ho
            reco.Vertical   =   Ve
            reco.Oblicuas   =   Ob
            reco.Semanas    =   Se
            reco.save()

        except RecoVarita.DoesNotExist:
            #print("No encontrado")
            p = RecoVarita(
                Estudiante  =   Est,
                FrecuenciaS =   Fs,
                Horizontal  =   Ho,
                Vertical    =   Ve,
                Oblicuas    =   Ob,
                Semanas     =   Se)
            p.save()

            pass
        except RecoVarita.MultipleObjectsReturned:
            print("Se encontraron varias recomendaciones para el usuario.")
            pass


    clp.reset()
    print("Recomendado")
    Eval.save()
    



