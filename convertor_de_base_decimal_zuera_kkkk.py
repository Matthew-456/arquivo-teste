# OBS !!! : aparentimente o VScode não esta execultando o arquivo, tente usar outra IDLE, eu recomendo as online, como a " Programiz " 
# https://www.programiz.com/python-programming/online-compiler/

import random

# Mensagem de boas-vindas
print("🎉 Bem-vindo ao Conversor de Números! 🎉")
print("Aqui, você pode transformar números em diferentes bases!")
print("Escolha um número e uma opção para ver a mágica acontecer! ✨")
print("Pronto para começar? Vamos lá! 🚀\n")

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

# Opções de conversão
print("""Agora escolhe uma das opções aí, mas escolhe direito hein: 
      [ 1 ] Transformar essa bagaça em BINÁRIO 🖥️
      [ 2 ] Mandar pra OCTAL, sei lá pra quê 🧮
      [ 3 ] HEXADECIMAL, pros programador raiz 🤓""")
option = int(input("Manda a boa, qual vai ser? "))

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
    "Com esse poder, você vai estar mais preparado que jogador do Flamengo no Maracanã! 🏟️",
    "Agora é só pegar o ônibus lotado e ir mostrar isso pra galera! Cuidado com os assaltos! 🚍",
    "Com esse BINÁRIO, você já pode fazer uma música de pagode! É pra você, meu amor...🎶",
    "Se isso não impressionar sua crush, pelo menos dá pra fazer piada de 'sou programador'! 😂"
]

octal_msgs = [
    "Agora é só impressionar alguém... ou não. 😅",
    "Nem sei quem usa isso, mas tá aí. 🤷",
    "OCTAL? Nem o professor de matemática entende isso! pra que existe? kkk 🧮",
    "Eu juro que isso faz sentido pra alguém... só não sei pra quem. 🤔",
    "Olha só, um número que ninguém vai usar! 👏",
    "OCTAL? Aí é onde o bicho pega, hein? É tipo entender a letra de uma música de rap do Eminem! 🎤",
    "Cê tá sabendo, né? Isso é mais raro que show de artista famoso no Brasil! 🤷‍♂️",
    "Essa conversão é mais complicada que fazer receita de brigadeiro sem receita! 🍬",
    "Agora é só mostrar isso na quebrada e ver a galera ficar confusa! Eita trem! 😅",
    "Se tá octal, cê tá paia, mano! Aqui é binário que impressiona! 🤪",
    "OCTAL? Isso é mais raro que encontrar ingresso pra ver o Caetano Veloso ao vivo! Vale a pena só pra ver a cara de quem não entende! 😂",
    "Ninguém usa isso, mas quem sabe faz ao vivo! Como uma roda de samba! 🎶",
    "OCTAL é tipo aquele tiozão que só aparece em festa de família! Raro, mas divertido! 🎉",
    "Mostra esse código e se prepara pra ver a galera se perder na dança! 💃",
    "Cuidado! Esse OCTAL é tipo ônibus lotado: pode causar desconforto! 🚍"
]

hexadecimal_msgs = [
    "É isso que os nerds amam! 🤓",
    "Agora você tá no nível programador raiz. 💻",
    "Mostra isso pra um amigo e diz que é mágica! 🪄",
    "Parece complicado, mas é só HEXA mesmo. 🤓",
    "Esse HEXADECIMAL tá mais estiloso que eu no rolê! 😎",
    "Com isso você vai fazer o(a) crush magar em tu! 🥰 Tenho certeza! 😉",
    "Esse HEXA tá mais afiado que facão em roça! Pra cortar qualquer dúvida! 🔪",
    "Cê tá entendendo? Com esse HEXA, você é o verdadeiro artista do código! 🎨",
    "Agora você tá no estilo da quebrada, pronto pra brilhar no rap! 🎤",
    "É isso que eu chamo de HEXA, tá mais chique que baile de debutante! 🎉",
    "Esse HEXA é pra quem gosta de viver intensamente, tipo uma noite de sertanejo! 🤠",
    "Parece complicado, mas é tão gostoso quanto um acarajé bem temperado! 🍽️",
    "Mostra esse HEXA e vê se a galera não fica impressionada igual em show de rock! 🤘",
    "Com esse HEXA, você vai conquistar mais corações do que em festa junina! 💖",
    "Hexadecimal é o tipo de coisa que faz a gente dançar, igual forró na sanfona! 🎶",
    "Agora é só usar esse HEXA pra fazer sucesso na balada, eita trem bom! 🎉"
]

# Realizando a conversão com base na opção escolhida
if option == 1:
    print("O número {} convertido pra BINÁRIO ficou assim: {}. {}".format(n, bin(n)[2:], random.choice(binario_msgs)))
elif option == 2:
    print("O número {} em OCTAL é esse aqui: {}. {}".format(n, oct(n)[2:], random.choice(octal_msgs)))
elif option == 3:
    print("HEXIDECIMAL na tela! O número {} vira {}. {}".format(n, hex(n)[2:], random.choice(hexadecimal_msgs)))
else:
    print("AAAAAA! Opção inválida, amigão! Só vale 1, 2 ou 3. Bora tentar de novo! 😅")

# OBS !!! : aparentimente o VScode não esta execultando o arquivo, tente usar outra IDLE, eu recomendo as online, como a " Programiz " 
# sugestão : https://www.programiz.com/python-programming/online-compiler/
