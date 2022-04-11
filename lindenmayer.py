import re
import sys
import turtle as tr

from Stack import Stack

step = 20
ejeY = None
delta = None

turtle = None
regex_regla = re.compile(r'([a-zA-Z0-9]+)(\s*:\s)([\[\]\w\+\-]+)(\s*)$')

def iniciar_grafico():
	global turtle

	#turtle.position()
	turtle = tr.Turtle(visible = False)
	screen = tr.Screen()
	turtle.up()
	if ejeY == 0:
		turtle.setposition(0, 0)
	else:
		turtle.setposition(0, -screen.window_height()/2)
	turtle.left(90)
	turtle.showturtle()
	turtle.down()
	#print(screen.window_height(), screen.window_width())

def leer_reglas(archivo):
	global ejeY

	indice = 0
	palabra = ''
	reglas = {}
	delta = 0
	with open(archivo, 'r') as f:
		while True:
			if indice == 0:
				ejeY = float(f.readline())
				indice += 1
			elif indice == 1:
				delta = float(f.readline())
				indice += 1
			elif indice == 2:
				palabra = f.readline()
				indice += 1
			else:
				regla = f.readline()
				#print(regla)
				while regla:
					match = regex_regla.match(regla)
					if match:
						reglas[match.group(1)] = match.group(3)
					regla = f.readline()
				break

	return palabra, reglas, delta

def sustitucion(ciclos, palabra, reglas):
	temp = []
	indice = 0
	for i in range(ciclos):
		while len(palabra) > 0:
			valido = False
			for (regex, sucesor) in reglas.items():
				if(re.match(regex, palabra)):
					valido = True
					temp.append(sucesor)
					palabra = palabra[len(regex):]
					break

			#print(palabra, len(palabra))

			if not valido:
				temp.append(palabra[0])
				palabra = palabra[1:]

		palabra = ''.join(temp)
		temp = []

	return palabra

def simulacion(palabra):
	stack = Stack()

	for simbolo in palabra:
		if simbolo == 'F':
			turtle.forward(step)
		elif simbolo == '+':
			turtle.right(delta)
		elif simbolo == '-':
			turtle.left(delta)
		elif simbolo == '[':
			stack.push(turtle.heading(), turtle.position())
			#turtle.left(delta)
		elif simbolo == ']':
			angulo, posicion = stack.pop()
			turtle.setposition(posicion)
			turtle.setheading(angulo)
			#turtle.right(delta)

def main(args):
	global delta

	palabra, reglas, delta = leer_reglas(args[0])	
	palabra = sustitucion(int(args[1]), palabra, reglas)

	print(reglas)
	print(palabra)

	iniciar_grafico()
	simulacion(palabra)

	tr.exitonclick()

if __name__ == '__main__':
	main(sys.argv[1:])