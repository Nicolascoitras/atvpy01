Login = "Ok, Seja bem vindo"
Cadastraremail = input("Digite seu email para cadastro: ")
Cadastrarsenha = input('Digite sua senha para cadastro: ') 

print(" * Cadastro Realizado * ")

while True:
    LoginEmail = input('Digite seu email: ')
    LoginSenha = input('Digite sua senha: ')
    if LoginEmail == Cadastraremail and LoginSenha == Cadastrarsenha:
        print(Login)
        break
    if LoginEmail != Cadastraremail or LoginSenha != Cadastrarsenha:
        print("Senha ou email errados tente novamente :( ")
        continue
