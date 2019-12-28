#Escopo de importações
import turtle
import random
import time
import winsound

#Escopo de variaveis globais
velocidade = 15

#--- campo de registro de imagens
turtle.register_shape('bg.gif')

#Escopo de classes e funções

#-- criando a classe do pássaro
class Bird(turtle.Turtle):
	#registrado imagens da animação do passaro
	turtle.register_shape('bird_1.gif')
	turtle.register_shape('bird_2.gif')
	turtle.register_shape('bird_3.gif')
	turtle.register_shape('bird_4.gif')
	
	#construtor da classe
	def __init__(self):
		super().__init__()
		self.speed(0)
		self.pu()
		self.shape('bird_1.gif')
		
	#função de animação do voo e da queda do passaro
	def animar(self):
		frames =('bird_1.gif', 'bird_2.gif','bird_3.gif','bird_4.gif')
		gravidade =-10 
		for i in range(len(frames)):
			self.shape(frames[i])
		self.sety(self.ycor()+gravidade)
	
	#função que responde à barra de espaço, fazendo o passaro pular
	def pular(self):
		força = 40
		self.sety(self.ycor()+força)
	
#--criando a classe do chão (base)	
class Base(turtle.Turtle):
	turtle.register_shape('base.gif')
	def __init__(self):
		super().__init__()
		self.speed(0)
		self.pu()
		self.shape('base.gif')
		self.setpos(225,-250)
	
	#função que movimenta a base no eixo x
	def movimenta(self,velocidade):
		if self.xcor() > -675:
			self.setx(self.xcor()-velocidade)
		 
	
#--criando classe canos
class Cano(turtle.Turtle):
	turtle.register_shape('cano.gif')
	turtle.register_shape('cano_cima.gif')
	
	def __init__(self, forma, x, y):
		super().__init__()
		self.speed(0)
		self.pu()
		self.setpos(x,y)
		if forma ==0:
			self.shape('cano.gif')
		elif forma ==1:
			self.shape('cano_cima.gif')
	
	#função que movimenta os canos 
	def movimenta(self,velocidade):
		if self.xcor() > -250:
			self.setx(self.xcor()-velocidade)
		
		
	
	
	
#Escopo de objetos
janela = turtle.Screen()
janela.setup(450,600,0,0)
janela.title('FlapPy Bird - Turtle ')
janela.bgpic('bg.gif')
bird = Bird()
janela.listen()
janela.onkey(bird.pular,'space')

cano = Cano(0,150,-250)
cano2 = Cano(1,150,250)
base = Base()


#loop do jogo (mani_game_loop)

while True:
	bird.animar()
	base.movimenta(velocidade)
	cano.movimenta(velocidade)
	cano2.movimenta(velocidade)
	

janela.mainloop()
