# pygame_project
Игра-арканоид на Python
Название: Arcadia

Используемые внешние модули:
    pygame
    random  
    
--------------------------------    
    import pygame as pg
    from random import randrange
    
    ball = pg.Rect(randrange(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    background = pg.image.load('background.jpg').convert()
--------------------------------

Основной модуль:
    Имя: main.py
    Содержание: код проекта, содержит всю механику игры.
Дополнительные файлы:
    background.jpg - фон игры
    requirements.txt - список внешних зависимостей
    readme.md - описание проекта, инструкция
    
Инструкция по установке внешних модулей:
    1. Перейти в директорию, в которой находится проект;
    2. Скопировать путь к нему;
    3. Перейти в командную строку (win+R > cmd > Enter);
    4. Написать cd + путь к проекту;
    5. Написать pip install pygame.
