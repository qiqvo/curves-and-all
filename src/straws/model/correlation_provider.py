

import numpy as np


class CorrelationProvider():
    def __init__(self, corr_dict=None):
        self.corr_dict = corr_dict
        self.validate()

    def validate(self):
        if self.corr_dict is None:
            self.corr_dict = dict()
            return 
        
        keys = list(self.corr_dict.keys())
        for key in keys:
            if key[0] == key[1]:
                if self.corr_dict[key] != 1:
                    raise ValueError("Diagonal elements of correlation matrix should be 1")
            if key[0] != key[1]:
                if (key[1], key[0]) not in self.corr_dict:
                    self.corr_dict[(key[1], key[0])] = self.corr_dict[key]
                elif self.corr_dict[key] != self.corr_dict[(key[1], key[0])]:
                    raise ValueError("Correlation matrix is not symmetric")
                
        keys = list(self.corr_dict.keys())
        for key in keys:
            self.corr_dict[(key[0], key[0])] = 1
            self.corr_dict[(key[1], key[1])] = 1
                    

    def set_matrix(self, corr_matrix, names):
        n = len(names)
        for i in range(n):
            for j in range(n):
                self.corr_dict[(names[i], names[j])] = corr_matrix[i, j]
                self.corr_dict[(names[j], names[i])] = corr_matrix[i, j]
    
    def set_dict(self, corr_dict):
        self.corr_dict = self.corr_dict | corr_dict
        self.validate()

    def get_corr(self, name1, name2):
        return self.corr_dict[(name1, name2)]
    
    def get_corr_matrix(self, names):
        n = len(names)
        corr_matrix = np.eye(n)
        for i in range(n):
            for j in range(i, n):
                corr_matrix[i, j] = self.corr_dict[(names[i], names[j])]
                corr_matrix[j, i] = corr_matrix[i, j]

        return corr_matrix