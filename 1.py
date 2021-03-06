import csv

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    return dataset

attributes = ['Sky', 'Temp', 'Humidity', 'Wind', 'Water', 'Forecast']
print('Attributes =', attributes)
num_attributes = len(attributes)

dataset = loadCsv('tennis1.csv')
print(dataset)

hypothesis = ['0'] * num_attributes

print("The Hypothesis are")
for i in range(len(dataset)):
    target = dataset[i][-1]
    if(target == 'TRUE'):
        for j in range(num_attributes):
            if(hypothesis[j] == '0'):
                hypothesis[j] = dataset[i][j]
            if(hypothesis[j] != dataset[i][j]):
                hypothesis[j] = '?'
    print(i+1, '=', hypothesis)

print("Final Hypothesis")
print(hypothesis)
