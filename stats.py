def get_book_text(link):
    with open(link) as f:
        contents = f.read()
        contents = contents.split()
        return len(contents)

def get_char_count(link):
    with open(link) as f:
        contents = f.read()
        content = {}
        for char in contents:
            char = char.lower()
            if char in content:
                content[char] += 1
            else:
                content[char] = 1
        new_list = []
        for key in content:
            new_list.append({"char": key, "num": content[key]})

        return new_list

def sort_dict(dict):
    return dict["num"]

def sort_char_count(link):
    new_dict = get_char_count(link)
    new_dict.sort(reverse=True, key=sort_dict)
    return new_dict


    

