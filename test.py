import tensorflow as tf
base_model = tf.keras.applications.MobileNetV3Small(
    input_shape=(224,224,3),
    pooling='avg'
)
print(base_model.summary())