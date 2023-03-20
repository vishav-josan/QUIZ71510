def replace_all(input_file, output_file, search, replace):
    """
    Replace instances of search in input_file with replace.

    :param input_file: a string that represents the file where content is pulled from
    :param output_file: a string that represents the file where updated content will be written
    :param search: a string
    :param replace: a string
    :precondition: input_file must be a string
    :precondition: input_file must be the name of an existing file
    :precondition: output_file must be a string
    :precondition: output_file must be the name of an existing file
    :precondition: search must be a string
    :precondition: replace must be a string
    :postcondition: rewrites contents of input_file in output file with all instances of search replaced with replace
    :return: an integer for the number of words that were replaced
    """
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


def main():
    """
    Drive the program.
    """
    input_file = input("Please input the input file name:")
    output_file = input("Please input the output file name:")
    search = input("Please input the word that will be replaced:")
    replace = input("Please input the word that will replace it:")
    counter = replace_all(input_file, output_file, search, replace)
    print(f"Successfully replaced {counter} occurrences of {replace}")


if __name__ == "__main__":
    main()
