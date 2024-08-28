import os

mangás = [{"nome":"Bleach", "volume":"páginas", "em estoque":True},
          {"nome":"Aku no Hana", "volume":"páginas", "em estoque":True},
          {"nome":"Black Clover", "volume":"páginas", "em estoque":False}];

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
    
    def exibir_subtitulo(texto):
        os.system("cls");
        print(texto);
        print("");
        
    def retorna_menu():
        input("Aperte qualquer tecla para voltar ao menu principal");
        main();

    def cadastra_manga():
        exibir_subtitulo("Cadastro de novos mangás");
        nome_manga = input("Digite o nome do mangá que deseja cadastrar: \n");
        mangás.append(nome_manga);
        print(f"O mangá {nome_manga} foi cadastrado com sucesso\n");
        retorna_menu();
        
    def listar_manga():
        exibir_subtitulo("Lista de mangás cadastrados\n");
        for mangá in mangás:
            nome_mangá = mangá["nome"];
            volume_mangá = mangá["volume"];
            em_estoque = mangá["em estoque"];
            print(f"{nome_mangá} | {volume_mangá} | {em_estoque}");
        retorna_menu();

    def finalizar_programa():
        os.system("cls");
        print("Finalizando o programa\n");
    
    def opcao_invalida():
        print("Está é uma opção inválida, escolha outra opção\n");
        input("Aperte qualquer tecla para voltar ");
        main();

    try:
        opcao_escolhida = int(input("Escolha uma opção: "));

        if opcao_escolhida == 1:
            cadastra_manga();
        elif opcao_escolhida == 2:
            listar_manga();
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