# testcase
matrix = [['A', 'B', 'H', 'K'], ['C', 'C', 'D', 'G'], ['A', 'B', 'D', 'F']]

def dynamic_programming_func():
    mem = [[0]*(len(matrix[0])+1)]*(len(matrix)+1)
    for i in range(1, len(matrix[0])+1):
        for j in range(1, len(matrix)+1):
            max = 0
            print("====" + str(i-1) + " " + str(j-1) + "=====")
            print(str(i-1) + " " + str(j-1-1))
            if j-1-1 > 0 and i-1 >= 0:
                if abs(ord(matrix[i-1][j-1-1]) - ord(matrix[i-1][j-1])) == 1:
                    if max < mem[i][j-1]:
                        max = mem[i][j-1]+1
            print(str(i-1) + " " + str(j))
            if j < len(matrix[0]) and i-1 >= 0:
                if abs(ord(matrix[i-1][j-1+1]) - ord(matrix[i-1][j-1])) == 1:
                    if max < mem[i][j+1]:
                        max = mem[i][j+1]+1
            print(str(i-1-1) + " " + str(j-1))
            if i-1-1 > 0 and j-1 >= 0:
                if abs(ord(matrix[i-1-1][j-1]) - ord(matrix[i-1][j-1])) == 1:
                    if max < mem[i-1][j]:
                        max = mem[i-1][j]+1
            print(str(i) + " " + str(j-1))
            if 0 < i < len(matrix[0]) and len(matrix) > j-1 >= 0:
                if abs(ord(matrix[i-1+1][j-1]) - ord(matrix[i-1][j-1])) == 1:
                    if max < mem[i+1][j]:
                        max = mem[i+1][j]+1
            print(max)
            mem[i][j] = max
    print(mem)
dynamic_programming_func()