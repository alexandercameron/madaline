class Net:
	def __init__(self, inputD, outputD, pairs):
		pass
class InputVars:
	def __init__(self, input, output, pairs, samples):
		self.input = input
		self.output = output
		self.pairs = pairs
		self.samples = samples

class Sample:
	def __init__(self, inputD, outputD, s, t):
		self.x = {}
		i = 1
		while i <= inputD:
			self.x[i] = s[i-1]
			i = i + 1
		self.t = int(t)

def readFile(filename):
	f = open(filename, 'r')
	inputD = [int(s) for s in f.readline().split() if s.isdigit()]
	inputD = inputD[0]
	outputD = [int(s) for s in f.readline().split() if s.isdigit()]
	outputD = outputD[0]
	tpairs = [int(s) for s in f.readline().split() if s.isdigit()]
	tpairs = tpairs[0]
	f.readline()
	
	t = 0
	samples = {}
	while t < tpairs:
		s = f.readline().split()
		target = f.readline()
		f.readline()
		tmp = Sample(inputD, outputD, s, target)
		t = t + 1
		samples[t] = tmp
	return InputVars(inputD, outputD, tpairs, samples)
def a11():	
	weights_b = raw_input("Enter 0 to initialize weights to zero, or any other key to set to random values")
	if int(weights_b) is 0:
		weights_b = int(weights_b)
	else:
		weights_b = 1
	return weights_b

def a12():	
	max_epochs = raw_input("Enter the maximum number of training epochs:")
	try:
		max_epochs = int(max_epochs)
		if max_epochs > 0:
			return max_epochs
		else:
			print "Input failed. Setting max epochs to 5"
			return 5
	except:
		a12()
def a1():
	weights_b = a11()	
	max_epochs = a12()
	
def a2(filename):
	pass

def a(option):
	option = int(option)
	if option is 1:
		pass	
	if option is 2:
		a2 = raw_input("Enter the file name where the testing/deploying results will be saved:")
		a2(a2)
	if option is 3:
		print "Thanks for using this Madaline Neural Network!"
		exit(0)

def menu():
	a = raw_input("Enter 1 to train, 2 to test/deploy, or 3 to quit the network:")
	a(a)

def main():
	print "Welcome to my madaline neural network!"
	file = raw_input("Enter the data input file name:")
	vars = readFile(file)
	menu()

if __name__ == '__main__':
	main()
