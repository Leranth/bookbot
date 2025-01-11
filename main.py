with open("books/frankenstein.txt") as f:
    char_dict = {}
    file_contents = f.read()
    #print(len(file_contents.split()))
    lowered_string = file_contents.lower()
    print("--- Begin report of books/frankenstein.txt ---")

    for char in lowered_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for element in char_dict:
        print(f"The '{element}' character was found {char_dict[element]} times")
    print("--- End report ---")
    # for frodo
