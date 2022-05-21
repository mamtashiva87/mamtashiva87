import sys, pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = width, height = 800, 400
speed = [1, 1]

speed1 = [0, 0]

#background = 255, 0, 255
canvas = pygame.display.set_mode((width,height))

pygame.display.set_caption("Bouncing balls")
bg = pygame.image.load("bg2.gif").convert()
canvas.blit(bg,(0,0))
ball = pygame.image.load("ball2.png")
ball = pygame.transform.scale(ball,(40,40))
ball1 = pygame.image.load("ball1.png")
ball1 = pygame.transform.scale(ball1,(40,40))

x = 0
y = 0
newImage=pygame.transform.scale(ball,(x,y))
canvas.blit(newImage,(20,20))
pygame.display.flip()

newImage1=pygame.transform.scale(ball1,(x,y))
canvas.blit(newImage1,(20,20))
pygame.display.flip()



ballrect = ball.get_rect()
ballrect1 = ball1.get_rect()

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

    ballrect = ballrect.move(speed)
    ballrect1 =ballrect1.move(speed1)
    canvas.blit(ball, ballrect)
    canvas.blit(ball1, ballrect1)

    if ballrect.left < 0 or ballrect.right > width:

       speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

       speed[1] = -speed[1]
       
       if ballrect1.left > 0 or ballrect1.right < width:

          speed1[0] = -speed1[0]

       if ballrect1.top > 0 or ballrect1.bottom < height:

         speed1[1] = -speed1[1]

   # canvas.fill(BLACK)

    
    pygame.display.update()