
import tensorflow as tf
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# create 4 constants where tensor operations will be done
a=tf.constant(10,name="constant_a")
b=tf.constant(6,name="constant_b")
c=tf.constant(4,name="constant_c")
d=tf.constant(2,name="constant_d")

#perform operations (edges)
mul = tf.multiply(a,b, name="multiplication")
division = tf.add(c,d, name="division")
addition = tf.add_n(mul, division , name="addn")

#print to check shape,dataype and file name
print(addition)

#start session and file writer
sess = tf.Session()
#file writer 
writer = tf.summary.create_file_writer("owen",sess.graph)
#close session and writer
writer.close()
sess.close()
exit()

#now open the file from the terminal using
# tensorboard --logdir="fileName"
#open the tensorboard Ip given and navigate to the graphs section on tensorboard to view the computation on the graph


#DEFAULT AND EXPLICITLY SPECIFIED GRAPHS
#by default if tensors are not assigned to a specific graphs they are assigned to default graphs
import tensorflow as tf

#specify a graph
g1 = tf.Graph()
with g1.as_default():
    with tf.Session as sess:
        
        # y = Ax + b
        A = tf.constant([5,7], tf.int32, name='A')
        x = tf.placeholder(tf.int32, name='x')
        b = tf.constant([3,4], tf.int32, name='b')
        
        y = A * x + b
        
        print(sess.run(y, feed_dict={x:[10,100]}))
        
        #get to know if the g1 is the graph on execution
        assert y.graph is g1
        
        
        
#instanctiate another second graph
#instanctiate another second graph 
g2 =tf.Graph()
with g2.as_default():
    with tf.Session() as sess:

    # equation at hand:
    # Y = A ^ x
    A = tf.constant([5,7], tf.int32,name='A')
    x = tf.placeholder(int32, name='x')

    y = tf.pow(A,x, name='y_power')

    print(sess.run(y, feed_dict={x:[3,5]})

    assert y.graph is g2

#Adding computations to the deafult graph
default_graph = tf.get_default_graph()
with tf.Session() as sess:
    A = tf.constant([5,7], tf.int32,name='A')
    x = tf.placeholder(int32, name='x')

    y = A + x

    print(sess.run(y, feed_dict={[3,5]}))

    assert y.graph is default_graph

          
          
 #DEBUGGING WITH NAME_SCOPE.
#As machine learning gains more accuracy then there is need to introduce name_space
#to make it easy with debugging by reducing tensors
import tensorflow as tf

#declare constants
A = tf.constant([4], tf.int32, name='A')
B = tf.constant([5], tf.int32, name='B')
C = tf.constant([6], tf.int32, name='C')

x = tf.placeholder(tf.int32, name='x')

# Y = Ax^2 + Bx + C . Equation 1
AX_1 = tf.multiply(A, tf.pow(x,2), name='AX_1')
Bx = tf.multiply(B, x, name='Bx')
y1 = tf.add_n([AX_1, Bx, C], name='y1')

# Y = Ax^2 + Bx^2 Equation 2
AX_2 = tf.multiply(A, tf.pow(x,2), name='AX_2')
Bx2 = tf.multiply(B, x, name='Bx')
y2 = tf.add_n([AX_2, Bx2], name='y2')

y = y1 + y2

with tf.Session() as sess:
    print(sess.run(y, feed_dict={x: [10]}))
    
    writer = tf.summary.FileWriter('./file_location', sess.graph)
    writer.close()
    
# Run the above file before running the one below to compute the difference
    
 #NOW INTRODUCE NAME_SCOPE
          import tensorflow as tf

#declare constants
A = tf.constant([4], tf.int32, name='A')
B = tf.constant([5], tf.int32, name='B')
C = tf.constant([6], tf.int32, name='C')

x = tf.placeholder(tf.int32, name='x')

# Y = Ax^2 + Bx + C . Equation 1 and introduce the name_scope
with tf.name_scope("Equation_1"):
    AX_1 = tf.multiply(A, tf.pow(x,2), name='AX_1')
    Bx = tf.multiply(B, x, name='Bx')
    y1 = tf.add_n([AX_1, Bx, C], name='y1')

# Y = Ax^2 + Bx^2 Equation 2
with tf.name_scope("Equation_2"):
    AX_2 = tf.multiply(A, tf.pow(x,2), name='AX_2')
    Bx2 = tf.multiply(B, x, name='Bx')
    y2 = tf.add_n([AX_2, Bx2], name='y2')
    
with tf.name_scope("final_sum"):
    y = y1 + y2

with tf.Session() as sess:
    print(sess.run(y, feed_dict={x: [10]}))
    
    writer = tf.summary.FileWriter('./file_location', sess.graph)
    writer.close()
          
          
    # INTERACTIVE SESSION()
# allows one to run inferences without having to instantiate session each time

import tensorflow as tf

sess = tf.interactiveSession()

A = tf.constant([4], tf.int32, name='a')
x = tf.placeholder(tf.int32, name='x')

y = A * x

y.eval(feed_dict={x:[5]})  # array ([20]) dtype=int32

print(y.eval(feed_dict={[5]})) # prints[20]

sess.close()

          
   #LINEAR REGRESSION IN REALWORLD WITH TENSORFLOW
import tensorflow as tf

#Model parameters
W = tf.Variable([.3], dtype='float32')
b = tf.Variable([-.3], dtype='float32')

# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b

#output holder 
y = tf.placeholder(tf.float32)

#Loss model during training 
loss = tf.reduce_mean(tf.square(linear_model, - y))

#optimize your model for the best results and accuracy
optimizer = tf.train.GradientDescentOptimizer(0.01)

#Training the model
train = optimizer.minimize(loss)

#Training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

#initialize all variables
init = tf.global_variables_initializer()

#instantiate sessions and train in loops of 1000
with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        sess.run(train, {x: x_train, y: y_train})
        
    #evaluate training accuracy 
    curr_w, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
    
    print("W: %s b: %s loss: %s" %s(curr_w, curr_b, curr_loss))

