# take in file, pull out text wanted, output
# need to fill in blanks or incomplete vouchers 3-6 8-9 and 11, 7 is a marker,

# import re
import string

# def rewrite_cell(to_write, used_info):
#     if to_write == "":
#         to_write =

def taxonomy(list):
    t_count = 0

    for taxon in list:
        if taxon.title() == taxon:
            continue
        for letter in taxon:
            if letter.isupper() or letter.isdigit() or letter in string.punctuation or taxon == "unknown" or taxon == "family" or taxon == "genus" or taxon == "species":
                t_count += 1
    t_string = ""
    if t_count > 0:
        for tax in list:
            t_string = t_string + f"{tax} "
    return t_string


def data_extraction():
    filename = "database_all_01july2022.txt" #input("Please enter file name: ")
    to_create = "aug17_extraction.txt" #input("Please name created file with .txt: ")
    voucher_d = {}
    with open(filename) as reader:
        # header = reader.readline()

        for line in reader:
            lines = line.rstrip().split("\t")

            if len(lines) == 1:
                continue
            tax_notes = taxonomy([lines[4], lines[5], lines[6]])
            if lines[7].lower() == 'y':
                if lines[1] != "":
                    if len(lines) >= 12:
                        my_list = [lines[2], lines[3], lines[4], lines[5], lines[6], tax_notes,lines[8], lines[9], lines[11]]
                    elif len(lines) < 10:
                        my_list = [lines[2],lines[3],lines[4],lines[5],lines[6],tax_notes,lines[8]]
                    else:
                        my_list = [lines[2],lines[3],lines[4],lines[5],lines[6],tax_notes,lines[8], lines[9]]
                    if lines[1] not in voucher_d:
                        voucher_d[lines[1]] = []
                    else:
                        x = 1
                    voucher_d[lines[1]].append(my_list)
                else:
                    if len(lines) >= 12:
                        my_list = [lines[2],lines[3],lines[4],lines[5],lines[6],tax_notes,lines[8], lines[9],lines[11]]
                    elif len(lines) < 10:
                        my_list = [lines[2],lines[3],lines[4],lines[5],lines[6], tax_notes,lines[8]]
                    else:
                        my_list = [lines[2],lines[3],lines[4],lines[5],lines[6],tax_notes,lines[8], lines[9]]



    with open(to_create, 'w') as writer:

        key_list = []
        museum_list = []
        for key, value in voucher_d.items():
            for piece in value:
                try:
                    if value[1]:
                        if f"{piece[1]}" not in museum_list:
                            museum_list.append(f"{piece[1]}")
                        else:
                            museum_list.append(f"{piece[1]}")
                except:
                    continue
        for key, value in voucher_d.items():

# duplicates get _v1 _v2 etc; June 23 2022 - change implemented
# duplicate Museum IDs get _v work -
            count = 1
            for piece in value:
                try:
                    if value[1]:

                        if f"{key}" not in key_list:
                            writer.write(f"{key.rstrip()}_v1\t")
                            key_list.append(f"{key}")

                        else:
                            key_list.append(f"{key}")
                            writer.write(f"{key.rstrip()}_v{key_list.count(f'{key}')}\t")
# New changes as of June 23, 2022: allows for duplicate IDs to receive an appended "_v" with a number, and increment that number

                        for part in piece:
                            if part == piece[1]:
                                if museum_list.count(f"{part}") > 1:
                                    writer.write(f"{part.rstrip()}_v{count}\t")
                                    count += 1
                                else:
                                    writer.write(f"{part.rstrip()}\t")
                            else:
                                writer.write(f"{part.rstrip()}\t")
                        writer.write("\n")

                except:
                    writer.write(f"{key.rstrip()}\t")

                    for part in piece:
                        writer.write(f"{part}\t")
                    writer.write("\n")


# Evidently, something is causing duplication. i suspect it is line 63.

data_extraction()

