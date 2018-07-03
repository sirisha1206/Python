import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
session = tf.Session()
A = tf.constant([1,5,3,2],shape=[2,2])
B = tf.constant([1,7,4,2],shape=[2,2])
C = tf.constant([3,4,5,9],shape=[2,2])

D = tf.pow(A,2)#power of A and save it to D
E = tf.add(D,B)# add A * A to B and save it in E
F = tf.multiply(E,C)#multiply E and C and save it to F

print(session.run(F))#print the result
session.close()