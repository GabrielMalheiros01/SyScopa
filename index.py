import mysql.connector
#criando a conecxao com o banco
def criar_conexao(host,usuario,senha, banco):
    return mysql.connector.connect(host=host,user=usuario,password=senha,database=banco)

#criando o cursor
con = criar_conexao("localhost","root","admin","syscopa")
cursor = con.cursor()

#criando funções
def insere_arbitro(nomearbi):
    sql = "INSERT INTO arbitro (nome_arbitro) values (%s)"
    valores = nomearbi
    cursor.execute(sql,[valores])
    con.commit()

def insere_tecnico(nometecn):
    sql = "INSERT INTO tecnico (nome_tecnico) values (%s)"
    valores = nometecn
    cursor.execute(sql,[valores])
    con.commit()

def insere_selecao(nomeselecao):
    sql = "INSERT INTO equipe (nome_equipe) values (%s)"
    valores = nomeselecao
    cursor.execute(sql,[valores])
    con.commit()

#definindo verificação
def verificaarbi():
    cursor.execute("SELECT * FROM arbitro")
    resultarbi = len(cursor.fetchall())
    return resultarbi

def verificaTecnico():
    cursor.execute("SELECT * FROM tecnico")
    resulttec = len(cursor.fetchall())
    return resulttec
def verificaSelecao():
    cursor.execute("SELECT * FROM equipe")
    resultselec = len(cursor.fetchall())
    return resultselec

def existeSelecao():
    cursor.execute("SELECT nome_equipe FROM equipe")
    resultselec = cursor.fetchall()
    return resultselec
def existeTecnico():
    cursor.execute("SELECT nome_tecnico FROM tecnico")
    resulttec = cursor.fetchall()
    return resulttec

#associando tecnico na seleção
def associaTecNaSelec(tec,selec):
    sql = ("UPDATE equipe set tecnico_id = (%s) where nome_equipe = %s")
    valores = (tec,selec)
    cursor.execute(sql,valores)
    con.commit()

def editarNovotecnico(oldtec,newtec):
        sql = ("UPDATE tecnico SET nome_tecnico = (%s) "
         "WHERE nome_tecnico = (%s)")
        valores = (newtec,oldtec)
        cursor.execute(sql,valores)
        con.commit()
def editarNovoJuiz(oldjuiz,newjuiz):
        sql = ("UPDATE arbitro SET nome_arbitro = (%s) "
         "WHERE nome_arbitro = (%s)")
        valores = (newjuiz,oldjuiz)
        cursor.execute(sql,valores)
        con.commit()
def editarNovaSelecao(oldselec,newselec):
        sql = ("UPDATE equipe SET nome_equipe = (%s) "
         "WHERE nome_equipe = (%s)")
        valores = (newselec,oldselec)
        cursor.execute(sql,valores)
        con.commit()
def removerTecnico(delettec):
    sql = ("DELETE FROM tecnico WHERE nome_tecnico = %s")
    valores = (delettec)
    cursor.execute(sql,[valores])
    con.commit()
def removerJuiz(deletjuiz):
    sql = ("DELETE FROM tecnico WHERE nome_tecnico = %s")
    valores = (deletjuiz)
    cursor.execute(sql,[valores])
    con.commit()
def removerSelecao(deletselec):
    sql = ("DELETE FROM equipe WHERE nome_equipe = %s")
    valores = (deletselec)
    cursor.execute(sql,[valores])
    con.commit()
def verTodasSelecs():
    cursor.execute("SELECT * FROM equipe")
    resultselec = cursor.fetchall()
    for x in range (0,len(resultselec)):
        print(resultselec[x],"\n")

def criarfases():
    sql = ("INSERT IGNORE INTO fases (nome_fase) values (%s)")
    fsgrupo = "fase_grupo"
    cursor.execute(sql,[fsgrupo])
    con.commit()
    fsoita = "oitava_final"
    cursor.execute(sql,[fsoita])
    con.commit()
    fsquarta = "quarta_final"
    cursor.execute(sql,[fsquarta])
    con.commit()
    fssemi = "semi_final"
    cursor.execute(sql,[fssemi])
    con.commit()
    fsterce = "terceiro_lugar"
    cursor.execute(sql,[fsterce])
    con.commit()
    fsfinal = "final"
    cursor.execute(sql,[fsfinal])
    con.commit()

def criarGrupos():
    sql = ("INSERT IGNORE INTO grupos (nome_grupo,fase_id) values (%s,%s)")
    valores = ("grupo_A",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_B",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_C",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_D",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_E",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_F",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_G",1)
    cursor.execute(sql,valores)
    con.commit()
    valores = ("grupo_H",1)
    cursor.execute(sql,valores)
    con.commit()

def definirgrupos():
    sql=("update equipe set grupo_id = 1 where id_equipe = %s;")
    for x in range(1,5):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 2 where id_equipe = %s;")
    for x in range(5,9):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 3 where id_equipe = %s;")
    for x in range(9,13):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 4 where id_equipe = %s;")
    for x in range(13,17):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 5 where id_equipe = %s;")
    for x in range(17,21):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 6 where id_equipe = %s;")
    for x in range(21,25):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 7 where id_equipe = %s;")
    for x in range(25,29):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()
    sql=("update equipe set grupo_id = 8 where id_equipe = %s;")
    for x in range(29,33):
        valor1 = x
        valores = (valor1)  
        cursor.execute(sql,[valores])
        con.commit()

def criarPartida(local,id):
    sql = "INSERT INTO partidas (local_partida, arbitro_id) VALUES  (%s , %s)"
    valores = (local,id)
    cursor.execute(sql,valores)
    con.commit()
    
def definirPartidaEquipe(idtime1,idtime2,gols1,gols2,idpartida):
    sql = "INSERT INTO partidas_equipe (equipe_id,partida_id,gols) values (%s, %s, %s)"
    valores1 = (idtime1,idpartida,gols1)
    valores2 = (idtime2,idpartida,gols2)
    cursor.execute(sql,valores1)
    con.commit()
    cursor.execute(sql,valores2)
    con.commit()
    

def definirPrimeiraRodada():
    print("Primeira Rodada da copa dos Devs!")
    cursor.execute("select nome_equipe from equipe where id_equipe = 1;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 2;")
    time2=cursor.fetchone()
    print("Primeira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,1)
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(1,2,gols1,gols2,1)
    print("Primeira partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 3;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 4;")
    time2=cursor.fetchone()
    print("Segunda partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,2)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(3,4,gols1,gols2,2)
    print("Segunda partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 5;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 6;")
    time2=cursor.fetchone()
    print("Terceira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,3)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(5,6,gols1,gols2,3)
    print("Terceira partida foi finalizada.")



    cursor.execute("select nome_equipe from equipe where id_equipe = 7;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 8;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,4)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,4)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 9;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 10;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,5)
    print("Quarta partida foi finalizada.")


    cursor.execute("select nome_equipe from equipe where id_equipe = 11;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 12;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 13;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 14;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 15;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 16;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 17;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 18;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 19;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 20;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 21;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 22;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 23;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 24;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 25;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 26;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 27;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 28;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 29;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 30;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 31;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 32;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,6)
    print("Quarta partida foi finalizada.")







while(True):
    print("Seja Bem vindo a copa dos devs!")
    print("o que desejas?")
    print("1- Cadastrar seleção ")
    print("2- Cadastrar tecnico ")
    print("3- Cadastrar arbitro ")
    print("4- Associar tecnico a selecao:")
    print("10- INICIAR COPA!")
    print("5- Sair")
    variavel = int(input(""))

    if(variavel==5):
        break
    if(variavel==4):
        while(True):
            print("Digite o id do tecnico: ")
            asTecnico = int(input(""))
            print("Digite o nome da seleção: ")
            asSelecao = input("")
            extecnico = existeTecnico()
            print([asTecnico])
            exselec = existeSelecao()
            if(asSelecao=="0" or asTecnico=="0"):
                break
            else:
                associaTecNaSelec(asTecnico,asSelecao)

    elif(variavel==3):
        while(True):
            print("digite o nome do arbitro: (max 12)")
            print("Digite 0 para sair")
            arbi = input("")
            verificaar = verificaarbi()

            if(arbi=="0"):
                break
            elif(verificaar<=12):
                insere_arbitro(arbi)
            else:
                print("Quantidade maxima de arbitro atingida!")
                break

    elif(variavel==2):
        while(True):
            print("Digite o nome do tecnico: ")
            print("Digite 0 para sair")
            tecn = input("")

            verificatec = verificaTecnico()

            if(tecn=="0"):
                break
            elif(verificatec<=32):
                insere_tecnico(tecn)
            else:
                print("Quantidade maxima de tecnicos atingida!")
                break

    elif(variavel==1):
        while(True):
            print("Digite o nome da seleção: ")
            print("Digite 0 para sair")
            seleca = input("")

            verificasel = verificaSelecao()

            if(seleca=="0"):
                break
            elif(verificasel<=32):
                insere_selecao(seleca)
            else:
                print("Quantidade maxima de seleções atingida!")
                break
    elif(variavel==10):
        while(True):
            verificatec = verificaTecnico()
            verificaar = verificaarbi()
            verificasel = verificaSelecao()
            if(verificatec>=32 and verificaar>=12 and verificasel>=32):
                definirgrupos()
                print("qual o proximo comando?")
                print("1- editar: ")
                print("2- exibir participantes: ")
                print("3- voltar a tela principal")
                print("4-Começar os jogos")
                comando = int(input(""))
                if(comando==1):
                    while(True):
                        print("como você deseja editar?")
                        print("1- editar")
                        print("2- remover")
                        print("3- cancelar")
                        editar= int(input(""))
                        if(editar==3):
                            break
                        print("quem deseja editar?")
                        print("1-tecnico")
                        print("2-juiz")
                        print("3-selecao")
                        print("4- cancelar")                       
                        deseja = int(input(""))
                        if(deseja==4):
                            break
                        if(editar==1):
                            if(deseja==1):
                                print("Qual o nome atual do tecnico?")
                                oldtec = input("")
                                print("Qual o nome novo do tecnico?")
                                newtec = input("")
                                editarNovotecnico(oldtec,newtec)
                            elif(deseja==2):
                                print("Qual o nome atual do juiz?")
                                oldjuiz = input("")
                                print("Qual o nome novo do juiz?")
                                newjuiz = input("")
                                editarNovoJuiz(oldjuiz,newjuiz)
                            elif(deseja==3):
                                print("Qual o nome atual da seleção?")
                                oldselec = input("")
                                print("Qual o nome novo da seleção?")
                                newselec = input("")
                                editarNovoJuiz(oldselec,newselec)
                            else:
                                print("digite um numero valido.")
                        elif(editar==2):
                            if(deseja==1):
                                print("Qual o nome atual do tecnico?")
                                delettec = input("")
                                removerTecnico(delettec)
                            elif(deseja==2):
                                print("Qual o nome atual do juiz?")
                                deletjuiz = input("")
                                removerJuiz(deletjuiz)
                            elif(deseja==3):
                                print("Qual o nome atual da seleção?")
                                deleteselec = input("")
                                removerSelecao(deleteselec)
                            else:
                                print("digite um numero valido.")
                        else:
                            print("digite um numero valido")
                elif(comando==2):
                    print("id_selecão| nome Seleção|id Tecnico| Grupo")
                    verTodasSelecs()
                elif(comando == 3):
                    break
                elif(comando == 4):
                    definirPrimeiraRodada()
                else:
                    print("digite um numero valido")
            else:
                print("falta algum elemento.")
                break
    else:
        print("Digite um numero válido.")