from sudoku import Sudoku


def criar_sudoku():
    """
    Retorna um tabuleiro sudoku 3x3 com dificuldade média

    Returns:
        list [ list [ int ] ] : Uma lista que contém 9 listas e cada lista contém 9 números de 0 a 9
    """
    puzzle = Sudoku(3, 3).difficulty(0.5)
    puzzle = puzzle.board
    for linha in range(len(puzzle)):
        for coluna in range(len(puzzle[linha])):
            if puzzle[linha][coluna] == None:
                puzzle[linha][coluna] = 0

    return puzzle 

def exibir_sudoku(sudoku:list):
    """
    Imprime o sudoku formatado

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ] 
    """
    puzzle = Sudoku(3, 3, board = sudoku)
    puzzle.show()

def verificar_numero(sudoku:list, linha:int, coluna:int, numero:int):
    """
    Verifica se um número pode ocupar determinada posição linha x coluna no sudoku

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ] 
        linha   (int): número da linha na posição do sudoku
        coluna  (int): número da coluna na posição do sudoku
        numero  (int): número que vai ser verificado na posição linha x coluna do sudoku

    Returns:
        True:   se o número verificado é valido para a posição linha x coluna do sudoku
        False:  se o número verificado não é valido para a posição linha x coluna do sudoku
    """
    if sudoku[linha].count(numero) > 0:
        return False
            
    for lin in sudoku:
        if lin[coluna] == numero:
            return False

    lin_squade = (linha//3)*3
    col_squade = (coluna//3)*3

    for lin in range(0,3):
        for col in range(0,3):
            if sudoku[lin_squade + lin][col_squade + col] == numero:
                return False

    return True

def validar_numero(sudoku:list, linha:int, coluna:int):
    """
    Identifica se há apenas um número valido para ocupar determinada posição linha X coluna do sudoku

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ]
        linha   (int): número da linha no sudoku 
        coluna  (int): número da coluna no sudoku

    Returns:
        int:    o número se o número verificado é o único valido para a posição linha X coluna
        False:  se há mais de um número verificado valido para a posição linha X coluna
    """
    lista = []
    for num in range(1,10):
        if verificar_numero(sudoku, linha, coluna, num) == True:
                lista.append(num)
      
    if len(lista) == 1:
        return lista[0]

    return False
                
def verificar_sudoku(sudoku:list):
    """
    Percorre o sudoku e verifica se o jogo foi resolvido/concluído

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ] 

    Returns:
        True:   se o sudoku etiver completamente preenchido
        False:  se o sudoku ainda tiver quadrados vazios (0)
    """
    for linha in sudoku:
        if linha.count(0) > 0:
            return False

    return True

def validar_exclusivo(sudoku:list):
    """
    Verifica se existem quadrados no sudoku que só podem receber um único número

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ]

    Returns:
        True:   se o sudoku ainda tiver quadrados vazios (0) ou se o sudoku tiver quadrados que só podem conter um número
        False:  se não houver quadrados que só podem conter um número e se o sudoku não tiver quadrados vazios (0) 
    """
    for linha in range(len(sudoku)):
        for coluna in range(len(sudoku[linha])):
            if sudoku[linha][coluna] == 0:
                var_teste = validar_numero(sudoku, linha, coluna)

                if var_teste != False:
                    return True
            
    if verificar_sudoku(sudoku) == True:
        return True
    
    return False

def main():
    sudoku = criar_sudoku() #Cria um tabuleiro sudoku e armazena em sudoku
    exibir_sudoku(sudoku) #Imprime o tabuleiro formatado que será resolvido
    while verificar_sudoku(sudoku) == False: #Permanece execuntando até que o tabuleiro esteja concluído
        for linha in range(len(sudoku)): #Percorre o sudoku
            for coluna in range(len(sudoku[linha])): #Percorre as linhas do sudoku
                if sudoku[linha][coluna] == 0: #Verifica se a posição linha x coluna é um quadrado vazio
                    var_teste = validar_numero(sudoku, linha, coluna) #Armazena o return de validar_numero()
                    
                    if var_teste == False: continue #Se não houver um único número exclusivo para a posição linha X coluna --> Continue

                    else: sudoku[linha][coluna] = var_teste #Se houver um único número exclusivo para a posição linha X coluna --> Atualize o sudoku
        
        if validar_exclusivo(sudoku) == False: #Se não houverem quadrados que só podem receber um único número --> Utiliza py-sudoku para resolver
            puzzle = Sudoku(3, 3, board = sudoku) #Criar uma instância de Sudoku com o nosso tabuleiro sudoku
            sudoku = puzzle.solve().board #Resolve o sudoku e armazena um sudoku com estrutura list [ list [ int ] ] em sudoku
            break #Interrompe o laço while

    exibir_sudoku(sudoku) #Imprime o tabuleiro sudoku resolvido


if __name__ == '__main__':
    main()