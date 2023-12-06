#!/usr/bin/env python
import regex

class MinBallCount:
    RED = 0
    BLUE = 0
    GREEN = 0    
    def __repr__(self) -> str:
        return f"R: {self.RED} G:{self.GREEN} B:{self.BLUE}"


def get_game_ball_count(data:str):    

    get_red = regex.search(" ([0-9]*) red*",data)        
    get_blue = regex.search(" ([0-9]*) blue*",data)
    get_green = regex.search(" ([0-9]*) green*",data)

    red_count = 0
    blue_count = 0
    green_count = 0    

    if (get_red is not None):                
        red_count = int(get_red.groups()[0])
    
    if (get_blue is not None):        
        blue_count = int(get_blue.groups()[0]) 
    
    if (get_green is not None):        
        green_count = int(get_green.groups()[0]) 
    
    return [red_count, blue_count, green_count]

def check_input_line(line:str):
    #get game id
    _,data = line.split(':')        
    games = data.split(';')
    m = MinBallCount()    
    
    for game in games:
        t = get_game_ball_count(game)
        m.RED = max(t[0], m.RED)
        m.BLUE = max(t[1], m.BLUE)
        m.GREEN = max(t[2], m.GREEN)

    return m.RED * m.BLUE * m.GREEN        

running_total = 0 

with open("/home/rolex/dev/adventofcode-2023/day2/data.txt","r") as f:    
    for line in f:
        running_total += check_input_line(line)        

print(running_total)

