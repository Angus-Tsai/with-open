data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')	
sum_len = []
for x in data:
	sum_len.append(len(x))
answer = sum(sum_len) / len(data)
print('每筆留言平均長度為', answer)
n = 0
for y in sum_len:
	if y < 100:
		n = n + 1
print('一共有', n, '筆留言長度小於100')		

