import matplotlib.pyplot as plt

inp = int(input("Input number: "))
x_coor = [0]
y_coor = [inp]


def collatz(x):
    global counter
    counter += 1

    if x == 1:
        return x

    elif x % 2 == 0:
        result = x//2
        print(int(result))
        y_coor.append(result)
        x_coor.append(counter)
        collatz(x/2)

    elif x % 2 != 0:
        result = (x * 3) + 1
        print(int(result))
        y_coor.append(result)
        x_coor.append(counter)
        collatz(((x * 3) + 1))


counter = 0
collatz(inp)
print(f"number of steps: {counter-1}")

plt.xlabel('Step')
plt.ylabel('Value')
plt.title("Collatz conjecture visualisation")
g = plt.plot(x_coor, y_coor,)
plt.setp(g, color="r")
plt.show()
