import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 800


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('2 cars')
clock = pygame.time.Clock()

blue = (25,25,112)
black = (0,0,0)
white = (255,255,255)

redcaImg = pygame.image.load('redcars.png')
bluecaImg = pygame.image.load('bluecars.png')
redciImg = pygame.image.load('redcir.png')
redsqImg = pygame.image.load('redsqr.png')
blueciImg = pygame.image.load('bluecir.png')
bluesqImg = pygame.image.load('bluesqr.png')
lineImg = pygame.image.load('line.jpg')

def things_dodged(count):
	font = pygame.font.SysFont(None,35)
	text = font.render(str(count),True,white)
	gameDisplay.blit(text,(550,0))

def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(texts):
	largeText = pygame.font.SysFont(None, 45)
	TextSurf, TextRect = text_objects(texts, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
					
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash(dodged) :
	message_display('Game Over & Score is ' + str(dodged))

def redcar(xr,yr):
	gameDisplay.blit(redcaImg,(xr,yr))

def bluecar(xb,yb):
	gameDisplay.blit(bluecaImg,(xb,yb))
	
def redcir(redcx,redcy):
	gameDisplay.blit(redciImg,(redcx,redcy))

def redsqr(redsx,redsy):
	gameDisplay.blit(redsqImg,(redsx,redsy))

def bluecir(bluecx,bluecy):
	gameDisplay.blit(blueciImg,(bluecx,bluecy))

def bluesqr(bluesx,bluesy):
	gameDisplay.blit(bluesqImg,(bluesx,bluesy))

def line(xll,yll):
	gameDisplay.blit(lineImg,(xll,yll))

def game_loop():
	xr= display_width * 1/15
	yr= display_height * 5/8
	xb= display_width * 49/60
	yb= display_height * 5/8
	xl1= display_width * 1/4
	xl2= display_width *1/2
	xl3 = display_width*3/4
	yl = 0
	
	dodged=0
	flagr=0
	flagb=0
	redcir_startx = random.randrange(0,2)
	if redcir_startx == 0:
		redcir_startx = display_width *  11/120
	else:
		redcir_startx = display_width * 41/120
	redcir_starty = -600

	redsqr_startx = random.randrange(0,2)
	if redsqr_startx == 0:
		redsqr_startx = display_width *  41/120
	else:
		redsqr_startx = display_width * 11/120
	redsqr_starty = -1000

	bluecir_startx = random.randrange(0,2)
	if bluecir_startx == 0:
		bluecir_startx = display_width * 71/120
	else:
		bluecir_startx = display_width * 101/120
	bluecir_starty = - 500

	bluesqr_startx = random.randrange(0,2)
	if bluesqr_startx == 0:
		bluesqr_startx = display_width * 101/120
	else:
		bluesqr_startx= display_width * 71/120
	bluesqr_starty = -900
	
	multiple=10
	speed = 4
	gameExit = False
	while not gameExit :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					if xb == display_width *49/60:
						xb=490
					elif xb == display_width*17/30:
						xb =490
				if event.key == pygame.K_LEFT:
					if xb == display_width*49/60:
						xb=340
					elif xb == display_width*17/30:
						xb = 340
				if event.key ==pygame.K_a:
					xr=40
				if event.key == pygame.K_d:
					xr=190
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
					xb=xb
					xr=xr

		gameDisplay.fill(blue)

		redcir(redcir_startx,redcir_starty)
		redsqr(redsqr_startx,redsqr_starty)
		bluecir(bluecir_startx,bluecir_starty)
		bluesqr(bluesqr_startx,bluesqr_starty)
	
		redcir_starty += speed
		redsqr_starty += speed
		bluecir_starty += speed
		bluesqr_starty += speed
		
		line(xl1,yl)
		line(xl2,yl)
		line(xl3,yl)
		redcar(xr,yr)
		bluecar(xb,yb)
		things_dodged(dodged)
		
		if dodged > multiple:
			speed+=1
			multiple = multiple + 15

		if xr == 40 and redcir_startx == 55 and flagr==0:
			if redcir_starty == 467:
				dodged+=1
				flagr=1
	
		if xr >150 and redcir_startx == 205 and flagr==0:
			if redcir_starty <630 and redcir_starty > 500:
				dodged+=1
				flagr=1

		if xr < 150 and redcir_startx == 55 and flagr==0:
			if redcir_starty <630 and redcir_starty >500 :
				dodged+=1
				flagr=1

		if xr == 190 and redcir_startx == 205 and flagr==0:
			if redcir_starty ==467:
				dodged+=1	
				flagr=1

		if xb == 340 and bluecir_startx == 355 and flagb==0:
			if bluecir_starty == 467:
				dodged+=1
				flagb=1

		if xb > 450 and bluecir_startx == 505 and flagb==0:
			if bluecir_starty <630 and bluecir_starty>500:
				dodged+=1
				flagb=1

		if xb < 450 and bluecir_startx == 355 and flagb==0:
			if bluecir_starty <630 and bluecir_starty>500:
				dodged+=1
				flagb=1

		if xb == 490 and bluecir_startx == 505 and flagb==0:
			if bluecir_starty == 467:
				dodged+=1
				flagb=1

		if xr == 40 and redcir_startx ==205 and flagr==0:
			if redcir_starty > 630:
				crash(dodged)
		if xr == 190 and redcir_startx ==55 and flagr==0:
			if redcir_starty > 630:
				crash(dodged)
		
		if xb == 340 and bluecir_startx ==505 and flagb==0:
			if bluecir_starty > 630:
				crash(dodged)

		if xb == 490 and bluecir_startx ==355 and flagb==0:
			if bluecir_starty > 630:
				crash(dodged)



		if xr == 40 and redsqr_startx == 55:
			if redsqr_starty == 467 :
				crash(dodged)
	
		if xr >150 and redsqr_startx == 205:
			if redsqr_starty <630 and redsqr_starty > 500:
				crash(dodged)

		if xr < 150 and redsqr_startx == 55 :
			if redsqr_starty <630 and redsqr_starty >500 :
				crash(dodged)

		if xr == 190 and redsqr_startx == 205:
			if redsqr_starty ==467:
				crash(dodged)

		if xb == 340 and bluesqr_startx == 355:
			if bluesqr_starty == 467:
				crash(dodged)

		if xb > 450 and bluesqr_startx == 505:
			if bluesqr_starty <630 and bluesqr_starty>500:
				crash(dodged)

		if xb < 450 and bluesqr_startx == 355:
			if bluesqr_starty <630 and bluesqr_starty>500:
				crash(dodged)

		if xb == 490 and bluesqr_startx == 505:
			if bluesqr_starty == 467:
				crash(dodged)

		if redcir_starty > display_height:
			redcir_starty = -100
			flagr=0
			redcir_startx = random.randrange(0,2)
			if redcir_startx == 0:
				redcir_startx = display_width *  11/120
			else:
				redcir_startx = display_width * 41/120
		
		if redsqr_starty > display_height:
			redsqr_starty = -200
			redsqr_startx = random.randrange(0,2)
			if redsqr_startx == 0:
				redsqr_startx = display_width *  11/120			
			else:
				redsqr_startx = display_width * 41/120
		

		if bluecir_starty > display_height:
			flagb=0
			bluecir_starty = -150
			bluecir_startx = random.randrange(0,2)
			if bluecir_startx == 0:
				bluecir_startx = display_width *  101/120
			else:
				bluecir_startx = display_width * 71/120
		if bluesqr_starty > display_height:
			bluesqr_starty = -100
			bluesqr_startx = random.randrange(0,2)
			if bluesqr_startx == 0:
				bluesqr_startx = display_width *  71/120
			else:
				bluesqr_startx = display_width * 101/120
	
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
