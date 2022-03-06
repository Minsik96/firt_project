from gettext import npgettext
import numpy


import numpy as np

probs = np.array([1,8,2,3,5,4])
print("probs : ",probs)
idxs = np.argsort(probs)
print("indexs : ",idxs)

how = probs[idxs]
print("what R U : ",how)

 # 크기가 작은 -> 큰 순서 : 