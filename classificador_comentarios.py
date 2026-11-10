def classificar_com_ia(texto):
    #  Simulação com palavra chave, ainda não usa IA real
    texto = texto.lower()

    palavras_negativas = [
    "fria", "atrasou", "faltou", "ruim", "péssimo","não",
    ]
    palavras_positivas = [
     "simpático", "amei", "ótimo", "excelente",
        "bom", "gostei", "rápido", 
    ]
    if any(palavra in texto for palavra in palavras_negativas):
        return "negativo"
    elif any(palavra in texto for palavra in palavras_positivas):
        return "positivo"
    else:
        return "neutro"

def enviar_alerta_suporte(texto):
    # Simula o envio de um alerta
    print(f"Alerta para o suporte: {texto}")

def enviar_agradecimento_cliente():
    # simula o envio de um agradecimento
    print("obrigado pelo seu comentário!")

def salvar_no_banco_de_dados(texto):
    # simula o armazenamento usando uma lista
    banco_de_dados.append(texto)

banco_de_dados = []

comentarios = [
    "a pizza chegou fria e atrasou demais!",
    "o entregador foi muito simpático, gostei!",
    "faltou a bebida no meu pedido.",
]
for texto in comentarios:
    resultado_ia = classificar_com_ia(texto)
    
    if resultado_ia == "negativo":
        enviar_alerta_suporte(texto)

    elif resultado_ia == "positivo":
        enviar_agradecimento_cliente()
        salvar_no_banco_de_dados(texto)

    else:
        print(f"comentário neutro: {texto}")

while True:
    texto = input("Digite um comentário: ")
    if texto.strip() == "":
        print("Por favor, digite um comentário para continuar.")
        continue
    if texto.lower() == "sair":
        print("Programa encerrado!")
        break
    resultado = classificar_com_ia(texto)
    print("Classificação do comentário:", resultado)
    break

while True:
    try:
        avaliacao = int(input("Nos dê uma avaliação de 1 a 5: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue
        
    if 1 <= avaliacao <= 5:
        print("Avaliação recebida: ", avaliacao)
        break

    else:
        print("Avaliação inválida. Por favor, insira um número entre 1 e 5.")
        continue
