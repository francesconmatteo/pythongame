from upemtk import *
from time import *
from random import *
#from colors import *

largeurFenetre = 800
hauteurFenetre = 700


def settings() :
    botOrNah = 'P1 vs P2'
    coligne = '6'
    coligne2 = '6'
    rectangle(0, 600, 200, 700,couleur='black', remplissage='red', epaisseur=2, tag='quit')
    rectangle(201, 600, 400, 700,couleur='black', remplissage='blue', epaisseur=2, tag='rename')
    rectangle(401, 600, 600, 700,couleur='black', remplissage='purple', epaisseur=2, tag='color')
    rectangle(601, 600, 800, 700,couleur='black', remplissage='green', epaisseur=2, tag='ok')
    rectangle(0, 0, 800, 600,couleur='black', remplissage='black', epaisseur=1, tag='')

    color1 = 'white'
    color2 = 'white'
    texte(700,650,chaine = 'OK',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 30 ,tag='ok')
    texte(400,50,chaine = 'Taille du plateau :',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 60,tag='colignetxt')
    texte(400,350,chaine = 'Mode :',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 60,tag='coligneint')
    texte(100,650,chaine = 'Quitter',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 30 ,tag='quit')
    texte(300,650,chaine = 'Renommer',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 30 ,tag='rename')
    texte(500,650,chaine = 'Couleur',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 30 ,tag='color')

    tag1 = 'Joueur1'
    tag2 = 'Joueur2'
    colorB = 'grey'
    colorP = 'RoyalBlue3'
    colorL = 'black'

    while 1 :
        coligne = str(coligne)
        coligne2 = str(coligne2)
        texte(700,200,chaine = '>',couleur = color1,ancrage = 'center',police = 'Purisa',taille = 70 ,tag='fleche2')
        texte(100,200,chaine = '<',couleur = color2,ancrage = 'center',police = 'Purisa',taille = 70,tag='fleche1')
        texte(400,200,chaine = coligne+'X'+coligne2,couleur = 'white',ancrage ='center',police = 'Purisa',taille = 70 ,tag='x')
        texte(700,500,chaine = '>',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 70 ,tag='fleche3')
        texte(100,500,chaine = '<',couleur = 'white',ancrage = 'center',police = 'Purisa',taille = 70,tag='fleche4')
        texte(400,500,chaine = botOrNah,couleur = 'white',ancrage ='center',police = 'Purisa',taille = 70 ,tag='bot')

        ligne(0, 300, 800, 300, couleur='white', epaisseur = 3, tag='')
        xClique,yClique,typeClique = attente_clic()
        coligne = int(coligne)
        coligne2 = int(coligne2)
        if xClique > 0 and xClique < 400 and yClique > 0 and yClique < 300 :        #coligne gauche
            if coligne > 4 :
                coligne -= 1
                coligne2 -= 1
                color1 = 'white'

        if xClique > 400 and xClique < 800 and yClique > 0 and yClique < 300 :      #coligne droite
            if coligne < 10 :
                coligne += 1
                coligne2 += 1
                color2 = 'white'


        if xClique > 0 and xClique < 400 and yClique > 301 and yClique < 600 :      #bot gauche
            if botOrNah == 'P1 vs IA' :
                botOrNah = 'P1 vs P2'
            else :
                botOrNah = 'P1 vs IA'
        if xClique > 400 and xClique < 800 and yClique > 301 and yClique < 600 :    #bot droite
            if botOrNah == 'P1 vs IA' :
                botOrNah = 'P1 vs P2'
            else :
                botOrNah = 'P1 vs IA'

        if xClique > 0 and xClique < 200 and yClique > 601 and yClique < 700 :
            ferme_fenetre()

        if xClique > 201 and xClique < 400 and yClique > 601 and yClique < 700 :
            tag1 = input('Entrer le nom du joueur 1 (8 caracteres max)')
            tag2 = input('Entrer le nom du joueur 2 (8 caracteres max)')

        if xClique > 401 and xClique < 600 and yClique > 601 and yClique < 700 :
            print("Eviter d'utiliser plusieurs fois la meme couleur et ne pas utiliser 'black' pour la couleur de fond")
            print('Choisir parmis : white black blue red green orange yellow gold gray pink purple maroon brown cyan grey  lightblue lightgreen LightSteelBlue LightSteelBlue2 dodgerblue powderblue cadetblue skyblue deepskyblue')
            colorB = input('Choisir la couleur du fond: ')
            colorP = input('Choisir la couleur du plateau: ')
            colorL = input('Choisir la couleur des lignes: ')

        if xClique > 601 and xClique < 800 and yClique > 601 and yClique < 700 :
            efface_tout()
            return(coligne,botOrNah,tag1,tag2,colorB,colorP,colorL)

        efface('bot')
        efface('x')

def background() :
    rectangle(0, 0, 800, 700,couleur = colorB,remplissage = colorB, tag='fond')
    rectangle(25, 25, 625, 625,couleur = colorP,remplissage = colorP, tag='fondPlateau')
    rectangle(750, 650, 800, 700,couleur='black', remplissage='red', epaisseur=1, tag='')
    cercle(775, 675, 10, couleur='black', remplissage='red', epaisseur=4, tag='')
    rectangle(771, 660, 779, 670,couleur='red', remplissage='red', epaisseur=1, tag='')
    rectangle(773, 660, 777, 670,couleur='black', remplissage='black', epaisseur=1, tag='')

def lignes(x) :
    i = 0
    t = rapport
    while i < x+1 :
        ligne(t*i+25,25,t*i+25,625,couleur = colorL,epaisseur = 3)
        ligne(25,t*i+25,625,t*i+25,couleur = colorL,epaisseur = 3)
        i += 1

def detectionClic() :
    xClique,yClique,typeClique = attente_clic()
    if xClique > 25 and xClique < 625 and yClique > 25 and yClique < 625 :
        return(xClique,yClique,typeClique)
    elif xClique > 750 and xClique < 800 and yClique > 650 and yClique < 700 :
            ferme_fenetre()
    else :
        while xClique < 25 or xClique > 625 or yClique < 25 or yClique > 625 :
            print ("Cliquez a l'interieur du plateau")
            xClique,yClique,typeClique = attente_clic()
        return(xClique,yClique,typeClique)

def case(xClique,yClique) :
    xClique = xClique - 25
    yClique = yClique - 25
    x = xClique / rapport
    x = int(x)
    x = x +1
    y = yClique / rapport
    y = int(y)
    y = y +1
    #print('x =',x,'y =',y)
    return(x,y)

def sortirCase() :

    xClique,yClique,typeClique = detectionClic()
    x,y = case(xClique,yClique)
    x = str(x)
    y = str(y)
    if dico[x+y]==1 :
        return (x,y)
    else :
        while dico[x+y]!=1 :
            xClique,yClique,typeClique = detectionClic()
            x,y = case(xClique,yClique)
            x = str(x)
            y = str(y)
    return (x,y)

def limite(joueur,x,y,ox1,oy1,ox2,oy2) :
    x = int(x)
    y = int(y)
    ox1 = int(ox1)
    oy1 = int(oy1)
    ox2 = int(ox2)
    oy2 = int(oy2)

    if joueur % 2 == 0 :
        if x == ox2-1 or x == ox2+1 :
            if y == oy2-1 or y == oy2 or y == oy2 + 1 :
                return(True)
        elif x == ox2 :
            if y == oy2-1 or y == oy2 + 1 :
                return(True)

    elif joueur % 2 != 0 :
        if x == ox1-1 or x == ox1+1 :
            if y == oy1-1 or y == oy1 or y == oy1 + 1 :
                return(True)
        elif x == ox1 :
            if y == oy1-1 or y == oy1 + 1 :
                return(True)


def placerPion(x,y,rayon,color,tag) :

    efface(tag)
    dico[x+y] = 0
    x = int(x)
    y = int(y)
    x = x-1
    y = y-1
    xCercle = x*rapport + rapport/2 +25
    yCercle = y*rapport + rapport/2 +25
    cercle(xCercle, yCercle, rayon, couleur=color, remplissage=color, epaisseur=1, tag=tag)

def detruireCase(x,y) :

    dico[x+y] = 0
    #print('detruire',x+y,dico[x+y])
    x = int(x)
    y = int(y)
    ax = 25 + (x-1)*rapport
    ay = 25 + (y-1)*rapport
    bx = 25 + x*rapport
    by = 25 + y*rapport
    rectangle(ax, ay, bx, by,couleur='black', remplissage='black', epaisseur=1, tag='')

def verification(joueur,ox1,oy1,ox2,oy2,xPion,yPion,tag,sommeP1,sommeP2) :

    xPion = int(xPion)
    yPion = int(yPion)
    ox1 = int(ox1)
    oy1 = int(oy1)
    ox2 = int(ox2)
    oy2 = int(oy2)
    xP = xPion+1
    xM = xPion-1
    yP = yPion+1
    yM = yPion-1
    xPion = str(xPion)
    yPion = str(yPion)
    xP = str(xP)
    xM = str(xM)
    yP = str(yP)
    yM = str(yM)

    if dico[xM+yP] == 0 and dico[xPion+yP] == 0 and dico[xP+yP] == 0 and dico[xM+yPion] == 0 and dico[xP+yPion] == 0 and dico[xM+yM] == 0 and dico[xPion+yM] == 0 and dico[xP+yM] == 0:

        if tag == tag1 :
            print('Joueur2 gagne')
            vainqueur = tag2+' gagne'
        else :
            print('Joueur1 gagne')
            vainqueur = tag1+' gagne'

        print('Temps de reflexion total P1 :',sommeP1,'sec\n'+'Temps de reflexion total P2 :',sommeP2,'sec')
        suivant = rejouer(vainqueur)

        if suivant == 'yes' :
            return('yes')
        else :
            return('no')

    if joueur % 2 == 0 :
        xPion = int(xPion)
        yPion = int(yPion)
        xP = ox1+1
        xM = ox1-1
        yP = oy1+1
        yM = oy1-1
        xPion = str(xPion)
        yPion = str(yPion)
        xP = str(xP)
        xM = str(xM)
        yP = str(yP)
        yM = str(yM)
        ox1 = str(ox1)
        oy1 = str(oy1)
        x = ox1
        y = oy1
    else :
        xPion = int(xPion)
        yPion = int(yPion)
        xP = ox2+1
        xM = ox2-1
        yP = oy2+1
        yM = oy2-1
        xPion = str(xPion)
        yPion = str(yPion)
        xP = str(xP)
        xM = str(xM)
        yP = str(yP)
        yM = str(yM)
        ox2 = str(ox2)
        oy2 = str(oy2)
        x = ox2
        y = oy2

    if dico[xM+yP] == 0 and dico[x+yP] == 0 and dico[xP+yP] == 0 and dico[xM+y] == 0 and dico[xP+y] == 0 and dico[xM+yM] == 0 and dico[x+yM] == 0 and dico[xP+yM] == 0:
        if tag == tag1 :
            vainqueur = tag1+' gagne'
            print('Temps de reflexion total P1 :',sommeP1,'sec\n'+'Temps de reflexion total P2 :',sommeP2,'sec')
            suivant = rejouer(vainqueur)
            if suivant == 'yes' :
                return('yes')
            else :
                return('no')
        else :
           vainqueur = tag2+' gagne'
           print('Temps de reflexion total P1 :',sommeP1,'sec\n'+'Temps de reflexion total P2 :',sommeP2,'sec')
           suivant = rejouer(vainqueur)
           if suivant == 'yes' :
                return('yes')
           else :
                return('no')

def verification2(ox1,oy1,ox2,oy2,xPion,yPion,joueur,tag,sommeP1,sommeP2) :
    xPion = int(xPion)
    yPion = int(yPion)
    ox1 = int(ox1)
    oy1 = int(oy1)
    ox2 = int(ox2)
    oy2 = int(oy2)
    xP = xPion+1
    xM = xPion-1
    yP = yPion+1
    yM = yPion-1
    xPion = str(xPion)
    yPion = str(yPion)
    xP = str(xP)
    xM = str(xM)
    yP = str(yP)
    yM = str(yM)

    if dico[xM+yP] == 0 and dico[xPion+yP] == 0 and dico[xP+yP] == 0 and dico[xM+yPion] == 0 and dico[xP+yPion] == 0 and dico[xM+yM] == 0 and dico[xPion+yM] == 0 and dico[xP+yM] == 0:
        if tag == tag1 :
            vainqueur = 'IA gagne'
        else :
            vainqueur = tag+' gagne'


        suivant = rejouer(vainqueur)

        if suivant == 'yes' :
            return('yes')
        else :
            return('no')

    if joueur % 2 == 0 :
            xP = ox1+1
            xM = ox1-1
            yP = oy1+1
            yM = oy1-1
            xP = str(xP)
            xM = str(xM)
            yP = str(yP)
            yM = str(yM)
            ox1 = str(ox1)
            oy1 = str(oy1)
            x = ox1
            y = oy1

    else :
            xP = ox2+1
            xM = ox2-1
            yP = oy2+1
            yM = oy2-1
            xP = str(xP)
            xM = str(xM)
            yP = str(yP)
            yM = str(yM)
            ox2 = str(ox2)
            oy2 = str(oy2)
            x = ox2
            y = oy2


    if dico[xM+yP] == 0 and dico[x+yP] == 0 and dico[xP+yP] == 0 and dico[xM+y] == 0 and dico[xP+y] == 0 and dico[xM+yM] == 0 and dico[x+yM] == 0 and dico[xP+yM] == 0:
        if tag == tag1 :
            vainqueur = tag1+' gagne'
            suivant = rejouer(vainqueur)
            if suivant == 'yes' :
                return('yes')
            else :
                return('no')
        else :
            vainqueur = 'IA  gagne'
            suivant = rejouer(vainqueur)
            if suivant == 'yes' :
                return('yes')
            else :
                return('no')


def jeuP1P2(rayon,tag1,tag2) :
    sommeP2 = 0
    sommeP1 = 0
    tours = 1
    joueur = 1

    color1 = 'black'
    color2 = 'white'
    ox1 = 0
    ox2 = 0
    oy1 = 0
    oy2 = 0

    while 1 :
        #on analyse c'est à quel joueur de jouer
        if joueur % 2 == 0 :
            tours += 1
        tours = str(tours)
        texte(665, 220, chaine = 'Tours '+tours, police = 'Purisa', taille = 24, tag='action')
        tours = int(tours)
        suivant = 'yes'
        a = time()
        uneCase = 'rien'
        if joueur % 2 == 0 :
            color = color2
            tag = tag2
        else :
            color = color1
            tag = tag1



        efface('player')
        texte(665, 25, chaine = tag, couleur='black', police="Purisa", taille = 24, tag='player')
        efface('action')
        texte(665, 120, chaine = 'Placer \n  pion', police = 'Purisa', taille = 24, tag='action')

        if joueur > 2 :
            while uneCase != True :
                xPion,yPion = sortirCase()
                uneCase = limite(joueur,xPion,yPion,ox1,oy1,ox2,oy2)
                if uneCase != True :
                    print('Choisissez une autre case')
        else :
            xPion,yPion = sortirCase()

        placerPion(xPion,yPion,rayon,color,tag)
        if joueur >= 3 :
            ox1 = str(ox1)
            oy1 = str(oy1)
            ox2 = str(ox2)
            oy2 = str(oy2)
            if joueur % 2 == 0 :
                dico[ox2+oy2] = 1
            else :
                dico[ox1+oy1] = 1


        efface('action')
        texte(665,120,chaine = 'Detruire \n  case',police = 'Purisa',taille = 24,tag='action')

        if joueur > 2 :
            x,y = sortirCase()
            detruireCase(x,y)

        b = time()

        if joueur % 2 == 0 :
            sommeP2 = sommeP2 + (b-a)
        else :
            sommeP1 = sommeP1 + (b-a)

        if joueur >2:
            suivant = verification(joueur,ox1,oy1,ox2,oy2,xPion,yPion,tag,sommeP1,sommeP2)
            if suivant == 'yes' :
                return('yes')
            elif suivant == 'no' :
                return('no')

        #print(xPion,yPion,ox1,oy1,ox2,oy2)

        if joueur % 2 == 0 :
            ox2 = xPion
            oy2 = yPion
        elif joueur % 2 != 0 :
            ox1 = xPion
            oy1 = yPion

        joueur += 1


def rejouer(vainqueur) :

    i = -800
    while i <= 0 :
        rectangle(i, 300, i+800, 400, couleur = 'black',remplissage = 'black', epaisseur = 1, tag='anim')
        rectangle(-i, 200, (-i)+800, 299, couleur = 'green',remplissage = 'green', epaisseur = 1, tag='rejouer')
        rectangle(-i, 401, (-i)+800, 500, couleur = 'red',remplissage = 'red', epaisseur = 1, tag='quit')
        texte(i+400, 350, chaine=vainqueur,couleur='white', ancrage='center', police="Purisa", taille=24, tag='loser')
        texte((-i)+400, 250, chaine='Rejouer',couleur='white', ancrage='center', police="Purisa", taille=24, tag='rejouer')
        texte((-i)+400, 450, chaine='Quitter',couleur='white', ancrage='center', police="Purisa", taille=24, tag='quit')
        i += 3
        sleep(0.000000000000001)
        mise_a_jour()

    xClique,yClique,typeClique = attente_clic()
    if xClique > 0 and xClique < 800 and yClique > 200 and yClique < 300 :
        return('yes')
    elif xClique > 0 and xClique < 800 and yClique > 400 and yClique < 500 :
        return('no')

#Le code du bot qui va sélectionner une case autour de lui
def botPlacer(coligne,joueur,ox2,oy2) :
    if joueur <= 2 :
        x = '0'
        y = '0'
        while dico[x+y] != 1 :
            x = randint(0,coligne-1)
            y = randint(0,coligne-1)
            x = str(x)
            y = str(y)
        return(x,y)
    else :
        b = '0'
        d = '0'
        while dico[b+d] != 1:
            ox2 = int(ox2)
            oy2 = int(oy2)
            xM = ox2-1
            x = ox2
            xP = ox2+1
            yM = oy2-1
            y = oy2
            yP = oy2 +1

            a = randint(0,7)
            lstPos = [xM,xM,xM,x,x,xP,xP,xP]
            b = lstPos[a]
            c = randint(0,7)
            lstPos = [yM,yM,yM,y,y,yP,yP,yP]
            d = lstPos[c]
            b = str(b)
            d = str(d)
        print('bot place',b+d)
        return(b,d)

def botDetruire (ox1,oy1) :
    ox1 = int(ox1)
    oy1 = int(oy1)
    xM = ox1-1
    x = ox1
    xP = ox1+1
    yM = oy1-1
    y = oy1
    yP = oy1 +1
    b = '0'
    d = '0'

    while dico[b+d] != 1 :
        a = randint(0,7)
        lstPos = [xM,xM,xM,x,x,xP,xP,xP]
        b = lstPos[a]
        c = randint(0,7)
        lstPos = [yM,yM,yM,y,y,yP,yP,yP]
        d = lstPos[c]
        b = str(b)
        d = str(d)
    print('bot detruit',b+d)
    return(b,d)

def jeuP1Bot(rayon) :
    joueur = 1
    sommeP1 = 0
    sommeP2 = 0
    tours = 0

    ox1 = 0
    ox2 = 0
    oy1 = 0
    oy2 = 0
    suivant = 'yes'

    while 1 :


        if joueur % 2 == 0 :

            tag='bot'
            color  = 'white'
            a = time

            efface('player')
            texte(665, 25, chaine = tag, couleur='black', police="Purisa", taille = 24, tag='player')
            efface('action')
            texte(665, 120, chaine = 'Placer \n  pion', police = 'Purisa', taille = 24, tag='action')

            xPion,yPion = botPlacer(coligne,joueur,ox2,oy2)
            placerPion(xPion,yPion,rayon,color,tag)

            if joueur >= 3 :
                ox2 = str(ox2)
                oy2 = str(oy2)
                dico[ox2+oy2] = 1

            efface('action')
            texte(665,120,chaine = 'Detruire \n  case',police = 'Purisa',taille = 24,tag='action')

            if joueur != 2 :
                xCase,yCase = botDetruire(ox1,oy1)
                detruireCase(xCase,yCase)
                if joueur >2:
                    suivant = verification2(ox1,oy1,ox2,oy2,xPion,yPion,joueur,tag,sommeP1,sommeP2)
                    if suivant == 'yes' :
                        return('yes')
                    elif suivant == 'no' :
                        return('no')

            b = time
            #sommeP2 = sommeP2 + (b-a)



            ox2 = xPion
            oy2 = yPion

        else :

            tag = tag1
            color ='black'
            uneCase = 'rien'
            a = time

            efface('player')
            texte(665, 25, chaine = tag, couleur='black', police="Purisa", taille = 24, tag='player')
            efface('action')
            texte(665, 120, chaine = 'Placer \n  pion', police = 'Purisa', taille = 24, tag='action')

            if joueur > 2 :
                while uneCase != True :
                    xPion,yPion = sortirCase()
                    uneCase = limite(joueur,xPion,yPion,ox1,oy1,ox2,oy2)
                    if uneCase != True :
                        print('Choisissez une autre case')
            else :
                xPion,yPion = sortirCase()
            placerPion(xPion,yPion,rayon,color,tag)

            if joueur >= 3 :
                ox1 = str(ox1)
                oy1 = str(oy1)

            dico[ox1+oy1] = 1

            efface('action')
            texte(665,120,chaine = 'Detruire \n  case',police = 'Purisa',taille = 24,tag='action')

            if joueur != 1 :
                x,y = sortirCase()
                detruireCase(x,y)
                if joueur >2:
                    suivant = verification2(ox1,oy1,ox2,oy2,xPion,yPion,joueur,tag,sommeP1,sommeP2)
                    if suivant == 'yes' :
                        return('yes')
                    elif suivant == 'no' :
                        return('no')

            b = time()
            #sommeP1 = sommeP1 + (b-a)



            ox1 = xPion
            oy1 = yPion

        joueur += 1

###########################################################################################################################


cree_fenetre(largeurFenetre,hauteurFenetre)

suivant = 'yes'
nb = 1

while 1 :
    if suivant == 'no' or nb == 1 :
        coligne,botOrNah,tag1,tag2,colorB,colorP,colorL = settings()

    rapport = 600 / coligne
    rayon = rapport / 2 -5

    a = 0
    b = 0
    d = str(coligne +1)
    dico = {}
    while a < coligne+2 :
        a = str(a)
        b = str(b)
        if a == '0' or b == '0' or a == d  or b == d  :
            c = 0
        else :
            c = 1
        dico[a+b] = c
        #print(a+b,':',dico[a+b])
        a = int(a)
        b = int(b)
        b += 1
        if b > coligne+1 :
            a += 1
            b = 0

    #print(coligne,botOrNah)

    background()

    lignes(coligne)

    if botOrNah == 'P1 vs P2' :
        suivant = jeuP1P2(rayon,tag1,tag2)
    else :
        suivant = jeuP1Bot(rayon)
    nb += 1

ferme_fenetre()


