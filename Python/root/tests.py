from quoridor import *

nbTotalTests = 13
cptTests = 0
cptTestsPasses = 0

def testEgalite(valAttendue,valTest):
    global nbTotalTests,cptTestsPasses,cptTests
    if(valAttendue == valTest):
        print "test OK"
        cptTestsPasses += 1
    else:
        print "test FAIL!:"
        print "     valeur attendue: ", valAttendue
        print "     valeur testee:   ", valTest
    cptTests += 1
    if(cptTests == nbTotalTests):
        resultTest(cptTestsPasses,nbTotalTests)

def resultTest(cptTestsPasses, nbTotalTests):
    print '=================='
    print 'resultat: ', cptTestsPasses, '/',nbTotalTests
    if(cptTestsPasses == nbTotalTests):
        print 'Tous les tests sont bons!'
    else: print 'revoir vos fonctions'

voisins = [ 
    #0            1                2           3          4
    [5],        [2,6],          [1,3,7],    [2,4,8],    [3,9],
    #5            6                7           8          9
    [0,10],     [1,7,11],       [2,6,8],    [3,7,9],    [4,8,14],
    #10            11              12          13          14
    [5,11,15],  [6,10,12,16],   [11,17],    [14,18],    [9,13,19],
    #15            16              17          18          19
    [10,16,20], [11,15,17,21],  [12,16,22], [13,19,23], [14,18,24],
    #20            21              22          23          24
    [15,21],    [16,20,22],     [21,17,23], [22,18,24], [19,23]
]

voisinsAttendusApres3NouveauxMurs = [ 
    #0            1                2           3          4
    [5],        [2,6],          [1,3,7],    [2,4,8],    [3,9],
    #5            6                7           8          9
    [0],        [1,7],          [2,6,8],    [3,7,9],    [4,8,14],
    #10            11              12          13          14
    [11,15],    [10,12,16],     [11,17],    [14,18],    [9,13,19],
    #15            16              17          18          19
    [10,16,20], [11,15,21],     [12],       [13,19],    [14,18,24],
    #20            21              22          23          24
    [15,21],    [16,20],        [23],       [22,24],    [19,23]
]

voisinsAttendusApresRegeneration = [ 
    #0             1            2              3            4
    [1,5],      [0,2,6],     [1,3,7],       [2,4,8],      [3,9],
    #5              6             7             8           9
    [0,6,10],   [1,5,7,11],  [2,6,8,12],    [3,7,9,13],   [4,8,14],
    #10             11            12            13           14
    [5,11,15],  [6,10,12,16],[7,11,13,17],  [8,12,14,18], [9,13,19],
    #15            16              17            18           19
    [10,16,20], [11,15,17,21],[12,16,18,22],[13,17,19,23],[14,18,24],
    #20            21              22          23           24
    [15,21],    [16,20,22],    [17,21,23], [22,24,18],    [19,23]
]

plateauRegenereAttendu = (
    '\n    0   1   2   3   4'
    '\n  + M + M + M + M + M +'
    '\n0 M   |   |   |   |   M'
    '\n  + - + - + - + - + - +'
    '\n1 M   | 2 |   |   |   M'
    '\n  + - + - + - + - + - +'
    '\n2 M   |   |   |   |   M'
    '\n  + - + - + - + - + - +'
    '\n3 M   |   |   | 1 |   M'
    '\n  + - + - + - + - + - +'
    '\n4 M   |   |   |   |   M'
    '\n  + M + M + M + M + M +\n'
)

plateauApresPoseDeMurs = (
    '\n    0   1   2   3   4'
    '\n  + M + M + M + M + M +'
    '\n0 M   M   |   |   |   M'
    '\n  + - + - + - + - + - +'
    '\n1 M   M 2 |   |   |   M'
    '\n  + M + M + M + M + - +'
    '\n2 M   |   |   M   |   M'
    '\n  + - + - + - + - + - +'
    '\n3 M   |   M   M 1 |   M'
    '\n  + - + - + M + M + - +'
    '\n4 M   |   M   |   |   M'
    '\n  + M + M + M + M + M +\n'
)

positionJoureur1 = 18
positionJoureur2 = 6

distancesAttenduesJ1 = [
    8, 7, 6, 5, 4,
    7, 6, 5, 4, 3,
    6, 5, 4, 1, 2,
    5, 4, 3, 0, 1,
    4, 3, 2, 1, 2
]
lePlusCourtCheminAttenduJ1 = [18,13,14,9,4]

distancesAttenduesJ2 = [
    4, 1, 2, 3, 4,
    3, 0, 1, 2, 3,
    2, 1, 2, 5, 4,
    3, 2, 3, 6, 5,
    4, 3, 4, 5, 6
]
lePlusCourtCheminAttenduJ2 = [6,11,16,21]

distancesAttenduesJ2Apres3Murs = [
    -1,  1,  2, 3, 4,
    -1,  0,  1, 2, 3,
    -1, -1, -1, 5, 4,
    -1, -1, -1, 6, 5,
    -1, -1,  6, 5, 6
]
lePlusCourtCheminAttenduJ2Apres3Murs = [6,7,8,9,14,19,24]


distancesInitialesJ1 = calculerTableauDesDistances(voisins,positionJoureur1)
distancesInitialesJ2 = calculerTableauDesDistances(voisins,positionJoureur2)
testEgalite(distancesAttenduesJ1,distancesInitialesJ1)
testEgalite(distancesAttenduesJ2,distancesInitialesJ2)

casesArriveeAttenduesJoueur1 = [0,1,2,3,4]
casesArriveeAttenduesJoueur2 = [20,21,22,23,24]
casesArriveeAttenduesJoueur3 = [0,5,10,15,20]
casesArriveeAttenduesJoueur4 = [4,9,14,19,24]
testEgalite(casesArriveeAttenduesJoueur1,obtenirCasesDArriveePourJoueur(1,5))
testEgalite(casesArriveeAttenduesJoueur2,obtenirCasesDArriveePourJoueur(2,5))
testEgalite(casesArriveeAttenduesJoueur3,obtenirCasesDArriveePourJoueur(3,5))
testEgalite(casesArriveeAttenduesJoueur4,obtenirCasesDArriveePourJoueur(4,5))

lePlusCourtCheminJoueur1 = lePlusCourtChemin(positionJoureur1,voisins,casesArriveeAttenduesJoueur1,distancesInitialesJ1)
lePlusCourtCheminJoueur2 = lePlusCourtChemin(positionJoureur2,voisins,casesArriveeAttenduesJoueur2,distancesInitialesJ2)
testEgalite(lePlusCourtCheminAttenduJ1,lePlusCourtCheminJoueur1)
testEgalite(lePlusCourtCheminAttenduJ2,lePlusCourtCheminJoueur2)

poserMurHorizontal(17,voisins)
poserMurHorizontal(5,voisins)
poserMurVertical(16,voisins)
poserMurVertical(26,voisins)
testEgalite(plateauApresPoseDeMurs,dessinerPlateau(voisins,positionJoureur1,positionJoureur2))
distancesJoueur1ApresNouveauxMurs = calculerTableauDesDistances(voisins,positionJoureur1)
distancesJoueur2ApresNouveauxMurs = calculerTableauDesDistances(voisins,positionJoureur2)

lePlusCourtCheminJoueur1ApresMurs = lePlusCourtChemin(positionJoureur1,voisins,casesArriveeAttenduesJoueur1,distancesJoueur1ApresNouveauxMurs)
lePlusCourtCheminJoueur2ApresMurs = lePlusCourtChemin(positionJoureur2,voisins,casesArriveeAttenduesJoueur2,distancesJoueur2ApresNouveauxMurs)
testEgalite(lePlusCourtCheminAttenduJ1,lePlusCourtCheminJoueur1ApresMurs)
testEgalite(lePlusCourtCheminAttenduJ2Apres3Murs,lePlusCourtCheminJoueur2ApresMurs)

testEgalite(voisinsAttendusApres3NouveauxMurs,voisins)

voisinsRegeneres = genererNouveauPlateauCarreAvecNombreDeCasesParLigne(5)
testEgalite(plateauRegenereAttendu,dessinerPlateau(voisinsRegeneres,positionJoureur1,positionJoureur2))
