#簡單的邏輯迴歸模型
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
# 在scikit-learn套件的linear_model中匯入_logistic model
input_data = np.array([[0,0],[0.25,0.25],[0.5,0.5],[1,1]]) #二維 4*2
output_data = [0,0,1,1] #二元
logit_model = LogisticRegression() # 透過_logistic 將一個模型物件實例化
logit_model.fit(input_data,output_data) # 用fit函數(建立,訓練這個模型)，以input_data,output_data資料訓練一個邏輯回歸模型
print(logit_model.coef_) #印出係數 a+b1*X1+b2*X2... 的bi
print(logit_model.intercept_) #印出截距-->a

predict_output = logit_model.predict(input_data) #對新資料進行預測

plt.scatter( #若要建構散布圖則使用scatter函數
    x = input_data[:,0], #
    y = input_data[:,1],
    color = [("red" if x == 1 else "blue") for x in output_data]
)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("ACTUAL")
plt.grid()
plt.show()

plt.scatter( #若要建構散布圖則使用scatter函數
    x = input_data[:,0],
    y = input_data[:,1],
    color = [("red" if x == 1 else "blue") for x in predict_output]
)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Predicted")
plt.grid()
plt.show()