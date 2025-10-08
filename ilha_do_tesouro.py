#ilha do terouso (só pra treinar o basico)
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("""
                      /\  <<<<<           ()          [] >>>>>
                   ___||____|____  _______||____  ____||___|___
                  | ____    ____ || ____   ____ || ____   ____ |
                  | |VV|    |VV| || |WW|   |WW| || |UU|   |UU| |
                  | |==|    |==| || |==|   |==| || |==|   |==| |
                  | |__|    |__| || |__|   |__| || |__|   |__| |
                  | ____    ____ || ____   ____ || ____   ____ |
                  | |VV|    |VV| || |WW|   |WW| || |UU|   |UU| |
               () | |==|    |==| || |==|   |==| || |==|   |==| | ()
             ()\/() |__|    |__| || |__|   |__| || |__|   |__| ()\/()
            ._\()/_.             ||             ||            ._\()/_.
               || |              ||             ||             | ||
               || |       ______ ||      ______ ||      ______ | ||
               || | ____  | 42 | || ____ | 44 | || ____ | 46 | | ||
               || | |VV|  |    | || |WW| |    | || |UU| |    | | ||
               || | |==|  |   o| || |==| |   o| || |==| |   o| | ||
               || | |__|  |    | || |__| |    | || |__| |    | | ||
             __||_|       |    | ||      |    | ||      |    | |_||__
               || |_______|____|_||______|____|_||______|____|_| ||
               ||/_____/_____/_____/_____/_____/_____/_____/____\||lc
               ''''''''''''''''''''''''''''''''''''''''''''''''''''
               """)
print("você está em uma rua bifurcada com 2 caminhos, direita ou esquerda você escolhe? ")
escolha1 = input("direita ou esquerda? ").strip().lower()
if escolha1 == "esquerda":
    print("""   _______________________________________________   
     / __                   __                   __  \ 
     ||  |_________________|__|_________________|  | |     
     ||_/                                        \_| |
     |  |                                         |  |
     |  |                                         |  |
     |  |    /^\                                  |  |
     |  |   /   \                                 |  |
     |  |  /_____\                                |  |
     |  |                                         |  |
     |  |                                         |  |   
     |  |                                         |  |   
     | _| c=================================D     |_ |   
     || \ _______________________________________/ | |   
     ||__|                 |__|                 |__| |
     \_______________________________________________/  """)
    print("""você vira a esquerda e ve uma piscina imensa, que mais aparenta ser um grande oceano. A agua é turva e você
     nao consegue ver o fim. você decide nadar ou esperar? """)
    escolha2 = input("nadar ou esperar? ").strip().lower()
    if escolha2 == "nadar":
        print("""você toma coragem e decide nadar em meio a agua gelada, logo quando entra sente uma especie de alga 
        agarrando seu pé, você consegue se soltar mas decide continuar. Poucos metros a frente, você é puxada com toda
         a força para baixo sem ao menos conseguir ver oque é. Se afogando no final""")
        print("GAME OVER")
    elif escolha2 == "esperar":
        print(r"""      ______      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

""")
        print("""Você decide esperar para analisar com mais cuidado a agua. Surpreendentemente após alguns minutos,
         começa a emergir da agua 3 portas. Uma Vermelha, uma azul e uma amarela. Ambas com um caminho de pedras até elas.
         Qual você escolhe? """)
        escolha3 = input("vermelha, azul ou amarela? ").strip().lower()

        match escolha3:
            case "vermelha":
                print("""
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
 Você escolhe a porta vermelha, aproximando, a mesma emana uma labareda de fogo em suas frestas,
                 fazendo você sentir sua pele queimar aos poucos. Após perceber isso, você até tenta se afastar
                 , porem a porta se abre com um estrondo saindo diversas formas humanoides queimando de dentro. Te segurando
                  e fazendo sua pele queimar a cada puxada para dentro. Você Morreu carbonizada""")

                print("GAME OVER")

            case "azul":
                print("""Você decide então a porta Azul, se aproximando dela nada acontece, você a abre e verifica que 
                se encontra em uma floresta a noite. Atrás de você o caminho de pedras começa a se desfazer, sendo
                 o unico caminho, entrar na floresta. Ao entrar, nada acontece, escutando apenas o farfalhar dos galhos secos.
                  Andando mata a dentro, as arvores aparentam estar cada vez mais mortas e marcadas, e olhando para trás, 
                  você não consegue ver nada. Como se algo estivesse tapando seus olhos. Aceitando o seu destino, segue 
                  adentrando cada vez mais a floresta.\n 
                  Após caminhar por 1 hora, exausta e sem forças. Você acaba descansando aos pés de uma arvore morta. 
                  Infelizmente seu descanso dura pouco,
                   você escuta ao redor movimento na mata, passando de um lado ao outro como se estive te rondando.
                    você se levanta, o barulho aumenta, agora vindo de mais direções.
                   Você diz: \n
                   -Quem está ai?""")
                   
                print(r"""      
                                 /\*
                                ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'\**\--,
                           ,/",/W  u '`. ~  >,._..,   )'
                          ,/'  w  ,U^v  ;//^)/')/^\;~)'
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \*\*
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ''')/^"-;'
                                  \*
                                   '". _
                                        \*
                   no meio da escuridão, olhos vermelhos te cercam e antes de perceber, uma alcateia de lobos te mutila. VOCE MORREU""")
                print("GAME OVER")

            case "amarela":
                print(r"""
           __-----__
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.\
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    `;.,|.    |      '\.-'/
      ~~;;;,._|___.,-;;;~'
          ''=--'
Você então decide ir a porta amarela, ao se aproximar da porta, percebe que ela seria 
                completamente feita de ouro. seu bilho quase cegante te encanta. ao abrir a porta, se depara com diversas
                 moedas de ouro, pilhas e mais pilhas e ao topo dessa pilha, um baú resplandecente te aguarda.""")
                print(r"""                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.    """)
                print("Você ganhou!")
else:
    print(""" 
                              ...
           s,                .                    .s
            ss,              . ..               .ss
            'SsSs,           ..  .           .sSsS'
             sSs'sSs,        .   .        .sSs'sSs
              sSs  'sSs,      ...      .sSs'  sSs
               sS,    'sSs,         .sSs'    .Ss
               'Ss       'sSs,   .sSs'       sS'
      ...       sSs         ' .sSs'         sSs       ...
     .           sSs       .sSs' ..,       sSs       .
     . ..         sS,   .sSs'  .  'sSs,   .Ss        . ..
     ..  .        'Ss .Ss'     .     'sSs. ''        ..  .
     .   .         sSs '       .        'sSs,        .   .
      ...      .sS.'sSs        .        .. 'sSs,      ...
            .sSs'    sS,     .....     .Ss    'sSs,
         .sSs'       'Ss       .       sS'       'sSs,
      .sSs'           sSs      .      sSs           'sSs,
   .sSs'____________________________ sSs ______________'sSs,
.sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,
                        ...         sS'
                         sSs       sSs
                          sSs     sSs       
                           sS,   .Ss
                           'Ss   sS'
                            sSs sSs
                             sSsSs
                              sSs
                               s""")
    print("Você então escolhe a direta, ao se virar ela está bastante escura e você não percebe que está para cair em um buraco. VOCE MORREU")
    print("GAME OVER")
