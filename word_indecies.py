def word_indices(sentence):
    words = sentence.split()
    indices_dict = {}
    
    for index, word in enumerate(words):
        if word in indices_dict:
            indices_dict[word].append(index)
        else:
            indices_dict[word] = [index]
    
    return indices_dict


sentence = "I am afritec trainee and I am learning python"
result = word_indices(sentence)
print(result)
