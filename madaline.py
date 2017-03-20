class Net:
	def __init__(self, inputD, outputD, weightB):
		
		i = 1
		x = 0
		self.xneurons = {}
		if weightB == 1:
			x = 1	
		while i <= inputD:
			self.xneurons[i] = Neuron(inputD, x)
			i = i + 1
		self.xneurons['b'] = Neuron(inputD, x)
	
		j = 1
		self.zneurons = {}
		while j <= inputD:
			self.zneurons[j] = Neuron(outputD, 2)
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
		self.y = {}
		while i <= outputD:
			self.y[i] = 0
			if int(weightB) == 0:
				self.weights[i] = 0
			#for the hidden layer
			elif weightB is 2:
				self.weights[i] = .5
			else:
				#this needs to be random
				self.weights[i] = .5
			i = i + 1
		self.weights[1]
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
		j = 1
		self.t = {}
		while j <= outputD:
			self.t[j] = int(t)
			j = j + 1
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
			return fileinput()
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
	print "THE NET INITIALIZES TO", myNet.xneurons[1].weights[1]
	condition = False
	z = {}
	maxchange = 0
	while(condition is False): #step 1
		i = 1 
		epoch = 1
		while i <= tpairs: #step 2
			print "i is", i
			print "weights:"
			m = 1
			while m <= 2:
				ii = 1
				while ii<= 2:
					print myNet.xneurons[m].weights[ii]
					ii = ii + 1
				m = m + 1
			m = 1
			while m <= 2:
				print myNet.xneurons['b'].weights[1]
				m = m + 1
			
			#step 3, set activations of input units			
			j = 1
			while j <= inputD:
				myNet.xneurons[j].x = float(samples[i].x[j])
				j = j + 1
			
			#step 4, compute net input to each hidden ADALINE unit:
			k = 1
			zin = {}			
			while k <= inputD:	
				zin[k] =float( myNet.xneurons['b'].weights[k])
	
				l = 1
				while l <= inputD:	
					zin[k] = float(zin[k]) + float(myNet.xneurons[l].x * myNet.xneurons[l].weights[k])
					l = l + 1
				k = k + 1
			
			#step 5, determine output of ADALINE unit
			x = 1
			while x <= inputD:
				#print "zin is ", zin[x]
				if zin[x] >= 0:
					myNet.zneurons[x].x = 1
				else:
					myNet.zneurons[x].x = -1
				x = x + 1	
			
			#step 6, determine output of net
			k = 1
			yin = {}
			while k <= outputD:
				yin[k] = myNet.zneurons['b'].weights[k]
				l = 1
				while l <= inputD:
					yin[k] = yin[k] + (myNet.zneurons[l].weights[k] * myNet.zneurons[l].x)
					l = l + 1
				k = k + 1
			k = 1
			while k <= outputD:
				if yin >= 0:
					myNet.y[k] = 1
				else:
					myNet.y[k] = -1
				k = k + 1
			
			#step 7, determine error and update weights
			target = samples[i].t[1]
			#print "z1 is",myNet.zneurons[1].x, "z2 is", myNet.zneurons[2].x
			#print "target is ", target, "and output is ", myNet.y[1]
			print "max change is", maxchange
			if int(target) != myNet.y[1]:
				#print "The target and the output are different. I is",i
				
				if target == -1:
					k = 1
					while k <= inputD:
						if myNet.zneurons[k].x >= 0:
							g = 1
							while g <= inputD:
								
								alg = algorithmx(learning_rate, zin[k], myNet.xneurons[g].x, -1)
								print "ALG",alg
								myNet.xneurons[g].weights[k] = myNet.xneurons[g].weights[k] + alg
								
								#print "Delta from spot 1 is ", alg, "maxchange is", maxchange
								#print "Weight updated is now", myNet.xneurons[g].weights[k]
								
								if alg < 0:
									alg = alg * -1
								
								if alg > maxchange :
									maxchange = alg
								
								g = g + 1
							
								
							balg = algorithmx(learning_rate, zin[k], -1, 1)
							myNet.xneurons['b'].weights[k] = myNet.xneurons['b'].weights[k] + balg
							
							#print "Delta from spot 2 is", balg, "maxchange is", maxchange
							#print "Weight updated is now", myNet.xneurons['b'].weights[k]
							
							if balg < 0:
								balg = balg * -1
							if balg > maxchange:
								maxchange = balg
						k = k +1	
	
				#if target = 1
				else:	
					k = 1
					z2 = 1000000000
					j = k
					while k <= inputD:
						tmp = myNet.zneurons[k].x * myNet.zneurons[k].x
						if tmp < z2:
							j = k
							z2 = tmp			
						k = k + 1
					x = 1
					while x <= inputD:
						algor = algorithmx(learning_rate, zin[j], myNet.xneurons[x].weights[j] , 1)
						myNet.xneurons[x].weights[j] = myNet.xneurons[x].weights[j] + algor
						#print "Delta from spot 3 is ", algor
						#print "Weight updated is now ", myNet.xneurons[x].weights[j]
						if algor < 0:
							algor = algor * -1
						if algor > maxchange :
							maxchange = algor
						x = x + 1
					
					algo = algorithmx(learning_rate, zin[j], 1, 1)
					myNet.xneurons['b'].weights[j] = myNet.xneurons['b'].weights[j] + algo
					#print "Delta from spot 4 is", algo
					if algo < 0:
						algo = algo * -1
					if algo  > maxchange:
						maxchange = algo

			if i == 4:
			#step 8, test stopping condition
				if maxchange < .0001:
					print "Learning has converged after", epoch, "epochs."
					condition = True
					break
				if epoch == max_epochs:
					print "Maximum epochs reached."
					condition = True
					break	
				i = 0
				maxchange = 0
				epoch = epoch + 1
			p = 1
			while p <= inputD:
				zin[p] = 0
				p = p + 1
			i = i + 1	
		
		
		
	#we need to return the Net for the testing/deploying
	q = 1
	while q <= inputD:
		e = 1
		while e <= inputD:
			#print "xneuron", q, "weight", e
			#print myNet.xneurons[q].weights[e]
			e= e + 1
		print myNet.xneurons['b'].weights[1], myNet.xneurons['b'].weights[2]
		q = q + 1
	return myNet

def algorithmx(a, zin, x, t):
	return float(a) * float(( t - zin)) * float(x)
	
#THIS IS WHERE THE TESTING MADALINE GETS IMPLEMENTED
def madaline2(name, Net, data):
	samples = data.samples
	iD = data.input
	oD = data.output
	p = data.pairs

	for s in samples:
		#set x to s
		x = 1
		while x<= iD:
			Net.xneuron[x].x = s.x[x]
			x = x + 1
			
if __name__ == '__main__':
	main()
