import pygame as pg
import random as rd

try: #verifica pyhton cobrinha.py se inicializou com sucesso, senão ele imprime que deu erro
  pg.init() #inicia a biblioteca, usa sempre
except:
  print("Não iniciou com sucesso")

#cores que serão usadas - RGB
white= (255,255,255)
rose=(205,92,92)
red= (255,0,0)
green=(0,255,0)
black=(0,0,0)


#musicas
musica_comer= pg.mixer.Sound("smw_kick.wav")

#tamanho da tela
x=640
y=480
tamanho=10 #tamanho do personagem

relogio= pg.time.Clock() #Criar relógico para ver os fps
font= pg.font.SysFont(None, 25) #Cria a fonte que vai escrever na tela
#Fonte que vai utilizar e tamanho da fonte

fundo = pg.display.set_mode((x,y)) #cria tela
pg.display.set_caption("jogo da cobrinha") #nome que aparece no jogo

def texto(mensagem, cor):
  texto1= font.render(mensagem, True, black) #mensagem a ser escrita, suavizador de texto, cor do texto
  fundo.blit(texto1, [x/6 , y/2]) #escreve um desenho dentro de outro

def cobra(CobraXY): #def cobra(meiox, meioy):-- Sem crescer
   for XY in CobraXY:
    cobra =pg.draw.rect(fundo, green, [XY[0],XY[1], tamanho, tamanho]) #superfície, cor, posição x e y e tamanhos

def maca(valorx, valory): 
  #posição inicial da maçã - aleatória
  maca= pg.draw.rect(fundo, red, [valorx, valory, tamanho,tamanho])

def jogo():
  fimdejogo=False
  sair=True
  meiox=x/2   #posição inicial da cobra
  meioy= y/2
  valorx= rd.randrange(0, x-tamanho, 10)
  valory = rd.randrange(0,y-tamanho, 10)
  velocidadex=0
  velocidadey=0
  CobraXY=[] #Não fica vazia sempre
  Cobratam=1 #quantas vezes ela comeu a maçã
  while(sair): # loop do jogo
    while fimdejogo:
      fundo.fill(rose)
      texto("Fim de jogo, para continuar tecle C ou para sair tecle S", black)
      pg.display.update()
      for event in pg.event.get(): #espera eventos acontecerem
      #print(event)
        if event.type==pg.QUIT: #Verifica se terá fechamento da tela
          sair=False
          fimdejogo=False
        if event.type==pg.KEYDOWN: #Verifica teclado
          if event.key == pg.K_c: 
            jogo()
            fimdejogo=False
            sair=True
            meiox=x/2   #posição inicial da cobra
            meioy= y/2
            valorx= rd.randrange(0, x-tamanho,10)
            valory = rd.randrange(0,y-tamanho,10)
            velocidadex=0
            velocidadey=0
            CobraXY=[] #Não fica vazia sempre
            Cobratam=1
            
          if event.key == pg.K_s: 
            fimdejogo=False
            sair=False
            
    for event in pg.event.get(): #espera eventos acontecerem
      #print(event)
      if event.type==pg.QUIT: #Verifica se terá fechamento da tela
        sair=False
      if event.type==pg.KEYDOWN: #Verifica teclado
        if event.key == pg.K_LEFT and velocidadex != tamanho:
          velocidadey=0
        # velocidade_x=-tamanho
          velocidadex= -tamanho #velocidade para cada tecla
        if event.key == pg.K_RIGHT and velocidadex != -tamanho:
          velocidadey=0
          #velocidade_x=tamanho
          velocidadex=tamanho
        if event.key == pg.K_UP and velocidadey != tamanho:
          velocidadex=0
        #  velocidade_x=-tamanho
          velocidadey= -tamanho
        if event.key == pg.K_DOWN and velocidadey != -tamanho:
          velocidadex=0
        # velocidade_x=tamanho
          velocidadey= tamanho
    fundo.fill(white) #preenche o fundo
   
    meiox+=velocidadex
    meioy+=velocidadey
    #Cobra(posx,posy)

    #Se a cobra choca com a maçã, é porque a maçã foi comida
    if meiox == valorx and meioy == valory:
      valorx= rd.randrange(0, x-tamanho,10)
      valory = rd.randrange(0,y-tamanho,10)  
      Cobratam +=1
      musica_comer.play()
      
      


    """
    if meiox> x:
      meiox=0
      #meiox=x-tamanho
    
    if meiox < 0:
      meiox=x-tamanho
    if meioy > y:
      meioy=0
    if meioy < 0:
      meioy=y-tamanho
    """

    if meiox> x:
     fimdejogo = True #sair=False
     musica_gmov= pg.mixer.music.load("smw_game_over.wav")
     pg.mixer.music.play()
    if meiox < 0:
      fimdejogo= True
      musica_gmov= pg.mixer.music.load("smw_game_over.wav")
      pg.mixer.music.play()

    if meioy > y:
      fimdejogo= True
      musica_gmov= pg.mixer.music.load("smw_game_over.wav")
      pg.mixer.music.play()
    if meioy < 0:
      fimdejogo= True
      musica_gmov= pg.mixer.music.load("smw_game_over.wav")
      pg.mixer.music.play()
      
      
  

    CobraInicio=[]
    #Adiciona as posições de início na cobra
    CobraInicio.append(meiox)
    CobraInicio.append(meioy)
    CobraXY.append(CobraInicio) #Junta todas as posições que a cobra passou e junta numa lista

    if len(CobraXY) > Cobratam: #retira a cabeça da cobrinha se a lista for maior que a cobra
      del CobraXY[0]

    #verificar se a cobra bate nela mesma
    if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
      fimdejogo= True
      musica_gmov= pg.mixer.music.load("smw_game_over.wav")
      pg.mixer.music.play()

    
    #Coloca a maçã e a cobra no jogo
    cobra(CobraXY)
    maca(valorx,valory) #Cria um formato - superfície, cor, [posiçãox, posição y, tamanho x e tamanho y]
      
    pg.display.update() #atualização constante da tela
    #relogio.tick(15)
    relogio.tick(30) #Frames por segundo que vão acontecer
   
#Roda o jogo
jogo()

