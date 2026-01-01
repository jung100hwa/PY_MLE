import tensorflow as tf

x = tf.constant([2, 4, 6])
y = tf.constant([2, 5, 6])

# 결과가 요소마다 True, False로 표시된다.
result = tf.math.equal(x, y)
print(result)

print("#" * 50)

# 텐서와 스칼라 비교(브로드캐스트 적용)
x = tf.constant([6, 8, 12, 2])
y = 2
result = tf.math.equal(x, y)
print(result)
