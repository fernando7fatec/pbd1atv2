import psycopg2

class Usuario: 
    def __init__(self,login,senha):
        self.login = login
        self.senha = senha

def existe(usuario):
      # abrir uma conexão com o postgres
      with psycopg2.connect(
            host="localhost",
            dbname="db1",
            user="root",
            password="root"
        ) as conexao:

        # por meio da conexao obter uma abstracao do tipo cursor
        with conexao.cursor() as cursor:
           # por meio do cursor, executar o comando select
           cursor.execute(
              'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
              (usuario.login,usuario.senha)
           )
           result = cursor.fetchone()
      # devolver true ou false conforme o resultado. 
      return result != None

def main():
    # - chama f() menu
    menu()

def menu():
    texto = "0-Fechar\n1-Login\n2-Logoff"
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input(" Digite seu login : ")
            senha = input(" Digite sua senha : ")
            usuario = Usuario(login,senha)
            print(' Usuario OK' if existe(usuario) else 'Usuario Not OK')
        elif op == 2:
            usuario = None
            print(" Logoff realizado com sucesso ")
main()