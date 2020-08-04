# Crossy MilkyWay
Created for ISS Course Assignment(IIIT Hyderabad - 2019).

## Instructions
1. Clone the GitLab Repository to your local machine.
2. Run the file **mainfinal.py** by doing this :  
        *python3 mainfinal.py*
3. The game will open in another window. Enjoy.

## Dependencies
***pygame*** must be already installed in your local machine. If you do not have it, follow what's given in the link below :  
https://inventwithpython.com/pygame/chapter1.html

## Rules and Design Choices
- The players will not die as soon as they collide with an obstacle, instead they would be awarded an extra penalty to the final time.
- The time compared will include the penalty time added.
- The scores will be reset after every round.
- The round winner's obstacle moving speed will be increased by two units each time.
- To put it simple, the fastest one to reach the other end with the least number of collisions will be declared as the winner.
- In case of a tie, the obstacle speed of both of the players will be increased.
- **Player 1** uses the **Arrow Keys**
- **Player 2** uses **W , S , A , D**
