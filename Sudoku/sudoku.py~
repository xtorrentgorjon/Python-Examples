#!/usr/bin/env python

#    Copyright (C) 2015  Xavier Torrent Gorjon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


__author__ = "Xavier Torrent Gorjon"
__email__ = "sendotux@gmail.com"
__copyright__ = "Copyright 2015"

__license__ = "GPL"
__version__ = "1.0"


class Cell(object):
    """Cell Object
    
    Represents a cell in a sudoku board. It includes the actual value of the
    cell (0 if empty), and the range of values that could fit in that cell
    (only used for empty cells).
    """
    def __init__(self, value=0):
        self.__value = value
        self.__possibilities = range(1,10)
        
    def get_value(self, i=0):
        """Returns the data of the cell. Can return the actual value, the
        possible values, or both.
        """
        if i == 0:
            return self.__value
        elif i == 1:
            return self.__possibilities
        else:
            return (self.__value, self.__possibilities)
    
    def set_value(self, new_value):
        self.__value = new_value
    
    def rm_possibility(self, pos):
        self.__possibilities.remove(pos)
        
    def __str__(self):
        return str(self.__value)
    
    def __repr__(self):
        return str(self)

   
class sudoku(object):
    """Sudoku Object
    
    Represents a sudoku board in a 9x9 matrix format using Cell objects.
    """
    def __init__(self, matrix_in=None):
        if not matrix_in:
            self.__matrix = [[Cell(0)]*9]*9
        else:
            self.__matrix = []
            for col in matrix_in:
                column = []
                for element in col:
                    column.append(Cell(element))
                self.__matrix.append(column)
    
    def print_sudoku(self):
        for row in self.__matrix:
            print row
            
    def get_element(self, x, y):
        return self.__matrix[y][x].get_value(2)
            
    def get_row(self, row_num):
        return self.__matrix[row_num]
        
    def get_column(self, column_num):
        col = []
        for row in self.__matrix:
            col.append(row[column_num])
        return col
    
    def get_mini_square(self, x, y):
        m_square = []
        columns = range(y*3, y*3+3)
        for col in columns:
            m_square.append(self.__matrix[col][x*3:x*3+3])
        return m_square
        
    def set_element(self, new_value, x, y):
        self.__matrix[y][x] = new_value
        
    def check_list(self, l):
        """Given a list of Cells (either in a column, row or 3x3 square),
        removes invalid possibilities from each one of them.
        """
        for element in l:
            if element.get_value(0) != 0:
                search_value = element.get_value(0)
                for j in range(9):
                    if search_value in l[j].get_value(1):
                        l[j].rm_possibility(search_value)
                        
    def check_row(self, y):
        row = self.get_row(y)

        self.check_list(row)
            
    def check_column(self, x):
        col = self.get_column(x)
        
        self.check_list(col)
        
    def check_mini_square(self, x, y):
        sqr = self.get_mini_square(x, y)
        square_line = []
        for mini_line in sqr:
            square_line = square_line + mini_line
            
        self.check_list(square_line)
        
        # This part also sets values to cells using a very simple deduction.
        # It should be done on a different function to keep consistency.
        # But... yeah.
        
        poss_list = []
        for element in square_line:
            if element.get_value(0) == 0:
                poss_list.append(element)
        
        for i in range(1,10):
            count = 0
            for poss in poss_list:
                if i in poss.get_value(1):
                    count += 1
            if count == 1:
                for element in poss_list:
                    if i in element.get_value(1):
                        element.set_value(i)
        
    def check_everything(self):
        for i in range(9):
            self.check_row(i)
        for i in range(9):
            self.check_column(i)
        for i in range(3):
            for j in range(3):
                self.check_mini_square(i, j)
                
    def try_solve_element(self, x, y):
        """Checks all sudoku cells. If a cell has only one possibility, it
        applies it.
        """
        if self.__matrix[y][x].get_value(0) == 0:
            if len(self.__matrix[y][x].get_value(1)) == 1:
                self.__matrix[y][x].set_value(
                    self.__matrix[y][x].get_value(1)[0])
        
        
                
    def check_sudoku_solved(self):
        """Checks if all of the sudoku cells are filled."""
        for i in range(9):
            for j in range(9):
                if self.__matrix[j][i].get_value(0) == 0:
                    return False
        return True
        
        
                
    def solve_sudoku(self):
        """Main iterator. If the sudoku solutions have not changed in one
        iteration, the iteration stops as the algorithm has reached a situation
        that cannot solve.
        """
        last_it = hash(str(self.__matrix))
        while self.check_sudoku_solved() == False:
            self.check_everything()
            for i in range(9):
                for j in range(9):
                    self.try_solve_element(j,i)
                    
            if hash(str(self.__matrix)) == last_it:
                
                print "-------"
                for j in self.__matrix:
                    for i in j:
                        if i.get_value(0) == 0:
                            print i.get_value(2)
                    print "NEWLINE"
                print "-------"
                break
            else:
                last_it = hash(str(self.__matrix))
                    
        
        
if __name__ == "__main__":
    """This implementation can solve sudokus of easy to mid-high complexity.
    Sudokus requiring 'equation solving' cannot be solved with this code.
    """
    # test 1 EASY
    """
    matrix = [[0,0,8,6,0,0,0,3,0],
            [0,5,0,0,7,3,0,9,4],
            [0,3,0,8,4,5,0,0,0],
            [0,0,0,0,0,1,9,4,0],
            [2,8,1,0,0,0,6,5,7],
            [0,9,7,5,0,0,0,0,0],
            [0,0,0,4,5,6,0,7,0],
            [6,2,0,3,8,0,0,1,0],
            [0,7,0,0,0,2,3,0,0]]
    """
    
    # test 2 MEDIUM
    """
    matrix = [[0,0,0,0,8,6,2,0,0],
            [0,8,0,0,0,0,9,0,4],
            [0,7,0,0,1,0,5,0,0],
            [0,0,0,6,9,0,0,0,0],
            [0,0,2,8,0,1,4,0,0],
            [0,0,0,0,5,3,0,0,0],
            [0,0,8,0,4,0,0,1,0],
            [6,0,7,0,0,0,0,2,0],
            [0,0,5,7,6,0,0,0,0]]
    """
    
    # test 3 HARD -- Cannot solve.
    matrix = [[0,0,0,0,0,0,0,2,0],
            [0,0,9,0,0,1,0,0,4],
            [2,4,3,9,0,0,0,0,0],
            [0,6,4,7,1,0,0,0,0],
            [0,0,1,0,0,0,5,0,0],
            [0,0,0,0,4,8,6,3,0],
            [0,0,0,0,0,2,3,6,9],
            [9,0,0,6,0,0,4,0,0],
            [0,3,0,0,0,0,0,0,0]]    
    
    a = sudoku(matrix)
    a.print_sudoku()
    print "========="    
    a.solve_sudoku()
    a.print_sudoku()

