import os
from subprocess import call

def main():
    path = "/home/mark/metadata/Arrowmont/original_data/DC/Scrapbooks"
    output = f"{path}/output"
    for x in os.walk(path):
        for xml in x[2]:
            if xml.count("_") == 2:
                call(f"cp {path}/{xml} {output}/{xml}", shell=True)


if __name__ == "__main__":
    main()