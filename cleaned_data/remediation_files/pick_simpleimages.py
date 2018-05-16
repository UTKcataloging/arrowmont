import os
from subprocess import call

def move():
    path = "/home/mark/metadata/Arrowmont/original_data/DC/Scrapbooks"
    output = f"{path}/output"
    for x in os.walk(path):
        for xml in x[2]:
            if xml.count("_") == 2:
                call(f"cp {path}/{xml} {output}/{xml}", shell=True)

def main():
    path = "/home/mark/metadata/Arrowmont/original_data/DC/Scrapbooks_Images"
    for x in os.walk(path):
        for xml in x[2]:
            print(xml)
            current_record = SimpleImageRecord(xml, path)
            current_record.remove_record_lines()


class SimpleImageRecord:
    def __init__(self, file ,path):
        self.file = file
        self.path = path

    def insert_parent(self):
        parent_node = '<oai_dc:dc xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">'
        return parent_node

    def close_parent(self):
        close_tag = "</oai_dc:dc>"
        return close_tag


    def remove_record_lines(self):
        with open(f"{self.path}/{self.file}", "r") as input:
            with open(f"{self.path}/output/{self.file}", "w") as output:
                output.write(self.insert_parent())
                for line in input:
                    if "<record>" in line:
                        pass
                    elif "</record>" in line:
                        pass
                    else:
                        output.write(line)
                output.write(self.close_parent())


if __name__ == "__main__":
    main()