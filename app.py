import os

def mostra_opcoes():
    print("""
    ██████████████████████████████████████████████████████████████████████▀█████████████
    █▄─██─▄█▄─▄▄▀██▀▄─██─█─██▀▄─██▄─▄▄▀██▀▄─████▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█─▄▄▄▄██▀▄─██─▄▄▄▄█
    ██─██─███─▄─▄██─▀─██─▄─██─▀─███─▄─▄██─▀─█████─█▄█─███─▀─███─█▄▀─██─██▄─██─▀─██▄▄▄▄─█
    ▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
    """);

    print("1. Cadastrar mangá");
    print("2. Listar mangá");
    print("3. Ativar ID de identificação do mangá");
    print("4. sair");

opcao_escolhida = int(input("Escolha uma opção: "));
# Outra forma de fazer -> opcao_escolhida = int(opcao_escolhida);

def cadastrar_manga():
    print("Você escolheu cadastrar o mangá");

def listar_manga():
    print("Você escolheu listar o mangá");

def ativar_id():
    print("Você escolheu ativar o ID do mangá");

def finaliza_programa():
    os.system("cls");
    print("Finalizando o programa");

def escolher_opcoes():
    if opcao_escolhida == 1:
        cadastrar_manga();
    elif opcao_escolhida == 2:
        listar_manga();
    elif opcao_escolhida == 3:
        ativar_id();
    else:
        finaliza_programa()

def main():
    os.system("cls");
    mostra_opcoes();
    escolher_opcoes();

if __name__ == "__main__":
    main();