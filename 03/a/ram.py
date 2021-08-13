import sys, getopt

def binary(i, k):
	s = []
	for j in range(0,k):
		s.append("na" + str(j))
	t = 0
	while(i>0):
		if i % 2 == 1:
			s[t]= "address[" + str(t) + "]"
		t += 1
		i = int(i/2)
	return s

def hdl():
	try:
		opts, args = getopt.getopt(sys.argv[1:],"n:k:")
	except getopt.GetoptError as err:
		print(err)
		print('ram.py -n [number of register] -k [size of address]')
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-n':
			n = int(arg)
		elif opt == '-k':
			k = int(arg)

	for i in range(0,k):
		print(f"Not(in=address[{i}],out=na{i});")
	print()

	for i in range(0,n):
		s = binary(i,k)
		print(f"//R[{i}]")
		for j in range(0,k-1):
			if j==0:
				print(f"And(a={s[0]},b={s[1]},out=e{j}u{i});")
			elif j<k-2: 
				print(f"And(a=e{j-1}u{i},b={s[j+1]},out=e{j}u{i});")
			else:
				print(f"And(a=e{j-1}u{i},b={s[j+1]},out=e{i});")
		print(f"And(a=e{i},b=load,out=l{i});")
		print(f"Mux16(a=out{i},b=in,sel=e{i},out=i{i});")
		if i == 0:
			print(f"Register(in=i{i},load=l{i},out=out{i},out=ram0);")
		elif i < n-1:
			print(f"Register(in=i{i},load=l{i},out=out{i});")
			print(f"Mux16(a=ram{i-1},b=out{i},sel=e{i},out=ram{i});")
		else:
			print(f"Register(in=i{i},load=l{i},out=out{i});")
			print(f"Mux16(a=ram{i-1},b=out{i},sel=e{i},out=out);")
		print();

if __name__ == "__main__":
	hdl()