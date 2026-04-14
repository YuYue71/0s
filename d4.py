item = input("輸入商品名稱:")           # 獲得商品名稱輸入 (設輸入RAM)
price = int(input("輸入商品單價:"))     # 獲得商品單價輸入 (設輸入99999)
qty = int(input("輸入購買數量:"))       # 獲得購買數量輸入 (設輸入2)
total = price * qty                    # 計算總價
print(f"商品: {item}\n單價: {price:>6} 元\n數量: {qty:>6} 個\n總價: {total:>6} 元")
# 輸出如下:
# 商品: RAM
# 單價:  99999 元
# 數量:      2 個
# 總價: 199998 元