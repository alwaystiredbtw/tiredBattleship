from random import randint
from time import sleep

#declaracao de variaveis

nomeP1 = ""
#variavel que escolhe aleatoriamente quem vai ser o primeiro jogador e depois verifica qual sera o proximo
jogada = randint(1,2)
jogador = 0
#funcoes usadas para o funcionamento do programa

#funcao pra printar ascii art
def printaBomba():
    print("""
             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       
        _.-'#######`-._                    
     ,-'###############`-.                 
   ,'#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
          """)

#funcao usada para posicionar os barcos do jogador
def posicionaBarco(tabuleiro):
    print()
    print(".")
    sleep(1)
    print("..")
    sleep(1)
    print("Posicionando barcos...")
    cont = 1
    for i in range(5):
        print(f"Tabuleiro do(a): {nomeP1}")
        printaTabuleiro(tabuleiro)
        posicao = (input(f"digite a posicao do barco {cont}:\n(Use linha e coluna,exemplo: 06 ou 12):"))
        cont += 1
        posicaolist = [int(x) for x in str(posicao)]
        tabuleiro[posicaolist[0]][posicaolist[1]] = 1
        sleep(1)
        print(".\n.\n.\n.\n.\n.")
        sleep(2)
    sleep(1)
    print(".")
    sleep(1)
    print("..")
    sleep(1)
    print("Barcos posicionados !")

#funcao usada para posicionar os barcos do computador
def posicionaBarcoPC(tabuleiro):
    for i in range(5):
        # tabuleiroP2[randint(0,4)][randint(0,9)] = 1
        tabuleiroP2[i][i + 1] = 1

#funcao usada para criar os tabuleiros do jogo
def criaTabuleiro(l, c,param):
    tabuleiro = []
    for i in range(l):
        tabuleiro.append(c * [param])
    return tabuleiro

#funcao usada para menu
def menu():
    global nomeP1
    nomeP1 = input("Bem vindo ao Batalha naval!\nPrimeiro digite seu nome jogador(a):")
    print(f"Por favor, {nomeP1},selecione uma opcao.\n[1] Inciar jogo\n[2] creditos")
    opcao = int(input("O que deseja fazer?:"))
    match opcao:
        case 1:
            return True
        case 2:
            return False

#funcao usada para parabenizar o vencedor
def winner(vencedor):
    print(f"                                                 O {vencedor} venceu !")
    print("""      ,~.
   ,-'__ `-,
  {,-'  `. }              ,')                               WINNER WINNER CHICKEN DINNER 
 ,( a )   `-.__         ,',')~,
<=.) (         `-.__,==' ' ' '}                             
  (   )                      /                                      PARABENS !!!    
   `-'\   ,                  )
       |  \        `~.      /
       \   `._        \    /
        \     `._____,'   /
         `-.            ,'
            `-.      ,-'
               `~~~~'
               //_||
            __//--'/`   
          ,--'/`  '
             '
          """)

#funcao para printar creditos caso seja necessario
def creditos():
    print("Obrigado por jogar!\nJogo feito por:\nEduardo Moura,Gilmar Denck,Vittorio Caprioli,Andre Akim")

#funcao que recebe o input do ataque do jogador e realiza confirmacao
def inputAtaque():
    ataque = (input("Qual coodenada deseja atacar?(utilize a coordenada da matriz)"))
    return [int(x) for x in str(ataque)]

#funcao que printa o tabuleiro de forma organizada
def printaTabuleiro(tabuleiro):
    for i in range(5):
        print(tabuleiro[i])

#funcao que verifica onde foi a posicao do ataque e retorna o acerto ou erro para o feedback
def verificaHit(cordList,tabuleiro,retorno,jogador):
    global barcosPC
    global barcosP
    verificacao = False
    # verificar se existe barco posicionado na posicao escolhida
    if tabuleiro[cordList[0]][cordList[1]] == 1:
        verificacao = True
        # mudar valores na da matriz caso algum barco seja acertado, tira o valor da contagem de barcos
        if jogador == 1:
            retorno[cordList[0]][cordList[1]] = 1
            tabuleiro[cordList[0]][cordList[1]] = 0
            barcosPC = barcosPC - 1
        if jogador == 2:
            retorno[cordList[0]][cordList[1]] = 1
            tabuleiro[cordList[0]][cordList[1]] = 0
            barcosP = barcosP - 1
        # registrar erro na matriz se nenhum barco for acertado
    if verificacao == False:
        retorno[cordList[0]][cordList[1]] = 2

    # printar acerto/erro
    match verificacao:
         case True:
                 print("Acertou!")
         case False:
                 print("Errou!")  

#funcao que realiza toda a execucao do jogo
def jogo():
    #printar tabuleiros 
    print(f"Acertos do(a) {nomeP1}")
    printaTabuleiro(retornoP1)
    print(f"Barcos restantes:{barcosPC}")
    print("------------------------------")
    print("Acertos do computador")
    printaTabuleiro(retornoP2)
    print(f"Barcos restantes:{barcosP}")
    #definir de quem vai ser a vez de acordo com a jogada
    if jogada % 2 == 0:
        jogador = 1
    if jogada % 2 != 0:
        jogador = 2
    #contabilizar a jogada
    #jogada do humano
    match jogador:
        case 1:
            print(f"Vez do {nomeP1}!!")
            sleep(2)
            print(".")
            sleep(1)
            print(".")
            while True:
                hitCord = inputAtaque()
                confirmacao = input((f"Confirme o ataque na posicao [{hitCord[0]}][{hitCord[1]}](utilize S ou N)")).upper()
                if confirmacao == "S":
                    break
            print("...")
            sleep(2)
            print(f"ataque na posicao [{hitCord[0]}][{hitCord[1]}]!!")
            sleep(1)
            print(".")
            sleep(1)
            printaBomba()
            sleep(2)
            verificaHit(hitCord,tabuleiroP2,retornoP1, jogador)
    #jogada do computador
        case 2:
            print(f"Vez do Computador!!")
            sleep(2)
            print(".")
            sleep(1)
            print(".")
            hitPC = [randint(0,4),randint(0,9)]
            print(".")
            sleep(2)
            print(f"ataque na posicao [{hitPC[0]}][{hitPC[1]}]!!")
            sleep(1)
            printaBomba()
            sleep(2)
            verificacao = verificaHit(hitPC,tabuleiroP1,retornoP2,jogador)
    print("...")
    sleep(2)

# codigo principal

tabuleiroP1 = criaTabuleiro(5,10,0)
tabuleiroP2 = criaTabuleiro(5,10,0)
retornoP1 = criaTabuleiro(5,10,0)
retornoP2 = criaTabuleiro(5,10,0)
# while true que executa o jogo
while True:
    # escolha de modo a partir do menu
    match menu():
        # caso o jogo seja iniciado
        case True:
            barcosPC = 5
            barcosP = 5
            posicionaBarco(tabuleiroP1)
            posicionaBarcoPC(tabuleiroP2)
            while True:
                jogo()
                jogada += 1
                if barcosP == 0:
                    break
                if barcosPC == 0:
                    break
        #condicao de vitoria do jogador
            if barcosPC == 0:
                winner(nomeP1)
                menu()
        #condicao de vitoria do computador
            else:
                winner("Computador")
                menu()
        # caso o usuario escolha ver os creditos
        case False:
            creditos()
            