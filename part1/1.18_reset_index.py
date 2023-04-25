# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 행 인덱스를 정수형으로 초기화 
ndf = df.reset_index()
print(ndf)

new_idx = ['rr0', 'rr1', 'rr2']
# TypeError: reindex() got an unexpected keyword argument "inplace"
# ndf.reindex(new_idx, inplace = True)
ndf = ndf.reindex(new_idx)
print(ndf)

# 행 인덱스를 정수형으로 초기화 
ndf2 = df.reset_index()
print(ndf2)
ndf2.index = new_idx 
print(ndf2)
ndf3 = ndf2.reset_index()
print(ndf3)
ndf3.index = new_idx 
print(ndf3)
# ValueError: cannot insert level_0, already exists
# ndf4 = ndf3.reset_index()
# print(ndf4)