import numpy as np
a=np.array([[1, 1, 1]])
k=np.array([
    [1, 1, 1], 
    [1, 1, 1],
    [1, 1, 1]])
def conv(a,k):
	if (len(a)-len(k)+1)>0:
		output_size=(len(a)-len(k)+1)
		res=np.zeros([output_size,output_size],np.float32)
		for i in range(len(res)):
			for j in range(len(res)):
				res[i][j]=compute_conv(a,k,i,j)
				return res
	else: return 
	return res
	
def compute_conv(a,k,i,j):
	res=0
	for kk in range(3):
		for kl in range(3):
			res+=a[i+kk][j+kl]*k[kk][kl]
	return res
print(conv(a,k))
	
