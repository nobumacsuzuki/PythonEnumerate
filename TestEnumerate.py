import numpy as np

def main():
    arrayTest = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], dtype=float)
    for (index, element) in enumerate(arrayTest):
        print(index, element)
    for (index, element) in enumerate(arrayTest[1:10:2]):
        print(index, element)

if __name__ == "__main__":
    main()