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

def a1a():	
	weights_b = raw_input("Enter 0 to initialize weights to zero, or any other key to set to random values:\n")
	try:
		if int(weights_b) is 0:
			return 0
		else:
			return 1
	except:
		return 1
def a1b():	
	max_epochs = raw_input("Enter the maximum number of training epochs:\n")
	try:
		max_epochs = int(max_epochs)
		if max_epochs > 0:
			return max_epochs
		else:
			print "Negative numbers not allowed. Setting max epochs to 5."
			return 5
	except:
		print "Input failed. Try again."
		a1b()

def a1c():
	alpha = raw_input("Enter the desired learning rate:\n")
	try:
		alpha = float(alpha)
		if alpha > 1.0:
			print "Learning rate too large Enter an x value such that 0 < x <= 1."
		elif alpha <= 0.0:
			print "Learning rate is too small. Enter an x value such that 0 < x <= 1."
		else:
			return alpha
		a1c()
	except:
		print "Input failed. Try again."
		a1c()	
def a1d():
	filename = raw_input("Enter the file name where weights will be saved:")
	return filename

def a1():
	weights_b = a1a()	
	max_epochs = a1b()
	learning_rate = a1c()	
	weight_file = a1d()
	
	r = {}
	r['w'] = weights_b
	r['e'] = max_epochs
	r['l'] = learning_rate
	r['f'] = weight_file
	
	return r

def a2(filename):
	pass

def a(option, data):
	option = int(option)
	if option is 1:
		net_parameters = a1()
		madaline1(net_parameters, data)	
	if option is 2:
		x = raw_input("Enter the file name where the testing/deploying results will be saved:\n")
		a2(x)
	if option is 3:
		print "Thanks for using this Madaline Neural Network!"
		exit(0)

def menu(data):
	x = raw_input("Enter 1 to train, 2 to test/deploy, or 3 to quit the network:\n")
	a(x, data)

def fileinput():
	filename = raw_input( "Enter the data input file name:\n")
	try:
		open(filename, 'r')
		return readFile(filename)
	except:
		try:
			filename = filename + ".txt"
			open(filename,'r')
			return readFile(filename)
		except:
			print "File reading failed. Try again."
			fileinput()
def main():
	print "Welcome to my madaline neural network!"
	data = fileinput()
	while(1):
		menu(data)

#THIS IS WHERE THE MADALINE GETS IMPLEMENTED
def madaline1(net_params, data):
	'''
	How to refer to different params:
	
	net_params[key]:
		when key is 'l':
			learning rate
		when key is 'w':
			weight boolean
		when key is 'e':
			max epochs
		when key is 'f':
			filename where weights are saved
	data.key:
		when key is input:
			input dimensions
		when key is output:
			output dimensions
		when key is pairs:
			number of training pairs
		when key is samples:
			list of Sample objects
			
			data.samples[key]
			when key is x:
				dictionary ordered 1:input dimensions of s values
			when key is t:
				target
	'''
	
if __name__ == '__main__':
	main()
