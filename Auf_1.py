origin=[["A", "B"], [1, 2, 3]]
A=origin[0]
B=origin[-1]
final=[];
tempo=[];
for ele_A in A:
	tempo.append(ele_A)
	for ele_B in B:
		tempo.append(ele_B)
		final.append(tuple(tempo))
		tempo.pop()
	tempo.pop()
print(final)
