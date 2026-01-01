# li = [1,10,5,8,7,6,4,3,2,9]
li = [3,5,2,7,10,9,8,1,4,6]

def quickSort(data, start, end):
	if(start>=end): return

	key = start
	i = start + 1
	j = end

	while(i<=j):
		# 이 부분이 c++과 다르다. 등호를 반대로 하면 내림차순 >=
		while(data[i]<=data[key]):
			i = i+1
			if i > end: # 반드시 이렇게 해주어야 한다. 아니면 인덱스 범위를 벗어났다는 메세지를 만나게 된다.
				break

		while(data[j]>=data[key] and j>start): # 등호를 반대로 하면 내림차순 >=
			j = j-1

		if(i>j):
			temp = data[j]
			data[j] = data[key]
			data[key] = temp
		else:
			temp = data[j]
			data[j] = data[i]
			data[i] = temp

	quickSort(data, start, j-1)
	quickSort(data, j+1, end)
	return data # 이부분도 c++과 다르다. c++은 포인터라 리턴이 필요가 없는데 여기는 필요하다.

print("quicksort sample")
data = quickSort(li, 0, len(li)-1)

for item in data:
	print(item, end='')