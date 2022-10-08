password = "a123456" #可以自動化修改密碼?結合讀取txt或json檔修改
i = 3
while i > 0:
	account_password = input("請輸入密碼")
	if account_password == password:
		print("登入成功")
		break
	else:
		i -= 1
		print(f"密碼錯誤,還有{i}次機會,請重新輸入")
		