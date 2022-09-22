def fasta_writer():
    filename = input("Please input file name: ")
    to_create = input("Please input name of file to be created: ")

    with open(filename) as reader:
        with open(to_create, 'w') as writer:
            header = input("Does your file have a header? Y for Yes, N for No: ")
            column_id = int(input("What column is your ID in?: ")) - 1
            column_dna = int(input("What column is your DNA sequence in?: ")) - 1
            if header.lower() == "y":
                headline = reader.readline()

            for line in reader:
                lines = line.rstrip().split("\t")
                if lines[column_dna] == "" or lines[column_dna] == "":
                    continue
                else:
                    writer.write(f">{lines[column_id]}\n")
                    writer.write(f"{lines[column_dna]}\n")



fasta_writer()
