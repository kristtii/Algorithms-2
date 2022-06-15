def solve(s, word_dictionary):

    INPUT_LENTH = len(s)

    iterative_list = [""] * INPUT_LENTH + 1
    iterative_list[0] = []
    if(INPUT_LENTH == 0): return iterative_list[0]
    hashset = set()
    for word in word_dictionary:
        hashset.add(len(word))

    for i in range(INPUT_LENTH):
        iterative_list[i] = []
        for j in hashset:
            if(i - j >= 0):
                sub = s[i-j: i]
                if sub in word_dictionary:
                    tmp = [''] * i - j
                    if(i - j == 0):
                        iterative_list[i].push(sub)
                    else:
                        for word in tmp:
                            iterative_list[i].push(f'{word} {sub}')
        return iterative_list[INPUT_LENTH]


if __name__ == '__main__':
    d = int(input())
    s = input()
    word_dictionary = set()
    for _ in range(d):
        word_dictionary.add(input())

    answer = " ".join(solve(s, word_dictionary))

    print(f"Answer: {answer}")
