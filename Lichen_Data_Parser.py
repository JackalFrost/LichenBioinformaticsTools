
def unique_finder(filename):
    unique_species = []

    with open(filename) as lichens:
#    header = lichens.readline()

        for line in lichens:
            lines = line.rstrip().split("\t")
            print(f"{lines[0]} {lines[1]} {lines[2]}")
            if f"{lines[0]} {lines[1]} {lines[2]}" not in unique_species:
                unique_species.append(f"{lines[0]} {lines[1]} {lines[2]}")

        print(len(unique_species))


def finder_98(filename):
    under_98 = []
    above_98 = []
    with open(filename) as lichens:
        #    header = lichens.readline()

        for line in lichens:
            lines = line.rstrip().split("\t")
            if lines[0] == '':
                # under_98.append(f"{lines[8]} {lines[9]}")
                continue
            elif lines[0] == "multi-identity":
                # under_98.append(f"{lines[8]} {lines[9]}")
                continue
            elif float(lines[0]) >= 98.0:
                if f"{lines[8]} {lines[9]}" not in above_98:
                    above_98.append(f"{lines[8]} {lines[9]}")
            else:
                # if f"{lines[8]} {lines[9]}" not in above_98:
                    under_98.append(f"{lines[8]} {lines[9]}")

    return len(above_98)


def finder_985(filename):
    under_985 = []
    above_985 = []
    with open(filename) as lichens:
        #    header = lichens.readline()

        for line in lichens:
            lines = line.rstrip().split("\t")
            if lines[0] == '':
                continue
            elif lines[0] == "multi-identity":
                continue
            elif float(lines[0]) >= 98.5:
                if f"{lines[8]} {lines[9]}" not in above_985:
                    above_985.append(f"{lines[8]} {lines[9]}")
            else:
                under_985.append(f"{lines[8]} {lines[9]}")

    return len(above_985)

def main_function():
    file_is = input("Please input filename: ")
    start = True
    while start:
        user_input = input("98 for 98 analysis, 98.5 for 98.5 analysis, U for Unique, X for exit: ")
        if user_input == "98":
            print(finder_98(file_is))
        elif user_input == "98.5":
            print(finder_985(file_is))
        elif user_input.lower() == "u":
            print(unique_finder(file_is))
        elif user_input.lower() == "x":
            start = False


main_function()
