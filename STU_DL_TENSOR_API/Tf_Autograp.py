import tensorflow as tf

# 일반 함수
def my_function(x):
    return x**2
print(my_function(4))
print()

# autograph
@tf.function
def my_tf_function(x):
    return x**2

# 텐서형태로 리턴
print(my_tf_function(4))
print()

# 일반함수를 autograph 형태로 변환
my_convert_tf_my_function = tf.function(my_function)
print(my_convert_tf_my_function(4))
print()