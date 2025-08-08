def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        num_lines = count_lines(filename)
        print(f"Number of lines in '{filename}': {num_lines}")
    except FileNotFoundError:
        print("File not found.")