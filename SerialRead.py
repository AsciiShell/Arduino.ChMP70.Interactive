import pygame
import serial
# Инициализируем движок
pygame.init()
ser = serial.Serial("COM5", 9600)
# Определяем цвета
aqua      = (  0, 255, 255)   # морская волна
black     = (  0,   0,   0)   # черный       
blue      = (  0,   0, 255)   # синий        
fuchsia   = (255,   0, 255)   # фуксия       
gray      = (128, 128, 128)   # серый        
green     = (  0, 128,   0)   # зеленый      
lime      = (  0, 255,   0)   # цвет лайма   
maroon    = (128,   0,   0)   # темно-бордовый
navy_blue = (  0,   0, 128)   # темно-синий  
olive     = (128, 128,   0)   # оливковый    
purple    = (128,   0, 128)   # фиолетовый   
red       = (255,   0,   0)   # красный      
silver    = (192, 192, 192)   # серебряный   
teal      = (  0, 128, 128)   # зелено-голубой
white     = (255, 255, 255)   # белый        
yellow    = (255, 255,   0)   # желтый       


# Задаем ширину и высоту экрана
size = [1000,800]
screen = pygame.display.set_mode(size)

# Установить заголовок окна
pygame.display.set_caption("Окно игры")

done=False
clock=pygame.time.Clock()

# Основной цикл программы
while done==False:
    # Пользователь что-то сделал
    for event in pygame.event.get():
        # Реагируем на действия пользователя
        if event.type == pygame.QUIT:
            done=True


    screen.fill(yellow)
    # Тут можно рисовать
    s = ser.readline()
    s = s.decode("utf-8").replace("\n","").replace("\r","")
    fontObj = pygame.font.SysFont('Arial', 400)
    textSurfaceObj = fontObj.render(s, True, yellow, blue)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (500, 400)

    screen.fill(white)
    screen.blit(textSurfaceObj, textRectObj)

    # Рисунок появится после обновления экрана
    pygame.display.flip()

    # Экран будет перерисовываться 30 раз в секунду
    clock.tick(30)

# Корректный выход
pygame.quit()
