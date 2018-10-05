#1.维度shape的理解
#2.tf.reduce_sum()的理解

#   tf.reduce_sum(input_tensor,axis=None,keepdims=None,name=None,reduction_indices=None,keep_dims=None)
#  reduce:坍塌,也就是降维的意思   axis：是从轴的索引位置将为
#
import tensorflow as tf


matrix1 = tf.constant([ [[1,2], [3,4]], [[5,6], [7,8]], [[5,6], [7,8]] ])
matrix2 = tf.constant([   [[2], [4], [6]], [[8], [10], [12]], [[14], [16], [18]]   ])
matrix3 = tf.constant([    [ [1,2,3,4],[5,4,2,3],[8,4,2,3] ],  [ [4,2,3,5],[7,8,9,6],[5,4,3,5] ]   ])
matrix4 = tf.constant([ [ [[1,2], [3,4]] ], [ [[3,4], [5,6]] ] ])

matrix5 =tf.constant( [  [[[1,2],[2,3]],[[1,2],[2,3]]]  ,  [[[1,2],[2,3]],[[1,2],[2,3]]]  ])

### shape是张量维度，dim是二阶张量(矩阵)的尺寸
#  维度是用来索引一个多维数组中某个具体数所需要最少的坐标
# shape=(z,m,n)   z:几个m*n的矩阵z就是几;m行,n列,z个


#  axis是轴，axis是多维数组每个维度的坐标,tensorflow是从0开始索引的
# matrix = [ [[1,2], [3,4]], [[5,6], [7,8]], [[5,6], [7,8]] ]
# 在上面的三位数组中数字‘3’的坐标(0,1,0)      从左往右-从0开始检索；从上往下-从0开始检索
# 找到‘3’所在二维矩阵在这个三维立方的索引：从左往右,‘3’在第0个矩阵中，索引值‘0’
#找到‘3’所在一维数组在这个二维矩阵的索引：从上往下，‘3’在第1个数组中，索引值‘1’
#找到‘3’所在零维数组(这个数)在这个这个一维向量的索引：从左往右，‘3’在第零个位置，索引值‘0’

sess = tf.Session()
a = matrix1.get_shape()
b = matrix2.get_shape()
c = matrix3.get_shape()
d = matrix4.get_shape()
e = matrix5.get_shape()

print(a)
print(b)
print(c)
print(d)
print(e)


#练习  对于三维数组，分别计算axis=0,1,2
#注 axis=0，是列，axis=1，是行
import tensorflow as tf

a = tf.constant([ [[1,2], [3,4]], [[5,6], [7,8]] ])
b = tf.reduce_sum(a, reduction_indices=[0])
c = tf.reduce_sum(a, reduction_indices=[1])
d = tf.reduce_sum(a, reduction_indices=[2])
        # reduction_indiced = axis  如今是一模一样的，没什么区别，2者都可以使用
sess = tf.Session()
q = sess.run(b)
w = sess.run(c)
e = sess.run(d)

print(q)
print(w)
print(e)
#练习  对于四维数组，分别计算axis=0,1,2,3
import tensorflow as tf

matrix = tf.constant( [  [[[1,2],[2,3]],[[1,2],[2,3]]]  ,  [[[1,2],[2,3]],[[1,2],[2,3]]]  ])


a = tf.reduce_sum(matrix, axis=[0])    #[  [[[2,4],[4,6]],[[2,4],[4,6]]]
b = tf.reduce_sum(matrix, axis=[1])    #[  [[[2,4],[4,6]]]  ,  [[[2,4],[4,6]]]  ]
c = tf.reduce_sum(matrix, axis=[2])    #[  [[[3,5]],[[3,5]]]  ,  [[[3,5]],[[3,5]]]  ]
d = tf.reduce_sum(matrix, axis=[3])    # [  [[[3],[5]],[[3],[5]]]  ,  [[[3],[5]],[[3],[5]]]  ]


sess = tf.Session()


A = sess.run(a)
B = sess.run(b)
C = sess.run(c)
D = sess.run(d)

print(A)
print(B)
print(C)
print(D)
