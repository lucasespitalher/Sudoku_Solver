def exibir_sudoku(sudoku:list):
    """
    Método utilizado para imprimir o sudoku

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ] 
    """
    for linha in sudoku: print(linha) #Percorre o sudoku e imprime linha a linha

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
    if sudoku[linha].count(numero) > 0: #Verifica se a linha já tem o número --> Se sim retorna False
        return False
            
    for lin in sudoku: #Percorre as linhas do sudoku
        if lin[coluna] == numero: #Verifica se o número na linha atual no índice da coluna é igual ao número teste --> Se sim retorna False
            return False

    lin_squade = (linha//3)*3 #Determina o limite x de um squade (quadrado 3x3)
    col_squade = (coluna//3)*3 #Determina o limite y de um squade (quadrado 3x3)

    for lin in range(0,3): #Percorre a linha do squade
        for col in range(0,3): #Percorre a coluna do squade
            if sudoku[lin_squade + lin][col_squade + col] == numero: #Verifica se algum quadrado do squade conter o número teste --> Se sim retorna False
                return False

    return True #Se o número é valido

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
    lista = [] #Lista que armazena o(s) número(s) valido(s)
    for num in range(1,10): #Gera número de 1 a 9 para teste
        if verificar_numero(sudoku, linha, coluna, num) == True: #verifica se o número é válido para ocupar a posição linha X coluna do sudoku
                lista.append(num) #Adicona o número na lista
      
    if len(lista) == 1: return lista[0] #Verifica se há apenas um único número na lista --> Se sim retorna o número

    return False #Se existir mais de um número valido para ocupar a posição linha X coluna
                
def verificar_sudoku(sudoku:list):
    """
    Percorre o sudoku e verifica se o jogo foi resolvido/concluído

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ] 

    Returns:
        True:   se o sudoku etiver completamente preenchido
        False:  se o sudoku ainda tiver quadrados vazios (0)
    """
    for linha in sudoku: #Percorre as linhas do sudoku
        if linha.count(0) > 0: return False #Verifica se há algum quadrado vazio (0) no sudoku --> Se sim retorna False

    return True #Se o sudoku estiver concluído

def validar_exclusivo(sudoku:list):
    """
    Verifica se existem quadrados no sudoku que só podem receber um único número

    Parâmetros:
        sudoku  (list): tabuleiro sudoku --> Estrutura: list [ list [ int ] ]

    Returns:
        True:   se o sudoku ainda tiver quadrados vazios (0) ou se o sudoku tiver quadrados que só podem conter um número
        False:  se não houver quadrados que só podem conter um número e se o sudoku não tiver quadrados vazios (0) 
    """
    for linha in range(len(sudoku)): #Percorre o sudoku
        for coluna in range(len(sudoku[linha])): #Percorre as linhas do sudoku
            if sudoku[linha][coluna] == 0: #Verifica se a posição linha X coluna no sudoku contém um 0
                var_teste = validar_numero(sudoku, linha, coluna) #Armazena o return de validar_numero()

                if var_teste != False: return True #Verifica se var_teste é diferente de False, ou seja, é igual a num (int)
            
    if verificar_sudoku(sudoku) == True: return True #Percorre o sudoku e verifica se o jogo foi resolvido ou não --> Se sim retorna True
    
    return False #Se não existirem posições no sudoku que podem receber apenas um número

def main(sudoku:list):
    while verificar_sudoku(sudoku) == False: #Permanece execuntando até que o tabuleiro esteja concluído
        for linha in range(len(sudoku)): #Percorre o sudoku
            for coluna in range(len(sudoku[linha])): #Percorre as linhas do sudoku
                if sudoku[linha][coluna] == 0: #Verifica se a posição linha x coluna é um quadrado vazio
                    var_teste = validar_numero(sudoku, linha, coluna) #Armazena o return de validar_numero()
                    
                    if var_teste == False: continue #Se não houver um único número exclusivo para a posição linha X coluna --> Continue
                    
                    else: sudoku[linha][coluna] = var_teste #Se houver um único número exclusivo para a posição linha X coluna --> Atualize o sudoku
        
        if validar_exclusivo(sudoku) == False: #Se não houverem quadrados que só podem receber um único número --> Não da para resolver
            print("Impossível resolver!!!\nNão há quadrados com números exclusivos") #Informa o usuário
            exit() #Encerra o programa

    exibir_sudoku(sudoku) #Imprime o tabuleiro sudoku resolvido


if __name__ == '__main__':
    sudoku = [ #Tabuleiro sudoku
        [9,0,0,0,0,0,0,0,0],
        [0,8,7,0,6,2,9,0,0],
        [0,6,0,0,0,9,5,1,2],
        [1,5,9,3,7,8,0,4,0],
        [0,0,0,0,0,0,0,0,0],
        [7,3,0,0,0,4,0,8,9],
        [6,0,5,0,0,0,0,0,1],
        [0,9,3,8,5,0,0,0,7],
        [4,1,8,0,9,0,3,0,5]]

    main(sudoku)