import random


def generateRandomValues(entries, weights):
    # print('NUMERICAL VALUES QUANTITY: ', inputData["entries"])
    # print('WEIGHTS: ', inputData["weights"])
    # print(range(inputData["entries"]))
    entriesList = []
    for entry in range(entries):
        random_num = round(random.random(), 2)
        item_weight = []
        for w in range(weights):
            random_weight = round(random.random(), 2)
            item_weight.append(random_weight)
        entriesList.append({"value": random_num, "weights": item_weight})

    # for i in entriesList:
    #     print(f'{i}\n')

    return entriesList


def sumValues(dataSet, total_weights):
    sumValues = []
    idealValues = []
    print(dataSet)
    for w in range(total_weights):
        aux = round(random.random(), 2)
        idealValues.append(aux)
        sumOfValues = 0
        for i in dataSet:
            # print(i)
            sumOfValues += i["value"] * i["weights"][w]
        sumValues.append(round(sumOfValues, 2))
    # print(sumValues)
    return sumValues, idealValues


def cost(sumValues, idealValues):
    totalCost = 0
    for s in sumValues:
        totalCost += round(((s-idealValues[sumValues.index(s)])**2), 2)
    return totalCost

def calibrate(dataSet, total_weights):
    newDataSet = []
    for data in dataSet:
        for w in data["weights"]:
            w = data["weights"][random.randint(0, total_weights - 1)] = round(random.random(), 2)
        newDataSet.append(data)
    return newDataSet

def run():
    total_entries = 10
    total_weights = 10
    # dataSetList = []
    # dataSet = {"entries": total_entries, "weights": total_weights}
    dataSet = generateRandomValues(total_entries, total_weights)
    for x in range(5):
        sumV, idealV = sumValues(dataSet, total_weights)
        print(f'soma: {sumV}')
        print(f'ideal: {idealV}')
        finalCost = cost(sumV, idealV)
        print(f'custo total: {finalCost}')
        calibrate(dataSet, total_weights)


if __name__ == '__main__':
    run()
