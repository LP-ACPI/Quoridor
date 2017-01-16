import math
'''
Quelques definitions vois-a-vis de ce projet:
- Voisins :   pour chacune des cases du plateau du jeu, liste des cases accessibles depuis cette case (liste de listes)
- Bordure :   liste des cases accessibles d'une case (nimporte laquelle -> utilise pour calculer les distances
- Distances : pour chacune des cases (liste), distance a parcourrir (nombre de cases) pour atteindre cette case depuis la case d'origine
- Mur :       A cheval sur 4 cases - hautGauche|hautDroit|basGauche|basDroit - soit horizontal, soit vertical -> modifie les voisins de facon a rendre le passage entre certaines cases inaccessible  
'''
def calculerTableauDesDistances(voisins,origine):
    distances = [-1]*len(voisins)
    distances[origine] = 0
    bordure = [origine]
    while(len(bordure)!=0):
        bordure = calculerLaDistanceDesCasesVoisinesDeLaBordureEtRetournerLaNouvelleBordure(bordure,voisins,distances)
    return distances

def calculerLaDistanceDesCasesVoisinesDeLaBordureEtRetournerLaNouvelleBordure(bordure,voisins,distances):
    nouvelleBordure = []
    for case in bordure:
        nouvelleBordure += marquerLaDistanceDesVoisinsDeLaCaseDonneeEtRetournerLesnouvellesCasesAtteintesDepuisCetteCase(case,voisins,distances)
    return nouvelleBordure

def marquerLaDistanceDesVoisinsDeLaCaseDonneeEtRetournerLesnouvellesCasesAtteintesDepuisCetteCase(case,voisins,distances):
    indiceDistance = distances[case]
    casesAtteintes = []
    for caseAccessible in voisins[case]:
        if(distances[caseAccessible] == -1):
            distances[caseAccessible] = indiceDistance+1
            casesAtteintes.append(caseAccessible)
    return casesAtteintes

def poserMurHorizontal(caseHautGauche,voisins):
    taillePlateau = len(voisins)
    longueurLigne = longueurLigneDuPlateauSiCarre(taillePlateau)
    if(longueurLigne == 0):
        return
    binomesCasesMur = calculDesBinomesDuMurAPoserAPartirDeLaCaseHautGauche(caseHautGauche,taillePlateau,longueurLigne)
    caseHautGauche  = binomesCasesMur[0][0]
    caseBasGauche   = binomesCasesMur[1][0]
    caseHautDroit   = binomesCasesMur[0][1]
    caseBasDroit    = binomesCasesMur[1][1]
    poserMur([[caseHautGauche,caseBasGauche],[caseHautDroit,caseBasDroit]],voisins)

def poserMurVertical(caseHautGauche,voisins):
    taillePlateau = len(voisins)
    longueurLigne = longueurLigneDuPlateauSiCarre(taillePlateau)
    if(longueurLigne == 0):
        return
    binomesCasesMur = calculDesBinomesDuMurAPoserAPartirDeLaCaseHautGauche(caseHautGauche,taillePlateau,longueurLigne)
    caseHautGauche  = binomesCasesMur[0][0]
    caseHautDroit   = binomesCasesMur[0][1]
    caseBasGauche   = binomesCasesMur[1][0]
    caseBasDroit    = binomesCasesMur[1][1]
    poserMur([[caseHautGauche,caseHautDroit],[caseBasGauche,caseBasDroit]],voisins)


def calculDesBinomesDuMurAPoserAPartirDeLaCaseHautGauche(caseHautGauche,taillePlateau,longueurLigne):
    if(caseHautGauche >= taillePlateau):
        return [[-1,-1],[-1,-1]]

    caseHautDroit = caseHautGauche +1 
    caseBasGauche = caseHautGauche +longueurLigne
    caseBasDroit  = caseHautGauche +longueurLigne+1

    if(caseHautDroit%longueurLigne == 0):
        print 'Le mur depasse la ligne du plateau : ajustement...'
        caseHautGauche -= 1
        caseHautDroit  -= 1
        caseBasGauche  -= 1
        caseBasDroit   -= 1

    if(caseHautGauche+longueurLigne >= taillePlateau):
        print 'Le mur depasse bord bas du plateau : ajustement...'
        caseHautGauche -= longueurLigne
        caseHautDroit  -= longueurLigne
        caseBasGauche  -= longueurLigne
        caseBasDroit   -= longueurLigne

    return [[caseHautGauche,caseHautDroit],[caseBasGauche,caseBasDroit]]


def poserMur(binomesCasesAutourDuMur,voisins):
    poseOk = True
    for binome in binomesCasesAutourDuMur:
        poseOk &= binome[0] in voisins[binome[0]] or binome[1] in voisins[binome[0]]
        poseOk &= binome[0] in voisins[binome[1]] or binome[1] in voisins[binome[1]]

    if(poseOk):
        for binome in binomesCasesAutourDuMur:
            voisins[binome[1]].remove(binome[0])
            voisins[binome[0]].remove(binome[1])
    if not poseOk:
        print 'Pose du mur impossible'

def dessinerPlateau(voisins,positionJ1,positionJ2 = -1,positionJ3 = -1,positionJ4 = -1):
    dessinPlateau = '\n '
    taillePlateau = len(voisins)
    longueurLigne = longueurLigneDuPlateauSiCarre(taillePlateau)
    if(longueurLigne == 0):
        return ''

    numeroLigne = 0
    bordHorizontalPlateau = '  '
    for i in range (longueurLigne):
        dessinPlateau += '   ' + str(i)
    for i in range (longueurLigne):
        bordHorizontalPlateau += '+ M '
    dessinPlateau += '\n' + bordHorizontalPlateau + '+\n'+ str(numeroLigne) + ' M'

    for position,case in enumerate(voisins):
        dessinCase = '   '
        if(position == positionJ1):
            dessinCase = ' 1 '
        if(position == positionJ2):
            dessinCase = ' 2 '        
        if(position == positionJ3):
            dessinCase = ' 3 '
        if(position == positionJ4):
            dessinCase = ' 4 '

        dessinPlateau += dessinCase + dessinnerMurOuPassageLateral(position,case)
        dessinPlateau += dessinnerInterLigne(position,voisins,longueurLigne,taillePlateau)

    dessinPlateau += '\n' + bordHorizontalPlateau +'+\n'
    return dessinPlateau

def dessinnerInterLigne(position,voisins,longueurLigne, taillePlateau):
    dessinInterLigne = ''
    if( position%longueurLigne == longueurLigne-1 and position+longueurLigne < taillePlateau):
        numeroLigne = position//longueurLigne+1
        dessinInterLigne += '\n  '
        for i in range (position-longueurLigne+1,position+1):
            dessinInterLigne += '+ ' + dessinnerMurOuPassageVertical(i,voisins[i], longueurLigne) + ' '
        dessinInterLigne += '+\n' + str(numeroLigne) + ' M'
    return dessinInterLigne 

def dessinnerMurOuPassageLateral(position, case):
    if(position+1 in case):
        return '|'
    else : return 'M'

def dessinnerMurOuPassageVertical(position,case,lenLigne):
    if(position+lenLigne in case):
        return '-'
    else : return 'M'

def lePlusCourtChemin(positionActuelle,voisins,casesArrivee,distances):
    chemin = []
    positionChemin = indiceDistanceMinimaleVersDestination(distances,casesArrivee)
    if(positionChemin != -1):
        chemin.append(positionChemin)
        while(positionChemin != positionActuelle):
            positionChemin = indiceDistanceMinimaleVersDestination(distances,voisins[positionChemin])
            chemin.append(positionChemin)
    return chemin[::-1]

def indiceDistanceMinimaleVersDestination(distances,casesDestination):
    minDist = 99
    positionADistanceMin = -1
    for case in casesDestination:
        if(minDist > distances[case] and distances[case] != -1):
            positionADistanceMin = case
            minDist = distances[case]
    return positionADistanceMin

def genererNouveauPlateauCarreAvecNombreDeCasesParLigne(nbCasesDuPlateauParLigne):
    taillePlateau = nbCasesDuPlateauParLigne*nbCasesDuPlateauParLigne
    voisins = [[] for k in range(taillePlateau)]

    for i,x in enumerate(voisins):
        casesEnBas = i+nbCasesDuPlateauParLigne
        if(casesEnBas < taillePlateau):
            x.append(casesEnBas)
        caseGauche = i-1
        if(i%nbCasesDuPlateauParLigne != 0):
            x.append(caseGauche)
        caseDroite = i+1
        if(i%nbCasesDuPlateauParLigne != nbCasesDuPlateauParLigne-1):
            x.append(caseDroite)
        caseEnHaut = i-nbCasesDuPlateauParLigne
        if(caseEnHaut >= 0):
            x.append(caseEnHaut)
    return voisins
        
def longueurLigneDuPlateauSiCarre(tailleTableauVoisins):
    tailleLigne = math.sqrt(tailleTableauVoisins)
    if(not tailleLigne.is_integer()):
        print 'Le plateau n\'est pas carre'
        return 0
    else: 
        return int(tailleLigne)

def obtenirCasesDArriveePourJoueur(numeroJoueur,tailleLignePlateau):
    casesArrivee = []
    if(numeroJoueur == 1):
        for i in range (tailleLignePlateau):
            casesArrivee.append(i)
    if(numeroJoueur == 2):
        for i in range (tailleLignePlateau*tailleLignePlateau-tailleLignePlateau,tailleLignePlateau*tailleLignePlateau):
            casesArrivee.append(i)
    if(numeroJoueur == 3):
        for i in range (0,tailleLignePlateau*tailleLignePlateau,tailleLignePlateau):
            casesArrivee.append(i)
    if(numeroJoueur == 4):
        for i in range (tailleLignePlateau-1,tailleLignePlateau*tailleLignePlateau,tailleLignePlateau):
            casesArrivee.append(i)
    return casesArrivee