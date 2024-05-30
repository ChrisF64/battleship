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
    1. [The Welcome Message](#The-Welcome-Message)
    2. [The Game](#The-Game)
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
1. As a new user, I want to see the rules of the game and clear instructions for gameplay. 
2. As a new user, I want to see a visual representation of how many missiles I've launched and my remaining missiles.
3. As a new user, I want the ability to replay the game.

#### Current User
1. As a current user, I want the ability to replay the game.
2. As a current user, I want to guess and hit the various ships.
3. As a current user, I want see where the ships are at the end of the game. 

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
        - Interest in strategy
        - Interest in puzzles
    - Personality/Attitudes:
        - Focused
        - Forward-Thinking
        - Creative
    
The application needs to enable the **user** to:
- play the game "Battleship" using alpha characters and numbers.
- generate a random board on each play-through placing ships in different locations.
    

#### Scope
Using the information in the strategy plane, the identified required features have been broken into the following two categories.
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
The project will be deployed to a Heroku terminal, with no styling. 

#### Skeleton
A flowchart has been created to demonstrate the logic the functions will follow.

<details>
<summary>Flowchart</summary>

![Flowchart](assets/readme_files/battleship-flowchart.jpeg)

</details>

[Back to top ⇧](#battleship)

## Features

### The Welcome Message
- When a new game starts, the welcome message is displayed

  ![Welcome](assets/readme_files/Screenshot_01.png)


- The user is prompted to enter their name and asked if they are familiar with the rules

    ![Rules](assets/readme_files/Screenshot_02.png)


- If the user is not familiar with the rules, the rules are presented and the user is then asked to select a difficulty level

    ![Difficulty](assets/readme_files/Screenshot_03.png)


- The user is then prompted to press enter to set up the playing field

    ![Play-Field](assets/readme_files/Screenshot_04.png)


### The Game

- Once the board has been set up, the user is reminded that they can review the rules at any time by pressing '?' and is prompted to enter coordinates for first target

    ![Target](assets/readme_files/Screenshot_05.png)


- Each field on the play board has a coordinate marked on it, e.g. 'H4'

- Ships that have been hit will show up as **@@@@** and fields that were targeted but no ships were hit will show up as **----**



- If the missile has successfully hit a ship, it is displayed in the terminal

    ![Hit](assets/readme_files/Screenshot_06.png)


- Similarly, if a missle doesn't successfully hit a ship, it is displayed in the terminal

    ![Miss](assets/readme_files/Screenshot_08.png)


- Missile launch count and remaining missile count is displayed to the user, along with current amount of hits, and amount of hits remaining to win the game

    ![Missiles](assets/readme_files/Screenshot_07.png)


- When a ship has been completely destroyed, the user is notified of which ship has been sunk

    ![Sunk](assets/readme_files/Screenshot_10.png)


- If coordinates outside of the play board are chosen, the user will be notified

    ![Incorrect](assets/readme_files/Screenshot_12.png)


- If coordinates are chosen that have already been targeted, the user will be notified

    ![Already](assets/readme_files/Screenshot_13.png)


- If all ships are sunk, the user wins the game. However, if all missiles are used and ships still remain on the board, the user loses

    ![Loseer](assets/readme_files/Screenshot_14.png)


- When the game ends, the user is asked if they would like to play another round

    ![Another](assets/readme_files/Screenshot_15.png)


- If the user chooses yes, the game begins all over again. If the user chooses no, the game presents a farewell message

    ![Farewell](assets/readme_files/Screenshot_16.png)


