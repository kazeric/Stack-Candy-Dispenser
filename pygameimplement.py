import pygame 
import math
#stack Implementation 
class Stacky:
    
    def __init__(self) :
        self._data = []
    
    def len(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self, value):
        self._data.append(value)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self._data.pop()
        
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self._data[-1]



#initialise the stack
Eric  = Stacky()



#pygame implementation
pygame.init()
screen = pygame.display.set_mode((850,600))
#button constraints
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 0, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36
#buttons 
font = pygame.font.Font(None, FONT_SIZE)
buttonPush_text = "PUSH"
buttonPop_text = "POP"
buttonLen_text = "LEN"
buttonEmpty_text = "EMPTY?"
buttonTop_text = "TOP"




# Define button rectangles
buttonPush_rect = pygame.Rect(500, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
buttonPop_rect = pygame.Rect(650, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
buttonLen_rect = pygame.Rect(650, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
buttonEmpty_rect = pygame.Rect(500, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
buttonTop_rect = pygame.Rect(500, 300, BUTTON_WIDTH, BUTTON_HEIGHT)

#define case 
candyCase = pygame.Rect(100 ,100, 100, 500)
lid = pygame.image.load("./semicircle.png")
lid = pygame.transform.scale(lid, (100,100))
rotated_lid = pygame.transform.rotate(lid, 270)

# Initialize button click flags
buttonPush_clicked = False
buttonPop_clicked = False
buttonLen_clicked = False
buttonEmpty_clicked = False
buttonTop_clicked = False

#function to draw the button
def draw_button(button_rect, text, clicked):
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    if is_hovered:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    if clicked:
        pygame.draw.rect(screen, (0, 255, 0), button_rect, 3)  # Draw a green border when clicked



#text input
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(650,300,100,50)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
active = False


#does not work with elementary os 
# pygame.display.set_caption("Candy Dispenser")
# icon = pygame.image.load("./candy.png")
# pygame.display.set_icon(icon)


#players
#create static Players
springImg= pygame.image.load("./spring.png")
SpringMinHeight = 100
springHeight = 100
springWidth = 90
SPRING_SIZE = (90,100)
springImg = pygame.transform.scale(springImg, (springWidth,springHeight))
springx = 100
springy = 500
springpos= 500


#player detail lists
pygameImgL = []
playerx =  []
playery = []
ImgText = []

#append static players
pygameImgL.append(springImg)
playerx.append(springx)
playery.append(springy)

#keep count of player to be implemented 
number = 0

    
#function to determine collisions
def isCollision(x1,y1,x2,y2):
    distance = math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2)))
    if distance < 45:
        return True
    else:
        return False
    
#initialise cotrollers for candy movement
falling = False 
remove = False

   
        


running = True
while running:
    
    screen.fill((255,255,255))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttonPush_rect.collidepoint(event.pos):
                    buttonPush_clicked = True
                if buttonPop_rect.collidepoint(event.pos):
                    buttonPop_clicked = True 
                if buttonLen_rect.collidepoint(event.pos):
                    buttonLen_clicked=True                   
                if buttonEmpty_rect.collidepoint(event.pos):
                    buttonEmpty_clicked=True            
                if buttonTop_rect.collidepoint(event.pos):
                    buttonTop_clicked=True  
                if input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode  
                    
                    
    #text input implement 
    if active:
        color = color_active
    else:
        color = color_passive
        
    pygame.draw.rect(screen,color,input_rect,2)
    
    text_surface = base_font.render(user_text, True, (0,0,0))
    screen.blit(text_surface, (input_rect.x +5, input_rect.y + 15))
    input_rect.w = max(100,text_surface.get_width() + 10)
    
    #draw the candy case 
    pygame.draw.rect(screen,(0,0,0),candyCase,5)   
 
    
    #players implement 
    #rescale the spring 
    # it is here instead of at comperssion because we need to use it when blitting
    
    scaled_spring = pygame.transform.scale(pygameImgL[0],(springWidth,springHeight) )
    #blit image first and the text next so that the text can be superimposed onto the image 
    for i in range (len(pygameImgL)):
        if i == 0:
            screen.blit(scaled_spring,(playerx[i],playery[i])) 
        else:   
            screen.blit(pygameImgL[i],(playerx[i],playery[i]))
        
        
    # used the image co-ordinates for the x and y to sure the image and text are always attatched 
    for i in range (len(ImgText)):    
        screen.blit(ImgText[i], (playerx[i+1],playery[i+1]))
        
    #collisions and falling 
    collision2 = isCollision(playerx[number-1],playery[number-1],playerx[number],playery[number])
    
    #compress spring
    if collision2 and springHeight>SpringMinHeight and playery[0]>springpos:
        springHeight -= 1
        #lower the other candies in the stack as well
        for i in range (len(playery)):
            playery[i] += 1
        
    #spring flexion    
    if remove and springHeight<SpringMinHeight:
        springHeight += 1
        for i in range (len(playery)):
            playery[i] -= 1
            
            
    #pushing functionality 
    if falling == True and collision2 == False:
            #prevent unwanted clicks on the push before the last push is complete 
            buttonPush_clicked = False 
            #perform the falling functionality 
            playery[number] += 0.2
            
    #reset the falling attribute to enable the lid to close        
    if collision2 == True:
        falling = False        
            
    #popping functionality 
    if remove:
        #prevent unwanted clicks on the pop before the last pop is complete 
        buttonPop_clicked = False
        if playery[-1]>0:
            playery[-1] -= 0.7
        if playery[-1]<50:
            playerx[-1] -= 0.3
            playery[-1] -=0.3 
        if playerx[-1] <-50:
            remove = False 
            playerx.pop()
            playery.pop()
            pygameImgL.pop()
            ImgText.pop()
            number -=1
            user_text = ''
    
    #lid functionality     
    if falling:
        screen.blit(rotated_lid,(170,10))
    elif remove:
        screen.blit(rotated_lid,(170,10))
    else:
        screen.blit(lid,(100,24))            
    # if falling or remove:
    #     if collision2 == False:
    #         screen.blit(rotated_lid,(170,10))
    # elif collision2 == True:
    #     screen.blit(lid,(100,24))
    # else:
    #     screen.blit(lid,(100,24))
        
    
    # Draw buttons
    draw_button(buttonPush_rect, buttonPush_text, buttonPush_clicked)
    draw_button(buttonPop_rect, buttonPop_text, buttonPop_clicked)
    draw_button(buttonLen_rect, buttonLen_text, buttonLen_clicked)
    draw_button(buttonEmpty_rect, buttonEmpty_text, buttonEmpty_clicked)
    draw_button(buttonTop_rect, buttonTop_text, buttonTop_clicked)
    
    # Handle button actions
    if buttonPush_clicked:
        #prevent people from pushsing stack is empty or if theres no user input
        if user_text == "Stack is empty" or user_text=='' or user_text=='Stack is Full':
            #reset user text
            user_text=''
            buttonPush_clicked = False 
        #prevent it from candy overflow
        elif playery[number]<120:
            user_text='Stack is Full'
            buttonPush_clicked = False 
        else:
            #reduce spring height for spring compression
            springpos -= 5
            SpringMinHeight -=5
            #deactivate the poping functionality and fllexing of spring which may interfere with pushing
            remove = False
            # activate popping functionality 
            falling = True 
            #update the count for player creation 
            number+=1
            #push the user text to stack
            Eric.push(user_text)
            #create the player image 
            pygameImg = pygame.image.load("./candy.png")
            DEFAULT_IMAGE_SIZE = (50, 50)
            pygameImg = pygame.transform.scale(pygameImg, DEFAULT_IMAGE_SIZE)
            pygameImgL.append(pygameImg)
            playerx.append(120) 
            playery.append(-50)
            #create the lable for the players 
            text_surface = font.render(user_text, True, (0,0,0))
            #important to save lable in a list or it will disapear on refresh 
            ImgText.append(text_surface)
            #remove the user text once pushing is done
            user_text = ''
        buttonPush_clicked = False  # Reset the flag
        

    if buttonPop_clicked:
        print("Poped!")
        #dont pop the spring
        if len(pygameImgL)==1:
            user_text = str(Eric.pop())
        else:
            user_text = "Popped "+ str(Eric.pop())
        #check stack is empty  
        if user_text == "Stack is empty":
            remove = False
        else:
            #activate spring flexion and poping functionality
            remove= True
            #update the spring height for spring flextion
            springpos += 5
            SpringMinHeight +=5
            
        buttonPop_clicked = False  # Reset the flag
    
    if buttonLen_clicked:
        #display length
        user_text = str(Eric.len())
        # Add functionality for Button 2 here
        buttonLen_clicked = False  # Reset the flag
        
    if buttonEmpty_clicked:
        #display status
        user_text = str(Eric.is_empty())
        # Add functionality for Button 2 here
        buttonEmpty_clicked = False  # Reset the flag    

    if buttonTop_clicked:
        #display top
        user_text= str(Eric.top())
        # Add functionality for Button 2 here
        buttonTop_clicked = False  # Reset the flag     


    pygame.display.update()
    