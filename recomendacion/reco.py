
''''
def recomendacionEst(Est, Eval):
    clp = Environment()
    clp.load('SE.clp')

    idEvalEst
    nom=Est.nombre
    puntuacion=Est.
    PMF=estList.get('puntuacionMF')
    PMP=estList.get('puntuacionMP')
    edadEst=estList.get('edad_eval_mes')

    clp.eval("(assert  (Edad "+str(edadEst)+"))")
    #print("(assert  (Edad "+str(edadEst)+"))")

    clp.eval("(assert  (PMF "+str(PMF)+"))")
    #print("(assert  (PMF "+str(PMF)+"))")

    clp.eval("(assert  (PMP "+str(PMP)+"))")
    #print("(assert  (PMP "+str(PMP)+"))")

    contF=52
    for i in range(11):
        M = valList.get("M"+str(contF))
        if M == "Adquirido": val=2
        if M == "En proceso": val=1
        if M == "No adquirido": val=0
        sAuxF = "(assert  (M"+str(contF)+" "+ str(val)+"))"
        #print(sAuxF)
        clp.eval(sAuxF)
        contF=contF+1

    contP=66
    for i in range(12):
        M = valList.get("M"+str(contP))
        if M == "Adquirido": valP=2
        if M == "En proceso": valP=1
        if M == "No adquirido": valP=0
        sAuxP ="(assert  (M"+str(contP)+" "+ str(valP)+"))"
        #print(sAuxP)
        clp.eval(sAuxP)
        contP=contP+1

    clp.run()

    #------ Recommendation Peluche ---------------------------------------
    evaluar1 = "(find-all-facts ((?x recommendationPeluche )) TRUE)"
    value1 =  clp.eval(evaluar1)
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
        #print (nom+" Frecuencia Semanal Juegos S: "+str(Fs)+" Topos: "+ str(To)+" Laberinto: "+str(La)+" RompeC: "+ str(Ro)+" Colorear: "+str(Co)+" Letras: "+ str(Le)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Juego Serios
        
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
        #print (nom+" Frecuencia Semanal Tablero: "+str(Fs)+" Trazos: "+ str(Tr)+" Pinzas: "+str(Pi)+" Precision: "+ str(Pr)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Tablero
        

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
        #print (nom+" Frecuencia Semanal Varita: "+str(Fs)+" horizontal: "+ str(Ho)+" vertical: "+str(Ve)+" oblicuas: "+ str(Ob)+" Semanas: "+ str(Se) )
        #Metodo editar base de datos Tablero
    

    clp.reset()
    '''''
    
