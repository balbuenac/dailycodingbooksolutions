def merge_sort(myList):
	# Aprint('gola')
	if len(myList) > 1:
		mid = len(myList) // 2
		l = myList[:mid]
		r = myList[mid:]

		merge_sort(l)
		merge_sort(r)

		print(l, r)

		i, j, l = 0, 0, 0

		while i < len(l) and j < len(r):
			if l[i] < r[j]:
				myList[k] = l[i]
				i += 1
			else:
				myList[k] = r[j]
				j += 1
			k += 1
		
		while i < len(l):
			myList[k] = l[i]
			i += 1
			k += 1

		while j < len(r):
			myList[k] = r[j]
			j += 1
			k += 1


merge_sort([5, 4, 1, 2])
