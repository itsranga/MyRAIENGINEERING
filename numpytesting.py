import numpy as np

# Dataset: Exam scores
scores = np.array([45, 50, 55, 60, 65, 70, 75, 80, 200]) 

# Calculate basic statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev_score = np.std(scores)

print(f"Mean: {mean_score}, Median: {median_score}, Standard Deviation: {std_dev_score}")

arr = np.random.randint(10, size=(3, 3))
print(arr)


# Create arrays

a1 = np.array([1, 2, 3])    # 1D array
a2 = np.array([[1, 2], [3, 4]]) # 2D array
a3 = np.array([[[1, 2], [3, 4]],    # 3D array
               [[5, 6], [7, 8]]])

print(a1)
print(a2)
print(a3)

#2. Using Numpy Functions
import numpy as np

a0 = np.zeros((3, 3))
a1  = np.ones((2, 2))
ar  = np.arange(0, 10, 2)

print(a0)
print(a1)
print(ar)

#NumPy Array Indexing

#Accessing Elements in 1D Arrays
arr = np.array([10, 20, 30, 40, 50])

print(arr[-2])

#2. Accessing Elements in Multidimensional Arrays - 2D Arrays:matrix[row, column].
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[2, 1])

#3D Arrays - matrix[depth, row, column].
cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[0, 2, 2])

#3. Slicing Arrays
arr = np.array([0, 1, 2, 3, 4, 5])

print(arr[2:4])
#Slicing Multidimensional Arrays: 2D Arrays: matrix[row_start:row_end, column_start:column_end].
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(matrix[2:3, 0:3])

#5D Arrays - matrix[depth, row, column, time, ...].
array_4d = np.zeros((2, 3, 4, 5))
print(array_4d)

#4. Boolean Indexing
arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 18])

#We can also use logical operators like & (AND), | (OR) and ~ (NOT) to combine conditions.
arr = np.array([10, 15, 20, 25, 30])
print(arr[(arr > 10) & (arr < 25)])