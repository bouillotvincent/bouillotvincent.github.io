from js import document
import inspect

class Tortue:

	def __init__(self, context, x = 0, y = 0):
		self.x, self.y = x, y
		self.color = '#ff0000'
		self.width = 1
		self.style = '🐢'

	def pencolor(self, *args):
		if len(args) not in [0,1] : 
			raise TypeError(f"""{inspect.currentframe().f_code.co_name} takes 1 positional argument but {len(args)} were given""")
		if len(args) == 0:
			return self.color
		else:
			self.color = args
			
	def forward(self):
		context.fillStyle = self.color
		context.beginPath()
		context.moveTo(10, 10)
		context.lineTo(310, 310)
		context.stroke()

canvas = document.querySelector('canvas')
canvas.setAttribute('width', 640)
canvas.setAttribute('height', 480)
context = canvas.getContext("2d")
context.strokeStyle = "#df4b26"
context.lineJoin = "round"
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

Tortue(context)
