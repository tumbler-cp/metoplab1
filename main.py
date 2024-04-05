import half
import gold
import matplotlib.pyplot as plt
import numpy as np
import newton

def main():
    x = np.linspace(-1, 0, 100)
    y = x**2 + x + np.sin(x)

    x_s, f_s = half.solve(-1, 0)
    plt.figure('Метод половинного деления')
    plt.scatter(x_s, f_s, color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод половинного деления')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    x_s, f_s = gold.solve(-1, 0)
    plt.figure('Метод золотого сечения')    
    plt.scatter(x_s, f_s, color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод золотого сечения')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    x_s, f_s = newton.solve(-1, 0)
    plt.figure('Метод Ньютона')    
    plt.scatter(x_s, f_s, color='red', zorder=5)
    plt.plot(x, y)
    plt.title('Метод Ньютона')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()
    

if __name__ == "__main__":
    main()