


def permutation (string, curr_index, curr_string, all_perm):
    if (curr_index >= len(string)):
        all_perm.append("".join(list(curr_string)))
        return

    for i in range(0, len(curr_string)+1):
        permutation(string, curr_index + 1, curr_string[:i]+ string[curr_index] + curr_string[i:], all_perm)



all_perm= []
permutation("ABSG", 0 , "", all_perm)
print(all_perm)