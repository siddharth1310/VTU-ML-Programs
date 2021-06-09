
concepts = [['Sunny','Warm','Normal','Strong','Warm','Same'],
['Sunny','Warm','High','Strong','Warm','Same'],
['Rainy','Cold','High','Strong','Warm','Change'],
['Sunny','Warm','High','Strong','Cool','Change']]

target = ['TRUE','TRUE','FALSE','TRUE']
# print(concepts)


def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("initialization of specific_h and general_h")
    print(specific_h)
    general_h = [["?" for i in range(len(specific_h))]
                 for i in range(len(specific_h))]
    print(general_h)
    for i, h in enumerate(concepts):
        if target[i] == "TRUE":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "FALSE":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print(" steps of Candidate Elimination Algorithm", i+1)
        print(specific_h)
        print(general_h)
        
    general_h = [i for i in general_h if i != ['?', '?', '?', '?', '?', '?']]
    return specific_h, general_h


s_final, g_final = learn(concepts, target)
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")
