# 1. Ler comentários (Criamos uma lista com alguns exemplos)
comentarios = [
    "A pizza chegou fria e atrasou muito!", 
    "O entregador foi super simpático, amei!",
    "Faltou a bebida no meu pedido."
]

# O computador precisa olhar um por um (Sua primeira linha)
for texto in comentarios:
    
    # 2. Enviar texto para classificação (Simulando a chamada da IA)
    resultado_ia = classificar_com_ia(texto) 
    
    # 3. Se negativo, emita alerta para o time de suporte
    if resultado_ia == "negativo":
        enviar_alerta_suporte(texto)
        
    # 4. Se positivo, agradeça e salve em um banco de dados
    elif resultado_ia == "positivo":
        enviar_agradecimento_cliente()
        salvar_no_banco_de_dados(texto)
