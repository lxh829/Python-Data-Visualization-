###  以下代码，如何保存tensorflow模型的方法，CKTP持久化模型
import tensorflow as tf
    #remember to define the same dtype and shape when restore
v1 = tf.Variable(tf.constant(1.0, shape=[1], name="v1"))
v2 = tf.Variable(tf.constant(2.0, shape=[1], name="v2"))
result = v1 + v2

init = tf.global_variables_initializer()

saver = tf.train.Saver()   #此命令声明 tf.train.Saver 类用于保存模型

with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "TensorFlow模型持久化/model.ckpt")  #将模型保存的文件目录
    print("Save to path: ", save_path)  #打印出保存的路径位置
###  此保存会出现4个文件
##  model.ckpt.meta   保存了tensorflow的计算图的结构(元图的数据),tensorflow通过元图(MetaGraph）来记录计算图中节点的信息以及运行计算图中所需要的元数据。
##  model.ckpt        保存了tensorflow中每一个变量的取值
##  checkpoint        保存了一个目录下所有的模型文件的列表





###  以下代码给出了加载这个已经保存的tensorflow模型的方法，调用CKTP持久化模型
import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0, shape=[1], name="v1"))
v2 = tf.Variable(tf.constant(2.0, shape=[1], name="v2"))
result = v1 + v2

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "TensorFlow模型持久化/model.ckpt")
    print (sess.run(result))
        ##  这段加载模型的代码基本上和保存模型的代码是一样的，与唯一的不同是，在加载模型的代码中没有运行变量的初始化过程
        ##  而是将变量的值通过已经保存的模型加载进来。如果不希望重复定义图上的运算，也可以直接加在已经持久化的图


### 直接加载已经持久化的图(比上面的简单)--代码如下--调用CKTP持久化模型
import tensorflow as tf
saver = tf.train.import_meta_graph("TensorFlow模型持久化/model.ckpt/model.ckpt.meta")
with tf.Session() as sess:
    saver.restore(sess, "TensorFlow模型持久化/model.ckpt")
    print (sess.run(tf.get_default_graph().get_tensor_by_name("add:0")))
