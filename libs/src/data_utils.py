import pandas as pd 
import numpy as np 
from typing import Literal 

class normalizer():

    def __init__(self,
                 df,
                 strategy : Literal['minMaxScaller', 'absMaxScaller'] = 'absMaxScaller' ):
        
        
        self.dict_abs_max = {c : df[c].apply(lambda x: np.abs(x)).max() for c in df.columns}
        self.dict_min = {c : df[c].min() for c in df.columns}    
        self.dict_max = {c : df[c].max() for c in df.columns}
        self.strategy = strategy
         
         
    def getDfcolumnNormalized(self, 
                              df):
        
        df_normalized = df.copy()

        if self.strategy == 'absMaxScaller':
            
            for c in df.columns:
                df_normalized.loc[:, c] = df_normalized.loc[:,c].apply(lambda x: x/self.dict_abs_max[c])

        if self.strategy == 'minMaxScaller':
            
            for c in df.columns:
                df_normalized.loc[:, c] = df_normalized.loc[:,c].apply(lambda x: (x - self.dict_min[c])/(self.dict_max[c] - self.dict_min[c]) )

        
        return df_normalized 
    

    def getDfcolumnDeNormalized(self,
                                df_normalized):
        
        
        df_normalized = df_normalized.copy()

        if self.strategy == 'absMaxScaller':
            
            for c in df_normalized.columns:
                df_normalized.loc[:, c] = df_normalized.loc[:,c].apply(lambda x: x*self.dict_abs_max[c])
        
        if self.strategy == 'minMaxScaller':
            for c in df_normalized.columns:
                df_normalized.loc[:, c] = df_normalized.loc[:,c].apply(lambda x: x * (self.dict_max[c] - self.dict_min[c]) + self.dict_min[c])

        return df_normalized 
    

