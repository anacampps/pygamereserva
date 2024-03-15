import pygame 
from funcoes_auxiliares import *

def inicializa(): ##-- não tem argumento porque apenas cria coisas sem depender de nada (informações externas) --##
    assets = {}

    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, 45)

    
    assets['font'] = font                        
    assets['num gerado']= gera_num(2)

    assets['fase'] = 'Memorizar'
    tempo_passado = pygame.time.get_ticks()
    assets['tempo_passado']= tempo_passado
    assets['tempo']  = 0
    assets['qtd_dígitos_seq_num'] = 2
    
    assets['num_digitado'] = ''

    assets['contagem_vidas'] = 3
    assets['contagem_acertos'] = 0

    #pygame.mixer.music.load('C:\Users\anaju\projeto.pygame\projeto-pygame-azul\codigo\sucess-1-6287.mp3')
    #pygame.mixer.music.play('Sucess-1-6287.mp3')

    assets['acerto_som'] = pygame.mixer.Sound('success-1-6297.mp3')
    assets['erro_som'] = pygame.mixer.Sound("negative_beeps-6008.mp3")


    window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Jogo da Memória')

    window.fill((0, 0, 0))
   
    return window, assets  ##


def recebe_eventos():

    game = True

    for event in pygame.event.get(): ##-- tudo que fica dentro do for event está relacionado com o mouse/teclado --##
        # print(event)   ## -- ótimo para achar posições da tela sem rachar a cabeça --##
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        if assets['fase'] == 'Digitar':
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE:
                    assets['num_digitado'] = assets['num_digitado'][:-1]
                elif event.key == pygame.K_RETURN:
                    assets['fase'] = 'Verificar'
                else:
                    if len(assets['num_digitado']) < assets['qtd_dígitos_seq_num']:
                        if event.unicode in ['0','2', '3', '4', '5', '6', '7', '8', '9']:
                            assets['num_digitado'] += event.unicode ## unicode é o valor da tecla pressionada (event.keydown é o evento de pressionar a tecla digitada)
                        
                   
                         ##-- não precisa verificar se o número tem dois dígitos no começo #=--
                
                                            # if assets['tempo'] == 0:   ##-- inúteis
             #     tempo = pygame.time.get_ticks()
    
    if assets['fase'] == 'Memorizar':
        atual = pygame.time.get_ticks()
        if atual - assets['tempo_passado'] > 4000:
            assets['fase'] = 'Digitar'
    elif assets['fase'] == 'Verificar':
        if str(assets['num gerado']) == assets['num_digitado']: ## -- comparar sempre dous valores do mesmo tipo
            assets['contagem_acertos'] += 1
            assets['qtd_dígitos_seq_num'] += 1
            assets['acerto_som'].play()

            
        else:
            assets['contagem_vidas'] -= 1
            assets['erro_som'].play()
        assets['fase'] = 'Memorizar'
        assets['tempo_passado'] = pygame.time.get_ticks()
        assets['num_digitado'] = '' ##-- tem de ficar depois do if de acerto/erro, pois se ficar antes os comandos debaixp serao ignorados--##
        assets['num gerado'] = gera_num(assets['qtd_dígitos_seq_num']) ##-- chamando funcao para passar numero novo --##
        
    #    


    return game


def desenha(window, assets): ##-- função (sem return): não retorna nada porque desenha na tela diretamente --##

    window.fill((0, 0 , 0))

    caixa_branca = pygame.draw.rect(window, (255, 255, 255), (100, 250, 500, 125))
    caixa_vermelha = pygame.draw.rect(window,(255, 0, 0), (120, 230, 460, 75))

    if assets['fase'] == 'Memorizar':
        memorize = assets['font'].render(str('MEMORIZE....'), True, (255, 255, 255)) 
        window.blit(memorize, (200, 150))
 
        num_gerado= assets['font'].render(str(assets['num gerado']),True, (0, 0 , 0))  #
        window.blit(num_gerado, (320, 240))
        ##-------Aqui implementamos a primeira fase: 2 digitos--------

    elif assets['fase'] == 'Digitar': 
        digite = assets['font'].render(str('DIGITE: '), True, (255, 255 ,255)) #
        window.blit(digite, (265, 150))

    chute = assets['font'].render(str(assets['num_digitado']), True, (0, 0, 0)) 
    


    window.blit(chute, (300, 330))

    vidas = assets['font'].render(str('Vidas: ' + str(assets['contagem_vidas'])), True, (255, 255, 255))
    window.blit(vidas, (10, 10))
    acertos = assets['font'].render(str('Acertos: ' + str(assets['contagem_acertos'])), True, (255, 255, 255))
    window.blit(acertos, (10, 50))
     #-------------------------------------------------------------------
          
    
    # pygame.rect

        
    pygame.display.update()


def game_loop(window, assets):   ##  ## equivalente ao while GAME

# : receber assets como argumento e repassar para desenha
    while recebe_eventos():  
        desenha(window, assets)  ##         #adcionar assets depois

if __name__ == '__main__':
    pygame.init()
        ##-- : receber assets aqui e repassar para game_loop
    window, assets = inicializa() ##
   
    # window.fill((0, 0, 0))
 
    game_loop(window,assets)  ##