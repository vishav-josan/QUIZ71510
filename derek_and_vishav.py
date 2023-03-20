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
