def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase

    lines = []
    for i in range(size):
        
        left = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        
        line = left.center(4 * size - 3, '-')
        lines.append(line)

    
    full_rangoli = lines[::-1][:-1] + lines  
    print('\n'.join(full_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
