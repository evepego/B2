from dic import villes

# Vitesse maximale en km/h.
vit_max = 90
# Temps d'une pause
pause = 15
# Temps pour arriver à la vitesse maximale (90 km/h) en minutes.
temps_vit_max = 9
temps = 0

# On demande de saisir une ville de départ et une ville d'arrivée.
vil_dep = input("Choisir une ville de départ : \n (Bordeaux-Bayonne-Lille-Mulhouse-Orthez- \n Pau-Paris-Poitiers-Royan-Toulouse) \n ")
vil_arr = input("Choisir une ville d'arrivée : \n (Bordeaux-Bayonne-Lille-Mulhouse-Orthez- \n Pau-Paris-Poitiers-Royan-Toulouse) \n ")
# Algo pour la saisir 2 villes différentes.
while vil_dep == vil_arr :
    print('Erreur ! Veuillez réessayer.')
    vil_dep = input("Choisir une ville de départ : ")
    vil_arr = input("Choisir une ville d'arrivée : ")

# Tableau d'affichage.
tab = []
distance = villes[vil_dep][vil_arr]

if vil_dep != vil_arr :
    # Déterminer le temps de toutes les pauses.
    if (temps/2)%2 == 0 :
        temps_pause = (temps/2) * pause + temps_vit_max * 2
    # Déterminer le temps du trajet sans pauses.
    temps_sans_pause = distance/vit_max
    # Déterminer le temps total.
    temps_total = temps_pause + temps_sans_pause + temps_vit_max
    # Ligne pour remplir le tableau.
    tab.extend((vil_dep, vil_arr, distance, temps_total))
print(tab)