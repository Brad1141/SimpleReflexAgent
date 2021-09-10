import pygame

class Agent:
    speed = 5

    def changePOS(self, mousePOS, agentPOS, screen, robotImage):
        # do not update the agent's position if the mouse cannot be found
        if mousePOS.all() == None:
            return agentPOS

        newPOS = [0, 0]

        # calculate new position for the agent
        if agentPOS[0] < mousePOS[0]:
            newPOS[0] = agentPOS[0] + 5
        else:
            newPOS[0] = agentPOS[0] - 5

        if agentPOS[1] < mousePOS[1]:
            newPOS[1] = agentPOS[1] + 5
        else:
            newPOS[1] = agentPOS[1] - 5

        # make sure agent does not go out of bounds
        if 50 > newPOS[0] or newPOS[0] > 750:
            newPOS[0] = agentPOS[0]

        if 50 > newPOS[1] or newPOS[1] > 750:
            newPOS[1] = agentPOS[1]

        # update environment and return new agent position for the next cycle
        screen.fill((175, 238, 238))
        screen.blit(robotImage, (newPOS[0] - 50, newPOS[1] - 50))
        return newPOS
