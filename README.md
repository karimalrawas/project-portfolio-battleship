# Battleship-of-Destiny

Battleship of Destiny is a Python terminal game, which runs on Heroku.
You can beat the game by sinking all of the computer's three battleships before the computer sinks yours. CI template has been used for essential files. 

[Here is the live project](https://project-portfolio-battleship.herokuapp.com/)


__How to play and Features__

- Based on the classic pen-and-paper game. You can read more about it on Wikipedia.
In this version, the board is set to 5x5, with three ships for both AI and user. 

- The player cannot see his ships to add an element of surprise and excitement, indicated by an 0, and of course cannot see where the computer's ships are either.

- Guesses are marked on the board with an X. Hits are indicated by
The player and the computer then take it in turns to make guesses and try to sink each other's battleships. 

- The score will be displayed after each round, to avoid having to scroll up each time. 

__Future Features__

 - The option to set board size and ship count



__Data Model__

- Board class has been used for this game.  


__Solved Bugs__ 

- I was getting an error message after first deployment to Heroku and was not able to login through gitpod terminal, but then I realized that I had to fix Nodes, Engine, and edit Config Vars in Heroku settings for the key: PORT and value: 8000, then the deployment worked as expected. 


__Testing__

- I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Tested in my Gitpod terminal and Heroku terminal

__Validator Testing__

  - No errors were returned from pep8ci.herokuapp.com



__Deployment__

- This project was deployed using Heroku.
-  Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy
Credits

__Credits__

I looked at a structure from a similar project from [Here is the live project](https://project-portfolio-battleship.herokuapp.com/)





