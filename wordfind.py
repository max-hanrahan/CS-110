"""
 *****************************************************************************
   FILE:        wordfind.py

   AUTHOR:      Max Hanrahan

   ASSIGNMENT:  Word Finder

   DATE:        10/8/2019

   DESCRIPTION: Given a grid and a list of words, the function detects the words
   that are in the grid and prints a version of the grid in which these words
   are capitalized. Collaborated with Ben Kallus (TA), Preston Comer, and
   Truffaut Harper.

 *****************************************************************************
"""

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]
def print_grid(grid):
    """ Display the grid in a nice way """
    for row in grid:
        print(row)


def wordfind(grid, words):
    """ For each word in words, if possible, find it once in the grid, case 
        insensitive.  Convert those found letters in the grid 
        to upper-case."""
    words_found = 0

    for word in words:
        first_letter_loc_list = []
        #iterate over rows and columns to find instances of the first letter
        #save a list of those locations
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c]).lower() == word[0]:
                    first_letter_loc_list.append((r, c))
                    #if the word is just one letter long, capitalize it in this loop
                    if len(word) == 1:
                         grid[r][c] = grid[r][c].upper()
                         words_found += 1

        for loc in first_letter_loc_list:
            for direc in directions:
                letter_two_row = loc[0] + direc[0]
                letter_two_col = loc[1] + direc[1]
                #check each direction and if the direction is valid AND leads to
                #the right word, keep iterating in that direction
                if is_in_bounds(grid, letter_two_row, letter_two_col) and (grid[letter_two_row][letter_two_col]).lower() == word[1]:
                    for let in range(1, len(word)):
                        #iterates over the rest of the word in the same direction
                        remaining_path_row = loc[0] + direc[0] * let
                        remaining_path_col = loc[1] + direc[1] * let
                        #if it's not a point on the grid or isn't equal to the 
                        #letter we're seeking, then STOP
                        if (not is_in_bounds(grid, remaining_path_row, remaining_path_col)) or ((grid[remaining_path_row][remaining_path_col]).lower() != word[let]):
                            break
                        #on the iteration of the last letter, capitalize the word and add one words_found
                        if let + 1 == len(word):
                            capitalize(grid, direc, loc, len(word))
                            words_found += 1

    return words_found


def capitalize(grid, direction, loc, length):
    """For specified locations in the grid, capitalize the value at that location.
    Iterates over the length of the word in that direction to capitalize the whole word."""
    for let in range(length):
        grid[loc[0] + direction[0] * let][loc[1] + direction[1] * let] = grid[loc[0] + direction[0] * let][loc[1] + direction[1] * let].upper()


def is_in_bounds(grid, r, c):
    """ Return True if (r, c) is a legal position within grid.
        Return False otherwise. """
    #If one of the coords is bigger than the grid or negative, it is false
    if (r >= len(grid)) or (c >= len(grid[0])) or r < 0 or c < 0:
        return False
    return True


def main():
    """ The main program is just for your own testing purposes.
        Modify this in any way you wish.  It will not be graded. """
    
    # my_grid = [['j', 'm', 'w', 'e'],
    #            ['e', 'e', 'p', 'p'],
    #            ['q', 'o', 'x', 'u'],
    #            ['w', 'w', 'e', 'd'],
    #            ['w', 'g', 'j', 'o']]
    # words = ['meow', 'wed', 'do', 'justice']
    my_grid = [['a']]
    words = ['a']
    count = wordfind(my_grid, words)
    print_grid(my_grid)
    print(count)


    return count

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
