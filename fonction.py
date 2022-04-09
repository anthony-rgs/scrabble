from random import randint
import os
import random

# • AFFICHAGE TEXTE •

# 1 - texte couleur :
RED     = '\033[31m'
GREEN   = '\033[32m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
YELLOW  = '\033[33m'
RESET   = '\033[39m'

# 2 - texte écriture :
BRIGHT  = '\033[1m'
NORMAL  = '\033[22m'

# 3 - preset affichage :
style = WHITE + BRIGHT
style_dieu = CYAN + BRIGHT
style_satan = RED + BRIGHT
end_style = NORMAL + RESET


# • LISTES •
def list_selection(choice_menu, player_choice_sub_menu):

    # 1 - CLASSIQUE         
    if choice_menu == "1":
        # 3 lettres                 (1)
        if player_choice_sub_menu == "1":
            List = ["lit", "bus", "bol", "sac","ado", "âge", "âme", "art", "bar", "bio", "bec", "boa", "bob", "bon", "cul", "cil", "dix", "écu", "fer", "feu", "ère", "été", "fil", "gaz", "ici", "île", "jeu", "lac", "lui", "mai", "mec", "mur", "nid", "nez", "pas", "pet", "psy", "rat", "rue", "sel", "sec", "ski", "sol", "tas", "web", "zoo", "mie", "mal", "les", "des"]
            return List
        # 4 lettres                 (2)
        elif player_choice_sub_menu == "2":
            List = ["robe", "jupe", "pull", "jour", "rose", "bleu", "gros", "beau", "nuit", "lune", "lampe", "vert", "vers", "lire", "vélo", "moto", "café", "amis", "acné", "amer", "aide", "amie", "bain", "bide", "beuh", "banc", "bide", "cuir", "dans", "elle", "écus", "face", "faux", "geek", "cave", "golf", "gros", "glue", "haut", "jeux", "lave", "neuf", "note", "noix", "peau", "rêve", "sage", "sauf", "tome", "zoom"]
            return List 
        # 5 lettres                 (3)
        elif player_choice_sub_menu == "3":
            List = ["stylo", "règle", "rouge", "jaune", "piano", "mince", "tasse", "belle", "photo", "lapin", "carte", "cadre", "prise", "porte", "verre", "livre", "vache", "table", "avion", "train", "arbre", "fleur", "petit", "grand", "métro", "accro", "actif", "aucun", "bille", "carpe", "crabe", "cycle", "draps", "drôle", "fesse", "fable", "gazon", "gosse", "igloo", "malin", "mamie", "noire", "pages", "puits", "quand", "repos", "sabre", "short", "tueur", "zèbre"]
            return List   
        # 6 lettres                 (4)
        elif player_choice_sub_menu == "4":
            List = ["cahier", "soleil", "violet", "valise", "violon", "cheval", "animal", "crayon", "montre", "maison", "douche", "mouche", "chaise", "chèvre", "mouton", "cochon", "fleuve", "canapé", "gâteau", "souris", "action", "acides", "adepte", "balcon", "banane", "ananas", "regard", "bonnet", "cantal", "copine", "copain", "doutes", "facile", "espèce", "famine", "frigos", "froide", "hanche", "kebabs", "lacune", "menace", "navale", "patron", "paysan", "racine", "raisin", "sabres", "trente", "whisky", "zombie"]
            return List
        # 3 à 6 lettres             (5)
        elif player_choice_sub_menu == "5":
            List = ["lit", "bus", "bol", "sac","ado", "age", "ame", "art", "bar", "bio", "bec", "boa", "bob", "bon", "cul", "cil", "dix", "écu", "fer", "feu", "ère", "été", "fil", "gaz", "ici", "île", "jeu", "lac", "lui", "mai", "mec", "mur", "nid", "nez", "pas", "pet", "psy", "rat", "rue", "sel", "sec", "ski", "sol", "tas", "web", "zoo", "mie", "mal", "les", "des", "robe", "jupe", "pull", "jour", "rose", "bleu", "gros", "beau", "nuit", "lune", "lampe", "vert", "vers", "lire", "vélo", "moto", "café", "amis", "acné", "amer", "aide", "amie", "bain", "bide", "beuh", "banc", "bide", "cuir", "dans", "elle", "écus", "face", "faux", "geek", "cave", "golf", "gros", "glue", "haut", "jeux", "lave", "neuf", "note", "noix", "peau", "rêve", "sage", "sauf", "tome", "zoom", "stylo", "règle", "rouge", "jaune", "piano", "mince", "tasse", "belle", "photo", "lapin", "carte", "cadre", "prise", "porte", "verre", "livre", "vache", "table", "avion", "train", "arbre", "fleur", "petit", "grand", "métro", "accro", "actif", "aucun", "bille", "carpe", "crabe", "cycle", "draps", "drôle", "fesse", "fable", "gazon", "gosse", "igloo", "malin", "mamie", "noire", "pages", "puits", "quand", "repos", "sabre", "short", "tueur", "zèbre", "cahier", "soleil", "violet", "valise", "violon", "cheval", "animal", "crayon", "montre", "maison", "douche", "mouche", "chaise", "chèvre", "mouton", "cochon", "fleuve", "canapé", "gâteau", "souris", "action", "acides", "adepte", "balcon", "banane", "ananas", "regard", "bonnet", "cantal", "copine", "copain", "doutes", "facile", "espèce", "famine", "frigos", "froide", "hanche", "kebabs", "lacune", "menace", "navale", "patron", "paysan", "racine", "raisin", "sabres", "trente", "whisky", "zombie"]
            return List

    # 2 - MONDE
    elif choice_menu == "2":
        # Présidents USA            (1)
        if player_choice_sub_menu == "1":
            List = ["george washington", "john adams", "thomas jefferson", "james madison", "james monroe", "john quincy adams", "andrew jackson", "martin van buren", "william henry harrison", "john tyler", "james polk", "zachary taylor", "millard fillmore", "franklin pierce", "james buchanan", "abraham lincoln", "andrew johnson", "ulysses grant", "rutherford hayes", "james garfield", "chester arthur", "grover cleveland", "benjamin harisson", "william mckinley", "theodore roosevelt", "william taft", "woodrow wilson", "warren harding", "calvin coolidge", "herbert hoover", "franklin delano roosevelt", "harry truman", "dwight eisenhower", "john fitzgerald kennedy", "lyndon johnson", "richard nixon", "gerald ford", "jimmy carter", "ronald reagan", "george h w bush", "bill clinton", "george w bush", "barack obama", "donald trump", "joe biden"]
            return List
        # Capitales UE              (2)
        if player_choice_sub_menu == "2":
            List = ["berlin", "vienne", "bruxelles", "sofia", "nicosie", "zagreb", "copenhague", "madrid", "tallinn", "helsinki", "paris", "athènes", "budapest", "dublin", "rome", "riga", "vilnius", "luxembourg", "la valette", "amsterdam", "varsovie", "lisbonne", "prague", "bucarest", "bratislava", "ljubljana", "stockholm"]
            return List
        # Pays UE                   (3)
        if player_choice_sub_menu == "3":
            List = ["allemagne", "autriche", "belgique", "bulgarie", "chypre", "croatie", "danemark", "espagne", "estonie", "finlande", "france", "grèce", "hongrie", "irlande", "italie", "lettonie", "lituanie", "luxembourg", "malte", "pays-bas", "pologne", "portugal", "république tchèque", "roumanie", "slovaquie", "slovénie", "suède"]    
            return List
        # Capitales & Pays UE       (4)
        if player_choice_sub_menu == "4":
            List = ["allemagne", "autriche", "belgique", "bulgarie", "chypre", "croatie", "danemark", "espagne", "estonie", "finlande", "france", "grèce", "hongrie", "irlande", "italie", "lettonie", "lituanie", "luxembourg", "malte", "pays-bas", "pologne", "portugal", "république tchèque", "roumanie", "slovaquie", "slovénie", "suède", "berlin", "vienne", "bruxelles", "sofia", "nicosie", "zagreb", "copenhague", "madrid", "tallinn", "helsinki", "paris", "athènes", "budapest", "dublin", "rome", "riga", "vilnius", "luxembourg", "la valette", "amsterdam", "varsovie", "lisbonne", "prague", "bucarest", "bratislava", "ljubljana", "stockholm"]  
            return List
        # Capitales Monde           (5)       
        if player_choice_sub_menu == "5":
            List = ["abou dabi", "abuja", "accra", "achgabat", "addis-abeba", "alger", "alofi", "amman", "amsterdam", "andorre-la-vieille", "ankara", "antananarivo", "apia", "asmara", "asuncion", "athènes", "avarua", "bagdad", "bakou", "bamako", "bandar seri begawan", "bangkok",  "bangui", "banjul", "basseterre", "belgrade", "belmopan", "berlin", "berne", "beyrouth", "bichkek", "bissau", "bloemfontein", "bogota", "brasilia", "bratislava", "brazzaville", "bridgetown", "bruxelles", "bucarest", "budapest", "buenos aires", "le caire", "canberra", "le cap", "caracas", "castries", "chisinau", "sri jayawardenapura kotte", "conakry", "copenhague", "dakar", "damas", "delap-uliga-darrit", "dacca", "dili", "djibouti", "djouba", "dodoma", "doha", "douchanbé", "dublin", "erevan", "freetown", "funafuti", "gaborone", "georgetown", "gitega", "guatemala", "hanoï", "harare", "la havane", "helsinki", "honiara", "islamabad", "jakarta", "jérusalem", "kaboul", "kampala", "katmandou", "khartoum", "kiev", "kigali", "kingston", "kingstown", "kinshasa", "melekeok", "koweït", "kuala lumpur", "libreville", "lilongwe", "lima", "lisbonne", "ljubljana", "lomé", "londres", "luanda", "lusaka", "luxembourg", "madrid", "malabo", "malé", "managua", "manama", "manille", "maputo", "mascate", "maseru", "mbabane", "mexico", "minsk", "mogadiscio", "monaco", "monrovia", "montevideo", "moroni", "moscou", "mairobi", "massau", "naypyidaw", "n'djaména", "new delhi", "niamey", "nicosie", "nouakchott", "noursoultan","nuku'alofa", "oslo", "ottawa", "ouagadougou", "oulan-bator", "palikir", "panama", "paramaribo", "paris", "la paz", "pékin", "phnom penh", "podgorica", "port moresby", "port-au-prince", "port-d'espagne", "port-louis", "porto-novo", "port-vila", "prague", "praia", "pretoria", "putrajaya", "pyongyang", "quito", "rabat", "reykjavik", "riga", "riyad", "rome", "roseau", "saint john's", "saint-domingue", "saint-georges", "saint-marin", "san josé", "san salvador", "sanaa", "santiago", "são tomé" "sarajevo", "séoul", "singapour", "skopje", "sofia", "stockholm", "sucre" , "suva", "tachkent", "tallinn", "tbilissi", "tegucigalpa", "téhéran", "thimphou", "tirana", "tokyo", "tripoli", "tunis", "vaduz", "la valette", "varsovie", "cité du vatican", "victoria", "vienne", "vientiane", "vilnius", "washington d.c", "wellington", "windhoek", "yamoussoukro", "yaoundé", "yaren", "zagreb"]
            return List
        # Pays Monde                (6)
        if player_choice_sub_menu == "6":
            List = ["afrique du sud", "afghanistan", "albanie", "algérie", "allemagne", "andorre", "angola", "antigua-et-barbuda", "arabie saoudite", "argentine", "arménie", "australie", "autriche", "azerbaïdjan", "bahamas", "bahreïn", "bangladesh", "barbade", "belgique", "belize", "bénin", "bhoutan", "biélorussie", "birmanie", "bolivie", "bosnie-herzégovine", "botswana", "brésil", "brunei", "bulgarie", "burkina faso", "burundi", "cambodge", "cameroun", "canada", "cap-vert", "république centrafricaine", "chili", "chine", "chypre", "colombie", "comores", "république du congo", "république démocratique du congo", "îles cook", "corée du nord", "corée du sud", "costa rica", "côte d'ivoire", "croatie", "cuba", "danemark", "djibouti", "république dominicaine", "dominique", "égypte", "émirats arabes unis", "équateur", "érythrée", "espagne", "estonie", "eswatini", "états-unis", "éthiopie", "fidji", "finlande", "france", "gabon", "gambie", "géorgie", "ghana", "grèce", "grenade", "guatemala", "guinée", "guinée-bissau", "guinée équatoriale", "guyana", "haïti", "honduras", "hongrie", "inde", "indonésie", "irak", "iran", "irlande", "islande", "israël", "italie", "jamaïque", "japon", "jordanie", "kazakhstan", "kenya", "kirghizistan", "kiribati", "koweït", "laos", "lesotho", "lettonie", "liban", "liberia", "libye", "liechtenstein", "lituanie", "luxembourg", "macédoine du nord", "madagascar", "malaisie", "malawi", "maldives", "mali", "malte", "maroc", "îles marshall", "maurice", "mauritanie", "mexique", "micronésie", "moldavie", "monaco", "mongolie", "monténégro", "mozambique", "namibie", "nauru", "népal", "nicaragua", "niger", "nigeria", "niue", "norvège", "nouvelle-zélande", "oman", "ouganda", "ouzbékistan", "pakistan", "palaos", "palestine", "panamá", "papouasie-nouvelle-guinée", "paraguay", "pays-bas", "pérou", "philippines", "pologne", "portugal", "qatar", "roumanie", "royaume-uni", "russie", "rwanda", "saint-christophe-et-niévès", "saint-marin", "saint-vincent-et-les grenadines", "sainte-lucie", "îles salomon", "salvador", "samoa", "são tomé-et-principe", "sénégal", "serbie", "seychelles", "sierra leone", "singapour", "slovaquie", "slovénie", "somalie", "soudan", "soudan du sud", "sri lanka", "suède", "suisse", "suriname", "syrie", "tadjikistan", "tanzanie", "tchad", "république tchèque", "thaïlande", "timor oriental", "togo", "tonga", "trinité-et-tobago", "tunisie", "turkménistan", "turquie", "tuvalu", "ukraine", "uruguay", "vanuatu", "vatican", "venezuela", "viêt nam", "yémen", "zambie", "zimbabwe"]
            return List
        # Capitales & Pays Monde    (7)
        if player_choice_sub_menu == "7":
            List = ["abou dabi", "abuja", "accra", "achgabat", "addis-abeba", "alger", "alofi", "amman", "amsterdam", "andorre-la-vieille", "ankara", "antananarivo", "apia", "asmara", "asuncion", "athènes", "avarua", "bagdad", "bakou", "bamako", "bandar seri begawan", "bangkok",  "bangui", "banjul", "basseterre", "belgrade", "belmopan", "berlin", "berne", "beyrouth", "bichkek", "bissau", "bloemfontein", "bogota", "brasilia", "bratislava", "brazzaville", "bridgetown", "bruxelles", "bucarest", "budapest", "buenos aires", "le caire", "canberra", "le cap", "caracas", "castries", "chisinau", "sri jayawardenapura kotte", "conakry", "copenhague", "dakar", "damas", "delap-uliga-darrit", "dacca", "dili", "djibouti", "djouba", "dodoma", "doha", "douchanbé", "dublin", "erevan", "freetown", "funafuti", "gaborone", "georgetown", "gitega", "guatemala", "hanoï", "harare", "la havane", "helsinki", "honiara", "islamabad", "jakarta", "jérusalem", "kaboul", "kampala", "katmandou", "khartoum", "kiev", "kigali", "kingston", "kingstown", "kinshasa", "melekeok", "koweït", "kuala lumpur", "libreville", "lilongwe", "lima", "lisbonne", "ljubljana", "lomé", "londres", "luanda", "lusaka", "luxembourg", "madrid", "malabo", "malé", "managua", "manama", "manille", "maputo", "mascate", "maseru", "mbabane", "mexico", "minsk", "mogadiscio", "monaco", "monrovia", "montevideo", "moroni", "moscou", "mairobi", "massau", "naypyidaw", "n'djaména", "new delhi", "niamey", "nicosie", "nouakchott", "noursoultan","nuku'alofa", "oslo", "ottawa", "ouagadougou", "oulan-bator", "palikir", "panama", "paramaribo", "paris", "la paz", "pékin", "phnom penh", "podgorica", "port moresby", "port-au-prince", "port-d'espagne", "port-louis", "porto-novo", "port-vila", "prague", "praia", "pretoria", "putrajaya", "pyongyang", "quito", "rabat", "reykjavik", "riga", "riyad", "rome", "roseau", "saint john's", "saint-domingue", "saint-georges", "saint-marin", "san josé", "san salvador", "sanaa", "santiago", "são tomé" "sarajevo", "séoul", "singapour", "skopje", "sofia", "stockholm", "sucre" , "suva", "tachkent", "tallinn", "tbilissi", "tegucigalpa", "téhéran", "thimphou", "tirana", "tokyo", "tripoli", "tunis", "vaduz", "la valette", "varsovie", "cité du vatican", "victoria", "vienne", "vientiane", "vilnius", "washington d.c", "wellington", "windhoek", "yamoussoukro", "yaoundé", "yaren", "zagreb", "afrique du sud", "afghanistan", "albanie", "algérie", "allemagne", "andorre", "angola", "antigua-et-barbuda", "arabie saoudite", "argentine", "arménie", "australie", "autriche", "azerbaïdjan", "bahamas", "bahreïn", "bangladesh", "barbade", "belgique", "belize", "bénin", "bhoutan", "biélorussie", "birmanie", "bolivie", "bosnie-herzégovine", "botswana", "brésil", "brunei", "bulgarie", "burkina faso", "burundi", "cambodge", "cameroun", "canada", "cap-vert", "république centrafricaine", "chili", "chine", "chypre", "colombie", "comores", "république du congo", "république démocratique du congo", "îles cook", "corée du nord", "corée du sud", "costa rica", "côte d'ivoire", "croatie", "cuba", "danemark", "djibouti", "république dominicaine", "dominique", "égypte", "émirats arabes unis", "équateur", "érythrée", "espagne", "estonie", "eswatini", "états-unis", "éthiopie", "fidji", "finlande", "france", "gabon", "gambie", "géorgie", "ghana", "grèce", "grenade", "guatemala", "guinée", "guinée-bissau", "guinée équatoriale", "guyana", "haïti", "honduras", "hongrie", "inde", "indonésie", "irak", "iran", "irlande", "islande", "israël", "italie", "jamaïque", "japon", "jordanie", "kazakhstan", "kenya", "kirghizistan", "kiribati", "koweït", "laos", "lesotho", "lettonie", "liban", "liberia", "libye", "liechtenstein", "lituanie", "luxembourg", "macédoine du nord", "madagascar", "malaisie", "malawi", "maldives", "mali", "malte", "maroc", "îles marshall", "maurice", "mauritanie", "mexique", "micronésie", "moldavie", "monaco", "mongolie", "monténégro", "mozambique", "namibie", "nauru", "népal", "nicaragua", "niger", "nigeria", "niue", "norvège", "nouvelle-zélande", "oman", "ouganda", "ouzbékistan", "pakistan", "palaos", "palestine", "panamá", "papouasie-nouvelle-guinée", "paraguay", "pays-bas", "pérou", "philippines", "pologne", "portugal", "qatar", "roumanie", "royaume-uni", "russie", "rwanda", "saint-christophe-et-niévès", "saint-marin", "saint-vincent-et-les grenadines", "sainte-lucie", "îles salomon", "salvador", "samoa", "são tomé-et-principe", "sénégal", "serbie", "seychelles", "sierra leone", "singapour", "slovaquie", "slovénie", "somalie", "soudan", "soudan du sud", "sri lanka", "suède", "suisse", "suriname", "syrie", "tadjikistan", "tanzanie", "tchad", "république tchèque", "thaïlande", "timor oriental", "togo", "tonga", "trinité-et-tobago", "tunisie", "turkménistan", "turquie", "tuvalu", "ukraine", "uruguay", "vanuatu", "vatican", "venezuela", "viêt nam", "yémen", "zambie", "zimbabwe"]
            return List

    # 3 - PERSONNAGES
    elif choice_menu == "3":
    # ANIMÉS
        # Naruto                    (1)
        if player_choice_sub_menu == "1":
            List = ["yamato", "naruto", "sakura", "sasuke", "chôji", "ino", "shikamaru", "hinata", "kiba", "shino", "neji", "rock", "tenten", "konohamaru", "hashirama", "hiruzen", "tobirama", "danzô", "hiruzen", "jiraya", "orochimaru", "tsunade", "kakashi", "obito", "lin", "hanabi", "shisui", "sakumo", "inoichi", "hiashi", "shikaku", "shizune", "asuma", "gaï", "kurenai", "saï", "minato", "itahci", "kabuto", "madara", "kushina", "hokage", "mizukage", "raikage", "kazekage", "tsuchikage", "killer bee", "suigetsu", "karin", "jûgo", "temari", "kakurô", "gaara", "pain", "konan", "nagato", "yahiko", "kisame", "hidan", "zetsu", "deidara", "sasori", "kakuzu", "ichibi", "nibi", "sanbi", "yonbi", "gobi", "rokubi", "nanabi", "hachibi", "kyûbi", "kurama"]
            return List
        # Boruto                    (2)
        elif player_choice_sub_menu == "2":
            List = ["boruto", "sarada", "mitsuki", "anko", "kinshiki", "shinki", "metal", "katasuke", "sukea", "kawaki", "denki", "namida", "sumire", "iwabee", "wasabi", "kagura", "urashiki", "sekiei", "akkun", "tosaka", "kuu", "kokuyou", "kakou", "koji", "delta", "mugino", "isshiki", "code", "boro", "shojoji", "momoshiki"]
            return List
        # Naruto & Boruto           (3)
        elif player_choice_sub_menu == "3":
            List = ["yamato", "naruto", "sakura", "sasuke", "chôji", "ino", "shikamaru", "hinata", "kiba", "shino", "neji", "rock", "tenten", "konohamaru", "hashirama", "hiruzen", "tobirama", "danzô", "hiruzen", "jiraya", "orochimaru", "tsunade", "kakashi", "obito", "lin", "hanabi", "shisui", "sakumo", "inoichi", "hiashi", "shikaku", "shizune", "asuma", "gaï", "kurenai", "saï", "minato", "itahci", "kabuto", "madara", "kushina", "hokage", "mizukage", "raikage", "kazekage", "tsuchikage", "killer bee", "suigetsu", "karin", "jûgo", "temari", "kakurô", "gaara", "pain", "konan", "nagato", "yahiko", "kisame", "hidan", "zetsu", "deidara", "sasori", "kakuzu", "ichibi", "nibi", "sanbi", "yonbi", "gobi", "rokubi", "nanabi", "hachibi", "kyûbi", "kurama", "boruto", "sarada", "mitsuki", "anko", "kinshiki", "shinki", "metal", "katasuke", "sukea", "kawaki", "denki", "namida", "sumire", "iwabee", "wasabi", "kagura", "urashiki", "sekiei", "akkun", "tosaka", "kuu", "kokuyou", "kakou", "koji", "delta", "mugino", "isshiki", "code", "boro", "shojoji", "momoshiki"]
            return List
        # Hunter X Hunter           (4)
        elif player_choice_sub_menu == "4":
            List = ["gon", "kirua", "kurapika", "leolio", "hisoka", "beans", "biscuit", "irumi", "kaito", "morau", "pamû", "satotsu", "jin", "mito", "netero", "meruem", "neferupito", "shaupfufu", "montutyupi", "koruto", "karuto", "zeno", "silva", "sharnalk", "kuroro", "nobunaga", "feitan", "machi", "phinks", "franklin", "shizuku", "bonorenof", "pakunoda", "zushi", "mizaisutomu", "parisuton", "piyon", "kanzai", "chiidoru", "botobai", "geru", "kurukku", "ginta"]
            return List
        # L'Attaque Des Titans      (5)
        elif player_choice_sub_menu == "5":
            List = ["eren", "mikasa", "armin", "grisha", "levi", "sasha", "hans", "jean", "annie", "reiner", "christa", "erwin", "ymir", "marco", "mina", "daris", "keith", "bertolt", "gaby", "titan assaillant", "titan colossal", "titan mâchoire", "titan bestial", "titan cuirassé", "titan marteau d'arme", "titan charrette", "titan féminin", "titan originel", "sieg", "historia"]
            return List
        # My Hero Academia          (6)
        elif player_choice_sub_menu == "6":
            List = ["nezu", "recovery girl", "numéro13", "hound dog", "all might", "aizawa", "ectoplasm", "gran torino", "yuga", "mina", "tsuyu", "tenya", "ochaco", "mashirao", "denki", "eijiro", "koji", "rikido", "mezo", "kyoka", "hanta", "fumikage", "shoto", "toru", "katsuki", "izuku", "minoru", "momo", "uraraka", "kaminari", "kirishima", "shoji", "sero", "tokoyami", "todoroki", "bakugo", "midoriya", "mineta", "tetsutetsu", "neito", "mirio", "nejire", "tamaki", "hatsume", "inasa", "eri", "brainless", "stain", "all for one", "hawks", "shigaraki", "himiko", "dabi", "muscular", "moonfish", "kurogiri", "nana", "nighteye", "eraser head", "cementos", "fat gum", "ryukyu", "dieu sylvetre", "gang orca", "endeavor", "best jeanist", "edgeshot", "mante lady"]
            return List
        # Jujutsu Kaisen            (7)
        elif player_choice_sub_menu == "7":
            List = ["jogo", "hanami", "mahito", "kechizu", "eso", "sukuna", "junpei", "suguru", "nanami", "aoi", "noritoshi", "momo", "mai", "kasumi", "ultimate mechamaru", "gakuganji", "maki", "toge", "panda", "yuji", "megumi", "nobara", "masamichi", "satoru", "gojo", "sheko", "akari"]
            return List
        # Food Wars                 (8)
        elif player_choice_sub_menu == "8":
            List = ["sôma", "erina", "yuki", "ryôko", "satoshi", "hisako", "ikumi", "takumi", "isami", "alice", "megumi", "jôichirô", "kojirô", "dôjima", "shun", "zenji", "fumio", "senzaemon", "hinako", "ryô", "mayumi", "fuyumi", "akira", "jun", "miyoko", "daigo", "shôji", "kanichi", "eishi", "terunori", "nene", "momo", "tôsuke", "nakiri", "yukihira", "aldini", "shinomiya"]
            return List 
        # Tous les animés           (9)
        elif player_choice_sub_menu == "9":
            List = ["yamato", "naruto", "sakura", "sasuke", "chôji", "ino", "shikamaru", "hinata", "kiba", "shino", "neji", "rock", "tenten", "konohamaru", "hashirama", "hiruzen", "tobirama", "danzô", "hiruzen", "jiraya", "orochimaru", "tsunade", "kakashi", "obito", "lin", "hanabi", "shisui", "sakumo", "inoichi", "hiashi", "shikaku", "shizune", "asuma", "gaï", "kurenai", "saï", "minato", "itahci", "kabuto", "madara", "kushina", "hokage", "mizukage", "raikage", "kazekage", "tsuchikage", "killer bee", "suigetsu", "karin", "jûgo", "temari", "kakurô", "gaara", "pain", "konan", "nagato", "yahiko", "kisame", "hidan", "zetsu", "deidara", "sasori", "kakuzu", "ichibi", "nibi", "sanbi", "yonbi", "gobi", "rokubi", "nanabi", "hachibi", "kyûbi", "kurama", "boruto", "sarada", "mitsuki", "anko", "kinshiki", "shinki", "metal", "katasuke", "sukea", "kawaki", "denki", "namida", "sumire", "iwabee", "wasabi", "kagura", "urashiki", "sekiei", "akkun", "tosaka", "kuu", "kokuyou", "kakou", "koji", "delta", "mugino", "isshiki", "code", "boro", "shojoji", "momoshiki", "gon", "kirua", "kurapika", "leolio", "hisoka", "beans", "biscuit", "irumi", "kaito", "morau", "pamû", "satotsu", "jin", "mito", "netero", "meruem", "neferupito", "shaupfufu", "montutyupi", "koruto", "karuto", "zeno", "silva", "sharnalk", "kuroro", "nobunaga", "feitan", "machi", "phinks", "franklin", "shizuku", "bonorenof", "pakunoda", "zushi", "mizaisutomu", "parisuton", "piyon", "kanzai", "chiidoru", "botobai", "geru", "kurukku", "ginta", "eren", "mikasa", "armin", "grisha", "levi", "sasha", "hans", "jean", "annie", "reiner", "christa", "erwin", "ymir", "marco", "mina", "daris", "keith", "bertolt", "gaby", "titan assaillant", "titan colossal", "titan mâchoire", "titan bestial", "titan cuirassé", "titan marteau d'arme", "titan charrette", "titan féminin", "titan originel", "sieg", "historia", "nezu", "recovery girl", "numéro13", "hound dog", "all might", "aizawa", "ectoplasm", "gran torino", "yuga", "mina", "tsuyu", "tenya", "ochaco", "mashirao", "denki", "eijiro", "koji", "rikido", "mezo", "kyoka", "hanta", "fumikage", "shoto", "toru", "katsuki", "izuku", "minoru", "momo", "uraraka", "kaminari", "kirishima", "shoji", "sero", "tokoyami", "todoroki", "bakugo", "midoriya", "mineta", "tetsutetsu", "neito", "mirio", "nejire", "tamaki", "hatsume", "inasa", "eri", "brainless", "stain", "all for one", "hawks", "shigaraki", "himiko", "dabi", "muscular", "moonfish", "kurogiri", "nana", "nighteye", "eraser head", "cementos", "fat gum", "ryukyu", "dieu sylvetre", "gang orca", "endeavor", "best jeanist", "edgeshot", "mante lady", "jogo", "hanami", "mahito", "kechizu", "eso", "sukuna", "junpei", "suguru", "nanami", "aoi", "noritoshi", "momo", "mai", "kasumi", "ultimate mechamaru", "gakuganji", "maki", "toge", "panda", "yuji", "megumi", "nobara", "masamichi", "satoru", "gojo", "sheko", "akari", "sôma", "erina", "yuki", "ryôko", "satoshi", "hisako", "ikumi", "takumi", "isami", "alice", "megumi", "jôichirô", "kojirô", "dôjima", "shun", "zenji", "fumio", "senzaemon", "hinako", "ryô", "mayumi", "fuyumi", "akira", "jun", "miyoko", "daigo", "shôji", "kanichi", "eishi", "terunori", "nene", "momo", "tôsuke", "nakiri", "yukihira", "aldini", "shinomiya"]
            return List
    # FILMS
        # Princesses Disney         (10)
        elif player_choice_sub_menu == "10":
            List = ["blanche neige", "cendrillon", "aurore", "ariel", "belle", "jasmine", "pocahontas", "mulan", "tiana", "raiponce", "merida", "elsa", "anna", "vaiana"]
            return List 
        # Harry Potter              (11)
        elif player_choice_sub_menu == "11":
            List = ["sirius", "black", "harry", "potter", "hermione", "granger", "voldemort", "drago", "malfoy", "severus", "rogue", "albus", "dumbledore", "ron", "weasley", "rubeus", "hagrid", "dobby", "luna", "lovegood", "minerva", "mcgonagall", "bellatrix", "lestrange", "neville", "londubat", "ginny", "remus", "lupin", "dolores", "ombrage", "peter", "pettigrow", "fleur", "delacour", "hedwige", "choixpeau", "james", "mimi", "geignarde", "lucius", "seamus", "sibylle", "lily", "fred", "alastor", "maugrey", "narcissa", "dudley", "argus", "rusard", "lavande", "george", "cedric", "diggory"]
            return List 
        # Star Wars                 (12)
        elif player_choice_sub_menu == "12":
            List = ["anakin", "skywalker", "dark vador", "padmé", "amidala", "r2-d2", "c-3po", "qui-gon", "jinn", "jar jar", "obi-wan", "kenobi", "yoda", "dark maul", "boba fett", "jango fett", "dooku", "sheev", "palpatine", "dark sidious", "luke", "leia", "han", "solo", "chewbacca", "jabba", "rey", "finn", "ben", "kylo ren"]
            return List 
        # Seigneur Des Anneaux      (13)
        elif player_choice_sub_menu == "13":
            List = ["gandalf", "aragorn", "frodon", "gollum", "legolas", "arwen", "sauron", "bilbon", "sacquet", "galadriel", "éowyn", "nazgûl", "peregrin", "éomer", "radagast", "saroumane"]
            return List 
        # Héros Marvel              (14)
        elif player_choice_sub_menu == "14":
            List = ["iron man", "tony stark", "captain america", "avangers", "steve rogers", "thor", "hulk", "bruce banner", "black widow", "natasha romanoff", "spider man", "peter parker", "black panther", "t'challa", "captain marvel", "carole denvers", "ant-man", "scott lang", "doctor strange", "stephen strange", "star-lord", "peter quill", "thanos", "deadpool", "wade wilson", "wolverine", "logan", "dardevil", "matt murdock", "le fauve", "hank mccoy", "luke cage", "drax", "vision", "groot", "colossus", "loki", "nick fury", "oeil-de-faucon", "ultron", "faucon", "pepper potts", "war machine", "jarvis", "stan lee", "sheild", "la chose", "la torche humaine", "mr fantastique", "la femme invisible", "iron fist", "tornade", "rocket racoon", "shang-chi", "ronin", "yondu", "bucky", "la guêpe", "cyclope", "wanda", "nébula", "gamora", "charles xavier", "phoenix"]
            return List 
        # Héros DC                  (15)
        elif player_choice_sub_menu == "15":
            List = ["superman", "clark kent", "batman", "bruce wayne", "justice league", "flash", "barry allen", "green arrow", "green lanter", "aquaman", "wonder woman", "superboy", "robin", "hourman", "wonder girl", "atom smasher", "loose cannon", "ultra boy", "big barda", "omac", "mary marvel", "lobo", "donna troy", "supergirl", "bizarro", "orion", "harley queen", "le joker", "power girl", "shazam", "damage"]
            return List 
        # Héros Marvel & DC         (16)
        elif player_choice_sub_menu == "16":
            List = ["iron man", "tony stark", "captain america", "avangers", "steve rogers", "thor", "hulk", "bruce banner", "black widow", "natasha romanoff", "spider man", "peter parker", "black panther", "t'challa", "captain marvel", "carole denvers", "ant-man", "scott lang", "doctor strange", "stephen strange", "star-lord", "peter quill", "thanos", "deadpool", "wade wilson", "wolverine", "logan", "dardevil", "matt murdock", "le fauve", "hank mccoy", "luke cage", "drax", "vision", "groot", "colossus", "loki", "nick fury", "oeil-de-faucon", "ultron", "faucon", "pepper potts", "war machine", "jarvis", "stan lee", "sheild", "la chose", "la torche humaine", "mr fantastique", "la femme invisible", "iron fist", "tornade", "rocket racoon", "shang-chi", "ronin", "yondu", "bucky", "la guêpe", "cyclope", "wanda", "nébula", "gamora", "charles xavier", "phoenix", "superman", "clark kent", "batman", "bruce wayne", "justice league", "flash", "barry allen", "green arrow", "green lanter", "aquaman", "wonder woman", "superboy", "robin", "hourman", "wonder girl", "atom smasher", "loose cannon", "ultra boy", "big barda", "omac", "mary marvel", "lobo", "donna troy", "supergirl", "bizarro", "orion", "harley queen", "le joker", "power girl", "shazam", "damage"]
            return List 
        # Tous les Films            (17)
        elif player_choice_sub_menu == "17":
            List = ["blanche neige", "cendrillon", "aurore", "ariel", "belle", "jasmine", "pocahontas", "mulan", "tiana", "raiponce", "merida", "elsa", "anna", "vaiana", "sirius", "black", "harry", "potter", "hermione", "granger", "voldemort", "drago", "malfoy", "severus", "rogue", "albus", "dumbledore", "ron", "weasley", "rubeus", "hagrid", "dobby", "luna", "lovegood", "minerva", "mcgonagall", "bellatrix", "lestrange", "neville", "londubat", "ginny", "remus", "lupin", "dolores", "ombrage", "peter", "pettigrow", "fleur", "delacour", "hedwige", "choixpeau", "james", "mimi", "geignarde", "lucius", "seamus", "sibylle", "lily", "fred", "alastor", "maugrey", "narcissa", "dudley", "argus", "rusard", "lavande", "george", "cedric", "diggory", "anakin", "skywalker", "dark vador", "padmé", "amidala", "r2-d2", "c-3po", "qui-gon", "jinn", "jar jar", "obi-wan", "kenobi", "yoda", "dark maul", "boba fett", "jango fett", "dooku", "sheev", "palpatine", "dark sidious", "luke", "leia", "han", "solo", "chewbacca", "jabba", "rey", "finn", "ben", "kylo ren", "gandalf", "aragorn", "frodon", "gollum", "legolas", "arwen", "sauron", "bilbon", "sacquet", "galadriel", "éowyn", "nazgûl", "peregrin", "éomer", "radagast", "saroumane", "iron man", "tony stark", "captain america", "avangers", "steve rogers", "thor", "hulk", "bruce banner", "black widow", "natasha romanoff", "spider man", "peter parker", "black panther", "t'challa", "captain marvel", "carole denvers", "ant-man", "scott lang", "doctor strange", "stephen strange", "star-lord", "peter quill", "thanos", "deadpool", "wade wilson", "wolverine", "logan", "dardevil", "matt murdock", "le fauve", "hank mccoy", "luke cage", "drax", "vision", "groot", "colossus", "loki", "nick fury", "oeil-de-faucon", "ultron", "faucon", "pepper potts", "war machine", "jarvis", "stan lee", "sheild", "la chose", "la torche humaine", "mr fantastique", "la femme invisible", "iron fist", "tornade", "rocket racoon", "shang-chi", "ronin", "yondu", "bucky", "la guêpe", "cyclope", "wanda", "nébula", "gamora", "charles xavier", "phoenix", "superman", "clark kent", "batman", "bruce wayne", "justice league", "flash", "barry allen", "green arrow", "green lanter", "aquaman", "wonder woman", "superboy", "robin", "hourman", "wonder girl", "atom smasher", "loose cannon", "ultra boy", "big barda", "omac", "mary marvel", "lobo", "donna troy", "supergirl", "bizarro", "orion", "harley queen", "le joker", "power girl", "shazam", "damage"]
            return List 
        # Animés & Films            (18)
        elif player_choice_sub_menu == "18":
            List = ["yamato", "naruto", "sakura", "sasuke", "chôji", "ino", "shikamaru", "hinata", "kiba", "shino", "neji", "rock", "tenten", "konohamaru", "hashirama", "hiruzen", "tobirama", "danzô", "hiruzen", "jiraya", "orochimaru", "tsunade", "kakashi", "obito", "lin", "hanabi", "shisui", "sakumo", "inoichi", "hiashi", "shikaku", "shizune", "asuma", "gaï", "kurenai", "saï", "minato", "itahci", "kabuto", "madara", "kushina", "hokage", "mizukage", "raikage", "kazekage", "tsuchikage", "killer bee", "suigetsu", "karin", "jûgo", "temari", "kakurô", "gaara", "pain", "konan", "nagato", "yahiko", "kisame", "hidan", "zetsu", "deidara", "sasori", "kakuzu", "ichibi", "nibi", "sanbi", "yonbi", "gobi", "rokubi", "nanabi", "hachibi", "kyûbi", "kurama", "boruto", "sarada", "mitsuki", "anko", "kinshiki", "shinki", "metal", "katasuke", "sukea", "kawaki", "denki", "namida", "sumire", "iwabee", "wasabi", "kagura", "urashiki", "sekiei", "akkun", "tosaka", "kuu", "kokuyou", "kakou", "koji", "delta", "mugino", "isshiki", "code", "boro", "shojoji", "momoshiki", "gon", "kirua", "kurapika", "leolio", "hisoka", "beans", "biscuit", "irumi", "kaito", "morau", "pamû", "satotsu", "jin", "mito", "netero", "meruem", "neferupito", "shaupfufu", "montutyupi", "koruto", "karuto", "zeno", "silva", "sharnalk", "kuroro", "nobunaga", "feitan", "machi", "phinks", "franklin", "shizuku", "bonorenof", "pakunoda", "zushi", "mizaisutomu", "parisuton", "piyon", "kanzai", "chiidoru", "botobai", "geru", "kurukku", "ginta", "eren", "mikasa", "armin", "grisha", "levi", "sasha", "hans", "jean", "annie", "reiner", "christa", "erwin", "ymir", "marco", "mina", "daris", "keith", "bertolt", "gaby", "titan assaillant", "titan colossal", "titan mâchoire", "titan bestial", "titan cuirassé", "titan marteau d'arme", "titan charrette", "titan féminin", "titan originel", "sieg", "historia", "nezu", "recovery girl", "numéro13", "hound dog", "all might", "aizawa", "ectoplasm", "gran torino", "yuga", "mina", "tsuyu", "tenya", "ochaco", "mashirao", "denki", "eijiro", "koji", "rikido", "mezo", "kyoka", "hanta", "fumikage", "shoto", "toru", "katsuki", "izuku", "minoru", "momo", "uraraka", "kaminari", "kirishima", "shoji", "sero", "tokoyami", "todoroki", "bakugo", "midoriya", "mineta", "tetsutetsu", "neito", "mirio", "nejire", "tamaki", "hatsume", "inasa", "eri", "brainless", "stain", "all for one", "hawks", "shigaraki", "himiko", "dabi", "muscular", "moonfish", "kurogiri", "nana", "nighteye", "eraser head", "cementos", "fat gum", "ryukyu", "dieu sylvetre", "gang orca", "endeavor", "best jeanist", "edgeshot", "mante lady", "jogo", "hanami", "mahito", "kechizu", "eso", "sukuna", "junpei", "suguru", "nanami", "aoi", "noritoshi", "momo", "mai", "kasumi", "ultimate mechamaru", "gakuganji", "maki", "toge", "panda", "yuji", "megumi", "nobara", "masamichi", "satoru", "gojo", "sheko", "akari", "sôma", "erina", "yuki", "ryôko", "satoshi", "hisako", "ikumi", "takumi", "isami", "alice", "megumi", "jôichirô", "kojirô", "dôjima", "shun", "zenji", "fumio", "senzaemon", "hinako", "ryô", "mayumi", "fuyumi", "akira", "jun", "miyoko", "daigo", "shôji", "kanichi", "eishi", "terunori", "nene", "momo", "tôsuke", "nakiri", "yukihira", "aldini", "shinomiya", "blanche neige", "cendrillon", "aurore", "ariel", "belle", "jasmine", "pocahontas", "mulan", "tiana", "raiponce", "merida", "elsa", "anna", "vaiana", "sirius", "black", "harry", "potter", "hermione", "granger", "voldemort", "drago", "malfoy", "severus", "rogue", "albus", "dumbledore", "ron", "weasley", "rubeus", "hagrid", "dobby", "luna", "lovegood", "minerva", "mcgonagall", "bellatrix", "lestrange", "neville", "londubat", "ginny", "remus", "lupin", "dolores", "ombrage", "peter", "pettigrow", "fleur", "delacour", "hedwige", "choixpeau", "james", "mimi", "geignarde", "lucius", "seamus", "sibylle", "lily", "fred", "alastor", "maugrey", "narcissa", "dudley", "argus", "rusard", "lavande", "george", "cedric", "diggory", "anakin", "skywalker", "dark vador", "padmé", "amidala", "r2-d2", "c-3po", "qui-gon", "jinn", "jar jar", "obi-wan", "kenobi", "yoda", "dark maul", "boba fett", "jango fett", "dooku", "sheev", "palpatine", "dark sidious", "luke", "leia", "han", "solo", "chewbacca", "jabba", "rey", "finn", "ben", "kylo ren", "gandalf", "aragorn", "frodon", "gollum", "legolas", "arwen", "sauron", "bilbon", "sacquet", "galadriel", "éowyn", "nazgûl", "peregrin", "éomer", "radagast", "saroumane", "iron man", "tony stark", "captain america", "avangers", "steve rogers", "thor", "hulk", "bruce banner", "black widow", "natasha romanoff", "spider man", "peter parker", "black panther", "t'challa", "captain marvel", "carole denvers", "ant-man", "scott lang", "doctor strange", "stephen strange", "star-lord", "peter quill", "thanos", "deadpool", "wade wilson", "wolverine", "logan", "dardevil", "matt murdock", "le fauve", "hank mccoy", "luke cage", "drax", "vision", "groot", "colossus", "loki", "nick fury", "oeil-de-faucon", "ultron", "faucon", "pepper potts", "war machine", "jarvis", "stan lee", "sheild", "la chose", "la torche humaine", "mr fantastique", "la femme invisible", "iron fist", "tornade", "rocket racoon", "shang-chi", "ronin", "yondu", "bucky", "la guêpe", "cyclope", "wanda", "nébula", "gamora", "charles xavier", "phoenix", "superman", "clark kent", "batman", "bruce wayne", "justice league", "flash", "barry allen", "green arrow", "green lanter", "aquaman", "wonder woman", "superboy", "robin", "hourman", "wonder girl", "atom smasher", "loose cannon", "ultra boy", "big barda", "omac", "mary marvel", "lobo", "donna troy", "supergirl", "bizarro", "orion", "harley queen", "le joker", "power girl", "shazam", "damage"]
            return List 

    # 4 - JEUX VIDÉOS
    elif choice_menu == "4":
        # Pokédex 1ère Gen          (1)
        if player_choice_sub_menu == "1":
            List = ["bulbizarre", "herbizarre", "florizarre", "salamèche", "reptincel", "dracaufeu", "carapuce", "carabaffe", "tortank", "chenipan", "chrysacier", "papilusion", "aspicot", "coconfort", "dardargnan", "roucool", "roucoups", "roucarnage", "rattata", "rattatac", "piafabec", "rapasdepic", "abo", "arbok", "pikachu", "raichu", "sabelette", "sablaireau", "nidoran", "nidorina", "nidoqueen", "nidorino", "nidoking", "mélofée", "mélodelfe", "goupix", "feunard", "rondoudou", "grodoudou", "nosferapti", "nosferalto", "mystherbe", "ortide", "rafflesia", "paras", "parasect", "mimitoss", "aéromite", "taupiqueur", "triopikeur", "miaouss", "persian", "psykokwak", "akwakwak", "férosinge", "colossinge", "caninos", "arcanin", "ptitard", "têtarte", "tartard", "abra", "kadabra", "alakazam", "machoc", "machopeur", "mackogneur", "chétiflor", "boustiflor", "empiflor", "tentacool", "tentacruel", "racaillou", "gravalanch", "grolem", "ponyta", "galopa", "ramoloss", "flagadoss", "magnéti", "magneton", "canarticho", "doduo", "dodrio", "otaria", "lamantine", "tadmorv", "grotadmorv", "kokiyas", "crustabri", "fantominus", "spectrum", "ectoplasma", "onix", "soporifik", "hypnomade", "krabby", "krabboss", "voltorbe", "électrode", "noeufnoeuf", "noadkoko", "osselait", "ossatueur", "kicklee", "tygnon", "excelangue", "smogo", "smogogo", "rhinocorne", "rhinoféros", "leveinard", "saquedeuneu", "kangourex", "hypotrempe", "hypocéan", "poissirène", "poissoroy", "stari", "staross", "m.mime", "insécateur", "lippoutou", "élektek", "magmar", "scarabrute", "tauros", "magicarpe", "léviator", "lokhlass", "métamorph", "évoli", "aquali", "voltali", "pyroli", "porygon", "amonista", "amonistar", "kabuto", "kabutops", "ptéra", "ronflex", "artikodin", "élechtor", "sulfura", "minidraco", "draco", "dracolosse", "mewtwo", "mew"]
            return List
        # Pokédex 2ème Gen          (2)
        elif player_choice_sub_menu == "2":
            List = ["germignon", "macronium", "méganium", "héricendre", "feurisson", "typhlosion", "kaiminus", "crocodil", "aligatueur", "fouinette", "fouinard", "hoothoot", "noarfang", "coxy", "coxyclaque", "mimigal", "migalos", "nostenfer", "loupio", "lanturn", "pichu", "mélo", "toudoudou", "togepi", "togetic", "natu", "xatu", "wattouat", "lainergie", "pharamp", "joliflor", "marill", "azumarill", "simularbre", "tarpaud", "granivol", "floravol", "cotovol", "capumain", "tournegrin", "héliatronc", "yanma", "axoloto", "maraiste", "mentali", "noctali", "cornèbre", "roigada", "feuforêve", "zarbi", "qulbutoké", "girafarig", "pomdepik", "foretress", "insolourdo", "scorplane", "steelix", "snubbull", "granbull", "qwilfish", "cizayox", "caratroc", "scarhino", "farfuret", "teddiursa", "ursaring", "limagma", "volcaropod", "marcacrin", "cochignon", "corayon", "rémoraid", "octillery", "cadoizo", "démanta", "airmure", "malosse", "démolosse", "hyporoi", "phanpy", "donphan", "porygon2", "cerfrousse", "queulorior", "debugant", "kapoera", "lippouti", "élekid", "magby", "écrémeuh", "leuphorie", "raikou", "entei", "suicune", "embrylex", "ymphect", "tyranocif", "lugia", "ho-oh", "celebi"]
            return List
        # Pokédex 3ème Gen          (3)
        elif player_choice_sub_menu == "3":
            List = ["arcko", "massko", "jungko", "poussifeu", "galifeu", "braségali", "gobou", "flobio", "laggron", "medhyèna", "grahyèna", "zigzaton", "linéon", "chenipotte", "armulys", "charmillon", "blindalys", "papinox", "nénupiot", "lombre", "ludicolo", "grainipiot", "pifeuil", "tengalice", "nirondelle", "hélédelle", "goélise", "békipan", "tarsal", "kirlia", "gardevoir", "arakdo", "maskadra", "balignon", "chapignon", "parecool", "vigoroth", "monaflémit", "ningale", "ninjask", "munja", "chuchmur", "ramboum", "brouhabam", "makhuita", "hariyama", "azurill", "tarinor", "skitty", "delcatty", "ténéfi", "mysdibule", "galekid", "galegon", "galeking", "méditikka", "charmina", "dynavolt", "élécsprint", "posipi", "négapi", "muciole", "lumivole", "rosélia", "gloupti", "avaltout", "carvanha", "sharpedo", "wailmer", "wailord", "chamallot", "camérupt", "chartor", "spoink", "groret", "spinda", "kraknoix", "vibranif", "libégon", "cacturne", "tylton", "altaria", "mangriff", "séviper", "séléroc", "solaroc", "barloche", "barbicha", "écrapince", "colhomard", "balbuto", "kaorine", "lilia", "vacilys", "anorith", "armaldo", "barpau", "milobellus", "morphéo", "kecleon", "polichombr", "branette", "skélénox", "téraclope", "tropius", "éoko", "absol", "okéoké", "stalgamin", "oniglali", "obalie", "phogleur", "kaimorse", "coquiperl", "serpang", "rosabyss", "relicanth", "lovdisc", "draby", "drackhaus", "drattak", "terhal", "métang", "métalosse", "regirock", "regice", "registeel"," latias", "latios", "kyogre", "groudon", "rayquaza", "jirachi", "deoxys"] 
            return List
        # Pokédex 4ème Gen          (4)
        elif player_choice_sub_menu == "4":
            List = ["tortipouss", "boskara", "torterra", "ouisticram", "chimpenfeu", "simiabraz", "tiplouf", "prinplouf", "pingoléon", "étourmi", "étourvol", "étouraptor", "keunotor", "castorno", "crikzik", "mélokrik", "lixy", "luxio", "luxray", "rozbouton", "roserade", "kranidos", "chrakos", "dinoclier", "bastiodon", "cheniti", "cheniselle", "papilord", "apitrini", "apireine", "pachirisu", "mustébouée", "mustéflott", "ceribou", "ceriflor", "sancoki", "tritosor", "capidextre", "baudrive", "grodrive", "laporeille", "lockpin", "magirêve", "corboss", "chaglam", "chaffeurx", "korillon", "moufouette", "moufflair", "archéomire", "archéodong", "manzaï", "mime jr.", "ptiravi", "pijako", "spiritomb", "griknot", "carmache", "carchacrok", "goinfrex", "riolu", "lucario", "hippopotas", "hippodocus", "rapion", "drascore", "cradopaud", "coatox", "vortente", "écayon", "luminéon", "babimanta", "blizzi", "blizzaroi", "dimoret", "magnézone", "coudlangue", "rhinastoc", "bouldeneu", "élekable", "maganon", "togekiss", "yanmega", "phyllali", "givrali", "scorvol", "mammochon", "porygon-z", "gallame", "tarinorme", "noctunoir", "momartik", "motisma", "créhelf", "créfollet", "créfadet", "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia", "phione", "manaphy", "darkrai", "shaymin", "arceus"]
            return List
        # Tous les Pokédex          (5)
        elif player_choice_sub_menu == "5":
            List = ["bulbizarre", "herbizarre", "florizarre", "salamèche", "reptincel", "dracaufeu", "carapuce", "carabaffe", "tortank", "chenipan", "chrysacier", "papilusion", "aspicot", "coconfort", "dardargnan", "roucool", "roucoups", "roucarnage", "rattata", "rattatac", "piafabec", "rapasdepic", "abo", "arbok", "pikachu", "raichu", "sabelette", "sablaireau", "nidoran", "nidorina", "nidoqueen", "nidorino", "nidoking", "mélofée", "mélodelfe", "goupix", "feunard", "rondoudou", "grodoudou", "nosferapti", "nosferalto", "mystherbe", "ortide", "rafflesia", "paras", "parasect", "mimitoss", "aéromite", "taupiqueur", "triopikeur", "miaouss", "persian", "psykokwak", "akwakwak", "férosinge", "colossinge", "caninos", "arcanin", "ptitard", "têtarte", "tartard", "abra", "kadabra", "alakazam", "machoc", "machopeur", "mackogneur", "chétiflor", "boustiflor", "empiflor", "tentacool", "tentacruel", "racaillou", "gravalanch", "grolem", "ponyta", "galopa", "ramoloss", "flagadoss", "magnéti", "magneton", "canarticho", "doduo", "dodrio", "otaria", "lamantine", "tadmorv", "grotadmorv", "kokiyas", "crustabri", "fantominus", "spectrum", "ectoplasma", "onix", "soporifik", "hypnomade", "krabby", "krabboss", "voltorbe", "électrode", "noeufnoeuf", "noadkoko", "osselait", "ossatueur", "kicklee", "tygnon", "excelangue", "smogo", "smogogo", "rhinocorne", "rhinoféros", "leveinard", "saquedeuneu", "kangourex", "hypotrempe", "hypocéan", "poissirène", "poissoroy", "stari", "staross", "m.mime", "insécateur", "lippoutou", "élektek", "magmar", "scarabrute", "tauros", "magicarpe", "léviator", "lokhlass", "métamorph", "évoli", "aquali", "voltali", "pyroli", "porygon", "amonista", "amonistar", "kabuto", "kabutops", "ptéra", "ronflex", "artikodin", "élechtor", "sulfura", "minidraco", "draco", "dracolosse", "mewtwo", "mew", "germignon", "macronium", "méganium", "héricendre", "feurisson", "typhlosion", "kaiminus", "crocodil", "aligatueur", "fouinette", "fouinard", "hoothoot", "noarfang", "coxy", "coxyclaque", "mimigal", "migalos", "nostenfer", "loupio", "lanturn", "pichu", "mélo", "toudoudou", "togepi", "togetic", "natu", "xatu", "wattouat", "lainergie", "pharamp", "joliflor", "marill", "azumarill", "simularbre", "tarpaud", "granivol", "floravol", "cotovol", "capumain", "tournegrin", "héliatronc", "yanma", "axoloto", "maraiste", "mentali", "noctali", "cornèbre", "roigada", "feuforêve", "zarbi", "qulbutoké", "girafarig", "pomdepik", "foretress", "insolourdo", "scorplane", "steelix", "snubbull", "granbull", "qwilfish", "cizayox", "caratroc", "scarhino", "farfuret", "teddiursa", "ursaring", "limagma", "volcaropod", "marcacrin", "cochignon", "corayon", "rémoraid", "octillery", "cadoizo", "démanta", "airmure", "malosse", "démolosse", "hyporoi", "phanpy", "donphan", "porygon2", "cerfrousse", "queulorior", "debugant", "kapoera", "lippouti", "élekid", "magby", "écrémeuh", "leuphorie", "raikou", "entei", "suicune", "embrylex", "ymphect", "tyranocif", "lugia", "ho-oh", "celebi", "arcko", "massko", "jungko", "poussifeu", "galifeu", "braségali", "gobou", "flobio", "laggron", "medhyèna", "grahyèna", "zigzaton", "linéon", "chenipotte", "armulys", "charmillon", "blindalys", "papinox", "nénupiot", "lombre", "ludicolo", "grainipiot", "pifeuil", "tengalice", "nirondelle", "hélédelle", "goélise", "békipan", "tarsal", "kirlia", "gardevoir", "arakdo", "maskadra", "balignon", "chapignon", "parecool", "vigoroth", "monaflémit", "ningale", "ninjask", "munja", "chuchmur", "ramboum", "brouhabam", "makhuita", "hariyama", "azurill", "tarinor", "skitty", "delcatty", "ténéfi", "mysdibule", "galekid", "galegon", "galeking", "méditikka", "charmina", "dynavolt", "élécsprint", "posipi", "négapi", "muciole", "lumivole", "rosélia", "gloupti", "avaltout", "carvanha", "sharpedo", "wailmer", "wailord", "chamallot", "camérupt", "chartor", "spoink", "groret", "spinda", "kraknoix", "vibranif", "libégon", "cacturne", "tylton", "altaria", "mangriff", "séviper", "séléroc", "solaroc", "barloche", "barbicha", "écrapince", "colhomard", "balbuto", "kaorine", "lilia", "vacilys", "anorith", "armaldo", "barpau", "milobellus", "morphéo", "kecleon", "polichombr", "branette", "skélénox", "téraclope", "tropius", "éoko", "absol", "okéoké", "stalgamin", "oniglali", "obalie", "phogleur", "kaimorse", "coquiperl", "serpang", "rosabyss", "relicanth", "lovdisc", "draby", "drackhaus", "drattak", "terhal", "métang", "métalosse", "regirock", "regice", "registeel"," latias", "latios", "kyogre", "groudon", "rayquaza", "jirachi", "deoxys", "tortipouss", "boskara", "torterra", "ouisticram", "chimpenfeu", "simiabraz", "tiplouf", "prinplouf", "pingoléon", "étourmi", "étourvol", "étouraptor", "keunotor", "castorno", "crikzik", "mélokrik", "lixy", "luxio", "luxray", "rozbouton", "roserade", "kranidos", "chrakos", "dinoclier", "bastiodon", "cheniti", "cheniselle", "papilord", "apitrini", "apireine", "pachirisu", "mustébouée", "mustéflott", "ceribou", "ceriflor", "sancoki", "tritosor", "capidextre", "baudrive", "grodrive", "laporeille", "lockpin", "magirêve", "corboss", "chaglam", "chaffeurx", "korillon", "moufouette", "moufflair", "archéomire", "archéodong", "manzaï", "mime jr.", "ptiravi", "pijako", "spiritomb", "griknot", "carmache", "carchacrok", "goinfrex", "riolu", "lucario", "hippopotas", "hippodocus", "rapion", "drascore", "cradopaud", "coatox", "vortente", "écayon", "luminéon", "babimanta", "blizzi", "blizzaroi", "dimoret", "magnézone", "coudlangue", "rhinastoc", "bouldeneu", "élekable", "maganon", "togekiss", "yanmega", "phyllali", "givrali", "scorvol", "mammochon", "porygon-z", "gallame", "tarinorme", "noctunoir", "momartik", "motisma", "créhelf", "créfollet", "créfadet", "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia", "phione", "manaphy", "darkrai", "shaymin", "arceus"]
            return List
        # Nom Jeux Vidéos           (6)
        elif player_choice_sub_menu == "6":
            List = ["minecraft", "grand theft auto", "tetris", "fortnite", "world of warcraft", "red dead redemption", "the legend of zelda", "league of legends", "pac-man", "final fantasy", "the elder scrolls", "pubg", "animal crossing", "pokémon", "wii sports", "super mario bros", "halo", "the last of us", "dark souls", "street fighter", "mario kart", "the witcher", "half-life", "cyberpunk", "call of duty", "assassin's creed", "roblox", "space invaders", "diablo", "counter-srike", "resident evil", "tomb raider", "uncharted", "earthstone", "far cry", "albion", "warms", "around the word"]
            return List

    # 666 - Easter Egg
    elif choice_menu == "666":
        List = ["minecraft", "grand theft auto", "tetris", "fortnite", "world of warcraft", "red dead redemption", "the legend of zelda", "league of legends", "pac-man", "final fantasy", "the elder scrolls", "pubg", "animal crossing", "pokémon", "wii sports", "super mario bros", "halo", "the last of us", "dark souls", "street fighter", "mario kart", "the witcher", "half-life", "cyberpunk", "call of duty", "assassin's creed", "roblox", "space invaders", "diablo", "counter-srike", "resident evil", "tomb raider", "uncharted", "earthstone", "far cry", "albion", "warms", "around the word", "lit", "bus", "bol", "sac","ado", "age", "ame", "art", "bar", "bio", "bec", "boa", "bob", "bon", "cul", "cil", "dix", "écu", "fer", "feu", "ère", "été", "fil", "gaz", "ici", "île", "jeu", "lac", "lui", "mai", "mec", "mur", "nid", "nez", "pas", "pet", "psy", "rat", "rue", "sel", "sec", "ski", "sol", "tas", "web", "zoo", "mie", "mal", "les", "des", "robe", "jupe", "pull", "jour", "rose", "bleu", "gros", "beau", "nuit", "lune", "lampe", "vert", "vers", "lire", "vélo", "moto", "café", "amis", "acné", "amer", "aide", "amie", "bain", "bide", "beuh", "banc", "bide", "cuir", "dans", "elle", "écus", "face", "faux", "geek", "cave", "golf", "gros", "glue", "haut", "jeux", "lave", "neuf", "note", "noix", "peau", "rêve", "sage", "sauf", "tome", "zoom", "stylo", "règle", "rouge", "jaune", "piano", "mince", "tasse", "belle", "photo", "lapin", "carte", "cadre", "prise", "porte", "verre", "livre", "vache", "table", "avion", "train", "arbre", "fleur", "petit", "grand", "métro", "accro", "actif", "aucun", "bille", "carpe", "crabe", "cycle", "draps", "drôle", "fesse", "fable", "gazon", "gosse", "igloo", "malin", "mamie", "noire", "pages", "puits", "quand", "repos", "sabre", "short", "tueur", "zèbre", "cahier", "soleil", "violet", "valise", "violon", "cheval", "animal", "crayon", "montre", "maison", "douche", "mouche", "chaise", "chèvre", "mouton", "cochon", "fleuve", "canapé", "gâteau", "souris", "action", "acides", "adepte", "balcon", "banane", "ananas", "regard", "bonnet", "cantal", "copine", "copain", "doutes", "facile", "espèce", "famine", "frigos", "froide", "hanche", "kebabs", "lacune", "menace", "navale", "patron", "paysan", "racine", "raisin", "sabres", "trente", "whisky", "zombie", "george washington", "john adams", "thomas jefferson", "james madison", "james monroe", "john quincy adams", "andrew jackson", "martin van buren", "william henry harrison", "john tyler", "james polk", "zachary taylor", "millard fillmore", "franklin pierce", "james buchanan", "abraham lincoln", "andrew johnson", "ulysses grant", "rutherford hayes", "james garfield", "chester arthur", "grover cleveland", "benjamin harisson", "william mckinley", "theodore roosevelt", "william taft", "woodrow wilson", "warren harding", "calvin coolidge", "herbert hoover", "franklin delano roosevelt", "harry truman", "dwight eisenhower", "john fitzgerald kennedy", "lyndon johnson", "richard nixon", "gerald ford", "jimmy carter", "ronald reagan", "george h w bush", "bill clinton", "george w bush", "barack obama", "donald trump", "joe biden", "abou dabi", "abuja", "accra", "achgabat", "addis-abeba", "alger", "alofi", "amman", "amsterdam", "andorre-la-vieille", "ankara", "antananarivo", "apia", "asmara", "asuncion", "athènes", "avarua", "bagdad", "bakou", "bamako", "bandar seri begawan", "bangkok",  "bangui", "banjul", "basseterre", "belgrade", "belmopan", "berlin", "berne", "beyrouth", "bichkek", "bissau", "bloemfontein", "bogota", "brasilia", "bratislava", "brazzaville", "bridgetown", "bruxelles", "bucarest", "budapest", "buenos aires", "le caire", "canberra", "le cap", "caracas", "castries", "chisinau", "sri jayawardenapura kotte", "conakry", "copenhague", "dakar", "damas", "delap-uliga-darrit", "dacca", "dili", "djibouti", "djouba", "dodoma", "doha", "douchanbé", "dublin", "erevan", "freetown", "funafuti", "gaborone", "georgetown", "gitega", "guatemala", "hanoï", "harare", "la havane", "helsinki", "honiara", "islamabad", "jakarta", "jérusalem", "kaboul", "kampala", "katmandou", "khartoum", "kiev", "kigali", "kingston", "kingstown", "kinshasa", "melekeok", "koweït", "kuala lumpur", "libreville", "lilongwe", "lima", "lisbonne", "ljubljana", "lomé", "londres", "luanda", "lusaka", "luxembourg", "madrid", "malabo", "malé", "managua", "manama", "manille", "maputo", "mascate", "maseru", "mbabane", "mexico", "minsk", "mogadiscio", "monaco", "monrovia", "montevideo", "moroni", "moscou", "mairobi", "massau", "naypyidaw", "n'djaména", "new delhi", "niamey", "nicosie", "nouakchott", "noursoultan", "nuku'alofa", "oslo", "ottawa", "ouagadougou", "oulan-bator", "palikir", "panama", "paramaribo", "paris", "la paz", "pékin", "phnom penh", "podgorica", "port moresby", "port-au-prince", "port-d'espagne", "port-louis", "porto-novo", "port-vila", "prague", "praia", "pretoria", "putrajaya", "pyongyang", "quito", "rabat", "reykjavik", "riga", "riyad", "rome", "roseau", "saint john's", "saint-domingue", "saint-georges", "saint-marin", "san josé", "san salvador", "sanaa", "santiago", "são tomé" "sarajevo", "séoul", "singapour", "skopje", "sofia", "stockholm", "sucre" , "suva", "tachkent", "tallinn", "tbilissi", "tegucigalpa", "téhéran", "thimphou", "tirana", "tokyo", "tripoli", "tunis", "vaduz", "la valette", "varsovie", "cité du vatican", "victoria", "vienne", "vientiane", "vilnius", "washington d.c", "wellington", "windhoek", "yamoussoukro", "yaoundé", "yaren", "zagreb", "afrique du sud", "afghanistan", "albanie", "algérie", "allemagne", "andorre", "angola", "antigua-et-barbuda", "arabie saoudite", "argentine", "arménie", "australie", "autriche", "azerbaïdjan", "bahamas", "bahreïn", "bangladesh", "barbade", "belgique", "belize", "bénin", "bhoutan", "biélorussie", "birmanie", "bolivie", "bosnie-herzégovine", "botswana", "brésil", "brunei", "bulgarie", "burkina faso", "burundi", "cambodge", "cameroun", "canada", "cap-vert", "république centrafricaine", "chili", "chine", "chypre", "colombie", "comores", "république du congo", "république démocratique du congo", "îles cook", "corée du nord", "corée du sud", "costa rica", "côte d'ivoire", "croatie", "cuba", "danemark", "djibouti", "république dominicaine", "dominique", "égypte", "émirats arabes unis", "équateur", "érythrée", "espagne", "estonie", "eswatini", "états-unis", "éthiopie", "fidji", "finlande", "france", "gabon", "gambie", "géorgie", "ghana", "grèce", "grenade", "guatemala", "guinée", "guinée-bissau", "guinée équatoriale", "guyana", "haïti", "honduras", "hongrie", "inde", "indonésie", "irak", "iran", "irlande", "islande", "israël", "italie", "jamaïque", "japon", "jordanie", "kazakhstan", "kenya", "kirghizistan", "kiribati", "koweït", "laos", "lesotho", "lettonie", "liban", "liberia", "libye", "liechtenstein", "lituanie", "luxembourg", "macédoine du nord", "madagascar", "malaisie", "malawi", "maldives", "mali", "malte", "maroc", "îles marshall", "maurice", "mauritanie", "mexique", "micronésie", "moldavie", "monaco", "mongolie", "monténégro", "mozambique", "namibie", "nauru", "népal", "nicaragua", "niger", "nigeria", "niue", "norvège", "nouvelle-zélande", "oman", "ouganda", "ouzbékistan", "pakistan", "palaos", "palestine", "panamá", "papouasie-nouvelle-guinée", "paraguay", "pays-bas", "pérou", "philippines", "pologne", "portugal", "qatar", "roumanie", "royaume-uni", "russie", "rwanda", "saint-christophe-et-niévès", "saint-marin", "saint-vincent-et-les grenadines", "sainte-lucie", "îles salomon", "salvador", "samoa", "são tomé-et-principe", "sénégal", "serbie", "seychelles", "sierra leone", "singapour", "slovaquie", "slovénie", "somalie", "soudan", "soudan du sud", "sri lanka", "suède", "suisse", "suriname", "syrie", "tadjikistan", "tanzanie", "tchad", "république tchèque", "thaïlande", "timor oriental", "togo", "tonga", "trinité-et-tobago", "tunisie", "turkménistan", "turquie", "tuvalu", "ukraine", "uruguay", "vanuatu", "vatican", "venezuela", "viêt nam", "yémen", "zambie", "zimbabwe", "yamato", "naruto", "sakura", "sasuke", "chôji", "ino", "shikamaru", "hinata", "kiba", "shino", "neji", "rock", "tenten", "konohamaru", "hashirama", "hiruzen", "tobirama", "danzô", "hiruzen", "jiraya", "orochimaru", "tsunade", "kakashi", "obito", "lin", "hanabi", "shisui", "sakumo", "inoichi", "hiashi", "shikaku", "shizune", "asuma", "gaï", "kurenai", "saï", "minato", "itahci", "kabuto", "madara", "kushina", "hokage", "mizukage", "raikage", "kazekage", "tsuchikage", "killer bee", "suigetsu", "karin", "jûgo", "temari", "kakurô", "gaara", "pain", "konan", "nagato", "yahiko", "kisame", "hidan", "zetsu", "deidara", "sasori", "kakuzu", "ichibi", "nibi", "sanbi", "yonbi", "gobi", "rokubi", "nanabi", "hachibi", "kyûbi", "kurama", "boruto", "sarada", "mitsuki", "anko", "kinshiki", "shinki", "metal", "katasuke", "sukea", "kawaki", "denki", "namida", "sumire", "iwabee", "wasabi", "kagura", "urashiki", "sekiei", "akkun", "tosaka", "kuu", "kokuyou", "kakou", "koji", "delta", "mugino", "isshiki", "code", "boro", "shojoji", "momoshiki", "gon", "kirua", "kurapika", "leolio", "hisoka", "beans", "biscuit", "irumi", "kaito", "morau", "pamû", "satotsu", "jin", "mito", "netero", "meruem", "neferupito", "shaupfufu", "montutyupi", "koruto", "karuto", "zeno", "silva", "sharnalk", "kuroro", "nobunaga", "feitan", "machi", "phinks", "franklin", "shizuku", "bonorenof", "pakunoda", "zushi", "mizaisutomu", "parisuton", "piyon", "kanzai", "chiidoru", "botobai", "geru", "kurukku", "ginta", "eren", "mikasa", "armin", "grisha", "levi", "sasha", "hans", "jean", "annie", "reiner", "christa", "erwin", "ymir", "marco", "mina", "daris", "keith", "bertolt", "gaby", "titan assaillant", "titan colossal", "titan mâchoire", "titan bestial", "titan cuirassé", "titan marteau d'arme", "titan charrette", "titan féminin", "titan originel", "sieg", "historia", "nezu", "recovery girl", "numéro13", "hound dog", "all might", "aizawa", "ectoplasm", "gran torino", "yuga", "mina", "tsuyu", "tenya", "ochaco", "mashirao", "denki", "eijiro", "koji", "rikido", "mezo", "kyoka", "hanta", "fumikage", "shoto", "toru", "katsuki", "izuku", "minoru", "momo", "uraraka", "kaminari", "kirishima", "shoji", "sero", "tokoyami", "todoroki", "bakugo", "midoriya", "mineta", "tetsutetsu", "neito", "mirio", "nejire", "tamaki", "hatsume", "inasa", "eri", "brainless", "stain", "all for one", "hawks", "shigaraki", "himiko", "dabi", "muscular", "moonfish", "kurogiri", "nana", "nighteye", "eraser head", "cementos", "fat gum", "ryukyu", "dieu sylvetre", "gang orca", "endeavor", "best jeanist", "edgeshot", "mante lady", "jogo", "hanami", "mahito", "kechizu", "eso", "sukuna", "junpei", "suguru", "nanami", "aoi", "noritoshi", "momo", "mai", "kasumi", "ultimate mechamaru", "gakuganji", "maki", "toge", "panda", "yuji", "megumi", "nobara", "masamichi", "satoru", "gojo", "sheko", "akari", "sôma", "erina", "yuki", "ryôko", "satoshi", "hisako", "ikumi", "takumi", "isami", "alice", "megumi", "jôichirô", "kojirô", "dôjima", "shun", "zenji", "fumio", "senzaemon", "hinako", "ryô", "mayumi", "fuyumi", "akira", "jun", "miyoko", "daigo", "shôji", "kanichi", "eishi", "terunori", "nene", "momo", "tôsuke", "nakiri", "yukihira", "aldini", "shinomiya", "blanche neige", "cendrillon", "aurore", "ariel", "belle", "jasmine", "pocahontas", "mulan", "tiana", "raiponce", "merida", "elsa", "anna", "vaiana", "sirius", "black", "harry", "potter", "hermione", "granger", "voldemort", "drago", "malfoy", "severus", "rogue", "albus", "dumbledore", "ron", "weasley", "rubeus", "hagrid", "dobby", "luna", "lovegood", "minerva", "mcgonagall", "bellatrix", "lestrange", "neville", "londubat", "ginny", "remus", "lupin", "dolores", "ombrage", "peter", "pettigrow", "fleur", "delacour", "hedwige", "choixpeau", "james", "mimi", "geignarde", "lucius", "seamus", "sibylle", "lily", "fred", "alastor", "maugrey", "narcissa", "dudley", "argus", "rusard", "lavande", "george", "cedric", "diggory", "anakin", "skywalker", "dark vador", "padmé", "amidala", "r2-d2", "c-3po", "qui-gon", "jinn", "jar jar", "obi-wan", "kenobi", "yoda", "dark maul", "boba fett", "jango fett", "dooku", "sheev", "palpatine", "dark sidious", "luke", "leia", "han", "solo", "chewbacca", "jabba", "rey", "finn", "ben", "kylo ren", "gandalf", "aragorn", "frodon", "gollum", "legolas", "arwen", "sauron", "bilbon", "sacquet", "galadriel", "éowyn", "nazgûl", "peregrin", "éomer", "radagast", "saroumane", "iron man", "tony stark", "captain america", "avangers", "steve rogers", "thor", "hulk", "bruce banner", "black widow", "natasha romanoff", "spider man", "peter parker", "black panther", "t'challa", "captain marvel", "carole denvers", "ant-man", "scott lang", "doctor strange", "stephen strange", "star-lord", "peter quill", "thanos", "deadpool", "wade wilson", "wolverine", "logan", "dardevil", "matt murdock", "le fauve", "hank mccoy", "luke cage", "drax", "vision", "groot", "colossus", "loki", "nick fury", "oeil-de-faucon", "ultron", "faucon", "pepper potts", "war machine", "jarvis", "stan lee", "sheild", "la chose", "la torche humaine", "mr fantastique", "la femme invisible", "iron fist", "tornade", "rocket racoon", "shang-chi", "ronin", "yondu", "bucky", "la guêpe", "cyclope", "wanda", "nébula", "gamora", "charles xavier", "phoenix", "superman", "clark kent", "batman", "bruce wayne", "justice league", "flash", "barry allen", "green arrow", "green lanter", "aquaman", "wonder woman", "superboy", "robin", "hourman", "wonder girl", "atom smasher", "loose cannon", "ultra boy", "big barda", "omac", "mary marvel", "lobo", "donna troy", "supergirl", "bizarro", "orion", "harley queen", "le joker", "power girl", "shazam", "damage", "bulbizarre", "herbizarre", "florizarre", "salamèche", "reptincel", "dracaufeu", "carapuce", "carabaffe", "tortank", "chenipan", "chrysacier", "papilusion", "aspicot", "coconfort", "dardargnan", "roucool", "roucoups", "roucarnage", "rattata", "rattatac", "piafabec", "rapasdepic", "abo", "arbok", "pikachu", "raichu", "sabelette", "sablaireau", "nidoran", "nidorina", "nidoqueen", "nidorino", "nidoking", "mélofée", "mélodelfe", "goupix", "feunard", "rondoudou", "grodoudou", "nosferapti", "nosferalto", "mystherbe", "ortide", "rafflesia", "paras", "parasect", "mimitoss", "aéromite", "taupiqueur", "triopikeur", "miaouss", "persian", "psykokwak", "akwakwak", "férosinge", "colossinge", "caninos", "arcanin", "ptitard", "têtarte", "tartard", "abra", "kadabra", "alakazam", "machoc", "machopeur", "mackogneur", "chétiflor", "boustiflor", "empiflor", "tentacool", "tentacruel", "racaillou", "gravalanch", "grolem", "ponyta", "galopa", "ramoloss", "flagadoss", "magnéti", "magneton", "canarticho", "doduo", "dodrio", "otaria", "lamantine", "tadmorv", "grotadmorv", "kokiyas", "crustabri", "fantominus", "spectrum", "ectoplasma", "onix", "soporifik", "hypnomade", "krabby", "krabboss", "voltorbe", "électrode", "noeufnoeuf", "noadkoko", "osselait", "ossatueur", "kicklee", "tygnon", "excelangue", "smogo", "smogogo", "rhinocorne", "rhinoféros", "leveinard", "saquedeuneu", "kangourex", "hypotrempe", "hypocéan", "poissirène", "poissoroy", "stari", "staross", "m.mime", "insécateur", "lippoutou", "élektek", "magmar", "scarabrute", "tauros", "magicarpe", "léviator", "lokhlass", "métamorph", "évoli", "aquali", "voltali", "pyroli", "porygon", "amonista", "amonistar", "kabuto", "kabutops", "ptéra", "ronflex", "artikodin", "élechtor", "sulfura", "minidraco", "draco", "dracolosse", "mewtwo", "mew", "germignon", "macronium", "méganium", "héricendre", "feurisson", "typhlosion", "kaiminus", "crocodil", "aligatueur", "fouinette", "fouinard", "hoothoot", "noarfang", "coxy", "coxyclaque", "mimigal", "migalos", "nostenfer", "loupio", "lanturn", "pichu", "mélo", "toudoudou", "togepi", "togetic", "natu", "xatu", "wattouat", "lainergie", "pharamp", "joliflor", "marill", "azumarill", "simularbre", "tarpaud", "granivol", "floravol", "cotovol", "capumain", "tournegrin", "héliatronc", "yanma", "axoloto", "maraiste", "mentali", "noctali", "cornèbre", "roigada", "feuforêve", "zarbi", "qulbutoké", "girafarig", "pomdepik", "foretress", "insolourdo", "scorplane", "steelix", "snubbull", "granbull", "qwilfish", "cizayox", "caratroc", "scarhino", "farfuret", "teddiursa", "ursaring", "limagma", "volcaropod", "marcacrin", "cochignon", "corayon", "rémoraid", "octillery", "cadoizo", "démanta", "airmure", "malosse", "démolosse", "hyporoi", "phanpy", "donphan", "porygon2", "cerfrousse", "queulorior", "debugant", "kapoera", "lippouti", "élekid", "magby", "écrémeuh", "leuphorie", "raikou", "entei", "suicune", "embrylex", "ymphect", "tyranocif", "lugia", "ho-oh", "celebi", "arcko", "massko", "jungko", "poussifeu", "galifeu", "braségali", "gobou", "flobio", "laggron", "medhyèna", "grahyèna", "zigzaton", "linéon", "chenipotte", "armulys", "charmillon", "blindalys", "papinox", "nénupiot", "lombre", "ludicolo", "grainipiot", "pifeuil", "tengalice", "nirondelle", "hélédelle", "goélise", "békipan", "tarsal", "kirlia", "gardevoir", "arakdo", "maskadra", "balignon", "chapignon", "parecool", "vigoroth", "monaflémit", "ningale", "ninjask", "munja", "chuchmur", "ramboum", "brouhabam", "makhuita", "hariyama", "azurill", "tarinor", "skitty", "delcatty", "ténéfi", "mysdibule", "galekid", "galegon", "galeking", "méditikka", "charmina", "dynavolt", "élécsprint", "posipi", "négapi", "muciole", "lumivole", "rosélia", "gloupti", "avaltout", "carvanha", "sharpedo", "wailmer", "wailord", "chamallot", "camérupt", "chartor", "spoink", "groret", "spinda", "kraknoix", "vibranif", "libégon", "cacturne", "tylton", "altaria", "mangriff", "séviper", "séléroc", "solaroc", "barloche", "barbicha", "écrapince", "colhomard", "balbuto", "kaorine", "lilia", "vacilys", "anorith", "armaldo", "barpau", "milobellus", "morphéo", "kecleon", "polichombr", "branette", "skélénox", "téraclope", "tropius", "éoko", "absol", "okéoké", "stalgamin", "oniglali", "obalie", "phogleur", "kaimorse", "coquiperl", "serpang", "rosabyss", "relicanth", "lovdisc", "draby", "drackhaus", "drattak", "terhal", "métang", "métalosse", "regirock", "regice", "registeel"," latias", "latios", "kyogre", "groudon", "rayquaza", "jirachi", "deoxys", "tortipouss", "boskara", "torterra", "ouisticram", "chimpenfeu", "simiabraz", "tiplouf", "prinplouf", "pingoléon", "étourmi", "étourvol", "étouraptor", "keunotor", "castorno", "crikzik", "mélokrik", "lixy", "luxio", "luxray", "rozbouton", "roserade", "kranidos", "chrakos", "dinoclier", "bastiodon", "cheniti", "cheniselle", "papilord", "apitrini", "apireine", "pachirisu", "mustébouée", "mustéflott", "ceribou", "ceriflor", "sancoki", "tritosor", "capidextre", "baudrive", "grodrive", "laporeille", "lockpin", "magirêve", "corboss", "chaglam", "chaffeurx", "korillon", "moufouette", "moufflair", "archéomire", "archéodong", "manzaï", "mime jr.", "ptiravi", "pijako", "spiritomb", "griknot", "carmache", "carchacrok", "goinfrex", "riolu", "lucario", "hippopotas", "hippodocus", "rapion", "drascore", "cradopaud", "coatox", "vortente", "écayon", "luminéon", "babimanta", "blizzi", "blizzaroi", "dimoret", "magnézone", "coudlangue", "rhinastoc", "bouldeneu", "élekable", "maganon", "togekiss", "yanmega", "phyllali", "givrali", "scorvol", "mammochon", "porygon-z", "gallame", "tarinorme", "noctunoir", "momartik", "motisma", "créhelf", "créfollet", "créfadet", "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia", "phione", "manaphy", "darkrai", "shaymin", "arceus"]
        return List


# • SÉLECTIONS MOTS LISTE •
def words_selection(List):
    
    word1 = List[randint(0, len(List)-1)]
    List.remove (word1)
    word2 = List[randint(0, len(List)-1)]
    List.remove (word2)
    word3 = List[randint(0, len(List)-1)]
    List = [ word1, word2, word3 ]

    return word1, word2, word3


# • MOT SANS LETTRES DOUBLES ET MÉLANGÉ
def words_shuffle(words, game_display):

    # coller les mots + nouvelle liste
    affiche = "".join(words)
    new_list = list(affiche)  
    
    # supprimer les espaces, les points, les apostrophes et les tirets (du jeu)
    i = 0
    while i < len(new_list):
        if new_list[i] == "-":            
            new_list.remove("-")
        elif new_list[i] == " ":
            new_list.remove(" ")
        elif new_list[i] == ".":
            new_list.remove(".")
        elif new_list[i] == "'":
            new_list.remove("'")    
        else:
            i = i + 1

    # supp doublons
    final_list = []
    for i in new_list : 
        if i not in final_list: 
            final_list.append(i)
    
    # random les lettres de la nouvelle liste sans doublons
    random_letters = final_list
    random.shuffle(random_letters) 

    # affichage du jeu de la manche
    if game_display == "1":                     # abcd
        game = "".join(random_letters)
    elif game_display == "2":                   # a b c d
        game = " ".join(random_letters)
        
    return game   


# • MENU •
def game_menu(choice_menu):          

    # 1 - Classique  
    if choice_menu == "1":       
        print(style,'''
      MENU     
   
• Classique     1    --->    - 3 lettres                    1
• Monde         2            - 4 lettres                    2
• Personnages   3            - 5 lettres                    3
• Jeux Vidéo    4            - 6 lettres                    4
• Magasin       5            - 3 à 6 lettres                5
• Règles        6            
• Quitter       7            - Retour                       0
        ''', end_style)       
        return choice_with_no_bugg(["0", "1", "2", "3", "4", "5"])

    # 2 - Monde
    elif choice_menu == "2":      
        print(style,'''
      MENU

• Classique     1 
• Monde         2    --->    - Présidents USA               1  
• Personnages   3            - Capitales UE                 2
• Jeux Vidéo    4            - Pays UE                      3
• Magasin       5            - Capitales & Pays UE          4
• Règles        6            - Capitales Monde              5   
• Quitter       7            - Pays Monde                   6
                             - Capitales & Pays Monde       7 

                             - Retour                       0 
        ''', end_style)
        return choice_with_no_bugg(["0", "1", "2", "3", "4", "5", "6", "7"])
    
    # 3 - Personnages
    elif choice_menu == "3":      
        print(style ,'''
      MENU 

• Classique     1 
• Monde         2            •            ANIMÉ             •
• Personnages   3    --->    - Naruto                       1
• Jeux Vidéo    4            - Boruto                       2
• Magasin       5            - Naruto & Boruto              3
• Règles        5            - Hunter X Hunter              4
• Quitter       7            - L'Attaque des Titans         5
                             - My Hero Academia             6
                             - Jujutsu Kaisen               7 
                             - Food Wars                    8
                             - Tous les Animés              9
                                                         
                             •             FILM             •
                             - Princesses Disney            10
                             - Harry Potter                 11
                             - Star Wars                    12
                             - Seigneur Des Anneaux         13
                             - Héros Marvel                 14
                             - Héros DC                     15
                             - Héros Marvel & DC            16
                             - Tous les Films               17

                             - Animés & Films               18

                             - Retour                       0
        ''', end_style)
        return choice_with_no_bugg(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"])
    
    # 4 - Jeux Vidéos
    elif choice_menu == "4":      
        print(style,'''
      MENU     

• Classique     1 
• Monde         2
• Personnages   3            
• Jeux Vidéo    4    --->    - Pokédex 1ère Gen             1
• Magasin       5            - Pokédex 2ème Gen             2
• Règles        6            - Pokédex 3ème Gen             3          
• Quitter       7            - Pokédex 4ème Gen             4
                             - Tous les Pokédex             5

                             - Nom de Jeux Vidéos           6
                            
                             - Retour                       0 
        ''', end_style)
        return choice_with_no_bugg(["0", "1", "2", "3", "4", "5", "6"])

    # 5 - Shop
    elif choice_menu == "5":      
        print(style,'''
      MENU     

• Classique     1 
• Monde         2
• Personnages   3
• Jeux Vidéo    4            •            ACHATS            •
• Magasin       5    --->    - Première lettre     200 $    1
• Règles        6            - Dernière lettre     400 $    2           
• Quitter       7            - Double Points       500 $    3
                             - Double Cash         600 $    4

                             •            VENTES            •
                             - 10 Points           100 $    5   

                             - Victoire          5 000 $    6
                             
                             - Retour                       0
        ''', end_style)
        return choice_with_no_bugg(["0", "1", "2", "3", "4", "5", "6"])

    # 6 - Règles
    elif choice_menu == "6":      
        print(style,'''
      MENU     

• Classique     1 
• Monde         2
• Personnages   3
• Jeux Vidéo    4
• Magasin       5
• Règles        6    --->    Around the Word est un jeu simple.                   
• Quitter       7            
                             Le but du jeu est de trouver les 3
                             mots cachés de la manche.
                             
                             Une partie se déroule en 3 manches.

                             À chaque bonne réponse vous gagnez
                             des points et du cash. Servez-vous en
                             pour acheter des bonus dans le magasin
                             ou en partie. 

                             Arriverez-vous à sortir victorieux 
                                     de Around the Word ?  

                             - Retour                     0
        ''',end_style)
        return choice_with_no_bugg(["0"])

    # 7 - Quitter le jeu
    elif choice_menu == "7":  
        print(style,'''

                                         █████╗    ██████╗ ██╗███████╗███╗  ██╗████████╗ █████╗ ████████╗    █████╗ ██╗  ██╗ █████╗  █████╗  █████╗ ██╗
                                        ██╔══██╗   ██╔══██╗██║██╔════╝████╗ ██║╚══██╔══╝██╔══██╗╚══██╔══╝   ██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔══██╗██║
                                        ███████║   ██████╦╝██║█████╗  ██╔██╗██║   ██║   ██║  ██║   ██║      ██║  ╚═╝███████║███████║██║  ╚═╝███████║██║
                                        ██╔══██║   ██╔══██╗██║██╔══╝  ██║╚████║   ██║   ██║  ██║   ██║      ██║  ██╗██╔══██║██╔══██║██║  ██╗██╔══██║██║
                                        ██║  ██║   ██████╦╝██║███████╗██║ ╚███║   ██║   ╚█████╔╝   ██║      ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║  ██║███████╗
                                        ╚═╝  ╚═╝   ╚═════╝ ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝    ╚════╝    ╚═╝       ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝

        ''', end_style)
                

    # 666 - Easter Egg / Mode de jeu ~ENFER~
    elif choice_menu == "666":      
        print("\n""\n" "??? :", style_dieu + "Salut l'ami c'est moi, le créateur ...", end_style)
        input()
        print("\n" "Dieu :", style_dieu + "Tu t'es mis dans un sacré pétrin ...", end_style)
        input()
        print("\n" "Dieu :", style_dieu + "J'espère que tu as bien révisé, parce qu'ici tu ne peux rien choisir ...", end_style)
        input()
        print("\n" "Dieu :", style_dieu + "Eh bien, je te souhaite bonne chance et à bientôt.", end_style)
        input()
        print("\n" "Dieu :", style_dieu + "Du moins j'espère ... Mes amitiés à Satan.", end_style)
        input()
        print("\n" "Satan :", style_satan + "𝔥𝔲𝔪 .. 𝔮𝔲𝔢 𝔣𝔞𝔦𝔰 𝔱𝔲 𝔦𝔠𝔦 𝔥𝔲𝔪𝔞𝔦𝔫 ... 𝔱𝔲 𝔳𝔞𝔰 𝔪𝔬𝔲𝔯𝔦𝔯 !", end_style)
        input()
        print("\n" "Satan :", style_satan + "𝔰𝔦 𝔱𝔲 𝔞𝔰 𝔞𝔲 𝔪𝔬𝔦𝔫𝔰 7 𝔟𝔬𝔫𝔫𝔢𝔰 𝔯𝔢́𝔭𝔬𝔫𝔰𝔢𝔰, 𝔭𝔢𝔲𝔱 𝔢̂𝔱𝔯𝔢 𝔮𝔲𝔢 𝔧𝔢 𝔱𝔢 𝔩𝔞𝔦𝔰𝔰𝔢𝔯𝔞𝔦 𝔩𝔞 𝔳𝔦𝔢 𝔰𝔞𝔲𝔳𝔢 (𝔪𝔲𝔞𝔥𝔞𝔥𝔞𝔥)", end_style)
        print("\n""\n" "Le niveau secret", style_satan + "~ Enfer ~", end_style + "commence !" "\n")
        input()

# • CHOIX SANS BUGG •
def choice_with_no_bugg(list_menu):
    
    print("Entrez votre choix :") 
    sub_menu_choice = input(" → ")
    while True:
        if sub_menu_choice in list_menu:
            break
        else:
            i = 0
            while i < 1:
                print("\n" "Il y a une erreur, réessayez :")
                sub_menu_choice = input(" → ")
                if sub_menu_choice in list_menu:
                    i = i + 1
                else: 
                    i = 0
            if i == 1:
                break 

    return sub_menu_choice


# • AFFICHAGE DÉBUT & FIN •
def start_end(print_value, player_name):

    # 1 - Début partie
    if print_value == 1:
        print(WHITE,'''



                                       █████╗ ██████╗  █████╗ ██╗   ██╗███╗  ██╗██████╗    ████████╗██╗  ██╗███████╗    ██╗       ██╗ █████╗ ██████╗ ██████╗
                                      ██╔══██╗██╔══██╗██╔══██╗██║   ██║████╗ ██║██╔══██╗   ╚══██╔══╝██║  ██║██╔════╝    ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗
                                      ███████║██████╔╝██║  ██║██║   ██║██╔██╗██║██║  ██║      ██║   ███████║█████╗      ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║
                                      ██╔══██║██╔══██╗██║  ██║██║   ██║██║╚████║██║  ██║      ██║   ██╔══██║██╔══╝       ████╔═████║ ██║  ██║██╔══██╗██║  ██║
                                      ██║  ██║██║  ██║╚█████╔╝╚██████╔╝██║ ╚███║██████╔╝      ██║   ██║  ██║███████╗     ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝
                                      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚═╝  ╚══╝╚═════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝      ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝



        ''', RESET)

    # 2 - Fin Partie Victoire
    if print_value == 2:
        print(style)
        print("Félicitations", player_name, "vous avez finit le jeu !", end_style)
        input()
        print(WHITE,'''

                                                                ██╗   ██╗██╗ █████╗ ████████╗ █████╗ ██╗██████╗ ███████╗
                                                                ██║   ██║██║██╔══██╗╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝
                                                                ╚██╗ ██╔╝██║██║  ╚═╝   ██║   ██║  ██║██║██████╔╝█████╗
                                                                 ╚████╔╝ ██║██║  ██╗   ██║   ██║  ██║██║██╔══██╗██╔══╝
                                                                  ╚██╔╝  ██║╚█████╔╝   ██║   ╚█████╔╝██║██║  ██║███████╗
                                                                   ╚═╝   ╚═╝ ╚════╝    ╚═╝    ╚════╝ ╚═╝╚═╝  ╚═╝╚══════╝
        
        ''', RESET)    

    # 3 - Fin partie Mort Satan ~ 666 ~
    if print_value == 3:
        print("\n" "Satan :", style_satan + "𝔪𝔲𝔞𝔥𝔞𝔥𝔞𝔥𝔞𝔥𝔞 𝔪𝔢𝔲𝔯𝔰 𝔥𝔲𝔪𝔞𝔦𝔫 !", end_style)
        input()
        print("Dieu :", style_dieu + "À tout de suite", player_name, "...", end_style)
        input()
        print(style_satan, '''

                                                               ██╗   ██╗ █████╗ ██╗   ██╗      ██████╗ ██╗███████╗██████╗
                                                               ╚██╗ ██╔╝██╔══██╗██║   ██║      ██╔══██╗██║██╔════╝██╔══██╗
                                                                ╚████╔╝ ██║  ██║██║   ██║      ██║  ██║██║█████╗  ██║  ██║
                                                                 ╚██╔╝  ██║  ██║██║   ██║      ██║  ██║██║██╔══╝  ██║  ██║
                                                                  ██║   ╚█████╔╝╚██████╔╝      ██████╔╝██║███████╗██████╔╝
                                                                  ╚═╝    ╚════╝  ╚═════╝       ╚═════╝ ╚═╝╚══════╝╚═════╝
            
            
            ''')

# • Clear Terminal Pendant Le Jeu •   (fonctions inutiles créées juste pour faire "propre")
def clear_terminal(plateforme): 
    if plateforme == "1":
        os.system('cls')
    elif plateforme == "2":
        os.system('clear')

def clear_shop(player_name, player_points, player_cash, plateforme):
    input()
    clear_terminal(plateforme), start_end(1, player_name)
    print("\n" "\n" "\n" "Points :", BLUE, player_points, RESET,"    Cash :", GREEN, player_cash, "$", RESET)