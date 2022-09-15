class StopW:
    def get_stop_words(self,funct):
        if funct=="PER":
            return ["Ti","Las","Papa","Odi","Oce","Obr","Ober","Ny","Nor","Pay","Cha","No","Que","On","Ola","Ol","Hasta","Pad","Nie","Cin","Bi",
            "Ayer","PM","P","Oye","Pere","Perdona","Pen","Cha","Cham","Pay","Patr","Pascua","Py","Plaza","Plan","Pl","Pira","Pin","Pey",
            "Pete","No","Perfecto","Porter","Porque","To","Ponlo","Prefer","Pre","Pr","Pu","Psico","Profesor","Pro","Prim","Rap","Ran","Rah",
            "Rain","Rab","Quin","Qui","Q","Ol","Can","Rica","Ric","Rena","Reg","Ref","Ree","Red","Qué","Rat","Cu","Arro","Ru","Shi","Sep","Sel",
            "Se","Sand","Sac","Sabe","S","Tranquilo","Tranquila","The","Tha","Th","Super","Sul","Su","Da","Vé","Voy","Vive","Vern","Vent","D",
            "Anto","An","Ame","Ib","sul","nuestra","iv","gen","estruc","el Abi","Universidad","la","am","Y","y","Cor","Can","Bus","Bos","Bona",
            "Blan","Ball","Ayer","Ast","Ari","Bueno","Buen","Bra","Em","Echa","Dí","Dime","Del","Dar","Dam","Dal","In","Il","Flor","Fi","Eu",
            "Et","Esca","En","Hey","Hel","Har","Han","Gab","Fre","Lá","Ira","Ly","Lind","Ley","Mei","Max","Mas","Cán","Mano","Mada","M","Por",
            "Pat","Mí","Mé","Muy","Mo","Mont","Meli","Pue","Pri","Post","Pose","Tul","Tra","To","Sti","Sha","Ram","Pun","Ing","Bail","Art","Y",
            "Via","Ve","V","Ur","Tur","Dale","Cyn","Cons","Cari","Bl","Bet","Bal","Gale","Ga","Rad","Que","Pues","Po","Pi","Ori","Min","Mes",
            "Men","Ad","Ac","de","Tú","Ton","Sí","She","Rub","Ray","Nie","Elo","Cay","Ber","Bar","Arro","Na","Master","Mag","Lo","Gris","Ger",
            "Gar","Le","Pet","Or","Ir","Er","De","Cer","Bel","Ay","Ang","Ama","Agu","Ade","Ver","Sal", "Mire","La","Cán","Con","Ce","Ar","And",
            "Vit","Ser","Lin","Lea","Sin","Ol","Nada","Is","I","de","Bor","Bi","Ye","Co","Perfecto","Ai", "Cele","May","Ara","Tan","Ta","Cha",
            "Cab","Este","Can","Perdona","Be","Fab","Cami","Dan","Let","Pal","Val","Lor",".","Nú","Ma","Lu","Gi","Emi","Tu","Sor","Gem","Amp",
            "A","Yu","Vul","Vivi","Vel","Vaya","Te","er","Tara","Tar","Sat","R","N","Rem","Per","Pa","Oye Elena","Os","Ner","Ne","Nat","Nar",
            "Nac","Me",". Ti","Yo","Mira","Mir","Li","Hum","El","Yi","Tu Mir","Ti Ama","Son","Si","Say","Ros","Rom","Ro","W","[UNK]","Ra",
            "Vale","Nu","Mal","Beat","Tin","So","Sab","Sa","Roc","O","Nad","Má","Man","Mad","Hal","Hab","Gracias","Gracia","Gra","Go","Fla",
            "Esco","Es","Char","Cel","B","Al","Ag","Punto","Abra","Eun","Fru","At","Debí","Venga","Che","Tun","basta","Bac","Fabric","España",
            "Vill","Muerte","Acaso","Ecu","Mat","Che","Au","del","Gui","Nate","L","Eng","Fan","Chur","Fil","Disculpa","Pe","d","Gre","Du","Pe",
            "Fa","Ad","A","Abi","Conocí","Vio","Big","Van","Mur","tío","da","Vin","Gau"
            ]
        if funct=="LOC":
            return ["[UNK]","Lor","asi","Universi","Te","Qu","Ped","Pa","Mei","Or","D","Alej","Az","Vale","Se","R","Perdona","Ib","Cer","Camp",
            "Ana","plaza Gen Gracias","de la","W","Vir","Troy","Ter","Son","Rosa","Por","Per","On","O","María Luisa","Mal","Disculpa","Daniel",
            "D Or","Cali","Bol","Bill","Ave","Alfa","Al","Las","Internacional","La","Este","Verónica","Victoria","Tara","Pre","No","Mon","María","Lu"
            ,"El","Castell","plaza","del","Valle","Tarra","Sofía","Sara","Sar","Pilar","Par","Os","Oran","Ner","Nar","Misiones","Marta","Mar","Main",
            "Las","Huel","Can","Gran","De","Cá","Co","Car","Belén","Bel","Allá","Alba","de","Lu","Gen","Gracias","Amar","mi","hablando","Carlos",
            "de","la","Invita","Yor","Yo","Ye","Vega","Var","Vanessa","Van","Inglés","Tras","Igual","Val","Va","Universidad","de","Entre",
            "Um","Tu","Tor","Todo","To","Tira","lo","Blan","Tel","Tara","Mira","Tar","T","Sí","Sé","Syl","Sos","Sol","Ca","Si","Sexta","Sem",
            "Seguramente","Sede","Sali","S","Rosas","Ro","Rica","Reyes","Res","Pérez","Pri","Porto","Pi","País","Parad","Palau","Oro","Ore","Nicol",
            "Nat","Nan","Mar","La","Haya","So","Monts","Mo","Sil","Mire","Miguel","Mesa","Menor","Melo","Mat","Mass","María","Luisa","Marta","Marion",
            "Marina","Mari","Carmen","Mano","Mala","Ma","Lou","Los","Lo","Let","Le","Lang","Lad","La","Haya","Gom","Isabel","Is","In","Ida","Hue",
            "Hu","Bull","Haz","Haya","Ha","Gracias","Gon","Genial","Francisco","Gal","Den","Ga","G","Flor","FL","Eve","Esta","la","Franja","Hor","Y",
            "Es","Encantada","Ci","El","Du","Dor","Domingo","Dolores","Dile","Den","Dan","Dal","Cán","Vi","Cá","Cu","Exper","Colle","Co","mi","Ciencias",
            "Cin","Cielo","Ci","Chá","Sa","Chap","Chal","Ce","y","-","Casa","Carlos","3","Cara","Can","Campos","CER","Bueno","Bri","Bi","Bes","Bern","Ben",
            "Be","Bas","Bar","Bal","Bada","Ba","Avi","As","Arro","Aran","Ara","Ar","Apa","Huel","Amari","All","Alex","Adri","Ad","A","Abi","Conocí","Vio",
            "Big"
            ]
        if funct=="ORG":
            return ["[UNK]","Vo","Vir","L","Marina","Ma","Men","Cari","CON","CO","Bi","Hip","AR","B","Aca","Viol","IN","Bo","At",",","UN","T","W",
            "Sala","Refu","Rad","RA", "Ox", "Om Post","Mira","Hor","G","F . M","Digital","Can","Alba","An","Vale","Sub","Ac","ANE","Navarra",
            "Secretaría","Comité","U","TC","ER","Estado","Al","Infan","Estados","Unidos","Administración","Universi","R","Plaza","Nosotros","Log","End","De",
            "Conse","CS","VI","Gracias","PR","On","O","Nación","Lex","Laura","La","IF","Forma","E","Chile","Camp","CB","Big","R","BN","Amaz","Abi","w",
            "de","Doce","Ye","Yan","Vivo","Vista","Van","Punto","Huel","88","V",".","Vivi","Tú","Trans","Rafael","Sch","Vanessa","Generalitat","Eva","Robo",
            "U","Ty","Tro","Gracias","Tranquilo","Tranquila","Conde","In","TE","Surin","Sur","Sofía","Si","Sel","Secre","Sea","Barra","Crí","San","Salta",
            "Sa","SOL","S","Ro","Ris","Doce","Ra","R","Punto","Pues","Pu","Princip","Pre","Perdona","Pay","On","0","ON","O","To","Nor","Nega","Ne",
            "Motor","Misiones","Mire","Acom","para","Pen","acá","Sat","A","qué","Para","Infan","Gracias","Cu","Exper","Mer","Mat","Master","Marie","Mala",
            "Mal","Saba","MI","ME","Lu","Lin","Levante","Ga","Rosa","Amelia","Abi","Ca","Ca","La","Inteligencia","In","Hola","HA","H","CL","Gran","Red","Glo",
            "Glad","Ré","Ce","Fom","Gracias","Pues","Fac","Estudios","Estudio","Ricardo","Estrella","Estre","Esther","Vin","Perdon","Est","E","Emp","Pa","El",
            "Ejerci","ET","ES","ER","Miguel","EN","EL","Disculpa","San","Descu","Des","Del","Def","Dec","De","Dan","DI","DE","BU","D","Ener","Brit","Dia",
            "Cár","Pa","Hombre","Cri","Corte","Conven","2","Consul","Con","Hein","na","Reno","Ps","Co","mi","Cl","Qui","Les","Cir","Econom","Cine","Char",
            "Vi","Caja","CI","C","Bueno","Bol","Bio","Bill","Be","Barra","come","Ban","Bale","R","BO","Aven","Avi","Arte","Arro","Apla","Aparte","Ap","Amari",
            "Alma","Alar","Al","Ai","Af","Ras","Luc","Acer","Abo","Abi","Uni","AG","AF","AD","2"
            ]
