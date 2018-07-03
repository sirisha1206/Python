import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
session = tf.Session()
A = tf.constant([1,5,3,2],shape=[2,2])
B = tf.constant([1,7,4,2],shape=[2,2])
C = tf.constant([3,4,5,9],shape=[2,2])

D = tf.pow(A,2)
E = tf.add(D,B)
F = tf.multiply(E,C)

print(session.run(F))