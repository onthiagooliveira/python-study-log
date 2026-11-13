"""
Módulo: Leitura Segura de Arquivos de Texto
Descrição:
    Este script demonstra o padrão recomendável em Python para manipulação de
    arquivos de texto, abrangendo o uso de gerenciadores de contexto (with),
    tratamento específico de exceções e inspeção de caminhos do sistema operacional.
"""

import os.path

try:
    # -----------------------------------------------------------------
    # 1. Função open() e Gerenciador de Contexto (with)
    # -----------------------------------------------------------------
    # A função interna 'open()' abre o canal de comunicação com o arquivo.
    # Parâmetros utilizados:
    #   - 1º: O caminho do arquivo (utilizando Raw String 'r' para evitar
    #         problemas com barras invertidas no Windows).
    #   - 2º: O modo de abertura ('r' significa 'read' / leitura).
    #   - encoding: Define a codificação ('utf-8') para suportar acentuação.
    #
    # O bloco 'with' (Context Manager) gerencia o ciclo de vida do recurso:
    # Ele garante que o arquivo será fechado automaticamente ao sair do bloco,
    # liberando recursos do sistema mesmo se ocorrerem exceções no meio.
    # -----------------------------------------------------------------
    with open(r"C:\Users\onthi\Downloads\jack-hannaford.txt", "r", encoding="utf-8") as meuArquivo:

        # -------------------------------------------------------------
        # 2. Leitura e Processamento dos Dados
        # -------------------------------------------------------------

        # Leitura Completa (.read())
        # Lê todo o conteúdo textual do arquivo de uma só vez e o armazena na variável como string.
        content = meuArquivo.read()
        print("\nTipo de conteúdo: ", type(content))
        print("Conteúdo lido pelo read(): ")
        print(repr(content))
        print("-------------------------------------------------------")

        # Retorna o cursor ao início do arquivo (posição 0) para testarmos as outras funções de leitura
        meuArquivo.seek(0)

        # Leitura Linha a Linha (.readline())
        contentLine = meuArquivo.readline()
        print("\nTipo de conteúdo: ", type(contentLine))
        print("Conteúdo lido pelo readLine(): ")
        print(contentLine)

        nextContent = meuArquivo.readline()
        print("Próximo conteúdo retornado: ")
        print(repr(nextContent))
        print("-------------------------------------------------------")

        # Retorna o cursor novamente ao início
        meuArquivo.seek(0)

        # Leitura em Lote de Linhas (.readlines())
        # Retorna uma lista onde cada elemento é uma linha do arquivo.
        contentLines = meuArquivo.readlines()
        print("\nTipo de conteúdo: ", type(contentLines))
        print("Conteúdo lido pelo readLines(): ")
        print(repr(contentLines))

        # -------------------------------------------------------------
        # 3. Inspeção de Caminhos (Módulo os.path)
        # -------------------------------------------------------------
        # os.path.realpath: Resolve links simbólicos e retorna o caminho absoluto canônico.
        print(f"\nCaminho Real: {os.path.realpath(meuArquivo.name)}")

        # os.path.abspath: Retorna o caminho absoluto normalizado a partir do diretório atual.
        print(f"Caminho Absoluto: {os.path.abspath(meuArquivo.name)}")

        # -------------------------------------------------------------
        # 4. Tabela de Referência: Modos de Acesso a um Arquivo
        # -------------------------------------------------------------
        # Informam ao Python a intenção de operação sobre o arquivo:
        #   - "r": Read (leitura - padrão).
        #   - "w": Write (escrita - trunca/apaga o arquivo existente primeiro).
        #   - "x": Exclusive Creation (cria novo arquivo; lança FileExistsError se já existir).
        #   - "a": Append (escrita no final do arquivo sem apagar o conteúdo anterior).
        #   - "b": Binary (modo binário, usado para imagens, áudios, etc. ex: "rb", "wb").
        #   - "t": Text (modo texto padrão, ex: "rt" ou apenas "r").
        #   - "+": Update (abre para atualização: leitura e escrita combinadas, ex: "r+").

        # -------------------------------------------------------------
        # 5. Atributos do Objeto tipo Arquivo
        # -------------------------------------------------------------
        print("Nome do Arquivo: ", meuArquivo.name)
        print("Modo do Arquivo: ", meuArquivo.mode)
        print("Formato (Encoding): ", meuArquivo.encoding)
        print("Arquivo Fechado (dentro do bloco with): ", meuArquivo.closed)

        # NOTA DE BOAS-PRÁTICAS: O comando abaixo é redundante dentro do 'with',
        # pois o próprio gerenciador fechará o arquivo ao sair do bloco automaticamente.
        meuArquivo.close()

        print("Arquivo Fechado (após close manual): ", meuArquivo.closed)

# ---------------------------------------------------------------------
# 6. Tratamento de Exceções (Resiliência de Código)
# ---------------------------------------------------------------------
# Captura especificamente a exceção FileNotFoundError caso o arquivo não exista
# no diretório especificado, evitando que o programa sofra um crash inesperado
# e exibindo uma mensagem amigável para o usuário/sistema.
except FileNotFoundError:
    print("\nErro: Arquivo não encontrado no caminho especificado.")