# Name: Brad D. LaMontagne
# Class: Artificial Intelligence Section 02

# Simple Reflex agent that moves to user's mouse cursor using pygame
import pygame
import numpy as np
from Classes import Agent

screen = pygame.display.set_mode((800, 800))
running = True

# Start coordinates
aX = 100
aY = 100

robotImage = pygame.image.load('rover.png')
robotImage = pygame.transform.scale(robotImage, (100, 100))

agentPOS = [aX - 50, aY - 50]

srAgent = Agent.Agent()

while running:
    # pause the program for 5 miliseconds
    pygame.time.wait(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the mouse cursor position
    mousePOS = pygame.mouse.get_pos()

    # get the new agent position
    aX, aY = srAgent.changePOS(np.array(mousePOS), agentPOS, screen, robotImage)

    agentPOS = [aX, aY]

    # update the environment
    pygame.display.update()
