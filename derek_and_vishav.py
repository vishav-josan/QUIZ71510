def replace_all(input_file, output_file, search, replace):
    with open(input_file) as file_object:
        contents = file_object.read()
    with open(output_file, "w") as output:
        new_contents = ""
        count = 0
        for word in contents:
            if word == search:
                new_contents += replace
                count += 1
            else:
                new_contents += word
        output.write(new_contents)

    return count
