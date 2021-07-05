from js import document

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