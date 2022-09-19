# CS4750-7750-HW2
Artificial Intelligence HW2
Collaborators
    Ryan Christopher
    Olivia Shouse
    Luke Schaefer

Prompt
    Consider a 2-D 20-room vacuum-clearner world as follows:
        The world is a 2-D grid with 4x5 = 20 rooms, as shown below. The agent knows the environment and dirt distribution. This is a fully observable problem. 
        The agent can choose to move left (Left), right (Right), up (Up), down (Down), or suck up the dirt (Suck). Clean rooms stay clean. The agent cannot go outside the environment, i.e., the actions to bring the agent outside the environment are not allowed.
        Goal: clean up all dirt in the environment, i.e., make all rooms clean.
        Action Cost:
            a) 1.0 for Left
            b) 0.9 for Right
            c) 0.8 for Up
            d) 0.7 for Down
            e) 0.6 for Suck
