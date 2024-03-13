# 輸入所需模組
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# # 使用線性模型
# Create a Sequential model
model = Sequential()
# # 建立輸入層和隱藏層
# Add a dense layer with 256 neurons and relu activation
model.add(Dense(units=256, input_dim=784, kernel_initializer='normal', activation='relu'))
# # 建立輸出層
# Add the output layer with 10 units and softmax activation
model.add(Dense(units=10, kernel_initializer='normal', activation='softmax'))
# # 查看模型的摘要
# Print the model summary to see the structure
print(model.summary())