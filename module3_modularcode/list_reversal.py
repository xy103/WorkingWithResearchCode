def reversi(arr):
    """Reverses a list."""
    for i in range(len(arr) // 2):
        arr[-i - 1], arr[i] = arr[i], arr[-i - 1]
    return arr


a = [0, 1, 2]
b = reversi(a)
print(b)
print(a)