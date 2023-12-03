#!/usr/bin/env python
import regex
running_total = 0
with open("/home/rolex/dev/adventofcode-2023/day1/data.a.txt","r") as f:
    for line in f:
        r = regex.findall("([0-9]*)",line)                
        s = "".join(r)        
        v = int(s[0] + s[-1])
        running_total += v        
print(running_total)