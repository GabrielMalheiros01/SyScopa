import random
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
    sql = "INSERT INTO equipe (nome_equipe,gols,pontos,fase_id) values (%s,%s,%s,%s)"
    valores = (nomeselecao,0,0,1)
    cursor.execute(sql,valores)
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

def updateGols(idtime1,idtime2,gols1,gols2):

    if(gols1>gols2):
        sql1 = ("UPDATE equipe SET pontos = pontos + 3 "
        "where id_equipe = (%s)")
        valores1 = (idtime1)
        cursor.execute(sql,[valores1])
        con.commit()
    elif(gols1==gols2):
        sql1 = ("UPDATE equipe SET pontos = pontos + 1 "
        "where id_equipe = (%s)")
        valores5 = (idtime1)
        valores6 = (idtime2)
        cursor.execute(sql,[valores5])
        con.commit()
        cursor.execute(sql,[valores6])
        con.commit()
    else:
        sql1 = ("UPDATE equipe SET pontos = pontos + 3 "
        "where id_equipe = (%s)")
        valores1 = (idtime2)
        cursor.execute(sql,[valores1])
        con.commit()


    sql = ("UPDATE equipe SET gols = (%s)+gols "
    "WHERE id_equipe = (%s)")
    valores = (gols1,idtime1)
    valores2 = (gols2,idtime2)
    cursor.execute(sql,valores)
    con.commit()
    cursor.execute(sql,valores2)
    con.commit()

def classificacao():
    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 1 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo A")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 2 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo B")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 3 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo C")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 4 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo D")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 5 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo E")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 6 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo F")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 7 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo G")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

    cursor.execute("select nome_equipe,pontos,gols from equipe  where grupo_id = 8 order by pontos desc;")
    pri = cursor.fetchall()
    print("Grupo H")
    for x in range (0,len(pri)):
        print((x+1),pri[x],"\n")

def definirPrimeiraRodada():
    """print("Primeira Rodada da copa dos Devs!")
    cursor.execute("select nome_equipe from equipe where id_equipe = 1;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 2;")
    time2=cursor.fetchone()
    print("Primeira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,7)
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(1,2,gols1,gols2,1)
    updateGols(1,2,gols1,gols2)
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
    updateGols(3,4,gols1,gols2)
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
    updateGols(5,6,gols1,gols2)
    print("Terceira partida foi finalizada.")



    cursor.execute("select nome_equipe from equipe where id_equipe = 7;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 8;")
    time2=cursor.fetchone()
    print("a quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,4)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(7,8,gols1,gols2,4)
    updateGols(7,8,gols1,gols2)
    print("a quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 9;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 10;")
    time2=cursor.fetchone()
    print("a quinta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,5)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(9,10,gols1,gols2,5)
    updateGols(9,10,gols1,gols2)
    print("a quinta partida foi finalizada.")


    cursor.execute("select nome_equipe from equipe where id_equipe = 11;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 12;")
    time2=cursor.fetchone()
    print("a sexta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,6)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(11,12,gols1,gols2,6)
    updateGols(11,12,gols1,gols2)
    print("a sexta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 13;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 14;")
    time2=cursor.fetchone()
    print("a 7º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,7)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(13,14,gols1,gols2,7)
    updateGols(13,14,gols1,gols2)
    print("a 7º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 15;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 16;")
    time2=cursor.fetchone()
    print("a 8º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,8)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(15,16,gols1,gols2,8)
    updateGols(15,16,gols1,gols2)
    print("a 8º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 17;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 18;")
    time2=cursor.fetchone()
    print("a 9º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,9)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(17,18,gols1,gols2,9)
    updateGols(17,18,gols1,gols2)
    print("a 9º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 19;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 20;")
    time2=cursor.fetchone()
    print("a 10º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,10)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(19,20,gols1,gols2,10)
    updateGols(19,20,gols1,gols2)
    print("a 10º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 21;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 22;")
    time2=cursor.fetchone()
    print("a 11º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,11)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(21,22,gols1,gols2,11)
    updateGols(21,22,gols1,gols2)
    print("a 11º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 23;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 24;")
    time2=cursor.fetchone()
    print("a 12º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,12)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(23,24,gols1,gols2,12)
    updateGols(23,24,gols1,gols2)
    print("a 12º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 25;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 26;")
    time2=cursor.fetchone()
    print("a 13º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,1)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(25,26,gols1,gols2,13)
    updateGols(25,26,gols1,gols2)
    print("a 13º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 27;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 28;")
    time2=cursor.fetchone()
    print("a 14º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,2)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(27,28,gols1,gols2,14)
    updateGols(27,28,gols1,gols2)
    print("a 14º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 29;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 30;")
    time2=cursor.fetchone()
    print("a 15º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,3)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(29,30,gols1,gols2,15)
    updateGols(29,30,gols1,gols2)
    print("a 15º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 31;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 32;")
    time2=cursor.fetchone()
    print("a 16º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,4)

    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(31,32,gols1,gols2,16)
    updateGols(31,32,gols1,gols2)"""
    print("a 16º partida foi finalizada.")

def definirSegundaRodada():
    """print("Segunda Rodada da copa dos Devs!")
    cursor.execute("select nome_equipe from equipe where id_equipe = 1;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 3;")
    time2=cursor.fetchone()
    print("Primeira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(1,3,gols1,gols2,17)
    updateGols(1,3,gols1,gols2)
    print("Primeira partida foi finalizada.")


    cursor.execute("select nome_equipe from equipe where id_equipe = 4;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 2;")
    time2=cursor.fetchone()
    print("Segunda partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(4,2,gols1,gols2,18)
    updateGols(4,2,gols1,gols2)
    print("Segunda partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 8;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 6;")
    time2=cursor.fetchone()
    print("Terceira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(8,6,gols1,gols2,19)
    updateGols(8,6,gols1,gols2)
    print("Terceira partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 5;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 7;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(5,7,gols1,gols2,20)
    updateGols(5,7,gols1,gols2)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 12;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 10;")
    time2=cursor.fetchone()
    print("Quinta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(12,10,gols1,gols2,21)
    updateGols(12,10,gols1,gols2)
    print("Quinta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 9;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 11;")
    time2=cursor.fetchone()
    print("Sexta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(9,11,gols1,gols2,22)
    updateGols(9,11,gols1,gols2)
    print("Sexta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 16;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 14;")
    time2=cursor.fetchone()
    print("7º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(16,14,gols1,gols2,23)
    updateGols(16,14,gols1,gols2)
    print("7º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 13;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 15;")
    time2=cursor.fetchone()
    print("8º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(13,15,gols1,gols2,24)
    updateGols(13,15,gols1,gols2)
    print("8º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 20;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 18;")
    time2=cursor.fetchone()
    print("9º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(20,18,gols1,gols2,25)
    updateGols(20,18,gols1,gols2)
    print("9º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 17;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 19;")
    time2=cursor.fetchone()
    print("10º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(17,19,gols1,gols2,26)
    updateGols(17,19,gols1,gols2)
    print("10º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 21;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 23;")
    time2=cursor.fetchone()
    print("11º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(21,23,gols1,gols2,27)
    updateGols(21,23,gols1,gols2)
    print("11º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 24;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 22;")
    time2=cursor.fetchone()
    print("12º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(24,22,gols1,gols2,28)
    updateGols(24,22,gols1,gols2)
    print("12º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 28;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 26;")
    time2=cursor.fetchone()
    print("13º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(28,26,gols1,gols2,29)
    updateGols(28,26,gols1,gols2)
    print("13º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 25;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 27;")
    time2=cursor.fetchone()
    print("14º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(25,27,gols1,gols2,30)
    updateGols(25,27,gols1,gols2)
    print("14º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 32;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 30;")
    time2=cursor.fetchone()
    print("15º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(32,30,gols1,gols2,31)
    updateGols(32,30,gols1,gols2)
    print("15º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 29;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 31;")
    time2=cursor.fetchone()
    print("16º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(29,31,gols1,gols2,32)
    updateGols(29,31,gols1,gols2)"""
    print("16º partida foi finalizada.")

def definirTerceiraRodada():
    """print("Terceira Rodada da copa dos Devs!")
    cursor.execute("select nome_equipe from equipe where id_equipe = 4;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 1;")
    time2=cursor.fetchone()
    print("Primeira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(4,1,gols1,gols2,33)
    updateGols(4,1,gols1,gols2)
    print("Primeira partida foi finalizada.")


    cursor.execute("select nome_equipe from equipe where id_equipe = 2;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 3;")
    time2=cursor.fetchone()
    print("Segunda partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(2,3,gols1,gols2,34)
    updateGols(2,3,gols1,gols2)
    print("Segunda partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 06;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 07;")
    time2=cursor.fetchone()
    print("Terceira partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(6,7,gols1,gols2,35)
    updateGols(6,7,gols1,gols2)
    print("Terceira partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 8;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 5;")
    time2=cursor.fetchone()
    print("Quarta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(8,5,gols1,gols2,36)
    updateGols(8,5,gols1,gols2)
    print("Quarta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 12;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 9;")
    time2=cursor.fetchone()
    print("Quinta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(12,9,gols1,gols2,37)
    updateGols(12,9,gols1,gols2)
    print("Quinta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 10;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 11;")
    time2=cursor.fetchone()
    print("Sexta partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(10,11,gols1,gols2,38)
    updateGols(10,11,gols1,gols2)
    print("Sexta partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 16;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 13;")
    time2=cursor.fetchone()
    print("7º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(16,13,gols1,gols2,39)
    updateGols(16,13,gols1,gols2)
    print("7º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 14;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 15;")
    time2=cursor.fetchone()
    print("8º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(14,15,gols1,gols2,40)
    updateGols(14,15,gols1,gols2)
    print("8º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 20;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 17;")
    time2=cursor.fetchone()
    print("9º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(20,17,gols1,gols2,41)
    updateGols(20,17,gols1,gols2)
    print("9º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 18;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 19;")
    time2=cursor.fetchone()
    print("10º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(18,19,gols1,gols2,42)
    updateGols(18,19,gols1,gols2)
    print("10º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 24;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 21;")
    time2=cursor.fetchone()
    print("11º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(24,21,gols1,gols2,43)
    updateGols(24,21,gols1,gols2)
    print("11º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 22;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 23;")
    time2=cursor.fetchone()
    print("12º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(22,23,gols1,gols2,44)
    updateGols(22,23,gols1,gols2)
    print("12º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 28;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 25;")
    time2=cursor.fetchone()
    print("13º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(28,25,gols1,gols2,45)
    updateGols(28,25,gols1,gols2)
    print("13º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 26;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 27;")
    time2=cursor.fetchone()
    print("14º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(26,27,gols1,gols2,46)
    updateGols(26,27,gols1,gols2)
    print("14º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 32;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 29;")
    time2=cursor.fetchone()
    print("15º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(32,29,gols1,gols2,47)
    updateGols(32,29,gols1,gols2)
    print("15º partida foi finalizada.")

    cursor.execute("select nome_equipe from equipe where id_equipe = 30;")
    time1=cursor.fetchone()
    cursor.execute("select nome_equipe from equipe where id_equipe = 31;")
    time2=cursor.fetchone()
    print("16º partida é entre %s e %s"%(time1,time2))

    print("Digite o local da partida: ")
    local = input("")
    criarPartida(local,random.randint(1,12))
    print("Digite a quantidades de gols do ",time1)
    gols1 = int(input(""))
    print("Digite a quantidades de gols do ",time2)
    gols2 = int(input(""))
    definirPartidaEquipe(30,31,gols1,gols2,48)
    updateGols(30,31,gols1,gols2)"""
    print("16º partida foi finalizada.")

def definirOitavas():
    global a1,a2,b1,b2,c1,c2,d1,d2,e1,e2,f1,f2,g1,g2,h1,h2
    cursor.execute("select nome_equipe from equipe where grupo_id = 1 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    valores 
    a1 = resultselec
    a1 = list(a1)
    a1 = "".join(a1)

    print("1º classificado do grupo A:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 1 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    a2 = resultselec
    a2 = list(a2)
    a2 = "".join(a2)
    print("2º classificado do grupo A:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 2 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    b1 = resultselec
    b1 = list(b1)
    b1 = "".join(b1)
    print("1º classificado do grupo B:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 2 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    b2 = resultselec
    b2 = list(b2)
    b2 = "".join(b2)
    print("2º classificado do grupo B:",resultselec)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 3 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    c1 = resultselec
    c1 = list(c1)
    c1 = "".join(c1)
    print("1º classificado do grupo C:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 3 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    c2=resultselec
    c2 = list(c2)
    c2 = "".join(c2)
    print("2º classificado do grupo C:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 4 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    d1=resultselec
    d1 = list(d1)
    d1 = "".join(d1)
    print("1º classificado do grupo D:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 4 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    d2=resultselec
    d2 = list(d2)
    d2 = "".join(d2)
    print("2º classificado do grupo D:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 5 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    e1=resultselec
    e1 = list(e1)
    e1 = "".join(e1)
    print("1º classificado do grupo E:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 5 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    e2=resultselec
    e2 = list(e2)
    e2 = "".join(e2)
    print("2º classificado do grupo E:",valores)
    cursor.execute(sql,valores)
    con.commit()
    cursor.execute("select nome_equipe from equipe where grupo_id = 6 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    f1=resultselec
    f1 = list(f1)
    f1 = "".join(f1)
    print("1º classificado do grupo F:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 6 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    f2=resultselec
    f2 = list(f2)
    f2 = "".join(f2)
    print("2º classificado do grupo F:",valores)
    cursor.execute(sql,valores)
    con.commit()
    cursor.execute("select nome_equipe from equipe where grupo_id = 7 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    g1=resultselec
    g1 = list(g1)
    g1 = "".join(g1)
    print("1º classificado do grupo G:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 7 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    g2=resultselec
    g2 = list(g2)
    g2 = "".join(g2)
    print("2º classificado do grupo G:",valores)
    cursor.execute(sql,valores)
    con.commit()
    cursor.execute("select nome_equipe from equipe where grupo_id = 8 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    h1=resultselec
    h1 = list(h1)
    h1 = "".join(h1)
    print("1º classificado do grupo H:",valores)
    cursor.execute(sql,valores)
    con.commit()

    cursor.execute("select nome_equipe from equipe where grupo_id = 8 and fases = 1 order by pontos desc limit 1;")
    resultselec = cursor.fetchone()
    sql = ("UPDATE equipe set fases = (2) where nome_equipe = %s")
    valores = (resultselec)
    h2=resultselec
    h2 = list(h2)
    h2 = "".join(h2)
    print("2º classificado do grupo H:",valores)
    cursor.execute(sql,valores)
    con.commit()

def eliminatorias(nome1,nome2,gols1,gols2):
    if(gols1>gols2):
        sql = ("UPDATE equipe SET fases = fases + 1 "
        "where nome_equipe = (%s)")
        valores = (nome1)
        cursor.execute(sql,[valores])
        con.commit()
        print(nome1,"Foi Ganhador!")
    elif(gols2>gols1):
        sql = ("UPDATE equipe SET fases = fases + 1 "
        "where nome_equipe = (%s)")
        valores = (nome2)
        cursor.execute(sql,[valores])
        con.commit()
        print(nome2,"Foi Ganhador!")
    else:
        sql1 = ("UPDATE equipe SET fases = fases + 1 "
        "where id_equipe = (%s)")
        aleatorio = random.randint(1,2)
        if(aleatorio==1):
            valores=nome1
            print(nome1,"Foi Ganhador!")
        else:
            valores=nome2
            print(nome2,"Foi Ganhador!")
        cursor.execute(sql,[valores])
        con.commit()


def jogarOitavas():

    print("Primeiro jogo das oitavas!")
    print(a1,"x",b2)
    print("Quantos gols",a1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",b2," fez?")
    gols2 = int(input(""))
    eliminatorias(a1,b2,gols1,gols2)

    print(c1,"x",d2)
    print("Quantos gols",c1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",d2," fez?")
    gols2 = int(input(""))
    eliminatorias(c1,d2,gols1,gols2)

    print(e1,"x",f2)
    print("Quantos gols",e1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",f2," fez?")
    gols2 = int(input(""))
    eliminatorias(e1,f2,gols1,gols2)

    print(g1,"x",h2)
    print("Quantos gols",g1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",h2," fez?")
    gols2 = int(input(""))
    eliminatorias(g1,h2,gols1,gols2)

    print(b1,"x",a2)  

    print("Quantos gols",b1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",a2," fez?")
    gols2 = int(input(""))
    eliminatorias(b1,a2,gols1,gols2) 

    print(d1,"x",c2)
    print("Quantos gols",d1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",c2," fez?")
    gols2 = int(input(""))
    eliminatorias(d1,c2,gols1,gols2)

    print(f1,"x",e2)
    print("Quantos gols",f1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",e2," fez?")
    gols2 = int(input(""))
    eliminatorias(f1,e2,gols1,gols2)

    print(h1,"x",g2)
    print("Quantos gols",h1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",g2," fez?")
    gols2 = int(input(""))
    eliminatorias(h1,g2,gols1,gols2)

def definirQuartas():
    global v1,v2,v3,v4,v5,v6,v7,v8
    cursor.execute("SELECT nome_equipe FROM equipe WHERE fases = 3 ")
    v1 = cursor.fetchall()
    

    cursor.execute("SELECT nome_equipe FROM equipe WHERE fases = 3 ")
    v2 = cursor.fetchone()
    v2 = "".join(v2)

    
def jogarQuartas():
    print("Primeiro jogo das Quartas!")
    print(v1,"x",v2)
    print("Quantos gols",v1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",v2," fez?")
    gols2 = int(input(""))
    eliminatorias(v1,v2,gols1,gols2)

    print(v3,"x",v4)
    print("Quantos gols",v3," fez?")
    gols1 = int(input(""))
    print("Quantos gols",v4," fez?")
    gols2 = int(input(""))
    eliminatorias(v3,v4,gols1,gols2)
 
    print(v5,"x",v6)
    print("Quantos gols",v1," fez?")
    gols1 = int(input(""))
    print("Quantos gols",v2," fez?")
    gols2 = int(input(""))
    eliminatorias(v1,v2,gols1,gols2)

    print(v7,"x",v8)
    print("Quantos gols",v3," fez?")
    gols1 = int(input(""))
    print("Quantos gols",v4," fez?")
    gols2 = int(input(""))
    eliminatorias(v3,v4,gols1,gols2)

def jogarSemis():
    print()

def jogar3lugar():
    print()
def jogarFinal():
    print()

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
                    while(True):
                        print("1- Ver Classificação")
                        print("2- Seguir para 2º rodada")
                        segunda=int(input(""))
                        if(segunda==1):
                            classificacao()
                        elif(segunda==2):
                            definirSegundaRodada()
                            while(True):
                                print("1- Ver Classificação")
                                print("2- Seguir para 3º rodada")
                                terceira=int(input(""))
                                if(terceira==1):
                                    classificacao()
                                elif(terceira==2):
                                    definirTerceiraRodada()
                                    while(True):
                                        print("1- Ver Classificação")
                                        print("2- Seguir para as oitavas")
                                        oitavas=int(input(""))
                                        if(oitavas==1):
                                            classificacao()
                                        elif(oitavas==2):
                                            definirOitavas()
                                            jogarOitavas()
                                            definirQuartas()
                                            jogarQuartas()
                                            jogarSemis()
                                            jogar3lugar()
                                            jogarFinal()
                                        else:
                                            print("Numero invalido")
                                else:
                                    print("Numero invalido")
                        else:
                            print("Numero invalido")
                else:
                    print("digite um numero valido")
            else:
                print("falta algum elemento.")
                break
    else:
        print("Digite um numero válido.")