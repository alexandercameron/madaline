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

def menu():
	
def main():
	print "Welcome to my madaline neural network!"
	file = raw_input("Enter the data input file name:")
	vars = readFile(file)
	menu()
if __name__ == '__main__':
	main()
