import numpy as np
import matplotlib.pyplot as plt
from itertools import product


class Wheel:
    def __init__(self, data, start_pos=0):
        self.data = np.array(data)
        self.length = len(self.data)
        self.position = start_pos % self.length

    def tick(self, steps=1):
        self.position = (self.position + steps) % self.length

    def value(self):
        return self.data[self.position]

    def __str__(self):
        return f"Wheel(position={self.position}, data={self.data})"


class Clockwork:
    def __init__(self, wheels):
        self.wheels = wheels

    def tick(self, steps=1):
        layer = len(self.wheels) - 1
        while True:
            if layer == -1:
                break
            last_val = self.wheels[layer].value()
            if self.wheels[layer].position == self.wheels[layer].length-1:
                self.wheels[layer].tick()
                layer -= 1
            else:
                self.wheels[layer].tick()
                break


def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))


def generate_clockwork(num_wheels, wheel_lengths, starting_positions):
    wheels = []
    for i in range(num_wheels):
        wheels.append(Wheel([n + 1 for n in range(wheel_lengths[i])], start_pos=starting_positions[i]))

    operators = ['+'.join(p) for p in product(['+', '-'], repeat=num_wheels-1)]
    return Clockwork(wheels), operators


def apply_operators(operands, operators):
    values = [wheel.value() for wheel in operands]
    for op in operators:
        operand_indices = [int(c) for c in op.replace('+', '').replace('-', '')]
        op_symbols = [c for c in op if c in ['+', '-']]
        result = values[operand_indices[0]]
        for i, sym in enumerate(op_symbols):
            if sym == '+':
                result += values[operand_indices[i+1]]
            else:
                result -= values[operand_indices[i+1]]
        values = [result] + values[len(operand_indices)+1:]

    return digital_root(values[0])


def plot_clockwork(clockwork, operators, num_steps):
    for i in range(num_steps):
        clockwork.tick()
        result = apply_operators(clockwork.wheels, operators)
        plt.plot(i, result, 'ko')

    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.show()


# Generate clockwork with 3 wheels of random lengths between 2 and 9 and random starting positions
num_wheels = 3
wheel_lengths = np.random.randint(2, 10, size=num_wheels)
starting_positions = np.random.randint(0, wheel_lengths, size=num_wheels)
clockwork, operators = generate_clockwork(num_wheels, wheel_lengths, starting_positions)

# Plot the clockwork and display the starting positions and wheel lengths
plot_clockwork(clockwork, operators, 500)
print("Starting Positions:", starting_positions)
print("Wheel Lengths:", wheel_lengths)