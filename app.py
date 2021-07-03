###############################
######Sistema de Cadastro######
###############################
#########Marcos Samuh##########


#importando a biblioteca pymysql
from io import open_code
import pymysql

#Criando conexão com o banco de dados
conexao = pymysql.connect(
    host ='localhost',
    user = 'root',
    passwd= '',
    database = 'leogas'
)


cursor = conexao.cursor()


#Inserindo cliente no cadastro
def inserir():
    nome = input('Nome do cliente: ')
    endereço = input('Endereço: ')
    cep = input('Cep: ')
    telefone = input('Telefone')
    sql_comando = 'INSERT INTO cliente(nome,endereço,cep,telefone) VALUE (%s,%s,%s,%s)'
    valor = [(f'{nome}',f'{endereço}',f'{cep}',f'{telefone}')]
    cursor.executemany(sql_comando,valor)
    conexao.commit()
    print(cursor.rowcount,'Dados adicionados com sucesso!') 
    option =int( input('Pressione 1 para voltar ou 2 para sair: '))
    if option ==1:
        main()
    elif option == 2:
        exit  
    
    
#Funçao para pesquisar clientes na tabela   
def ler():
    pesquisar = input('Pesquisar ')
    cursor.execute(f"SELECT * FROM cliente WHERE nome = '{pesquisar}'")
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)
    option =int( input('Pressione 1 para voltar ou 2 para sair: '))
    if option ==1:
        main()
    elif option == 2:
        exit    


#Função para editar clientes na tabela
def editar():
    com_sql = 'SELECT * FROM cliente'
    cursor.execute(com_sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    id_cliente = input('Insira o ID do cliente a ser editado: ')    
    dado =int (input('Digite o numero correspondente ao dado a ser alterdo: \n1. Nome \n2. Endereço \n3. Cep \n4. Telefone'))    
    if dado == 1:
        dado = 'nome' 
    elif dado == 2:
        dado = 'endereço' 
    elif dado == 3:
        dado = 'Cep' 
    elif dado == 4:
        dado = 'Telefone'   
      
    novo_dado = input(f'Insira o novo {dado}: ')     
    com_sql2 =  f"UPDATE cliente SET {dado} ='{novo_dado}' WHERE id = '{id_cliente}'"   
    cursor.execute(com_sql2)
    conexao.commit()
    print(cursor.rowcount,'Dado alterado com sucesso')
    option =int( input('Pressione 1 para voltar ou 2 para sair: '))
    if option ==1:
        main()
    elif option == 2:
        exit
    
#Função para excluir clientes na tabela
def excluir():
    com_sql = 'SELECT * FROM cliente'
    cursor.execute(com_sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)
    id_cliente = input('Insira o ID do cliente a ser excluido: ')
    com_sql2 =  f"DELETE FROM cliente WHERE id = '{id_cliente}'"   
    cursor.execute(com_sql2)
    conexao.commit()
    print(cursor.rowcount,'Cliente deletado com sucesso')
    option =int( input('Pressione 1 para voltar ou 2 para sair: '))
    if option ==1:
        main()
    elif option == 2:
        exit

# Script principal do programa
def main():
    option = input('Insira o numero da opçao desejada: \n1. Pesquisar cliente  \n2. Cadastrar cliente  \n3. Editar cliente \n4. Excluir cliente   ')
    opçao1 ='1'
    opçao2 ='2'
    opçao3 = '3'
    opçao4 = '4'
    if option == opçao1:
        ler()
    elif option == opçao2:
        inserir()
    elif option == opçao3:
        editar()
    elif option == opçao4:
        excluir()    
    else:
        exit
if __name__ =='__main__':
    main()


