X = [[1, 2, 1],
     [0, 1, 0],
     [2, 3, 4]
     ]


y = [[2, 5],
     [6, 7],
     [1, 8]
     ]

result = [[0, 0],
          [0, 0],
          [0, 0]]

for X_rows in range(len(X)):  # Iterating through the rows of X
    for y_columns in range(len(y[0])):  # Iterate through the columns of y
        for y_rows in range(len(y)):  # Iterate through the rows of y
            result[X_rows][y_columns] += X[X_rows][y_rows] * \
                y[y_rows][y_columns]
for r in result:
    print(r)
