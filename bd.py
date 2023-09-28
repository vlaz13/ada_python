import pyodbc
from helper import valida_cpf, valida_data_nascimento, valida_rg


def retorna_cursor_bd():
    connection = pyodbc.connect(retorna_string_conexao_bd())
    cursor = connection.cursor()
    return cursor, connection


def retorna_string_conexao_bd():
        return(
    'Driver={SQL Server};'
    'Server=HOESQL633;'
    'Database=SkillUp_VLDSOUZ;'
    'Trusted_Connection=yes;'
    )

def select_bd():
   cursor, connection = retorna_cursor_bd()
   cursor.execute('select * from cliente;')
   clientes = cursor.fetchall()
   print(clientes)
   connection.commit()

def busca_bd(cpf):
  cursor, connection = retorna_cursor_bd()
  busca_query = "SELECT * FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(busca_query)
  cliente = cursor.fetchall()
  print(cliente)
  connection.commit()

def insert_bd(cliente):
   cursor, connection = retorna_cursor_bd() 
   insert_query = '''
        INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, numero_residencia)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
   values = (cliente['Nome'], cliente['CPF'], cliente['RG'], cliente['Nascimento'], cliente['CEP'], cliente['Numero'])
   cursor.execute(insert_query, values)
   connection.commit()

def update_bd(cpf):
  cursor, connection = retorna_cursor_bd()

  nome_n = input("Digite o Nome: "),
  cpf_n = valida_cpf(input("Digite o CPF: ")),
  rg_n = valida_rg(input("Digite o RG: ")),
  nascimento_n = valida_data_nascimento(),
  cep_n = input("Digite o CEP: "),
  numero_n = input("Digite o Número da casa: ")

  update_query = '''
   UPDATE cliente
   SET nome= ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ?
   WHERE cpf = ' + cpf + '
   '''
  set = (cliente['Nome'], cliente['CPF'], cliente['RG'], cliente['Nascimento'], cliente['CEP'], cliente['Numero'])
  cursor.execute(update_query, set)
  connection.commit()


def delete_bd(cpf):
  cursor, connection = retorna_cursor_bd()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()
  print('\nRegistro de CPF ' + cpf + ' deletado.')    


#insert_bd()
#delete_bd('037.509.231-59')
#select_bd()
