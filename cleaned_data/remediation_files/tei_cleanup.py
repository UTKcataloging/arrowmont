import os

path = "/home/mark/metadata/Arrowmont/original_data/TEI/Letters_TEI"
for x in os.walk(path):
    for file in x[2]:
        with open(f"{path}/{file}", "r") as input:
            with open(f"{path}/output/{file}", "w") as output:
                for line in input:
                    if line == '<?xml-stylesheet type="xml/xslt" href="../../frameworks/tei/xsl/html/teihtml-teic.xsl"?>\n':
                        pass
                    elif line.startswith('<!DOCTYPE TEI.2 SYSTEM '):
                        pass
                    else:
                        output.write(line)