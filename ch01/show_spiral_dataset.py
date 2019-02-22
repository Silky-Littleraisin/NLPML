import sys
sys.path.append('..')
import spiral 
import matplotlib .pyplot as plt 

x,t = spiral.load_data()
print('x',x.shape) #(300,2)
print ('t',t.shaps) #(300,3)
