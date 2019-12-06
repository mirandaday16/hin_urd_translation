def fileCleaner(messy_file):
    with open(messy_file, 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if not line == "\n":
                file.write(line)
    # for character in fin:
    #     if not character.isalpha():
    #         character = character.replace(character, "")
    #     fout.write(character)
    file.close()


def main():
    fileCleaner("premchand_ur_baby.txt")
