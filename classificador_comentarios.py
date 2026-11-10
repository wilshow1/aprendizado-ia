def classificar_com_ia(texto):
    #  Simulação com palavra chave, ainda não usa IA real
    texto = texto.lower()

    palavras_negativas = [
    "fria", "atrasou", "faltou", "ruim", "péssimo",
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
    
