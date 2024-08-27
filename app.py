import os

def mostra_titulo():
    print("""
        ██████████████████████████████████████████████████████████████████████▀█████████████
        █▄─██─▄█▄─▄▄▀██▀▄─██─█─██▀▄─██▄─▄▄▀██▀▄─████▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█─▄▄▄▄██▀▄─██─▄▄▄▄█
        ██─██─███─▄─▄██─▀─██─▄─██─▀─███─▄─▄██─▀─█████─█▄█─███─▀─███─█▄▀─██─██▄─██─▀─██▄▄▄▄─█
        ▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
        """);

def mostra_escolhas():
    print("1. Cadastrar mangá");
    print("2. Listar mangá");
    print("3. Ativar ID de identificação do mangá");
    print("4. sair");

def escolhe_opcao():

    def finalizar_programa():
        os.system("cls");
        print("Finalizando o programa\n");
    
    def opcao_invalida():
        print("Está é uma opção inválida, escolha outra opção\n");
        input("Aperte qualquer tecla para voltar ")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "));

        if opcao_escolhida == 1:
            print("Você escolheu cadastrar o mangá");
        elif opcao_escolhida == 2:
            print("Você escolheu listar o mangá");
        elif opcao_escolhida == 3:
            print("Você escolheu ativar a ID do mangá");
        elif opcao_escolhida == 4:
            finalizar_programa();
        else:
            opcao_invalida();
    except:
        opcao_invalida()

def main():
    mostra_titulo();
    mostra_escolhas();
    escolhe_opcao();

if __name__ == "__main__":
    main();