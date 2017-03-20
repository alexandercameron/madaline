class Net:
	def __init__(self, inputD, outputD, weightB):
		
		i = 1
		self.xneurons = {}	
		while i <= inputD:
			self.xneurons[i] = Neuron(inputD, weightB)
			i = i + 1
		self.xneurons['b'] = Neuron(inputD, weightB)
	
		j = 1
		self.zneurons = {}
		while j <= inputD:
			self.zneurons[i] = Neuron(outputD, 2)
			j = j + 1
		self.zneurons['b'] = Neuron(outputD, 2)
		
		k = 1
		self.y = {}
		while k <= outputD:
			self.y[k] = 0
			k = k + 1
class Neuron:
	def __init__(self, outputD, weightB):
		i = 1
		self.weights = {}
		while i <= outputD:
			self.y[i] = 0
			if weightB is 0:
				self.weights[i] = 0
			#for the hidden layer
			if weightB is 2:
				self.weights[i] = .5
			else:
				#this needs to be random
				self.weights[i] = .5
			i = i + 1
		self.x = 0
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
		return a1b()

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
		return a1c()	
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

def a(option, data, Net):
	option = int(option)
	if option is 1:
		net_parameters = a1()
		return madaline1(net_parameters, data)	
	if option is 2:
		if Net is 0:
			print "You need to train the net before you can deploy it. Try option 1."
			menu(data, Net)
		else:
			name = raw_input("Enter the file name where the testing/deploying results will be saved:\n")
			madaline2(name, Net, data)
	if option is 3:
		print "Thanks for using this Madaline Neural Network!"
		exit(0)

def menu(data, Net):
	x = raw_input("Enter 1 to train, 2 to test/deploy, or 3 to quit the network:\n")
	return  a(x, data, Net)
	
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
	Net = 0
	while(1):
		Net = menu(data, Net)

#THIS IS WHERE THE TRAINING MADALINE GETS IMPLEMENTED
def madaline1(n, data):
	
	learning_rate = float(n['l'])
	weight_b = int(n['w'])
	max_epochs = int(n['e'])
	filename = n['f']
	inputD = int(data.input)
	outputD = int(data.output)
	tpairs = int(data.pairs)
	samples = data.samples
	
	# samples has Sample objects in it
	# samples[1:pairs+1] has each object
	# samples[x].x[1:inputdimensions] is xy
	# samples[x].t is t

	#net construction
	myNet = Net(inputD, outputD, weight_b)
	print "WEIGHT", myNet.neurons[1].weights[1]
	


	#we need to return the Net for the testing/deploying
	return myNet
#THIS IS WHERE THE TESTING MADALINE GETS IMPLEMENTED
def madaline2(name, Net, data):
	pass
	
if __name__ == '__main__':
	main()
