import numpy as np
from keras.layers import Embedding , Reshape , Merge
from keras.models import Sequential

class MatrixFactor(Sequential):
    def __init__(self,n_users,m_items,k_factors,**kwargs):
        p = Sequential()
        p.add(Embedding(n_users,k_factors,input_length=1))
        p.add(Reshape((k_factors,))
              
        Q = Sequential()
        Q.add(Embedding(m_items, k_factors, input_length=1))
        Q.add(Reshape((k_factors,)))      
              
        super(CFModel, self).__init__(**kwargs)
              
        self.add(Merge([P, Q], mode='dot', dot_axes=1))
              
              
              
    def rate(self, user_id, item_id):
        return self.predict([np.array([user_id]), np.array([item_id])])[0][0]          