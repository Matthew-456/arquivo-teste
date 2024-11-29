import random

n = int(input("Digite um número qualquer (menos 666, por favor 🙃): "))
print("""Agora escolhe uma das opções aí, mas escolhe direito hein: 
      [ 1 ] Transformar essa bagaça em BINÁRIO 🖥️
      [ 2 ] Mandar pra OCTAL, sei lá pra quê 🧮
      [ 3 ] HEXADECIMAL, pros programador raiz 🤓""")
option = int(input("Manda a boa, qual vai ser? "))

binario_msgs = [
    "Tá parecendo código de hacker, hein? 😂",
    "Com isso aí dá pra invadir a NASA... ou não. 🤷‍♂️",
    "Esse BINÁRIO tá com cara de filme de ficção científica! 🛸",
    "Imagina mostrar isso pra vó e falar que é bruxaria? 🧙",
    "A programação nunca foi tão engraçada, né não? 😂"
]

octal_msgs = [
    "Agora é só impressionar alguém... ou não. 😅",
    "Nem sei quem usa isso, mas tá aí. 🤷",
    "OCTAL? Nem o professor de matemática entende isso! 🧮",
    "Eu juro que isso faz sentido pra alguém... só não sei pra quem. 🤔",
    "Olha só, um número que ninguém vai usar! 👏"
]

hexadecimal_msgs = [
    "É isso que os nerds amam! 🤓",
    "Agora você tá no nível programador raiz. 💻",
    "Mostra isso pra um amigo e diz que é mágica! 🪄",
    "Parece complicado, mas é só HEXA mesmo. 🤓",
    "Esse HEXADECIMAL tá mais estiloso que eu no rolê! 😎"
]

if option == 1:
    print("O número {} convertido pra BINÁRIO ficou assim: {}. {}".format(n, bin(n)[2:], random.choice(binario_msgs)))
elif option == 2:
    print("O número {} em OCTAL é esse aqui: {}. {}".format(n, oct(n)[2:], random.choice(octal_msgs)))
elif option == 3:
    print("HEXIDECIMAL na tela! O número {} vira {}. {}".format(n, hex(n)[2:], random.choice(hexadecimal_msgs)))
else:
    print("AAAAAA! Opção inválida, amigão! Só vale 1, 2 ou 3. Bora tentar de novo! 😅")
