string = input("Введите текст: ")
 
length = len(string)
let_s = let_b = 0
for i in string:
	if 'a'<=i<='z':
		let_s += 1
	elif 'A'<=i<='Z':
		let_b += 1
 
print("%% строчных букв: %.2f" % (let_s/length * 100))
print("%% прописных букв: %.2f" % (let_b/length * 100))