# Mensagens do Sistema
import os.path

welcomeMessage = """
    Auto Formatter - Editor de Textos
   _________________________________________________
   Instruções:
   - Insira os trechos de texto recebidos dos autores.
   - Digite 'sair' a qualquer momento para finalizar, 
     gerar o arquivo e aplicar a formatação em maiúsculas.
   _________________________________________________
"""

# Lista para armazenar temporariamente os trechos digitados na sessão
listOfPhrases = []


def generateTextFile(listOfPhrases):
    """
        Função responsável por persistir as frases no disco, realizar a leitura,
        padronizar o texto para letras maiúsculas e atualizar o arquivo.
    """
    if not listOfPhrases:
        print("\n[Aviso] Nenhuma frase foi inserida para gerar o arquivo.")
        return

    try:
        # Abertura com modo "w+"
        # - Se o arquivo não existir, ele é criado.
        # - Trunca (limpa) o arquivo ao abrir e permite operações críticas de escrita e leitura.
        with open("meu_arquivo.txt", 'w+', encoding="utf-8") as fileHandle:

            # 1. Escreve todas as frases acumuladas na lista no arquivo
            for phrase in listOfPhrases:
                fileHandle.write(phrase + "\n")

            # 2. Retorna o cursor para o início do arquivo na posição 0 para leitura
            fileHandle.seek(0)

            # 3. Lê todo o conteúdo gravado no arquivo
            textContent = fileHandle.read()

            # 4. Converte todo o texto em letras maiúsculas (padronização exercício)
            upperContent = textContent.upper()

            # 5. Retorna o cursor ao início, limpa o arquivo (truncante) e sobrescreve com o texto em maiúsculas
            fileHandle.seek(0)
            fileHandle.truncate()
            fileHandle.write(upperContent)

            # 6. Exibição para auditoria
            print("[Info] Conteúdo formatado e salvo com sucesso.")
            print(f"\n[Info] Armazeando em: {os.path.realpath(fileHandle.name)}")
            print(repr(upperContent))

    except Exception as e:
        print(f"\n[Erro Interno] Ocorreu uma falha na manipulação do arquivo: {e}")


def main():
    """
    Função principal que contral o fluxo de execução (entry point da aplicação.
    """
    print(welcomeMessage)

    # Loop contínuo para a captura fluída de múltiplos textos
    while True:
        user_text = input("> Digite o texto (ou 'sair'): ")

        # Condição de saída: se o usuário digitar 'sair' (ignorando maiúsculas/minúsculas ou espaços extras)
        if user_text.strip().lower() == 'sair':
            generateTextFile(listOfPhrases)
            break

        # Se houver conteúdo válido, armazena na lista temporária
        if user_text.strip():
            listOfPhrases.append(user_text)
            print("-> Texto armazenado com sucesso. Continue digitando ou digite 'sair'.")
        else:
            print("[Aviso] Entrada vazia ignorada.")


if __name__ == "__main__":
    main()
