class Neuron:
    def __init__(self):

        self.weight=0
        self.bias=0
        self.learning_rate = .01
    def learn(self, inputs, answers):
        self.inputs = inputs
        self.answers = answers

        for epoch in range(1000):

            for x, actual in zip(self.inputs, self.answers):
                prediction = self.weight * x + self.bias

                error = actual - prediction

                self.weight += self.learning_rate * error * x
                self.bias += self.learning_rate * error
        return [self.weight, self.bias]
    def predict(self,value):
        self.learn(self.inputs,self.answers)
        return (value*self.weight+self.bias)
calc=Neuron()
calc.learn([1, 2, 3, 4,5,6,7,8], [2, 4, 6, 8,10,12,14,16])
print(calc.predict(100))
