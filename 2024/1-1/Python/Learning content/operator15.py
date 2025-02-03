# collection unpacking
bar = [9, 4, 5, 7]  # 9, 4, 5, 7 -> List로 packing

seo, foo, pos, kin = bar  # collection unpacking
# collection unpacking이 일어나려면 좌항에 ,(쉼표)가 와야하고
# 우항에는 collection(list, tuple)이 오면
# collection unpacking이 일어남

print(f"{seo}, {foo}, {pos}, {kin}")