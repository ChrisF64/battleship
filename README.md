        B B B B        A      T T T T T  T T T T T  L          E E E E E    S S S S  H       H    I    P P P P
        B       B    A   A        T          T      L          E          S          H       H    I    P       P
        B       B  A       A      T          T      L          E          S          H       H    I    P       P
        B B B B    A A A A A      T          T      L          E E E        S S S    H H H H H    I    P P P P
        B       B  A       A      T          T      L          E                  S  H       H    I    P
        B       B  A       A      T          T      L          E                  S  H       H    I    P
        B B B B    A       A      T          T      L L L L L  E E E E E  S S S S    H       H    I    P



# Battleship

![Battleship Mockup Images](assets/readme_files/responsive.png)

[View the live project here](https://battleship-chrisf64-45141827d49d.herokuapp.com/)

## Table of contents
1. [Introduction](#Introduction)
    1. [How To Play](#How-To-Play)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features) 
    1. [Imagery](#Imagery)
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
    1. [Testing User Stories](#Testing-User-Stories)
    2. [Manual Testing](#Manual-Testing)
    3. [Automated Testing](#Automated-Testing) 
        - [Code Validation](#Code-Validation)
    4. [User Testing](#User-Testing)
7. [Deployment](#Deployment)
    1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
8. [Credits](#Credits)
    1. [Content](#Content)
    2. [Media](#Media)
    3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***


## Introduction

For PP3 Python Essentials, the developer built a battleship game. Although similar to the original player versus computer battleship game, this one is played only by the player. The computer randomly places 10 ships on a 10 x 10 grid and the player has to target them with missiles. The objective is to destroy the computers fleet.

### How To Play

- When the game begins, the player is requested to enter their name and choose a difficulty.
- Depending on the chosen difficulty, the player will have 80, 70, 60 or 50 missiles to launch.
- The computer randomly places 10 ships on the play board, occupying 20 spaces.
- Ships will be placed horizontally or vertically, but not diagonally.
- The player enters coordinates and launches a missile.
- The game logs how many missiles have been used and how many remain.
- If the player destroys all enemy ships before using all missiles, the player wins.
- If the player uses all missiles and all enemy ships have not been destroyed, the player loses.
- The rules of the game can be accessed at any time by entering '?'.

[Back to top ⇧](#battleship)

## UX
### Ideal User Demographic
The ideal user for this website is:
* New user
* Current user

#### New User Goals
1. As a new user, I want to see clear instructions for gameplay. 
2. As a new user, I want to see a visual representation of my remaining Shots.
3. As a new user, I want the ability to replay the game.

#### Current User
1. As a current user, I want the ability to replay the game.
2. As a current user, I want the guess and hit the various ships.
3. As a current user, I want the choice to use different ship sizes. 

### Development-Planes
To create a command-line application that allows the user to play a classic game Battleships or Sea Battle is a strategy type guessing game for two players.

#### Strategy
Strategy incorporates user needs as well as product objectives. This website will focus on the following target audience, divided into three main categories:
- **Roles:**
    - New users
    - Current users

- **Demographic:**
    - All ages
    - All puzzle playing levels

- **Psychographic:**
    - Lifestyles:
        - Interest in games
        - Interest in battles
        - Interest in Ships
        - Interest in puzzles
    - Personality/Attitudes:
        - Focused
        - Forward-Thinking
        - Creative
    
The application needs to enable the **user** to:
- play the game "Battleship" using alpha characters and numbers.
- generate a random board on each play-through placing ships in different locations.
    

#### Scope
The scope plane is about defining requirements based on the goals established on the strategy plane. Using the information in the strategy plane, the identified required features have been broken into the following two categories.
- Content Requirements:
    - The user will be looking for:
        - Clear and concise instructions.
        - A consistent theme, and game play. 
- Functionality Requirements:
    - The user will be able to:
        - Enter co-ordinates using numbers and letters.
        - Replay the game.
        - End the program at the end of the game.

#### Structure
The project will be deployed to a Heroku terminal. There will be no styling aside from the image of Funny Bones built using special characters within the terminal. 

#### Skeleton
A flowchart was created to show the logic the functions would follow.

<details>
<summary>Flowchart</summary>

![Flowchart](assets/readme_files/battleship-flowchart.jpeg)

</details>

[Back to top ⇧](#battleship)
