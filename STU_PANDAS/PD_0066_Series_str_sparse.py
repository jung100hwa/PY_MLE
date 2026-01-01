import pandas as pd
from scipy import sparse
import numpy as np

# sparse 희소행렬. 대부분이 0으로 채워진 행렬
# dense 밀집행렬. 대부분이 0이 아닌 값으로 채워진 행렬

# 희소행렬은 메모리 낭비가 심하기 때문에 0 이 아닌 행렬로 표시하는 방법 중 COO, CSR 방식이 있다.

# 내용이 너무 어려우니 제일 아래 부분을 참고로 하면 된다.
    
s = pd.arrays.SparseArray([0, 0, 1, 1, 2], fill_value=0)
print(s)

# non fill_value 개수
print(s.npoints)

# non fill_value 비율
print(s.density)

# fill_value 지정된 값
print(s.fill_value)

# non fill_value값들. 즉 여기서는 0 이 아닌값
print(s.sp_values)

# coo 매트리스 생성, 함수의 인자 형태를 알아 둘 필요가 있다.
A = sparse.coo_matrix(([3.0, 1.0, 2.0], ([1, 0, 0], [0, 2, 3])), shape=(3, 4))

# 원래의 매트리스
print(A.toarray())

# coo 매트리스를 생성하면
print(A)

# dense 매트리스, array 똑 같이 나오네
print(A.todense())

# 결국 판다스에서는 sci에서 coo 매트리스를 표현하면 중복된 행의 값은 표시를 안하는 정도??
ss = pd.Series.sparse.from_coo(A)
print(ss)


s2 = pd.Series([3.0, np.nan, 1.0, 3.0, np.nan, np.nan])
s2.index = pd.MultiIndex.from_tuples(
    [
        (1, 2, "a", 0),
        (1, 2, "a", 1),
        (1, 1, "b", 0),
        (1, 1, "b", 1),
        (2, 1, "b", 0),
        (2, 1, "b", 1),
    ],
    names=["A", "B", "C", "D"],
)
print(s2)

ss = s2.astype("Sparse")
print(ss)

A, rows, columns = ss.sparse.to_coo(
    row_levels=["A", "B"], column_levels=["C", "D"], sort_labels=True
)
print(A)

print(A.todense())


################################### 위의 내용이 너무 어렵다. 아래의 수위 예제를 보자

################# 희소행렬을 coo 매트리스
data = np.array([3, 1, 2])

# 행 위치와 열 위치를 각각 array로 생성, "(로우, 컬럼) 값 " 이런형태로 행렬을 만듬
row_pos = np.array([0, 0, 1])
col_pos = np.array([0, 2, 1])


# sparse 패키지의 coo_matrix를 이용하여 COO 형식으로 희소 행렬 생성
sparse_coo = sparse.coo_matrix((data, (row_pos, col_pos)))

print(type(sparse_coo))
print(sparse_coo)

# 즉 위의 행렬을 아래의 배열로 만든다.
dense01 = sparse_coo.toarray()
print(dense01)


################# 희소행렬을 csr 매트리스
# csr 매트리스는 coo의 반복성을 줄이기 위해. 이것을 더 많이 쓴다.
dense2 = np.array(
    [
        [0, 0, 1, 0, 0, 5],
        [1, 4, 0, 3, 2, 5],
        [0, 6, 0, 3, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 8],
        [1, 0, 0, 0, 0, 0],
    ]
)

# 0 이 아닌 데이터 추출
data2 = np.array([1, 5, 1, 4, 3, 2, 5, 6, 3, 2, 7, 8, 1])

# 행 위치와 열 위치를 각각 array로 생성
# 아래 행을 보면 결국 0이 아닌값의 행의 위치가 반복적이고 순차적으로 증가한다는 특성이 있음
# csr는 행의 위치값에 대한 시작 인덱스만 기재하고 마지막에 총개수를 추가한다.
# 0의 시작위치는 0, 1의 시작위치는 2, 2의 시작위치는 7...그리고 마지막에 총 개수 13
row_pos = np.array([0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5])
col_pos = np.array([2, 5, 0, 1, 3, 4, 5, 1, 3, 0, 3, 5, 0])

# COO 매트릭스로 표시해 보면
# sparse_coo3 = sparse.coo_matrix((data2, (row_pos, col_pos)))
# print(sparse_coo3)
# dense3 = sparse_coo3.toarray()
# print(dense3)


# 행 위치 배열의 고유한 값들의 시작 위치 인덱스를 배열로 생성
row_pos_ind = np.array([0, 2, 7, 9, 10, 12, 13])


# CSR 형식으로 변환
sparse_csr = sparse.csr_matrix((data2, col_pos, row_pos_ind))

print(sparse_csr)

print("COO 변환된 데이터가 제대로 되었는지 다시 Dense로 출력 확인")
print(sparse_coo.toarray())

print("CSR 변환된 데이터가 제대로 되었는지 다시 Dense로 출력 확인")
print(sparse_csr.toarray())
