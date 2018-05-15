import os

path = "/home/mark/metadata/Arrowmont/original_data/TEI/Arrow_Articles"
for x in os.walk(path):
    for file in x[2]:
        with open(f"{path}/{file}", "r") as input:
            with open(f"{path}/output/{file}", "w") as output:
                for line in input:
                    if line != '<!DOCTYPE TEI.2 SYSTEM "tei.dtd">\n':
                        output.write(line)