from fonction import *

# • VARIABLES •

# 1 - Cash & Points 
player_cash = 0
player_points = 0

# 2 - Valeur Départ Début Jeu 
print_value = 1     # "AROUND THE WORD"

# 3 - Shop 
bonus_first_letter = 0
bonus_last_letter = 0
bonus_double_cash = 0
bonus_double_points = 0
victory = 0
value_shop_menu = 0    # Value Pour Ne Pas Répéter "Choix Menu" Quand On Utilise Le Shop
shop_bonus_letters = 0
player_choice_word = 0

# 4 - Cash & Points
cash_good_answer = 25         # 25 $ / bonne réponse
points_good_answer = 1        # 1 point / bonne réponse
cash_good_answer_bonus = 10   # Bonus si 3 tous les mots de la manche découverts

# 5 - Menu de Base et Fin Jeu
base_menu = 0
end_game = 0

# • RÉGLER AFFICHAGE •
print(BRIGHT,'''


                                                                                       • PARAMÈTRAGE JEU • 


|                                                                                                                                                                                               |
|                                                                                 Pour votre expérience de jeu                                                                                  |
|                                                                                                                                                                                               |
|                                                                           Réglez l'affichage en vous servant des |                                                                            |
|                                                                                                                                                                                               |
|                                                                                                                                                                                               |

''', NORMAL)

input()

# • CHOIX PLATEFORME POUR 'CLEAR' •
print("\n" "Avant de commencer le jeu, vous êtes sur un pc Windows (1)   ou   Mac (2) ?")
plateforme = choice_with_no_bugg(["1", "2"])

# • CHOIX PSEUDO + "Easter Egg" AVEC LordPouic + AFFICHAGE JEU (abc / a b c ) 
print("\n" "Quel est votre pseudo ?")

# 1 - Pseudo
while True:
    player_name = input(" → ")
    while len(player_name) > 10 or len(player_name) < 4 : 
        print("\n" "Votre pseudo doit contenir au moins 4 caractères et ne doit pas être supérieur à 12 caractères. " "\n" "Veuillez réessayer :")
        player_name = input(" → ")    
    print("\n" "Votre pseudo est-il bien", style, player_name, end_style, "? Oui ou Non")
    choice_name_yes_no = input(" → ")

    yes = ["OUI", "OUi", "Oui", "OuI", "oUI", "oUi", "ouI", "oui"]
    no = ["NON", "NOn", "Non", "NoN", "nON", "nOn", "noN", "non"]

    if choice_name_yes_no in yes:
        break
    elif choice_name_yes_no in no:
        print("\n" "Veuillez renseigner votre pseudo :")
    else:
        i = 0
        while i < 1:
            print("\n" "Il y a une erreur, réessayez :")
            choice_name_yes_no = input(" → ")
            if choice_name_yes_no in yes:
                i = i + 1
            elif choice_name_yes_no in no:
                i = i + 2
            else: 
                i = 0
        if i == 1:
            break
        elif i == 2:
            print("\n" "Veuillez renseigner votre pseudo :")


# 2 - Easter Egg / Cash & Points Bonus
if player_name == "Antho":
    player_points = 50 
    player_cash = 10000
    print("\n" "~ Vous avez reçu", BLUE, "50", RESET,"points ~")
    print("~ Vous avez reçu", GREEN, "10 000 $", RESET," ~")

# 3 - Affichage jeu abc / a b c 
print("\n" "Selectionnez l'affichage du jeu", style, "fdeacb", end_style, " (1)  ou", style, "f d e a c b ", end_style, "(2)")
affichage_game = choice_with_no_bugg(["1", "2"])

# • AFFICHAGE DÉBUT JEU •
clear_terminal(plateforme), start_end(1, player_name)
print("Bienvenue dans Around the Word", player_name, "!" "\n")
print(style)
print("Pour commencer appuyez sur ENTRER")
input()
print(end_style)

# • JEU •
while True:

    # Variables Dans Boucle Jeu
    back_menu = 0
    skip_menu_quitte = 0 

    clear_terminal(plateforme), start_end(1, player_name)
    # 1 - Affichage Points & Cash
    print("\n" "\n" "\n" "Points :", BLUE, player_points, RESET,"    Cash :", GREEN, player_cash, "$", RESET)
    # 2 - Menu de Base
    if base_menu == 0:
        print(style,'''
Choisissez votre Mode de Jeu :

      MENU     

• Classique     1 
• Monde         2 
• Personnages   3 
• Jeux Vidéo    4 
• Magasin       5 
• Règles        6 
• Quitter       7
        ''',end_style)
    
    # 3 - Choix Sous-Menu + Easter Egg 666 Caché
    player_choice_menu = choice_with_no_bugg(["1", "2", "3", "4", "5", "6", "7", "666"])

    # 4 - Si Choix Sous-Menu -> "6" Shop  
    if player_choice_menu == "5":
        
        value_for_shop = 0
        while value_for_shop < 1:
            player_choice_sub_menu = game_menu(player_choice_menu)
            if player_choice_sub_menu == "0":
                value_shop_menu = 1
                break
            
            # 1/ Bonus 1ère Lettre
            if bonus_first_letter == 0:
                if player_choice_sub_menu == "1" and player_cash >= 200:
                    print("\n" "Bravo",player_name, "vous venez d'acheter le bonus :", YELLOW, "~ voir la Première Lettre de chaque mots ~", RESET)                    
                    player_cash = player_cash - 200
                    shop_bonus_letters = shop_bonus_letters + 1     
                    bonus_first_letter = 1 
                    clear_shop(player_name, player_points, player_cash, plateforme)
                elif player_choice_sub_menu == "1" and player_cash < 200:
                    print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    clear_shop(player_name, player_points, player_cash, plateforme)
            elif player_choice_sub_menu == "1" and bonus_first_letter == 1:
                print()
                print(player_name, "vous avez déjà acheté ce bonus.") 
            
            # 2/ Bonus Dernière Lettre
            if bonus_last_letter == 0:
                if player_choice_sub_menu == "2" and player_cash >= 300 :
                    print("\n" "Bravo",player_name, "vous venez d'acheter le bonus :", YELLOW, "~ voir la Dernière Lettre de chaque mots ~", RESET)                    
                    player_cash = player_cash - 300
                    shop_bonus_letters = shop_bonus_letters + 2
                    bonus_last_letter = 1
                    clear_shop(player_name, player_points, player_cash, plateforme)
                elif player_choice_sub_menu == "2" and player_cash < 300:
                    print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    clear_shop(player_name, player_points, player_cash, plateforme)
            elif player_choice_sub_menu == "2" and bonus_last_letter == 1:
                    print()
                    print(player_name, "vous avez déjà acheté ce bonus.") 

            # 3/ Bonus Double Points
            if bonus_double_points == 0:
                if player_choice_sub_menu == "3" and player_cash >= 500:
                    print("\n" "Bravo",player_name, "vous venez d'acheter le bonus :", YELLOW, "~ Double Points ~", RESET)                    
                    player_cash = player_cash - 500
                    points_good_answer = 2
                    bonus_double_points = 1
                    clear_shop(player_name, player_points, player_cash, plateforme)
                elif player_choice_sub_menu == "3" and player_cash < 500:
                    print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    clear_shop(player_name, player_points, player_cash, plateforme)
            elif player_choice_sub_menu == "3" and bonus_double_points == 1:
                    print()
                    print(player_name, "vous avez déjà acheté ce bonus.")

            # 4/ Bonus Double Cash
            if bonus_double_cash == 0:
                if player_choice_sub_menu == "4" and player_cash >= 600:
                    print("\n" "Bravo",player_name, "vous venez d'acheter le bonus :", YELLOW, "~ Double Cash ~", RESET)                    
                    player_cash = player_cash - 600
                    cash_good_answer = 50
                    bonus_double_cash = 1
                    clear_shop(player_name, player_points, player_cash, plateforme)
                elif player_choice_sub_menu == "4" and player_cash < 600:
                    print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    clear_shop(player_name, player_points, player_cash, plateforme)
            elif player_choice_sub_menu == "4" and bonus_double_cash == 1:
                    print()
                    print(player_name, "vous avez déjà acheté ce bonus.")

            # 5/ Vendre 10 Points Pour 100 $
            if player_choice_sub_menu == "5" and player_points >= 10:
                print("\n" "Bravo",player_name, "vous venez de vendre :", YELLOW, "~ 10 Points pour 100 $ ~", RESET)
                player_points = player_points - 10
                player_cash = player_cash + 100
                clear_shop(player_name, player_points, player_cash, plateforme)
            elif player_choice_sub_menu == "5" and player_points < 10:
                print("\n" "Vous n'avez pas les points nécessaire. Réessayez plus tard.")
                clear_shop(player_name, player_points, player_cash, plateforme)
            
            # 6.1/ Achat Victoire
            if player_choice_sub_menu == "6" and player_cash >= 5000:
                print_value = 2
                clear_terminal(plateforme)
                start_end(print_value, player_name)
                victory = 1
                break  
            elif player_choice_sub_menu == "6" and player_points < 5000:
                print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                clear_shop(player_name, player_points, player_cash, plateforme)
 
            value_for_shop = value_for_shop + 0

    # 6.2/ Fin de Partie - Victoire - Break Boucle While
    if victory == 1:
        break
    
    # 5 - Choix Sous-Menu 
    if value_shop_menu != 1:
        player_choice_sub_menu = game_menu(player_choice_menu)
    value_shop_menu = 0

    # 6 - Quitter Le Jeu Via Menu
    if player_choice_menu == "7": 
        input()
        clear_terminal(plateforme)         
        break
    
    # 7 - Sous-Menu -> Menu de Base
    if player_choice_sub_menu == "0":       
        base_menu = 0
    
    # (si il n'y a pas le "else", le jeu plante si je fais "Retour 0")
    else:                                   
        
        game_round = 1  

        # 8 - Nouveau Compteur de Points Pour le Mode de Jeu ~ Enfer ~
        if player_choice_menu == "666":
            gamemode_satan_points = 0   

        # 9 - Début Boucle des 3 Manches 
        while game_round < 4:                        
            
            # • AFFICHAGE / CONDITIONS / VARIABLES AVANT DÉBUT MANCHES •

            # 1/ Retour Menu Depuis Partie
            if back_menu == 1:
                break

            clear_terminal(plateforme), start_end(1, player_name)
            
            # 2/ Liste + 3 Mots de la Liste + Shuffle + Nouvelle Liste de Mots + Mots Ordre Croissant
            List = list_selection(player_choice_menu, player_choice_sub_menu)
            words = words_selection(List)
            game = words_shuffle(words, affichage_game)
            order = (sorted(words, key=len))
            
            
            # 3/ Afficher Caractères(, -.)
            value_for_while_3_words = 0
            value_for_list_words = 0

            while value_for_while_3_words < 3 :
                
                hide = "_"

                # 1. Mots List dans des Nouvelles Listes 
                if value_for_list_words == 0:
                    word = order[0]  
                elif value_for_list_words == 1:
                    word = order[1]  
                elif value_for_list_words == 2:
                    word = order[2]  
                list_word = list(word)  
                size = len(word) 
                cache = list(hide * size)
                affiche = " ".join(cache)

                #  2. Afficher les - . ' et espaces
                h = 0
                space = ' '
                dash = '-'
                apostrophe = "'"
                dot = "."
                while h < size:
                    if space == list_word[h]:
                        cache[h] = space
                    elif dash == list_word[h]:
                        cache[h] = dash
                    elif apostrophe == list_word[h]:
                        cache[h] = apostrophe
                    elif dot == list_word[h]:
                        cache[h] = dot    
                    affiche = " ".join(cache)
                    h += 1 

                    # 3. Liste de Lettres pour Bonus Shop + Bonus Shop Afficher 1ère Lettre / Dernière Lettre
                    listletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "î", "â","à", "é", "è", "ê", "ñ", "û", "ô", "ù"]
                    if shop_bonus_letters ==  1 :
                        if list_word[0] in listletter:
                            cache[0] = list_word[0]
                    elif shop_bonus_letters == 2 : 
                        if list_word[-1] in listletter:
                            cache[-1] = list_word[-1]
                    elif shop_bonus_letters == 3 :
                        if list_word[0] and list_word[-1] in listletter:
                            cache[0] = list_word[0]
                            cache[-1] = list_word[-1] 
                
                # 4. Nouvel Affichage des Nouveaux Mots
                if value_for_while_3_words == 0 :
                    word_1 = affiche
                elif value_for_while_3_words == 1:
                    word_2 = affiche
                elif value_for_while_3_words == 2:
                    word_3 = affiche

                value_for_while_3_words = value_for_while_3_words + 1
                value_for_list_words = value_for_list_words + 1 

            word_1_to_find = word_1
            word_2_to_find = word_2
            word_3_to_find = word_3

            # 5/ Affichage Skip Menu Quitte Pendant la Partie SAUF Dans le Mode de Jeu ~Enfer~
            if player_choice_menu == "666":
                skip_menu_quitte = 1

            if skip_menu_quitte == 0:
                print("\n" "• Si vous voulez passer la manche tapez :", style, "SKIP", end_style, "\n" "• Si vous voulez revenir au menu tapez : ", style, "MENU", end_style, "\n" "• Si vous voulez quitter le jeu tapez : ", style, "QUITTE", end_style, "\n")
            elif skip_menu_quitte == 1:       
                print("\n" "• Si vous voulez quitter le jeu tapez : ",style,"QUITTE",end_style, "\n")

            # 6/ Variables Avant Début Manches 
            error = 0 
            end_turn_with_points = 0
            choice_word_list = [""]
            words_to_find = " ".join(order)

            # • START GAME •
            while True: 
                
                # 0 - Affichage Début Jeu Classique / Enfer
                clear_terminal(plateforme), start_end(1, player_name)
                print("\n" "\n" "\n",style,"  DÉBUT DE LA MANCHE ", game_round, end_style)
                if player_choice_menu == "666":
                    print("Vous avez",BLUE, gamemode_satan_points, RESET, "points et", GREEN, player_cash, "$", RESET) 

                elif player_choice_menu != "666":    
                    print("Vous avez",BLUE, player_points, RESET, "points et", GREEN, player_cash, "$", RESET) 

                # print(order)                                           # pour voir les mots de la manche

                if skip_menu_quitte == 0:
                    print("\n" "• Si vous voulez passer la manche tapez :", style, "SKIP", end_style, "\n" "• Si vous voulez revenir au menu tapez : ", style, "MENU", end_style, "\n" "• Si vous voulez quitter le jeu tapez : ", style, "QUITTE", end_style, "\n" "• Si vous voulez acheter un mot tapez : ",style,"SHOP",end_style, "\n")
                elif skip_menu_quitte == 1:       
                    print("\n" "• Si vous voulez quitter le jeu tapez : ",style,"QUITTE",end_style, "\n" "• Si vous voulez acheter un mot tapez : ",style,"SHOP",end_style, "\n")
  

                # 1 - Affichage Mots Utilisés + Jeu + Mots à Trouver
                use_words = "  • ".join(choice_word_list)
                print("\n" "Mots déjà utilisé :", use_words)
                print("\n" "Votre jeu :", game)
                print("\n",style,"  Mot 1 :", end_style, word_1_to_find, "\n", style, "  Mot 2 :",end_style, word_2_to_find, "\n", style,"  Mot 3 :", end_style, word_3_to_find, style)
                
                # 2 - Donnez un Mot + Lower du Mot Donné
                print("\n" "Donnez un mot :", end_style)
                choice_word = input(" → ")
                choice_word_mini = choice_word.lower()

                # 3 - Mot Déjà Utilisé Ou Non
                while True:
                    if choice_word_mini not in choice_word_list:
                        break
                    else:
                        value_for_use_word = 0
                        while value_for_use_word < 1:
                            print(("\033[38;0HVous avez déjà utilisé ce mot, veuillez en réessayer un autre."))
                            choice_word = input(" → ")
                            choice_word_mini = choice_word.lower()
                            if choice_word_mini not in choice_word_list:
                                value_for_use_word = value_for_use_word + 1
                            else: 
                                value_for_use_word = 0
                        if value_for_use_word == 1:
                            break 

                # 4 - Ajouter le Mot Donné dans une Liste pour Comparer au Prochain Tour si Déjà Utilisé        
                if choice_word_mini != "shop":
                    choice_word_list.append(choice_word_mini)
                    
                # 5 - Quitter Skip ou Menu Pendant la Partie
                if choice_word_mini == "quitte":            # quitter le jeu en pleine partie 
                    end_game = 1
                    break
                if skip_menu_quitte == 0:              # mode bloqué si contre Satan
                    if choice_word_mini == "skip":          # changer de manche
                        break
                    elif choice_word_mini == "menu":        # revenir au menu
                        clear_terminal(plateforme), start_end(1, player_name)
                        back_menu = 1
                        break

                # 6 - Achat en Partie du Mot de Notre Choix
                if choice_word_mini == "shop":
                    print("\n" "Quel mot voulez vous acheter pour", GREEN, "100 $", RESET, "?" "\n" "Mot 1 / 2 / 3")
                    player_choice_word = choice_with_no_bugg(["1", "2", "3"])
                    if player_choice_word == "1" and player_cash >= 100:
                        player_cash = player_cash - 100
                        print("\n" "Le mot 1 est :", order[0])
                    elif player_choice_word == "1" and player_cash < 100:
                        print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    if player_choice_word == "2" and player_cash >= 100:
                        player_cash = player_cash - 100
                        print("\n" "Le mot 2 est :", order[1])
                    elif player_choice_word == "2" and player_cash < 100:
                        print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    if player_choice_word == "3" and player_cash >= 100:
                        player_cash = player_cash - 100
                        print("\n" "Le mot 3 est :", order[2])
                    elif player_choice_word == "3" and player_cash < 100:
                        print("\n" "Vous n'avez pas les fonds nécessaire. Réessayez plus tard.")
                    input()
                    
                # 6 - Mot Trouvé
                if choice_word_mini in words and choice_word_mini != "shop":
                    print(CYAN + BRIGHT)
                    print("Bravo",player_name, "vous avez trouvé un mot !", RESET, "\n")
                    
                    if player_choice_menu == "666":
                        gamemode_satan_points = gamemode_satan_points + 1
                        print("~ Vous avez reçu", GREEN, cash_good_answer, "$", RESET, "&", BLUE, gamemode_satan_points, style ,"points.", end_style, "~")
                    elif player_choice_menu != "666":    
                        player_points = player_points + points_good_answer
                        print("~ Vous avez reçu", GREEN, cash_good_answer, "$", RESET, "&", BLUE, points_good_answer, style ,"points.", end_style, "~")
                    input()

                    player_cash = player_cash + cash_good_answer
                    end_turn_with_points = end_turn_with_points + 1
                    
                    if choice_word_mini == order[0]:
                        word_1_to_find = choice_word_mini 
                    elif choice_word_mini == order[1]:
                        word_2_to_find = choice_word_mini 
                    elif choice_word_mini == order[2]:
                        word_3_to_find = choice_word_mini 
                
                # 7 - Mot Non Trouvé
                elif choice_word_mini not in words and choice_word_mini != "shop":
                    print(MAGENTA + BRIGHT)
                    print("Dommage", player_name, "le mot que vous venez de donner ne fait pas parti du jeu.",RESET, "\n")
                    error = error + 1
                    if error == 1 : 
                        print(player_name, "il vous reste 2 chances sur la manche.")
                        input()
                    elif error == 2:
                        print(player_name, "il vous reste 1 chance sur la manche.")
                        input()
                    elif error == 3:    
                        print(player_name, "il ne vous reste plus de chances, la prochaine erreur mettra fin à la manche", game_round, "!")
                        input()
                    elif error == 4:
                        if player_choice_menu != "666":
                            print("\n", style, "Fin de la manche ", game_round, "\n" "Vous avez",end_style, BLUE, player_points, RESET, style, "points.", end_style)
                        if player_choice_menu == "666":
                            print("\n", style, "Fin de la manche ", game_round, "\n" "Vous avez",end_style, BLUE, gamemode_satan_points, RESET, style, "points.", end_style)
                        print("\n" "Les mots étaient : ", words_to_find,)
                        input()
                        break

                # 8 - Victoire Avec 3 Points dans la Manche (si tous les mots découverts) + Bonus Argent 
                if end_turn_with_points == 3:
                    print("\n" "Les mots étaient : ", words_to_find)
                    player_cash = player_cash + cash_good_answer_bonus     # bonus victoire avec 3 bonnes réponses
                    if player_choice_menu != "666": 
                        print(style, "\n" "Vous avez trouvé toutes les bonnes réponses bravo !" "\n" "     Fin de la manche",game_round,"vous avez", BLUE, player_points, style ,"points.", end_style)
                    if player_choice_menu == "666": 
                        print(style, "\n" "Vous avez trouvé toutes les bonnes réponses bravo !" "\n" "     Fin de la manche",game_round,"vous avez", BLUE, gamemode_satan_points, style ,"points.", end_style)
                    print("\n" "~ Vous avez reçu", GREEN, cash_good_answer_bonus, "$", RESET, "en Bonus pour vos 3 bonnes réponses sur la manche ~")
                    input()
                    break


            game_round += 1

            if end_game == 1:
                break
    
        # YOU DIED -> Si QUITTE dans le mode de jeu Enfer
        if player_choice_menu == "666" and gamemode_satan_points < 7 or player_choice_menu == "666" and choice_word == "QUITTE":
            clear_terminal(plateforme)
            start_end(3, player_name)
            break
        
        # Victoire mode de Jeu Enfer
        elif player_choice_menu == "666" and gamemode_satan_points >= 7:
            print("\n" "Satan :", style_satan, "𝖏𝖊 𝖙𝖊 𝖑𝖆𝖎𝖘𝖘𝖊 𝖑𝖆 𝖛𝖎𝖊 𝖘𝖆𝖚𝖛𝖊 𝖕𝖔𝖚𝖗 𝖈𝖊𝖙𝖙𝖊 𝖋𝖔𝖎𝖘-𝖈𝖎 ...", end_style)
            input()
            print("Dieu :", style_dieu, "Waoh, t'es un sacré bon joueur ! Ou peut être un simple coup de chance ? ", end_style)
            input()
            print("Dieu :", style_dieu, "Enfin bref tiens, voilà pour te récompenser", end_style)
            input()
            print("~ Vous avez reçu", GREEN, "666 $", RESET, "~")
            player_cash = player_cash + 666
            input()

        elif end_game == 1:
            game_menu("7")
            input()
            clear_terminal(plateforme)
            break
