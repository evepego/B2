# Vitesse maximale en km/h.
vit_max = 90
# Temps d'une pause
pause = 15
# Vitesse accelération en km/h par minutes.
accelerer = 10
# Vitesse descelération en km/h par minutes.
ralentir = 10
# Temps du parcours en minutes.
temps = 0
# Temps pour arriver à la vitesse maximale (90 km/h) en minutes.
temps_vit_max = 9
# Tableau d'affichage.
tab = []

# On demande de saisir une ville de départ et une ville d'arrivée.
vil_dep = input("Choisir une ville de départ : ")
vil_arr = input("Choisir une ville d'arrivée : ")
# Algo pour la saisir 2 villes différentes.
while vil_dep == vil_arr :
    vil_dep = input("Choisir une ville de départ : ")
    vil_arr = input("Choisir une ville d'arrivée : ")

# Déterminer le temps de toutes les pauses.
if (temps/2)%2 == 0 :
    temps_pause = (temps/2) * pause + temps_vit_max * 2
# Déterminer le temps du trajet sans pauses.
temps_sans_pause = distance/vitesse_max
# Déterminer le temps total.
temps_total = temps_pause + temps_sans_pause + temps

# Ligne pour remplir le tableau.
tab.extend((vil_dep, vil_arr, distance, temps))
print(tab)