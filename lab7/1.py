import pygame
import datetime

pygame.init()
pygame.display.set_caption("AIUclock")

def rot_center(image, angle, x, y):
    rot_image = pygame.transform.rotate(image, angle)
    new_rect = rot_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rot_image, new_rect


H, W = 700, 700
screen = pygame.display.set_mode((H, W))
mickey = pygame.image.load("/Users/adilet/Desktop/PPHM/labs/lab7/assets/clock.png")
hand = pygame.image.load("/Users/adilet/Desktop/PPHM/labs/lab7/assets/min_hand.png")
hand1 = pygame.image.load("/Users/adilet/Desktop/PPHM/labs/lab7/assets/sec_hand.png")


mickey = pygame.transform.scale(mickey, (H, W))                                                                                                                                                                                                                                                                                     
hand = pygame.transform.scale(hand, (H / 2, W / 2))
hand1 = pygame.transform.scale(hand1, (H / 2, W / 2))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    x = (-6*minute) % 360
    y = ((-1)*second * 6) % 360

    rot_hand, x = rot_center(hand, x, H / 2, W / 2)
    rot_hand1, y = rot_center(hand1, y, H / 2, W / 2)
    screen.blit(mickey, (0, 0))
    screen.blit(rot_hand, x)
    screen.blit(rot_hand1, y)

    pygame.display.update()
clock.tick(60)
pygame.quit()

