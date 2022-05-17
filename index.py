import pygame,sys
pygame.init()
pantallaprincipal=True
pantallanatural=False
pantallapolitico=False
pantallasocial=False
pantallaeconomico=False
pantallacultural=False
pantallaorografia=False

def borrar():
    pygame.draw.rect(screen,WHITE,blanco,0)
def dibujar_boton(screen,boton,palabra,colordetexto,colordecuadrado,fuentedetexto):
    if boton.collidepoint(pygame.mouse.get_pos()):
        if colordecuadrado!=WHITE:
            pygame.draw.rect(screen,ORANGE,boton,0)
    else:
        pygame.draw.rect(screen, colordecuadrado, boton,0)

    naturalt = fuentedetexto.render(palabra,True,colordetexto)
    screen.blit(naturalt,(boton.left+(boton.width-naturalt.get_width())/2,boton.top+(boton.height-naturalt.get_height())/2))


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255, 87, 51)
GREEN = (91, 249, 27)
size = (1280,800)

screen = pygame.display.set_mode(size) #pygame.FULLSCREEN
pygame.display.set_caption("GEO EXPOESTADOS")
#fuentes y textos
fuente1 = pygame.font.SysFont("sitka text",50)
fuente2 = pygame.font.SysFont("sitka text",70)
fuente3 = pygame.font.SysFont("sitka text",30)
texto1 = fuente1.render("Componentes",True,BLACK)
#botones
componentes = pygame.Rect(400,40,500,200)
natural = pygame.Rect(200,200,300,100)
blanco = pygame.Rect(0,0,1280,800)
politico = pygame.Rect(800,200,300,100)
social = pygame.Rect(100,500,300,100)
cultural = pygame.Rect(500,500,300,100)
economico = pygame.Rect(900,500,300,100)
elotro = pygame.Rect(100,200,300,100)
elotro1 = pygame.Rect(500,200,300,100)
elotro2 = pygame.Rect(900,200,300,100)
#siguiente y regresar
siguiente = pygame.Rect(1200,100,50,50)
regresar = pygame.Rect(80,100,50,50)
#natural
orografia = pygame.Rect(200,200,300,100)
hidrografia = pygame.Rect(800,200,300,100)
clima = pygame.Rect(100,500,300,100)
florayfauna = pygame.Rect(500,500,300,100)
areasprotegidas = pygame.Rect(900,500,300,100)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:

            if politico.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=False
                pantallapolitico=True
            elif natural.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=False
                pantallanatural=True
            elif social.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=False
                pantallasocial=True
            elif economico.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=False
                pantallaeconomico=True
            elif cultural.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=False
                pantallacultural=True
            
            elif orografia.collidepoint(pygame.mouse.get_pos()): 
                pantallaorografia=True
                pantallanatural=False
                pantallapolitico=False
                pantallasocial=False
                pantallaeconomico=False
                pantallacultural=False
            elif regresar.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=True
                pantallanatural=False
                pantallapolitico=False
                pantallasocial=False
                pantallaeconomico=False
                pantallacultural=False
            print("clic")
    screen.fill(WHITE)
    pygame.Boton
    if pantallaprincipal == True:
        dibujar_boton(screen,componentes,"Componentes",BLACK,WHITE,fuente2)
        dibujar_boton(screen,natural,"Natural",BLACK,GREEN,fuente1)
        dibujar_boton(screen,politico,"Político",BLACK,GREEN,fuente1)
        dibujar_boton(screen,cultural,"Cultural",BLACK,GREEN,fuente1)
        dibujar_boton(screen,social,"Social",BLACK,GREEN,fuente1)
        dibujar_boton(screen,economico,"Económico",BLACK,GREEN,fuente1)
    elif pantallanatural == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,orografia,"Orografía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,hidrografia,"Hidrografía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,clima,"Clima",BLACK,GREEN,fuente1)
        dibujar_boton(screen,florayfauna,"Flora y fauna",BLACK,GREEN,fuente1)
        dibujar_boton(screen,areasprotegidas,"Areas protegidas",BLACK,GREEN,fuente1)
    elif pantallapolitico == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,elotro,"Capital",BLACK,GREEN,fuente1)
        dibujar_boton(screen,elotro2,"Colindancias",BLACK,GREEN,fuente1)
        dibujar_boton(screen,cultural,"Municipios",BLACK,GREEN,fuente1)
        dibujar_boton(screen,social,"Superficie",BLACK,GREEN,fuente1)
        dibujar_boton(screen,economico,"Escudo",BLACK,GREEN,fuente1)
        dibujar_boton(screen,elotro1,"Cartografía",BLACK,GREEN,fuente1)
    
    if pantallacultural == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,siguiente,"->",BLACK,GREEN,fuente3)
        dibujar_boton(screen,elotro,"Tradiciones/Costumbres",BLACK,GREEN,fuente1)
        dibujar_boton(screen,elotro2,"Artesanías",BLACK,GREEN,fuente1)
        dibujar_boton(screen,cultural,"Gastronomía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,social,"Música",BLACK,GREEN,fuente1)
        dibujar_boton(screen,economico,"Lenguas Indígenas",BLACK,GREEN,fuente1)
        dibujar_boton(screen,elotro1,"Traje típico",BLACK,GREEN,fuente1)

    print(pantallaorografia)

    pygame.display.flip()
