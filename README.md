# Classificador de comentários e avaliações

Aplicação de terminal em Python para receber comentários sobre pedidos de delivery, classificá-los como positivos, negativos ou neutros e coletar uma nota de 1 a 5.

## Como funciona

Digite um comentário para receber a classificação. Em seguida, informe uma nota inteira de 1 a 5. Se o comentário estiver vazio ou a nota for inválida, o programa mostra um aviso e pede uma nova resposta.

A classificação é feita por palavras-chave, sem uso de inteligência artificial. Comentários como “amei a comida” são classificados como positivos; “a pizza chegou fria” e “não gostei”, como negativos. Quando há termos das duas categorias, o resultado negativo tem prioridade. Se nenhuma palavra da lista for encontrada, o resultado será neutro.

```text
Digite um comentário: amei a comida
Classificação do comentário: positivo
Nos dê uma avaliação de 1 a 5: 9
Avaliação inválida. Por favor, insira um número entre 1 e 5.
Nos dê uma avaliação de 1 a 5: 4
Avaliação recebida: 4
```

Cada execução recebe um comentário válido e uma nota. Na avaliação, letras, campos vazios, valores decimais e números fora do intervalo são recusados. Após uma nota válida, o programa termina.

## Como executar

Com Python 3 disponível, execute na pasta do projeto:

```bash
python classificador.py
```

Não são necessárias bibliotecas externas.

## Sobre esta versão

Ao iniciar, o programa apresenta três comentários de demonstração, com mensagens que simulam alertas para o suporte e agradecimentos. Na etapa interativa, o comentário digitado recebe apenas a classificação; não há envio real de mensagens.

O comando `sair`, no campo de comentário, pula para a avaliação. A mensagem “Programa encerrado!” exibida nesse momento não indica o fim de toda a execução: a nota ainda será solicitada.

A análise não interpreta o contexto da frase. Por exemplo, “não tenho reclamações, amei a comida” é classificado como negativo por conter “não”, mesmo sendo um elogio. A busca também pode encontrar trechos dentro de outras palavras e não reconhece automaticamente variações de acentuação.

Os comentários e as notas não são salvos permanentemente. A lista `banco_de_dados` armazena apenas comentários positivos dos exemplos iniciais e é descartada quando o programa fecha.

## Tecnologias e conceitos

Desenvolvido em Python, com funções, listas, estruturas condicionais, laços de repetição e tratamento de erros com `try/except`. Projeto de estudo voltado à lógica de programação e à validação de entradas.

## Melhorias previstas

- Salvar comentário, classificação e nota juntos em um arquivo.
- Melhorar a classificação de frases com negações e variações de palavras.
- Separar a demonstração do uso interativo.
- Ajustar o comando de saída e as mensagens de encerramento.

---

Desenvolvido por **Wilson Silva Monteiro**.
