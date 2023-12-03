#!/usr/bin/env python

"""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.
"""
numbers = ["one","two","three","four","five","six","seven","eight","nine"]
number_starts = ['o','t','f','s','e','n']


def startsANumber(pos:int, target:str):    
    if target[pos] not in number_starts:        
        return None
    #possible number
    for n in numbers:                
        scanning = target[pos:len(n)+pos]        
        if len(scanning.strip())==0:
            return None                  
        if n in scanning:
            return convertNumber(n)        
        
def convertNumber(s:str):
    return numbers.index(s)+1

def extractAllNumbers(target:str):           
    result = []     
    for idx in range(len(target.strip())):                        
        if target[idx].isnumeric():
            result.append(int(target[idx]))
        else:
            b = startsANumber(idx, target)
            if b is not None:
                result.append(b)
                
    return result

running_total = 0
r = []
n = 1

with open("/home/rolex/dev/adventofcode-2023/day1/data.b.txt","r") as f:    
    for line in f:
        x = extractAllNumbers(target=line)        
        r.append([x[0],x[-1]])
        j = f"{x[0]}{x[-1]}"
        running_total = running_total + int(j)        
        print(f"{n} --> {x[0]}{x[-1]}")
        n +=1 

print(running_total)