from random import *
import dao


def maior(Jogador1, Jogador2,Jogador3, Jogador4 ):
    # Verifica o Jogador de Maior Pontuaço
    max = Jogador1
    if Jogador2 > max:
        max = Jogador2
    if Jogador3 > max:
        max = Jogador3
    if Jogador4 > max:
        max = Jogador4
    if max == Jogador1:
        return("Impulsivo")
    if max == Jogador2:
        return("exigente")
    if max == Jogador3:
        return("cauteloso")
    if max == Jogador4:
        return("aleatório")


def cond(valorCompra,saldo,jogador,valorALUGUEL):
    # Valida o perfil de cada jogado
    if jogador == "Jogador1":
        return True
    if jogador == "Jogador3":
        if saldo - valorCompra >= 80:
            return True
        else:
            return False
    if jogador == "Jogador2":
        if valorALUGUEL > 50:
            return True
        else:
            return False
    if jogador == "Jogador4":
        vontade = randrange(1, 3)
        if vontade == 1:
            return True
        else:
            return False
def Comprar(idJogador, saldo,idPro,valorCompra,posicaofim ):
    # Realiza a compra  da propriedade
    try:
        saldoNovo = saldo - valorCompra
        dao.UpdateJogador(idJogador, saldoNovo)
        dao.UpdateJogadorpos(idJogador, posicaofim)
        dono = True
        dao.UpdatePropriedade(idPro,idJogador,dono)
        return  saldoNovo
    except Exception as err:
        print(err)
def Aluguel(idJogador, saldopagador,idLocador,saldorecebido):
    # Realiza o pagamento ao jogador
    try:
        dao.UpdateJogador(idJogador, saldopagador)
        dao.UpdateJogador(idLocador, saldorecebido )
    except Exception as err:
        print(err)


def geerarpropriedade():
    # Gera a propriedade randomicamente
    try:
        listaJogadores=[]
        for i in range(0,20):
            valor = randrange(10,100,10)
            dicProp = {"Nome":"Propriedade"+str(i+1), "Valor":valor, "Aluguel":valor/2, "dono": False}
            listaJogadores.append(dicProp['Nome'])
            dao.insertProp(dicProp)
        return listaJogadores
    except Exception as err:
        print (err)

def jogar():
    # o jogo
    try:

        rodadas = 0
        # qts_jogador = input("Insira a quantidade de jogadores - (o jogo é para apens 6 jogadores) :") #Para jogos realizado por pessoas
        qts_jogador = 4
        listaPropiedade = geerarpropriedade()
        listaJogadores =["Jogador1", "Jogador2","Jogador3","Jogador4"]
        for jogador in listaJogadores:
            dicjogador = {"Nome": jogador, "pos": 0, "Saldo": 300, }
            dao.insertJogador(dicjogador)
        # if int(qts_jogador) > 6 or  int(qts_jogador) < 2 : Gerar lista de jogadores
        #     print("O jogo Não pode começar devido a quantidade de jogador!")
        #     pass
        # else:
        #     for x in (range(0,int(qts_jogador))):
        #         jogador =input("Digite o nome do jogador {}: ".format(x+1))
        #         dicjogador = {"Nome":jogador ,"pos":0, "Saldo":300 }
        #         dao.insertJogador(dicjogador)
        #         listaJogadores.append(dicjogador['Nome'])
        #     print (listaJogadores)
        while (rodadas<1000 ):

            for y in listaJogadores:
                if len(listaJogadores) > 1:
                    infoJogador= dao.selectJogador(y)
                    jogador = y
                    idJogador = infoJogador[0][0]
                    if infoJogador[0][2] == 0:
                        infoposinicio = "Inicio"
                    elif infoJogador[0][2] >= 21:
                        indice = infoJogador[0][2] - 20
                        infoposinicio = dao.selectProp(indice)[0][1]
                    else:
                        infoposinicio = dao.selectProp(infoJogador[0][2])[0][1]
                    saldo = infoJogador[0][3]
                    #print(str(jogador) + " você está na casa: " + str(infoposinicio))
                    #print(str(jogador) + " você possui em conta R$" + format(infoJogador[0][3], '.2f'))
                    #input("\n" + str(jogador) + ": Aperte ENTER para jogar o dado")
                    dado = randrange(1,6,1)
                    #print ('Valor do dado:' + str(dado))
                    posicaofim = int(infoJogador[0][2]) + int(dado)
                    if posicaofim >=21:
                        saldo = saldo + 100
                        posicaofim = posicaofim - 20
                    if saldo > 0:
                        if posicaofim == 0:
                            posicaofim =1
                        infopos = dao.selectProp(posicaofim)
                        idPro = infopos[0][0]
                        NomeProp = infopos[0][1]
                        valorCompra = infopos[0][2]
                        valorALUGUEL = infopos[0][3]
                        Proprietario = infopos[0][4]
                        avenda = infopos[0][5]
                        #print(" você está na propriedade: " + str(NomeProp))
                        if avenda == 0:
                            #print(str(jogador) + " Propriedade esta a venda no valor de R$:" + format( valorCompra, '.2f'))
                            #compra = input("Aperta S para Comprar e N para Não Comprar").lower()
                            compra = cond(valorCompra,saldo,jogador,valorALUGUEL)
                            if compra == True:
                                   if saldo >= valorCompra:
                                        saldo = Comprar(idJogador, saldo,idPro,valorCompra,posicaofim )
                                        #print("O "+ str(jogador)+" Comprou a propiedade: "+ str(NomeProp))
                                        #print ("O seu saldo atual é: R$"+str(saldo))
                                   else :
                                       print("O Jagador não tem saldo o suficiente para comprar.")
                            else:
                                #print("O Jagador não  deseja comprar.")
                                dao.UpdateJogadorpos(idJogador,posicaofim)
                                pass
                        else:

                            locador = dao.selectLocador(Proprietario)
                            idLocador = locador[0][0]
                            nomeLocador = locador[0][1]
                            saldoLocador = locador[0][3]
                            if jogador != nomeLocador:
                                saldopagador = saldo - valorALUGUEL
                                saldorecebido = saldoLocador + valorALUGUEL
                                #print("O jogador "+ str(jogador)+" tem que pagar o aluguel, no valor de R$"+str(valorALUGUEL)+ " para "+ str(nomeLocador))
                                Aluguel(idJogador, saldopagador,idLocador,saldorecebido)
                                dao.UpdateJogadorpos(idJogador, posicaofim)
                            else:
                                dao.UpdateJogadorpos(idJogador, posicaofim)
                    else:
                        #print("O jogador "+ str(jogador)+" Faliu e está fora do jogo")
                        dono = False
                        dao.deleteJogador(idJogador)
                        dao.UpdatePropriedadedevolvida(idJogador,dono)
                        listaJogadores.remove(jogador)
                        qts_jogador -=1
                else:
                    #print("O Jogo se encerrou e temos um vencedor!!!!!")
                    #print("O vencedor foi: " + str(listaJogadores[0]))
                    return (listaJogadores[0],rodadas)
            rodadas += 1
            print(" rodada numero: " + str(rodadas))
        return ("Os participantes desistiram de jogar", rodadas)

    except ValueError as err:
        print (err)
        return(err)

def main():
    timeout = 0
    Jogador1 = 0
    Jogador2 = 0
    Jogador3 = 0
    Jogador4 = 0
    turnos = []
    for i in range(0,10):
        resultado,rodadas = jogar()
        print ("Teste Numero: " + str(i))
        if resultado == "Os participantes desistiram de jogar":
            timeout +=1
            turnos.append(rodadas)
        if resultado == Jogador1:
            Jogador1 +=1
            turnos.append(rodadas)
        if resultado == Jogador2:
            Jogador2 += 1
            turnos.append(rodadas)
        if resultado == Jogador3:
            Jogador3 +=1
            turnos.append(rodadas)
        if resultado == Jogador4:
            Jogador4 +=1
            turnos.append(rodadas)
        dao.delete()

    print('O total de Partidas termindas em time out foram: ' + str(timeout))
    print('A porcentagem de vitoria de cada um é: /n')
    print("Impulsivo: "+ str(Jogador1))
    print("exigente: " + str(Jogador2))
    print("cauteloso: " + str(Jogador3))
    print("aleatório: " + str(Jogador4))
    print("O comportamento que mais vence é: "+ str(maior(Jogador1, Jogador2,Jogador3, Jogador4)))
    print("Amedia de turnos foram de:" + str((sum(turnos)/len(turnos))))



if __name__ == '__main__':
   main()


