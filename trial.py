import pygame
import time
import random
#to initialize python:
pygame.init()

white = (255,255,255)
black=(0,0,0)
red = (255,0,0)
green=(0,155,0)
#To store the console window. Remember to pass a tuple.
display_width=800
display_height=600
GameDisplay = pygame.display.set_mode((display_width,display_height))

#Same as update but updates the entire console not just the changes.
#pygame.display.flip()

font=pygame.font.SysFont(None,25)

def snake(char_width,char_height, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(GameDisplay, black, [XnY[0], XnY[1], char_width,char_height])

def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    GameDisplay.blit(screen_text, [display_width/2-220, display_height/2-50])

#To set the game title on console window:
pygame.display.set_caption('Slither')

char_height=10
char_width=10
GameSensitivity=10
FPS=20

clock = pygame.time.Clock()     #To set the number of frames per second

#Game loop:
def gameloop():    
    lead_x=display_width/2            #Starting position of moving character
    lead_y=display_height/2
    lead_x_change=0         #Change in position per frame
    lead_y_change=0

    snakelist = [] 
    snakelength=1
    gameExit = False
    gameover=False
    randApple_x= round(random.randrange(0, display_width-char_width)/10.0)*10.0
    randApple_y= round(random.randrange(0,display_height-char_height)/10.0)*10.0       
    while not gameExit :
        while gameover==True:
            GameDisplay.fill(white)
            message_to_screen("Game Over. Press C to play again or Q to exit", red)
            pygame.display.update()
            for event in pygame.event .get():
                if event.type==pygame.QUIT:
                    gameover=False
                    gameExit=True
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameover=False
                    if event.key == pygame.K_c:
                        gameloop() 
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:       #when the X button is pressed 
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change-=GameSensitivity               #sensitivity-needs less processing-better than changing fps
                    lead_y_change=0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change+=GameSensitivity    
                    lead_y_change=0
                elif event.key == pygame.K_UP:
                    lead_y_change-=GameSensitivity                #sensitivity-needs less processing-better than changing fps
                    lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    lead_y_change+=GameSensitivity
                    lead_x_change=0     
    #  if event.type == pygame.KEYUP:
        #        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #           lead_x_change=0
        if lead_x>=(display_width-char_width+1) or lead_x<0 or lead_y>=(display_height-char_height+1) or lead_y<=0:
            gameover= True  

        lead_x+=lead_x_change
        lead_y+=lead_y_change

        
        snakehead = []

        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]


        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover=True
            
        GameDisplay.fill(white)                         #To fill the background color in console
        #pygame.draw.rect(GameDisplay, red, [400,300,10,10])  #To draw a rectangle (surface,color,[x,y,width,height])
        AppleThickness=10
        pygame.draw.rect(GameDisplay, red, [randApple_x,randApple_y,AppleThickness,AppleThickness])
        snake(char_width,char_height, snakelist)
        pygame.display.update()                         #To update the display screen after changes are made
        
           
                
        if(lead_x >= randApple_x and lead_x <= randApple_x+AppleThickness):
           if(lead_y >= randApple_y and lead_y <= randApple_y+AppleThickness):
              randApple_x= round(random.randrange(0, display_width-char_width)/10.0)*10.0
              randApple_y= round(random.randrange(0,display_height-char_height)/10.0)*10.0
              snakelength += 1
    
    
        clock.tick(FPS)                                  #clock.tick(fps)
    #End of while loop
    pygame.quit()
    #To update the changes on the screen:
    #pygame.display.update()

gameloop()
    
#To uninitialize pygame and quit Pygame:



#To quit the program itself(check with IDLE to get it cleared):
#quit() or 
#sys.exit()

