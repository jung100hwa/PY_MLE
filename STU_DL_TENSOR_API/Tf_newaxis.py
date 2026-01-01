import tensorflow as tf

rank_4_tensors = tf.zeros(shape = [2,3,4,5])
print(rank_4_tensors)
print('DataType of every element:',rank_4_tensors.dtype)
print('Number of dimensions : ',rank_4_tensors.ndim)
print('Shape of tensors: ',rank_4_tensors.shape)
print('Elements along the 0 axis',rank_4_tensors.shape[0])
print('Elements along the last axis',rank_4_tensors.shape[-1])
print('Total number of elements in our tensor: ',tf.size(rank_4_tensors).numpy())


rank_2_tensors = tf.constant([[10,7],[3,4]])
print(rank_2_tensors)

rank_3_tensors = rank_2_tensors[...,tf.newaxis]
print(rank_3_tensors)