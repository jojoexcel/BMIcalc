height=int(input("請輸入你的身高(cm):"))
weight=int(input("請輸入你的體重(Kg):"))
bmi=weight/(height/100)**2
print("你的身高:"+(str(height)/100)+"公尺")
print("你的體重:"+str(weight)+"公斤")
print("你的BMI:"+(str(round(bmi,2)))
