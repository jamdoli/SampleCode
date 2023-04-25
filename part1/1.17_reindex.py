# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 인덱스를 [r0, r1, r2, r3, r4]로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

# reindex로 발생한 NaN값을 숫자 0으로 채우기
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)

ndf3 = df[:]
print(ndf3.index)
ndf3.index = ['rr0', 'rr1', 'rr2']
print(ndf3.index)
print(ndf3)
# ValueError: Length mismatch: Expected axis has 3 elements, new values have 5 elements
# ndf3.index = ['rr0', 'rr1', 'rr2', 'rr3', 'rr4']

new_index2 = ['r0', 'rr1', 'r2']
ndf4 = df.reindex(new_index2)
print(ndf4)