def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[-1]  # Get the previous row
        for j in range(1, i):
            # Each element (except the first and last) is the sum of the elements above-left and above-right in the previous row
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

# Test the function
print(pascal_triangle(5))
