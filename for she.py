import os
import time
from colorama import Fore, init

init(autoreset=True)

texto1 = """
Querida Maria,

Eu sei que você está passando por um momento difícil agora,
e eu quero que saiba que estou aqui para você, sempre. 

Sua tristeza não diminui em nada a pessoa incrível que você é. 
Na verdade, é apenas um lembrete de quão profundamente você sente as coisas
e o quanto você é humano.

Você é uma pessoa notável, e eu sou a pessoa    
mais sortuda do mundo por ter você ao meu lado.
Sua beleza, tanto por dentro quanto por fora, brilha como um raio de sol
em qualquer lugar que você vá. Sua inteligência é impressionante,
e sua compaixão é inigualável.

A maneira como você enfrenta os desafios com coragem  
e determinação é uma inspiração para mim e para todos ao seu redor. 
Sua risada é como música para meus ouvidos, e seu sorriso
ilumina meu dia, mesmo nos momentos mais sombrios.

Lembre-se de que cada desafio que você enfrenta é uma oportunidade de crescimento, 
e você tem a força e a resiliência para superar qualquer obstáculo.
Você é única, especial e absolutamente adorável.

Eu estou aqui para apoiá-la, segurá-la e amá-la,  
não importa o que aconteça. Vamos passar por isso juntos,
de mãos dadas, porque nós dois sabemos
que nada pode nos derrubar.

Você é mais do que suficiente, e eu te amo do fundo do meu coração. Não esqueça disso.

Com todo o meu amor,
Felipe.
"""

texto2 = """

Minha amada Maria,

Eu sei que todos nós temos dias em que nos sentimos um pouco inseguros em relação à nossa aparência,
mas quero que você saiba que, para mim, você é a pessoa mais linda do mundo,
não apenas por fora, mas principalmente por dentro.

A maneira como você ilumina qualquer ambiente com seu sorriso é incrível.
Seus olhos brilham com uma luz única, refletindo a sua alma gentil e amorosa.
Cada traço do seu rosto é perfeito à sua maneira,
e eu me apaixono por eles todos os dias.

Mas o que mais me encanta em você vai além da sua aparência física.  
Sua bondade, sua inteligência, sua compaixão e seu senso de humor 
são o que realmente fazem de você uma pessoa extraordinária.
Você faz as pessoas ao seu redor se sentirem bem e valorizadas,
e isso é uma qualidade rara e incrível.

Lembre-se de que a beleza está na diversidade e na singularidade de cada um de nós,
e você é uma verdadeira obra de arte.
Não importa como você se sinta em um determinado dia, 
saiba que você é absolutamente deslumbrante
aos meus olhos, todos os dias.

Ame a si mesma tanto quanto eu amo você, porque você merece todo o amor e admiração do mundo.

Com todo o meu amor e carinho,
Felipe.
"""

texto3 = """

Minha querida Maria,

Eu entendo que às vezes você pode se sentir sozinha,   
mas quero que saiba que você nunca está verdadeiramente sozinha,
porque meu amor está sempre com você, a qualquer hora e em qualquer lugar.

Sua presença é uma luz brilhante na minha vida.  
Você é uma pessoa incrível,e não é apenas porque
apaixonado por você, mas porque você tem uma essência
verdadeiramente cativante.
Sua beleza transcende a aparência física,
irradiando de dentro para fora.

Seu coração generoso e sua bondade inigualável fazem do mundo um lugar melhor. 
Você é inteligente, engraçada e incrivelmente talentosa
em tudo o que faz. Não há desafio que você não possa superar,
e cada obstáculo é apenas uma oportunidade para você brilhar ainda mais.

Lembre-se de que você é uma pessoa única e especial.  
O mundo é um lugar mais rico e colorido com você nele.
Sua companhia ilumina meus dias,  e eu sou profundamente grato
por tê-la em minha vida.

Sempre que se sentir sozinha, lembre-se de que você tem o meu amor
e apoio incondicionais. Estou aqui para você,
para ouvir, para abraçar e para compartilhar cada
alegria e desafio.
Juntos, podemos superar qualquer obstáculo que a vida nos apresentar.

Você é mais do que suficiente, e eu te amo mais a cada dia que passa.
Nunca duvide da pessoa incrível que você é.

Com todo o meu amor e carinho,
Felipe.
"""

banner = """
dP                                                    
88                                                    
88 .d8888b. dP   .dP .d8888b.                         
88 88'  `88 88   d8' 88ooood8                         
88 88.  .88 88 .88'  88.  ...dP                       
dP `88888P' 8888P'   `88888P'88                       
.d8888b. dP    dP .d8888b. d8888P .d8888b. 88d8b.d8b. 
Y8ooooo. 88    88 Y8ooooo.   88   88ooood8 88'`88'`88 
      88 88.  .88       88   88   88.  ... 88  88  88 
`88888P' `8888P88 `88888P'   dP   `88888P' dP  dP  dP 
              .88                                     
          d8888P                                      
"""

menu_text = """
MENU DE ESCOLHA - feito com muito carinho<3
1 - Veja quando estiver triste
2 - Veja quando se sentir feia
3 - Veja quando se sentir sozinha
4 - ?
0 - SAIR
"""

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def youtube():
        os.system('termux-open https://youtu.be/osrH9M87RsU?si=OGt9CtqR9c_rGFJy')
   

def efeito_digitar(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.03)

def menu_principal():
    clear_screen()
   
    
    while True:
        print(Fore.GREEN + banner + Fore.RESET)
        print(Fore.CYAN + menu_text + Fore.RESET)
        escolha = input("Escolha uma das opções: ")
        clear_screen()
        if escolha == '1':
            clear_screen()
            efeito_digitar("Ok, opção 1 escolhida. Aguarde um instante...\n")
            time.sleep(1)
            print("Lembre-se de que eu te amo! ❤️\n")
            time.sleep(2)
            
            clear_screen()
            efeito_digitar(texto1)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '2':
            clear_screen()
            efeito_digitar("Ok, opção 2 escolhida. Aguarde um instante...\n")
            time.sleep(1)
            print("Lembre-se de que eu te amo! ❤️\n")
            time.sleep(2)
            
            clear_screen()
            efeito_digitar(texto2)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '3':
            clear_screen()
            efeito_digitar("Ok, opção 3 escolhida. Aguarde um instante...\n")
            time.sleep(1)
            print("Lembre-se de que eu te amo! ❤️\n")
            time.sleep(2)
            
            clear_screen()
            efeito_digitar(texto3)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '4':
            clear_screen()
            efeito_digitar("Olha só! Você entrou em uma parte secreta, baby (curiosa demais, viu).\n")
            time.sleep(1)
            print("Bom, na verdade não tem muito segredo aqui.\n")
            time.sleep(2)
            
            print(f"{Fore.GREEN}Vou tocar uma música para você (bem que você poderia tocar uma para mim).{Fore.RESET}\n")
            time.sleep(1)
            print("Eu te amo! ❤️\n")
            time.sleep(2)
            youtube()
        elif escolha == '0':
            clear_screen()
            efeito_digitar("Aaaaaa vidaaa já vai? 😢\n")
            time.sleep(1)
            print("Eu te amo, amor! ❤️\n")
            time.sleep(2)
            
            print("Vou sentir saudades! Volte sempre. 😘\n")
            time.sleep(1)
            print("Saindo...\n")
            break
        else:
            clear_screen()
            efeito_digitar("Vida, escolha um número de 0 a 4, amor. 😅\n")
            print("Eu te amo! ❤️\n")
            time.sleep(2)
            

if __name__ == "__main__":
    menu_principal()
