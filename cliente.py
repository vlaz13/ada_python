

from helper import valida_cpf, valida_data_nascimento, valida_rg
from bd import insert_bd, delete_bd, select_bd, update_bd, busca_bd

def menu_cliente():
  validador_menu = True
  lista_cliente = []
  
  while validador_menu:
    print("\n------------------------------------------"
      "\n **Menu Cliente**"
      "\n------------------------------------------"
      "\n 1 - Cadastrar Cliente"
      "\n 2 - Alterar Cliente"
      "\n 3 - Buscar Cliente"
      "\n 4 - Deletar Cliente"
      "\n 5 - Listar Clientes"
      "\n 6 - Voltar ao menu anterior \n")
    opcao = int(input("Digite a opção desejada do menu cliente: "))
    if opcao == 1:
      cliente_dicionario = {
        "Nome": input("Digite o Nome: "),
        "CPF": valida_cpf(input("Digite o CPF: ")),
        "RG": valida_rg(input("Digite o RG: ")),
        "Nascimento": valida_data_nascimento(),
        "CEP": input("Digite o CEP: "),
        "Numero": input("Digite o Número da casa: ")
      }
      #lista_cliente.append(cliente_dicionario)
      insert_bd(cliente_dicionario) 
    elif opcao == 2:
      update_bd(input("\nDigite o CPF: "))
    elif opcao == 3:
      busca_bd(input("\nDigite o CPF: "))
    elif opcao == 4:
      delete_bd(input("\nDigite o CPF: "))
    elif opcao == 5:
      select_bd()
    elif opcao == 6:
      print("\nEncerrando a execução do programa.")
      validador_menu = False
    else:
      print("\nOpção inválida.\n")