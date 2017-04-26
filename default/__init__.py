import  tensorflow as tf
from default.clock import Clock


def main():
    clock = Clock()
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello).decode())
    print(clock.delta())

if __name__ == '__main__':
  main()