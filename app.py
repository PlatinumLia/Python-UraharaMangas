import os

mangás = [{"nome":"Bleach", "volume":"páginas", "ativo":True},
          {"nome":"Aku no Hana", "volume":"páginas", "ativo":False},
          {"nome":"Black Clover", "volume":"páginas", "ativo":True}];

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
    print("3. Ativar/Desativar ID de identificação do mangá");
    print("4. sair");

def escolhe_opcao():
    
    def exibir_subtitulo(texto):
        os.system("cls");
        linha = "-" * len(texto);
        print(linha);
        print(texto);
        print(linha);
        print("");
        
    def retorna_menu():
        input("Aperte qualquer tecla para voltar ao menu principal ");
        main();

    def cadastra_manga():
        exibir_subtitulo("Cadastro de novos mangás");

        nome_manga = input("Digite o nome do mangá que deseja cadastrar: \n");
        volume_manga = input(f"Digite quantas páginas têm o mangá: ");
        dados_do_manga = {"nome":nome_manga, "volume":volume_manga, "ativo":True};
        mangás.append(dados_do_manga);
        print(f"O mangá {nome_manga} foi cadastrado com sucesso\n");

        retorna_menu();
        
    def listar_manga():
        exibir_subtitulo("Lista de mangás cadastrados\n");
        for mangá in mangás:
            nome_mangá = mangá["nome"];
            volume_mangá = mangá["volume"];
            ativo = "Ativado" if mangá["ativo"] else "Desativado";
            print(f"{nome_mangá.ljust(20)} | {volume_mangá.ljust(20)} | {ativo.ljust(20)}");
            print()
        retorna_menu();
    
    def ativar_identificacao():
        exibir_subtitulo("Ativar/Desativar identificação do mangá");
        nome_manga = input("Digite o nome do mangá que deseja ativar ou desativar a identificação: ");

        manga_encontrado = False;
        
        for manga in mangás:
            if nome_manga == manga["nome"]:
                manga_encontrado = True;
                manga["ativo"] = not manga["ativo"];
                mensagem = f"O mangá {nome_manga} foi ativado com sucesso" if manga["ativo"] else f"O mangá {nome_manga} foi desativado com sucesso";
                print(mensagem);

            if not manga_encontrado:
                print("O mangá não foi encontrado");

        retorna_menu()
        
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
            ativar_identificacao();
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