
###通过以下代码整个tensorflow的计算图可以统一的存放在一个文件中，保存为PB格式的持久化模型
import tensorflow as tf
from tensorflow.python.framework import graph_util

v1 = tf.Variable(tf.constant(1.0, shape=[1], name="v1"))
v2 = tf.Variable(tf.constant(2.0, shape=[1], name="v2"))
result = v1 + v2

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)

    graph_def = tf.get_default_graph().as_graph_def() #导出当前计算图的GraphDef部分，只需要这一部分就可以完成从输入层到输出层的计算
                                                      # 返回的图将是Graph.as_default() 输入上下文的最内层图或者全局默认图(如果没有显示创建)
    output_graph_def = graph_util.convert_variables_to_constants(sess, graph_def, ['add'])
    #graph_util.convert_variables_to_constants()作用：用常量相同的值替换图中的所有变量，同时将不必要的节点去掉
    #最后一个参数["add"]给出了需要保存的节点名称，add节点是上面定义的2个变量相加的操作，注意这里给出的是计算节点的名称，所以后面没有0

    #将导出的模型存入文件
    with tf.gfile.GFile("tensorflow模型持久化1/combined_model.pb", "wb") as f:f.write(output_graph_def.SerializeToString())
        #运用 with……as 语句，做常用的作用是打开某个文件


### 通过以下代码来调用，PB格式的持久化模型

import tensorflow as tf
from tensorflow.python.platform import gfile

with tf.Session() as sess:
    model_filename = "tensorflow模型持久化1/combined_model.pb"#读取保存的文件模型
    with gfile.FastGFile(model_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        #读取保存的文件模型，并将文件解析成对应的GraphDef Protocol Buffer

        result = tf.import_graph_def(graph_def, return_elements=["add:0"])
        #将graph_def中保存的时候图加载到当前的图中，return_elements=["add:0"]给出了返回的张量的名称，在保存的时候给出的是计算节点的名称，所以为“add"
        #在加载时给出的是张量的名称，所以是add:0

        print(sess.run(result))

## gfile的作用：1,提供类似python的file对象的api。2,提供基于tensorflow下的c++ filesystem api的实现