class Move:

    def _initi_(self, initial ,final):
        #initial and final are squares 
        self.initial = initial 
        self.final = final 
    
    def __str__(self):
        s = ''
        s += f'({self.initial_col},{self.initial_row})'
        s += f'({self.final_col},{self.final_row})'
        return s

    def __eq__(self, other):
        return self.initial = other.initial and self.dinal == other.final