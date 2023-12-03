#!/usr/bin/env python

from enum import Enum
import regex

class BallConfigs(Enum):
    RED = 12
    GREEN  = 13
    BLUE = 14

def load_data(inputs:str):
    pass

def is_game_valid(data:str):    
    
    get_red = regex.search(" ([0-9]*) red*",data)        
    get_blue = regex.search(" ([0-9]*) blue*",data)
    get_green = regex.search(" ([0-9]*) green*",data)

    valid = True        

    if (get_red is not None):                
        valid = valid and int(get_red.groups()[0]) <= BallConfigs.RED.value
    
    if (get_blue is not None):        
        valid = valid and int(get_blue.groups()[0]) <= BallConfigs.BLUE.value
    
    if (get_green is not None):        
        valid = valid and int(get_green.groups()[0]) <= BallConfigs.GREEN.value
    
    return valid

def check_input_line(line:str):
    #get game id
    ids,data = line.split(':')
    m = regex.match("Game ([0-9]*)",ids)    
    id = int(m.groups()[0])
    games = data.split(';')
    
    input_line_is_valid = True    
    
    for game in games:
        input_line_is_valid = input_line_is_valid and is_game_valid(game)
    
    if (input_line_is_valid):
        return id
    else:
        print(f"INVALID GAME {id}")
    return 0

running_total = 0 
with open("/home/rolex/dev/adventofcode-2023/day2/data1.txt","r") as f:    
    for line in f:
        running_total += check_input_line(line)

print(running_total)

