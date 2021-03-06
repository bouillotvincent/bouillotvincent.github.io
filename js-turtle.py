from js import document, window
import inspect
from math import cos, sin, pi

class Turtle:

	def __init__(self, x = 0, y = 0, angle = 0):
		self.x, self.y = x, y
		self.angle = angle
		self.color = 'red'
		self.width = 2
		self.style = 'classic'
		self.canvas = document.querySelector('canvas')
		self.ctx = document.querySelector('canvas').getContext("2d")
		self.__set_default()
		self.state = dict()

	def __set_default(self):
		self.ctx.lineJoin = "miter"
		self.ctx.lineCap = "round"
		# self.ctx.shape = self.shape(self.style)  # to be checked


	def rad2deg(self, angle):
		return angle / pi *180

	def deg2rad(self, angle):
		return angle / 180 * pi

	def pencolor(self, *args):
		if len(args) not in [0,1] : 
			raise TypeError(f"""{inspect.currentframe().f_code.co_name} takes 1 positional argument but {len(args)} were given""")
		if len(args) == 0:
			return self.color
		else:
			self.color = args
			self.ctx.strokeStyle = self.color

	def pensize(self, width = None):
		self.ctx.lineWidth = width

	def shape(self, style = None):
		dico_style = {'arrow' : '➡︎', 'turtle' : '🐢', \
					  'circle' : '●', 'square' : '■', \
					  'triangle' : '▶︎', 'classic': '➤'}
		self.style = dico_style[style]

	def forward(self, L):
		self.state[f"""self._{inspect.currentframe().f_code.co_name}"""] = [self.angle, L]
		# self.ctx.beginPath()
		# self.ctx.moveTo(self.x, self.y)
		# self.ctx.lineTo(self.x + L * cos(self.deg2rad(self.angle)), \
		# 				self.y + L * sin(self.deg2rad(self.angle)))
		# self.ctx.stroke()
		# self.x += L * cos(self.deg2rad(self.angle))
		# self.y += L * sin(self.deg2rad(self.angle))
	
	def _forward(self, L, current_L=1):
		# if current_L < L:
		self.ctx.beginPath()
		self.ctx.moveTo(self.x, self.y)
		self.ctx.lineTo(self.x + L * cos(self.deg2rad(self.angle)), \
						self.y + L * sin(self.deg2rad(self.angle)))
		self.ctx.stroke()
			# return current_L + 1
		# else :
		self.x += L * cos(self.deg2rad(self.angle))
		self.y += L * sin(self.deg2rad(self.angle))

	def fd(self, L):
		self.forward(L)

	def right(self, angle):
		self.angle += angle

	def left(self, angle):
		self.angle -= angle

	def tick(self):
		# Clear canvas
		self.ctx.clearRect(0, 0, self.canvas.width, self.canvas.height)

		# Draw current state
		for command, vars in self.state.items() :
			a, L = vars
			eval(command)(L)


	def mainloop(self):
		self._animate()

	def _animate(self):
		self.tick()
		window.requestAnimationFrame(self._animate())

canvas = document.querySelector('canvas')
canvas.setAttribute('width', 640)
canvas.setAttribute('height', 480)
context = canvas.getContext("2d")

pen = False
lastPoint = (0, 0)

def onmousemove(e):
	global lastPoint
	if pen:
		newPoint = (e.offsetX, e.offsetY)
		context.beginPath()
		context.moveTo(lastPoint[0], lastPoint[1])
		context.lineTo(newPoint[0], newPoint[1])
		context.closePath()
		context.stroke()
		lastPoint = newPoint
	
def onmousedown(e):
	global pen, lastPoint
	pen = True
	lastPoint = (e.offsetX, e.offsetY)
  
def onmouseup(e):
	global pen
	pen = False

canvas.addEventListener('mousemove', onmousemove)
canvas.addEventListener('mousedown', onmousedown)
canvas.addEventListener('mouseup', onmouseup)

fred = Turtle()
