#!/usr/bin/python3
"""IslandPerimeterProblem
"""


defisland_perimeter(grid):
"""
Calculatestheperimeteroftheislanddescribedingrid
Args:
grid:2dlistofintegerscontaining0(water)or1(land)
Return:
theperimeteroftheisland
"""

p=0
foriinrange(len(grid)):
forjinrange(len(grid[i])):
if(grid[i][j]==1):
if(i<=0orgrid[i-1][j]==0):
p+=1
if(i>=len(grid)-1orgrid[i+1][j]==0):
p+=1
if(j<=0orgrid[i][j-1]==0):
p+=1
if(j>=len(grid[i])-1orgrid[i][j+1]==0):
p+=1
returnp
