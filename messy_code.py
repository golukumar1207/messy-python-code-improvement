# messy_code.py
# Example of unorganized legacy Python script with code smells:
# magic numbers, poor variable names (a, b, c, x, y), global state, no functions.

items = [["laptop", 55000, 2], ["mouse", 600, 5], ["keyboard", 1500, 3], ["monitor", 12000, 1]]

t = 0
for i in range(len(items)):
    p = items[i][1]
    q = items[i][2]
    cost = p * q
    # Magic discount logic
    if cost > 50000:
        d = cost * 0.15
    elif cost > 20000:
        d = cost * 0.10
    elif cost > 5000:
        d = cost * 0.05
    else:
        d = 0
    final = cost - d
    # GST tax magic number
    tax = final * 0.18
    net = final + tax
    t = t + net
    print("item: " + items[i][0] + " cost: " + str(cost) + " disc: " + str(d) + " tax: " + str(tax) + " total: " + str(net))

print("GRAND TOTAL: " + str(t))
