
import pygame,sys
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255, 87, 51)
GREEN = (91, 249, 27)
size = (1280,800)
exitoso=False


#imagenes cargadas
imagen1=pygame.image.load("imagenes/imagen1.png")
imagen2=pygame.image.load("imagenes/imagen2.png")
imagen3=pygame.image.load("imagenes/imagen3.png")
imagen4=pygame.image.load("imagenes/imagen4.png")
imagen5=pygame.image.load("imagenes/imagen5.png")
imagen6=pygame.image.load("imagenes/imagen6.png")
imagen7=pygame.image.load("imagenes/imagen7.png")
imagen8=pygame.image.load("imagenes/imagen8.png")
imagen9=pygame.image.load("imagenes/imagen9.png")
imagen10=pygame.image.load("imagenes/imagen10.png")
imagen11=pygame.image.load("imagenes/imagen11.png")
imagen12=pygame.image.load("imagenes/imagen12.png")
imagen13=pygame.image.load("imagenes/imagen13.png")
imagen14=pygame.image.load("imagenes/imagen14.png")
imagen15=pygame.image.load("imagenes/imagen15.png")
imagen16=pygame.image.load("imagenes/imagen16.png")
imagen17=pygame.image.load("imagenes/imagen17.png")
imagen18=pygame.image.load("imagenes/imagen18.png")
imagen19=pygame.image.load("imagenes/imagen19.png")
imagen20=pygame.image.load("imagenes/imagen20.png")
imagen21=pygame.image.load("imagenes/imagen21.png")
imagen22=pygame.image.load("imagenes/imagen22.png")
imagen23=pygame.image.load("imagenes/imagen23.png")
imagen24=pygame.image.load("imagenes/imagen24.png")
imagen25=pygame.image.load("imagenes/imagen25.png")
imagen26=pygame.image.load("imagenes/imagen26.png")
imagen27=pygame.image.load("imagenes/imagen27.png")
imagen28=pygame.image.load("imagenes/imagen28.png")
imagen29=pygame.image.load("imagenes/imagen29.png")
imagen30=pygame.image.load("imagenes/imagen30.png")
imagen31=pygame.image.load("imagenes/imagen31.png")
imagen32=pygame.image.load("imagenes/imagen32.png")
imagen33=pygame.image.load("imagenes/imagen33.png")
imagen34=pygame.image.load("imagenes/imagen34.png")


#pantallas
pantallaprincipal=True
pantallanatural=False
pantallapolitico=False
pantallasocial=False
pantallaeconomico=False
pantallacultural=False
pantallaorografia=False
pantallahidrografia=False
pantallaclima=False
pantallaflora=False
pantallafauna=False
pantallaareasprotegidas=False
pantallacapital=False
pantallacolindancias=False
pantallamunicipios=False
pantallasuperficie=False
pantallaescudo=False
pantallacartografia=False
pantallaPOBLACIÓNABSOLUTAYRELATIVA=False
pantallanatalidadymortalidad=False
pantallaesperanzadevida=False
pantallaalfabetismoyanalfabetismo=False
pantallaidh=False
pantallaactecono=False
pantallatraycos=False
pantallaartesanias=False
pantallagastronomia=False
pantallamusica=False
pantallalenguas=False
pantallatraje=False
pantallapersonajes=False
pantallaleyendas=False
pantallacultural2=False




def render_multi_line(texto, x, y, fontsize):
        lines = texto.splitlines()
        for i, l in enumerate(lines):
            font = pygame.font.SysFont("sitka text", fontsize)
            screen.blit(font.render(l, 0, 0), (x, y + fontsize*i))





fuente1 = pygame.font.SysFont("sitka text",50)
fuente2 = pygame.font.SysFont("sitka text",70)
fuente3 = pygame.font.SysFont("sitka text",30)
fuente4 = pygame.font.SysFont("sitka text",14)

textogastronomia="Quintana Roo cuenta con mucha variedad de platillos. \nLa mayoría son de pescado como el Pescado a la \nTikin Xic de Isla Mujeres que tiene achiote, naranja \nagria y pimientas para condimentar. Pero también \ncuenta con  varias pimientas. Pero Quintana Roo no solo tiene \nmariscos, también tiene comidas con otras carnes \ncomo el Makum de Repollo, hecho con lomo de cerdo \nmarinado en escabeche de jugo de naranja, Además condimentada \ncon orégano, pimienta y comino. Pero Quintana Roo tampoco \nse queda atrás en bebidas, contando con “Ojo Rojo”, \nuna bebida que mezcla licores como la cerveza y el clamato, \ncondimentos naturales como el apio y salsa Maggie."

def dibujar_boton(screen,boton,palabra,colordetexto,colordecuadrado,fuentedetexto):
    if boton.collidepoint(pygame.mouse.get_pos()):
        if colordecuadrado!=WHITE:
            pygame.draw.rect(screen,ORANGE,boton,0)
    else:
        pygame.draw.rect(screen, colordecuadrado, boton,0)

    naturalt = fuentedetexto.render(palabra,True,colordetexto)
    screen.blit(naturalt,(boton.left+(boton.width-naturalt.get_width())/2,boton.top+(boton.height-naturalt.get_height())/2))


screen = pygame.display.set_mode(size) 






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
siguientecultural= pygame.Rect(1200,100,50,50)
siguienteclima = pygame.Rect(1200,100,50,50)
siguienteclima2 = pygame.Rect(1200,100,50,50)
regresar = pygame.Rect(80,100,50,50)
#natural
orografia = pygame.Rect(100,200,300,100)
hidrografia = pygame.Rect(500,200,300,100)
flora = pygame.Rect(900,200,300,100)
clima = pygame.Rect(100,500,300,100)
fauna = pygame.Rect(500,500,300,100)
areasprotegidas = pygame.Rect(900,500,300,100)
#politico
capital = pygame.Rect(100,200,300,100)
colindancias = pygame.Rect(500,200,300,100)
superficie = pygame.Rect(900,200,300,100)
escudo = pygame.Rect(100,500,300,100)
municipios = pygame.Rect(500,500,300,100)
cartografia = pygame.Rect(900,500,300,100)
#social
poblacion = pygame.Rect(100,200,800,100)
nata = pygame.Rect(100,310,800,100)
espe = pygame.Rect(100,420,800,100)
alfa = pygame.Rect(100,530,800,100)
idh = pygame.Rect(100,640,800,100)
#economico/cultural
actecono = pygame.Rect(100,200,800,100)
traycos = pygame.Rect(100,310,800,100)
artesanias = pygame.Rect(100,420,800,100)
gastronomia = pygame.Rect(100,530,800,100)
musica = pygame.Rect(100,640,800,100)
lenguas = pygame.Rect(100,200,800,100)
traje = pygame.Rect(100,310,800,100)
personajes = pygame.Rect(100,420,800,100)
leyendas = pygame.Rect(100,530,800,100)







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pantallaprincipal==True:
                if natural.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=True
                    pantallaprincipal=False
                if politico.collidepoint(pygame.mouse.get_pos()):
                    pantallapolitico=True
                    pantallaprincipal=False
                if social.collidepoint(pygame.mouse.get_pos()):
                    pantallasocial=True
                    pantallaprincipal=False
                if economico.collidepoint(pygame.mouse.get_pos()):
                    pantallaeconomico=True
                    pantallaprincipal=False
                if cultural.collidepoint(pygame.mouse.get_pos()):
                    pantallacultural=True
                    pantallaprincipal=False

            
            elif pantallanatural == True:
                if orografia.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallaorografia=True
                elif hidrografia.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallahidrografia=True
                elif clima.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallaclima=True
                elif flora.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallaflora=True
                elif fauna.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallafauna=True
                elif areasprotegidas.collidepoint(pygame.mouse.get_pos()):
                    pantallanatural=False
                    pantallaareasprotegidas=True
                elif regresar.collidepoint(pygame.mouse.get_pos()):
                    pantallaprincipal=True
                    pantallanatural=False
            elif pantallapolitico == True:
                if capital.collidepoint(pygame.mouse.get_pos()):
                    pantallacapital=True
                    pantallapolitico=False
                elif superficie.collidepoint(pygame.mouse.get_pos()):
                    pantallasuperficie=True
                    pantallapolitico=False
                elif colindancias.collidepoint(pygame.mouse.get_pos()):
                    pantallacolindancias=True
                    pantallapolitico=False
                elif municipios.collidepoint(pygame.mouse.get_pos()):
                    pantallamunicipios=True
                    pantallapolitico=False
                elif cartografia.collidepoint(pygame.mouse.get_pos()):
                    pantallacartografia=True
                    pantallapolitico=False
                elif escudo.collidepoint(pygame.mouse.get_pos()):
                    pantallaescudo=True
                    pantallapolitico=False
            elif pantallasocial == True:
                if poblacion.collidepoint(pygame.mouse.get_pos()):
                    pantallaPOBLACIÓNABSOLUTAYRELATIVA=True
                    pantallasocial=False
                elif nata.collidepoint(pygame.mouse.get_pos()):
                    pantallanatalidadymortalidad=True
                    pantallasocial=False
                elif espe.collidepoint(pygame.mouse.get_pos()):
                    pantallaesperanzadevida=True
                    pantallasocial=False
                elif alfa.collidepoint(pygame.mouse.get_pos()):
                    pantallaalfabetismoyanalfabetismo=True
                    pantallasocial=False
                elif idh.collidepoint(pygame.mouse.get_pos()):
                    pantallaidh=True
            elif pantallaeconomico == True:
                if actecono.collidepoint(pygame.mouse.get_pos()):
                    pantallaactecono=True
                    pantallaeconomico=False
            elif pantallacultural == True:
                if siguientecultural.collidepoint(pygame.mouse.get_pos()):
                    pantallacultural2=True
                    pantallacultural=False
                if traycos.collidepoint(pygame.mouse.get_pos()):
                    pantallatraycos=True
                    pantallacultural=False
                elif artesanias.collidepoint(pygame.mouse.get_pos()):
                    pantallaartesanias=True
                    pantallacultural=False
                elif gastronomia.collidepoint(pygame.mouse.get_pos()):
                    pantallagastronomia=True
                    pantallacultural=False
                elif musica.collidepoint(pygame.mouse.get_pos()):
                    pantallamusica=True
                    pantallacultural=False
                elif lenguas.collidepoint(pygame.mouse.get_pos()):
                    pantallalenguas=True
                    pantallacultural=False  

            elif pantallacultural2 == True:
                if traje.collidepoint(pygame.mouse.get_pos()):
                    pantallatraje=True
                    pantallacultural2=False
                elif personajes.collidepoint(pygame.mouse.get_pos()):
                    pantallapersonajes=True
                    pantallacultural2=False
                elif leyendas.collidepoint(pygame.mouse.get_pos()):
                    pantallaleyendas=True
                    pantallacultural2=False

            if regresar.collidepoint(pygame.mouse.get_pos()):
                pantallaprincipal=True
                pantallanatural=False
                pantallapolitico=False
                pantallasocial=False
                pantallaeconomico=False
                pantallacultural=False
                pantallaorografia=False
                pantallahidrografia=False
                pantallaclima=False
                pantallaflora=False
                pantallafauna=False
                pantallaareasprotegidas=False
                pantallacapital=False
                pantallacolindancias=False
                pantallamunicipios=False
                pantallasuperficie=False
                pantallaescudo=False
                pantallacartografia=False
                pantallaPOBLACIÓNABSOLUTAYRELATIVA=False
                pantallanatalidadymortalidad=False
                pantallaesperanzadevida=False
                pantallaalfabetismoyanalfabetismo=False
                pantallaidh=False
                pantallaactecono=False
                pantallatraycos=False
                pantallaartesanias=False
                pantallagastronomia=False
                pantallamusica=False
                pantallalenguas=False
                pantallatraje=False
                pantallapersonajes=False
                pantallaleyendas=False
                pantallacultural2=False


    screen.fill(WHITE)
    

    if pantallaprincipal == True:

        dibujar_boton(screen,componentes,"Componentes",BLACK,WHITE,fuente2)
        dibujar_boton(screen,natural,"Natural",BLACK,GREEN,fuente1)
        dibujar_boton(screen,politico,"Político",BLACK,GREEN,fuente1)
        dibujar_boton(screen,cultural,"Cultural",BLACK,GREEN,fuente1)
        dibujar_boton(screen,social,"Social",BLACK,GREEN,fuente1)
        dibujar_boton(screen,economico,"Económico",BLACK,GREEN,fuente1)
    if pantallanatural == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,orografia,"Orografía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,hidrografia,"Hidrografía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,clima,"Clima",BLACK,GREEN,fuente1)
        dibujar_boton(screen,flora,"Flora",BLACK,GREEN,fuente1)
        dibujar_boton(screen,fauna,"Fauna",BLACK,GREEN,fuente1)
        dibujar_boton(screen,areasprotegidas,"Areas protegidas",BLACK,GREEN,fuente1)
    if pantallapolitico == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,escudo,"Escudo",BLACK,GREEN,fuente1)
        dibujar_boton(screen,municipios,"Municipios",BLACK,GREEN,fuente1)
        dibujar_boton(screen,superficie,"Superficie",BLACK,GREEN,fuente1)
        dibujar_boton(screen,cartografia,"Cartografía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,colindancias,"Colindancias",BLACK,GREEN,fuente1)
        dibujar_boton(screen,capital,"Capital",BLACK,GREEN,fuente1)
    if pantallasocial == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,poblacion,"Población Absoluta y Relativa",BLACK,GREEN,fuente1)
        dibujar_boton(screen,nata,"Natalidad y Mortalidad",BLACK,GREEN,fuente1)
        dibujar_boton(screen,espe,"Esperanza de vida",BLACK,GREEN,fuente1)
        dibujar_boton(screen,alfa,"Alfabetismo y Analfabetismo",BLACK,GREEN,fuente1)
        dibujar_boton(screen,idh,"Índice de Desarrollo Humano",BLACK,GREEN,fuente1)
    if pantallaeconomico == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,actecono,"Actividades Económicas",BLACK,GREEN,fuente1)
    if pantallacultural == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,siguientecultural,"->",BLACK,GREEN,fuente3)
        dibujar_boton(screen,traycos,"Tradiciones y costumbres",BLACK,GREEN,fuente1)
        dibujar_boton(screen,artesanias,"Artesanías",BLACK,GREEN,fuente1)
        dibujar_boton(screen,gastronomia,"Gastronomía",BLACK,GREEN,fuente1)
        dibujar_boton(screen,musica,"Música",BLACK,GREEN,fuente1)
        dibujar_boton(screen,lenguas,"Lenguas",BLACK,GREEN,fuente1)
    if pantallacultural2==True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        dibujar_boton(screen,traje,"Traje típico",BLACK,GREEN,fuente1)
        dibujar_boton(screen,personajes,"Personajes",BLACK,GREEN,fuente1)
        dibujar_boton(screen,leyendas,"Leyendas",BLACK,GREEN,fuente1)
    if pantallaorografia == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen1,(100,100))
        screen.blit(imagen2,(650,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallahidrografia == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen3,(100,100))
        screen.blit(imagen4,(650,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaclima == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen5,(200,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaflora == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen6,(200,1))
        screen.blit(imagen8,(200,300))
        screen.blit(imagen7,(650,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)

    if pantallafauna == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen9,(200,100))
        screen.blit(imagen10,(650,1))
        screen.blit(imagen11,(650,300))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaareasprotegidas == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen12,(100,100))
        screen.blit(imagen13,(650,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallacapital == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen14,(100,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallacolindancias == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen15,(100,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallamunicipios == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen16,(100,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallasuperficie == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen17,(100,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaescudo == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen18,(100,100))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallacartografia == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen19,(100,50))
        screen.blit(imagen20,(650,1))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaPOBLACIÓNABSOLUTAYRELATIVA == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen21,(100,200))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallanatalidadymortalidad == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen22,(100,200))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaesperanzadevida == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen23,(100,200))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaalfabetismoyanalfabetismo == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen24,(100,200))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaidh == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen25,(100,200))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaactecono == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen26,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallatraycos == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen27,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaartesanias == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen28,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallagastronomia == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen29,(650,400))
        render_multi_line(textogastronomia,150,50,30)
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallamusica == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen30,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallalenguas == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen31,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallatraje == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen32,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallapersonajes == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen33,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
    if pantallaleyendas == True:
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)
        screen.blit(imagen34,(100,150))
        dibujar_boton(screen,regresar,"<-",BLACK,GREEN,fuente3)

    if exitoso==False:
        print('Ejecución exitosa!')
        exitoso=True
    pygame.display.flip()

