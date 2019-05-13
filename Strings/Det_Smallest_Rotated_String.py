def bubble_swap(string,i,j):
    string = list(string)

    #Rotate so that i is at the beginning.
    while i > 0:
        string = string[1:] + string[:1]
        i -= 1

        string = string[:1] + string[2:] + string[1:2]
        string = string[1:] + string[:1]

        while len(string) > j + 1:
            string = string[1:] + string[:1]
            j += 1

        return ''.join(string)

def get_best_word(string,k):
    string = list(string)

    if k == 1:
        best = string
        for i in range(1,len(string)):
            if string[i:] + string[:i]:
                best = string[i:] + string[:i]
        return ''.join(best)
    else:
        return ''.join(sorted(string))
if __name__ == "__main__":
    print(get_best_word('daily',1))