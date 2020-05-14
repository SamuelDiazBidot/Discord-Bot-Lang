# Discord-Bot-Lang

## Description:
Discord Bot lang is a dynamically typed language that facilitates the creation of discord bots. 
### Purpose:
The purpose of the Discord Bot lang is to allow a direct connection to the discord API 
which in turn facilitates the creation and deployment of simple discord bots. 
The language allows for the implementation of commands for the bot to follow.
### Features:
* Closure support
* Python3 core library 
* Easy discord bot prototyping
* Auto-generated command error handling 
### Examples:
simple counter bot:
```python
token('NzAxODA3MzU4NjYxMDk5NTgy.XrMWEA.D10sg4j1LjIhLJycz_rzaZVqr-4')

counter = 1

command inc() {
    global counter
    counter = counter + 1
}

command dec() {
    global counter
    counter = counter - 1
}

command show() {
    global counter
    send(counter)
}
```

## Installation:
### Requirements
PLY and Discord.py must be installed. To install all required dependencies run the following command.

```pip install -r requirements.txt```
### To Run:
```python3 main.py <file_path>```

