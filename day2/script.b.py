#!/usr/bin/env python

from enum import Enum
import regex

class BallConfigs(Enum):
    RED = 12
    GREEN  = 13
    BLUE = 14

def load_data(inputs:str):
    pass


def get_min_set(game:str):
    return 0

def check_input_line(line:str):
    #get game id
    ids,data = line.split(':')
    m = regex.match("Game ([0-9]*)",ids)    
    id = int(m.groups()[0])
    games = data.split(';')            

    min_set = get_min_set(games)

    return 0

running_total = 0 
with open("/home/rolex/dev/adventofcode-2023/day2/data.b.txt","r") as f:    
    for line in f:
        running_total += check_input_line(line)

print(running_total)

