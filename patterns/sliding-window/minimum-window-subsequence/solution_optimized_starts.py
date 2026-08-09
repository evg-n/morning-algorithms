def minWindow(s1, s2):
    result = ""

    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            if j < len(s2) - 1:
                j += 1
            else:
                end_i = i
                while True:
                    if s1[i] == s2[j]:
                        if j == 0:
                            break
                        j -= 1
                    i -= 1

                if result == "" or end_i + 1 - i < len(result):
                    result = s1[i : end_i + 1]

                i += 1
        i += 1
    return result

if __name__ == "__main__":
    assert minWindow("abcdebdde", "bde") == "bcde"
    assert minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "kzed") == "kzxwqegknd"
    assert minWindow("abcdbebe", "bbe") == "bebe"
