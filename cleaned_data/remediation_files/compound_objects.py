import os
import csv

def main():
    output = "/home/mark/metadata/Arrowmont/cleaned_data/mods/3dobject-compound_objects"
    path_to_objects = "/gwork/mark/metadata/Arrowmont/original_data/MODS/Arrow_MODS"
    for path in os.walk(path_to_objects):
        for object in path[2]:
            new_Record = Record(object, output)
            new_Record.find_matching_row()

class Record:
    def __init__(self, filename, destination):
        self.filename = filename
        self.data = []
        self.output = destination

    def find_matching_row(self):
        my_csv = "/home/mark/metadata/Arrowmont/original_data/csvs/3dobject-videos.csv"
        with open(my_csv) as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            for row in readCSV:
                if row[6] in self.filename:
                    self.data = row
                    self.create_metadata_record()

    def create_metadata_record(self):
        output_file = self.filename.replace("TIF", "xml")
        root = '<mods xmlns="http://www.loc.gov/mods/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.5" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">'
        creator = f"<name><namePart>{self.data[0]}</namePart><role><roleTerm>Creator</roleTerm></role></name>"
        title = f"<titleInfo><title>{self.data[1]}</title></titleInfo>"
        origin = f"<originInfo><dateCreated>{self.data[2]}</dateCreated></originInfo>"
        physical = f"<physicalDescription><extent>{self.data[3]}</extent></physicalDescription>"
        abstract = f"<abstract>{self.data[4]}</abstract>"
        identifier = f'<identifier type="filename">{self.data[5]}</identifier>'
        rights = '<accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/CNE/1.0/">Copyright Not Evaluated</accessCondition>'
        record_info = '<recordInfo><recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource></recordInfo>'
        type_of_resource = '<typeOfResource>three dimensional object</typeOfResource>'
        with open(f"{self.output}/{output_file}", "w") as final_xml:
            final_xml.write('<?xml version="1.0" encoding="UTF-8"?>')
            final_xml.write(root)
            final_xml.write(title)
            final_xml.write(creator)
            final_xml.write(origin)
            final_xml.write(physical)
            final_xml.write(abstract)
            final_xml.write(identifier)
            final_xml.write(rights)
            final_xml.write(record_info)
            final_xml.write(type_of_resource)
            final_xml.write('</mods>')

if __name__ == "__main__":
    main()