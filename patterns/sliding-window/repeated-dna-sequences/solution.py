def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []

    seq_to_freq = {}
    
    for i in range(len(s) - 10 + 1):
        substr = s[i:i + 10]
        if substr not in seq_to_freq:
            seq_to_freq[substr] = 1
        else:
            seq_to_freq[substr] += 1
    
    results = []

    for k, v in seq_to_freq.items():
        if v > 1:
            results.append(k)
    return results
