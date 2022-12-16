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
    idtec = cursor.execute("select id_tecnico where nome_tecnico = "+tec)
    sql = ("UPDATE equipe set tecnico_id = (%s) where nome_equipe = "+selec)
    valores = (idtec)
    cursor.execute(sql,[valores])
    con.commit()


#Modulo Principal

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
            print("Digite o nome do tecnico: ")
            asTecnico = input("")
            print("Digite o nome da seleção: ")
            asSelecao = input("")
            extecnico = existeTecnico()
            print([asTecnico])
            exselec = existeSelecao()
            print(exselec)
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
            if(verificatec==12 and verificaar==12 and verificasel==32):
                print("qual o proximo comando?")
                print("1- editar: ")
                print("2- exibir confrontos: ")
                print("3- exibir classificatoria: ")
                print("4- voltar a tela principal")
                comando = int(input(""))
                if(comando==1):
                    while(True):
                        print("como você deseja editar?")
                        print("1- remover")
                        print("2- editar")
                        editar= int(input(""))

                        print("quem deseja editar?")
                        print("tecnico")
                        print("juiz")
                        print("selecao")                        
                        deseja = int(input(""))

                        if(editar==1):
                            print
                        elif(editar==2):
                            print()
                        else:
                            print("digite um numero valido")
                else:
                    print("digite um numero valido")
            else:
                print("falta algum elemento.")
                break
    else:
        print("Digite um numero válido.")