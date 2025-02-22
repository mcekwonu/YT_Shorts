#
# www.youtube.com/@mersthub_mentors
#

def transpose(mat):
    return [list(row) for row in zip(*mat)]


mat_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose(mat_A)

print(transposed)

# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]