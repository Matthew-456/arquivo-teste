import random

# Mensagem de boas-vindas
print("🎉 Bem-vindo ao Conversor de Números! 🎉")
print("Aqui, você pode transformar números em diferentes bases!")
print("Escolha um número e uma opção para ver a mágica acontecer! ✨")
print("Pronto para começar? Vamos lá! 🚀\n")

# Mensagens para cada base
binario_msgs = [
    "Tá parecendo código de hacker, né não? 😂",
    "Com isso aí dá pra invadir a NASA... ou não, cê que sabe kkk. 🤷‍♂️",
    "Esse BINÁRIO tá com cara de filme de ficção científica! 🛸",
    "Imagina mostrar isso pra vó e falar que é bruxaria? 🧙",
    "A programação nunca foi tão engraçada, né não? 😂",
    "Se isso não for mágica, não sei mais o que é! Se fosse no Brasil, ia chamar de 'bagulho doido'! 🎩",
    "Agora você vai impressionar sua crush e ainda ganhar um intercâmbio pra Harvard! Quem diria? 🤣",
    "A única coisa que falta aqui é o hexa... E cadê a seleção que não aparece? ⚽",
    "Só faltava essa conversão pra gente ganhar a Copa do Mundo! 7x1? Aqui não! 😅",
    "Se você mostrar isso pra sua mãe, ela vai achar que é coisa de hacker! 🕵️‍♂️",
]

octal_msgs = [
    "Agora é só impressionar alguém... ou não. 😅",
    "Nem sei quem usa isso, mas tá aí. 🤷",
    "OCTAL? Nem o professor de matemática entende isso! pra que existe? kkk 🧮",
    "Eu juro que isso faz sentido pra alguém... só não sei pra quem. 🤔",
    "Olha só, um número que ninguém vai usar! 👏",
]

hexadecimal_msgs = [
    "É isso que os nerds amam! 🤓",
    "Agora você tá no nível programador raiz. 💻",
    "Mostra isso pra um amigo e diz que é mágica! 🪄",
    "Parece complicado, mas é só HEXA mesmo. 🤓",
    "Esse HEXADECIMAL tá mais estiloso que eu no rolê! 😎",
]

while True:
    # Obtendo um número válido do usuário
    while True:
        try:
            n = int(input("Digite um número qualquer (menos 666, por favor 🙃): "))
            if n == 666:
                resposta = input("Você realmente quer usar o número 666? [sim]/[não]: ").strip().lower()
                if resposta == 'sim':
                    break
                else:
                    print("Beleza! Vamos tentar de novo.")
            else:
                break
        except ValueError:
            print("Isso não é um número válido! Tente novamente.")

    # Exibindo opções de conversão
    print("""Agora escolhe uma das opções aí, mas escolhe direito hein: 
          [ 1 ] Transformar essa bagaça em BINÁRIO 🖥️
          [ 2 ] Mandar pra OCTAL, sei lá pra quê 🧮
          [ 3 ] HEXADECIMAL, pros programador raiz 🤓""")
    
    while True:  # Laço para garantir que o usuário escolha uma opção válida
        try:
            option = int(input("Manda a boa, qual vai ser? "))
            if option == 1:
                print("O número {} convertido pra BINÁRIO ficou assim: {}. {}".format(n, bin(n)[2:], random.choice(binario_msgs)))
                break  # Sai do laço quando a opção for válida
            elif option == 2:
                print("O número {} em OCTAL é esse aqui: {}. {}".format(n, oct(n)[2:], random.choice(octal_msgs)))
                break  # Sai do laço quando a opção for válida
            elif option == 3:
                print("HEXIDECIMAL na tela! O número {} vira {}. {}".format(n, hex(n)[2:], random.choice(hexadecimal_msgs)))
                break  # Sai do laço quando a opção for válida
            else:
                print("AAAAAA! Opção inválida, amigão! Só vale 1, 2 ou 3. Bora tentar de novo! 😅")
        except ValueError:
            # Exibe a mensagem de erro e reexibe as opções
            print("Isso não é uma opção válida! Escolha 1, 2 ou 3.")
            print("""Agora escolhe uma das opções aí, mas escolhe direito hein: 
                  [ 1 ] Transformar essa bagaça em BINÁRIO 🖥️
                  [ 2 ] Mandar pra OCTAL, sei lá pra quê 🧮
                  [ 3 ] HEXADECIMAL, pros programador raiz 🤓""")
    
    # Perguntando se o usuário quer continuar
    continuar = input("Quer converter outro número? [sim]/[não]: ").strip().lower()
    if continuar != 'sim':
        despedidas = [
            "Valeu por usar o Conversor de Números! Até a próxima! 🎉",
            "Beleza, sem problemas! Lembre-se: números são como amigos, sempre há espaço para mais! Até a próxima! 🎉",
            "O show não pode parar! Se precisar, só me chamar! Estou mais disponível que operadora de telefone esperando você comprar o plano dela 🤩😂!",
            "Até logo, meu amigo! Lembre-se, números não morderão! Eles são mais tranquilos que um gato na sombra! 🐱",
            "Cuidado! Esse OCTAL é tipo ônibus lotado: pode causar desconforto! kkkk 🤣"
        ]
        print(random.choice(despedidas))

        # Mensagens motivacionais
        motivacionais = [
            "Lembre-se: a prática leva à perfeição! Tente converter um número sozinho na próxima vez! 🚀",
            "Cada erro é uma oportunidade de aprender algo novo. Continue tentando! 🌟",
            "Acredite em você mesmo! Você é capaz de resolver qualquer desafio! 💪",
            "A única maneira de aprender é praticando! Então, não desista! 🏆",
            "Você é mais inteligente do que pensa! Vá em frente e faça a conversão sozinho! 🧠",
        ]
        print(random.choice(motivacionais))
        break
