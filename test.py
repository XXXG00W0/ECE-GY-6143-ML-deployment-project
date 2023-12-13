# import tensorflow as tf
# base_model = tf.keras.applications.MobileNetV3Small(
#     input_shape=(224,224,3),
#     pooling='avg'
# )
# print(base_model.summary())

import PIL.Image as Image
from PIL import ImageEnhance
img = Image.open("custom_image_meat.jpg")
enhancer = ImageEnhance.Brightness(img)
factor_1 = 0.5
factor_2 = 1.5
shifted_image_1 = enhancer.enhance(factor_1)
shifted_image_2 = enhancer.enhance(factor_2)
shifted_image_1.show()
shifted_image_2.show()