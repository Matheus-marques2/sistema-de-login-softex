# Projeto 3 – Sistema de Login e Cadastro

usuarios = []                                                   # usuarios = [] armazenamento do usuario 

def cadastrar():                                                # def, cadrastro do usuario com nume e senha
    usuario = input("Digite o nome de usuário: ")               
    senha = input("Digite a senha: ")
   
    for u in usuarios:                                          # if, codigo de verificação do usuario
        if u["usuario"] == usuario:                            
            print("Usuário já existe. Tente outro nome.")
            return                                              # return, servi para parar o codigo
   
    usuarios.append({"usuario": usuario, "senha": senha})       # .append conclusão do cadrastro e armazenamento
    print("Usuário cadastrado !")

def login():                                                    # usado para tentativas de erros 
    tentativas = 3
    usuario = input("Digite o nome de usuário: ")
   
    for u in usuarios:                                          # usaso para repetiçoes 
        if u["usuario"] == usuario:
            while tentativas > 0:
                senha = input("Digite a senha: ")
                if senha == u["senha"]:
                    print("Login feito!")
                    return
                else:
                    tentativas -= 1
                    print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            print("Tentativas excedida!")
            return
    print("Usuário não encontrado.")

def excluir():
    usuario = input("Digite o nome de usuário que deseja excluir: ")       #VERIFICAÇAO DE USUÁRIO PARA EXCLUSÃO
    senha = input("Digite a senha do usuário: ")
   
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:                #COMFIRMAÇAO DA EXCLUSÃO CASO LOGIN E SENHA CORRETA.
            usuarios.remove(u)
            print("🗑️ Usuário excluído com sucesso!")
            return
    print("Usuário ou senha incorretos. Não foi possível excluir.")        #NÃO EXCLUSÃO DO USUÁRIO (LOGIN OU SENHA INCORRETA)

def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for u in usuarios:
            print(f"- {u['usuario']}")

while True:
    print("\n==== MENU ====")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Excluir usuário")
    print("4 - Listar usuários")
    print("5 - Sair")
   
    opcao = input("Escolha uma opção: ")
   
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")