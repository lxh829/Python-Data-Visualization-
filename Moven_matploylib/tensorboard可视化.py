import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):     # 新加

        with tf.name_scope('weight'):    #新加
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')

        with tf.name_scope('biases'):   #新加
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

        with tf.name_scope('Wx_plus_b'):    #新加
            Wx_plus_b = tf.matmul(inputs, Weights) + biases


        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise


with tf.name_scope('inputs'):        #新加
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')


l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

prediction = add_layer(l1, 10, 1,activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()


sess = tf.Session()

writer = tf.summary.FileWriter("xxx/", sess.graph)

sess.run(init)



for i in range(400):
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i % 100 == 0:


        print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))



## 在terminal中输入‘ tensorboard --logdir=logs’  敲击  ‘Enter’  ，会出现网址，复制 粘贴  即可

#  运行没成功，不知道怎么回事
