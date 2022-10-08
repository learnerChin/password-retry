password = "a123456" #可以自動化修改密碼?結合讀取txt或json檔修改
i = 3
while True:
	account_password = input("請輸入密碼")
	if account_password == password:
		print("登入成功")
		break
	else:
		i -= 1
		print(f"密碼錯誤,還有{i}次機會,請重新輸入")
		if i == 0:
			print("登入失敗,超過登入次數,補發登入密碼")
			break