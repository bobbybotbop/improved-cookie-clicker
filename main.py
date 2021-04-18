import turtle
import time

cps = 0
cookies = 0

cursor = 0
cursorPrice = 15

grandma = 0
grandmaPrice = 100

#window setup
s = turtle.Screen()
s.setup(width = 875,height = 550)

#second counter
starttime = time.time()


#cookie counter setup
counter = turtle.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-375,225)
counter.write("cookies:  " + str(int(cookies)), font = ("roberto",24))

#cps counter
cpsCounter = turtle.Turtle()
cpsCounter.hideturtle()
cpsCounter.speed(0)
cpsCounter.penup()
cpsCounter.goto(-375,175)
cpsCounter.write("cookies/second:  "+ str(cps) , font = ("roberto", 24))

#cookie drawer setup
c = turtle.Turtle()
c.hideturtle()
c.speed(0)

#shop setup
shop = turtle.Turtle()
shop.penup()
shop.speed(0)
shop.hideturtle()

#iconDrawer setup
iconDrawer = turtle.Turtle()
iconDrawer.penup()
iconDrawer.hideturtle()
iconDrawer.speed(0)

#cookie shop description
desc = turtle.Turtle()
desc.penup()
desc.speed(0)
desc.hideturtle()

#grandma shop description
desc2 = turtle.Turtle()
desc2.penup()
desc2.speed(0)
desc2.hideturtle()
desc2.rt(90)


def drawShopText():


  #cursor text
  cursorText()
  grandmaText()
  
def grandmaText():
  desc2.clear()

  desc2.goto(285, 125)
  desc2.write("grandma costs: " + str(grandmaPrice), font = ("roberto", 10))
  desc2.fd(20)
  desc2.write("1 cookie every", font = ("roberto", 10))
  desc2.fd(15)
  desc2.write("second", font = ("roberto", 10))
  desc2.lt(90)
  desc2.fd(100)
  desc2.write(str(grandma),  font = ("roberto", 35))
  desc2.rt(90)



def cursorText():
  desc.clear()

  desc.goto(280,185)
  desc.write("cursor costs: " + str(cursorPrice), font = ("roberto", 12))
  desc.goto(288,165)
  desc.write("1 cookie every ", font = ("roberto", 10))
  desc.goto(288,150)
  desc.write("5 seconds ", font = ("roberto", 10))

  desc.goto(385, 150)
  desc.write(str(cursor),  font = ("roberto", 35))

  desc.goto(280, 140)

def drawIcon():
  #cursor
  iconDrawer.goto(260,190)
  iconDrawer.rt(90)
  iconDrawer.pendown()
  iconDrawer.fd(30)
  iconDrawer.lt(180)
  iconDrawer.rt(60)
  iconDrawer.fd(10)
  iconDrawer.rt(90)
  iconDrawer.fd(15)
  iconDrawer.lt(90)
  iconDrawer.fd(7)
  iconDrawer.lt(90)
  iconDrawer.fd(15)
  iconDrawer.rt(90)
  iconDrawer.fd(10)
  iconDrawer.lt(115)
  iconDrawer.fd(30)

  #grandma
  iconDrawer.lt(125)
  iconDrawer.penup()
  iconDrawer.fd(80)
  iconDrawer.lt(90)
  iconDrawer.fd(10)
  iconDrawer.pendown()
  iconDrawer.circle(10)
  iconDrawer.rt(90)
  iconDrawer.fd(5)
  iconDrawer.rt(90)
  iconDrawer.fd(5)
  iconDrawer.rt(180)
  iconDrawer.fd(10)
  iconDrawer.rt(180)
  iconDrawer.fd(5)
  iconDrawer.lt(90)
  iconDrawer.fd(5)
  iconDrawer.lt(30)
  iconDrawer.fd(12)
  iconDrawer.rt(180)
  iconDrawer.fd(12)
  iconDrawer.lt(120)
  iconDrawer.fd(12)
  iconDrawer.hideturtle()

  

def drawShop():
  #draw rectangles
  shop.goto(250,200)
  shop.pendown()
  for i in range(4):
    for i in range(2):
      shop.fd(187)
      shop.rt(90)
      shop.fd(60)
      shop.rt(90)
    shop.rt(90)
    shop.fd(60)
    shop.lt(90)

  shop.penup()
  #draw the upgrades



def drawCookie():

  c.pendown()

  c.circle(50)

  c.penup()
  c.goto(-15,23)
  c.pendown()
  c.circle(3)
  c.penup()
  c.goto(-22, 35)
  c.pendown()
  c.circle(2)
  c.penup()
  c.goto(-15, 70)
  c.pendown()
  c.circle(4)
  c.penup()
  c.goto(10, 85)
  c.pendown()
  c.circle(3)
  c.penup()
  c.goto(2, 50)
  c.pendown()
  c.circle(2)
  c.penup()
  c.goto(17, 35)
  c.pendown()
  c.circle(3)
  c.penup()
  c.goto(10, 15)
  c.pendown()
  c.circle(3)

def cookieRefresh():
    counter.clear()
    counter.goto(-375,225)
    counter.write("cookies:  " + str(int(cookies)), font = ("roberto",24))

def cpsRefresh():
  cpsCounter.clear()
  cpsCounter.goto(-375,175)
  cpsCounter.write("cookies/second:  "+ str(cps) , font = ("roberto", 24))

def cookieClick(x, y):
  global cookies
  global cps
  global cursor
  global cursorPrice
  global grandmaPrice
  global grandma




#if click cookie
  if x >= -50 and x <= 50 and y >= 0 and y <= 100:
    cookies += 1
    cookieRefresh()

#if buy cursor
  if x > 250 and x < 437 and y > 140 and y < 200:
    if cookies >= cursorPrice:
      cookies -= cursorPrice
      cursor += 1
      cursorPrice = round(cursorPrice * 1.1)

      cursorText()
      cpsRefresh()
      cookieRefresh()

#if buy grandma
  if x > 250 and x < 437 and y > 80 and y  < 140:
    if cookies >= grandmaPrice:
      cookies -= grandmaPrice
      grandma += 1
      grandmaPrice = round(grandmaPrice * 1.1)

      grandmaText()
      cpsRefresh()
      cookieRefresh()




#every second, this fuction does stuff so cps stuff goes here
def tick():
  global cookies
  global cps

  if(cps > 0):
    cookies += cps
    cookieRefresh()



drawCookie()
drawShop()
drawIcon()
drawShopText()


s.onclick(cookieClick)

while True:

    #cps calc
  cps = (cursor * .2) + (grandma * 1)
  
#every second activates the tick function
  rntime = time.time()
  if (rntime - starttime) >= 1:
    tick()
    starttime = time.time()
    