with open('../expense.txt') as f:
    expenses = f.read().splitlines()

expenses = list(map(int, expenses))
for i in range(len(expenses)):
    for j in range(i+1, len(expenses)):
        if expenses[i] + expenses[j] == 2020:
            print(expenses[i] * expenses[j])
        for k in range(j+1, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(expenses[i] * expenses[j] * expenses[k])