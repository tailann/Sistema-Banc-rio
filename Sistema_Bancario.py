##SISTEM BANCARIO SEM INTERFACE GRAFICA DESENVOLVIDA DURANTE O CURSO Luizalabs - Back-end com Python

def main():
    entrada=input("""
[1] LOGUIN
[2] CADASTRO                 
""")
    return entrada
def loguin(entrada):

    lista_nome={}
    while True:
        with open(lista_nome, "r") as arquivo:
            nome=input("Digite seu nome")
            if nome =="":
                break
            elif nome == lista_nome:
                senha=input("digite sua senha")
                if senha == lista_nome[nome]:
                    print("Login efetuado com sucesso")