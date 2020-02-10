import os
import sys

import pygame
import requests

response = None
coords = input("Ведите координаты:").strip()
spn = input("Введите масштаб:").strip()
map_request = "http://static-maps.yandex.ru/1.x/?ll=" + coords + '&spn=' + spn + "&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
while pygame.event.wait().type != pygame.QUIT:
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()

os.remove(map_file)
