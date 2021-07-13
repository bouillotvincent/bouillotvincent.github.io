from js import document
import inspect
from math import cos, sin, pi
import time
class Turtle:

	def __init__(self, context, x = 0, y = 0, angle = 0):
		self.x, self.y = x, y
		self.angle = angle
		self.color = '#ff0000'
		self.width = 1
		self.style = 'classic'
		self.ctx = context
		self.__set_default()
		self.state = {}

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

	# def forward(self, L):
	# 	self.state.append((self._forward, self.x, self.y, self.angle, L))

	def forward(self, L):
		self.ctx.beginPath()
		self.ctx.moveTo(self.x, self.y)
		i = 1
		while i < L :
			self.ctx.lineTo(self.x + cos(self.deg2rad(self.angle)), \
						self.y + sin(self.deg2rad(self.angle)))			
			self.x = self.x + cos(self.deg2rad(self.angle))
			self.y = self.y + sin(self.deg2rad(self.angle))
			self.ctx.stroke()
			i+=1
	
	def fd(self, L):
		self.forward(L)

	def right(self, angle):
		self.angle += angle

	def left(self, angle):
		self.angle -= angle
	
	# def mainloop(self, L, current_L = 0):
	# 	if current_L != L:
	# 		current_L += 1
	# 		self.forward(current_L)
	# 		time.sleep(100)
	# 		self.mainloop(current_L, L)

canvas = document.querySelector('canvas')
canvas.setAttribute('width', 640)
canvas.setAttribute('height', 480)
context = canvas.getContext("2d")
context.strokeStyle = "red"
context.lineWidth = 5
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

fred = Turtle(context)
