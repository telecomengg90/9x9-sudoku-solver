# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:57:58 2020

@author: Dell
"""

# initialize a  9x9 board
# find the empty values(emtpy_grid_space) in the board
# spply possible solutions on the empty value
# backtrack


board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,0],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if check_board_validity(bo,i,(row,col)) == True:
            bo[row][col]=i
            
        
            if solve(bo) ==True:  #recursion
             return True
            else:       
             bo[row][col] = 0
        
    return False    
        
            

#check_board_validity(board,5,(1,5))
def check_board_validity(bo, entry, pos):      # checking if the current no fits according to the rules of sudoku
    for i in range(len(bo[0])):
        #check row
        if bo[pos[0]][i]==entry and pos[1]!=i:
            return False
        
    #check column 
    for i in range(len(bo)):
        if bo[i][pos[1]]==entry and pos[0]!=i:
            return False 
    box_y = pos[1] //3                      # check the little 3x3 grid that you're in 
    box_x = pos[0] //3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if bo[i][j]==entry and (i,j)!= pos:
                return False
    return True        
    
def print_board(bo):  #visualize the board (not important)
    for i in range(len(bo)):
        if i% 3==0 and i!=0:
            print("- - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | " , end= "")
            #if j==8:    
            print(bo[i][j] ,end = " ") 
        print("\n")    
            
       

def find_empty(bo):  # return the spot with a 0 
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None        

print_board(board)
print("------------------------------------------")
solve(board)
print_board(board)


            