from quoridor import *

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

positionJoureurA = 2
positionJoureurB = 18
casesArriveeJoueurA = [20,21,22,23,24]
casesArriveeJoueurB = [0,1,2,3,4]

distances = calculerTableauDesDistances(voisins,positionJoureurA)
print dessinerPlateau(voisins,positionJoureurA,positionJoureurB)

poserMurHorizontal(17,voisins)
poserMurHorizontal(5,voisins)
poserMurVertical(16,voisins)
poserMurVertical(11,voisins)
dessinerPlateau(voisins,positionJoureurA,positionJoureurB)

distancesJoueurA = calculerTableauDesDistances(voisins,positionJoureurA)
distancesJoueurB = calculerTableauDesDistances(voisins,positionJoureurB)
print dessinerPlateau(voisins,positionJoureurA,positionJoureurB)

print lePlusCourtChemin(positionJoureurA,voisins,casesArriveeJoueurA,distancesJoueurA)
print lePlusCourtChemin(positionJoureurB,voisins,casesArriveeJoueurB,distancesJoueurB)

newPlateau = genererNouveauPlateauCarreAvecNombreDeCasesParLigne(9)
print dessinerPlateau(newPlateau,4,76)

poserMurVertical(7,newPlateau)
poserMurVertical(76,newPlateau)
print dessinerPlateau(newPlateau,4,76)
