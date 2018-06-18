import requests
import csv


class Settings:
    def __init__(self):
        self.pdf_output = "/home/mark/metadata/Arrowmont/original_data/pdfs"
        self.metadata_output = "/home/mark/metadata/Arrowmont/cleaned_data/mods/historical_essays"


class Set:
    def __init__(self, the_csv):
        self.path_to_csv = the_csv

    def process_records(self):
        config = Settings()
        with open(self.path_to_csv) as my_csv:
            csv_contents = csv.reader(my_csv, delimiter=',')
            i = 0
            for row in csv_contents:
                if i != 0:
                    new_record = Record(row)
                    new_record.download_pdf(config.pdf_output, i)
                    new_record.create_metadata_record(i, config.metadata_output)
                i +=1


class Record:
    def __init__(self, row_data):
        self.data = row_data

    def download_pdf(self, pdf_output, unique_id):
        r = requests.get(self.data[2], verify=False)
        if r.status_code == 200:
            print(f"Downloading {unique_id}.pdf to {pdf_output}.")
            with open(f"{pdf_output}/{unique_id}.pdf", 'wb') as work:
                work.write(r.content)
        return

    def create_metadata_record(self, unique_id, metadata_output):
        root = '<mods xmlns="http://www.loc.gov/mods/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="3.5" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">\n'
        title = f"<titleInfo><title>{self.data[1]}</title></titleInfo>\n"
        subject = f"<subject><topic>{self.data[0]}</topic></subject>\n"
        author = f"<name><namePart>Steve Davis</namePart><role><roleTerm authority='marcrelators' valueURI='http://id.loc.gov/vocabulary/relators/aut'>Author</roleTerm></role></name>\n"
        record_info = '<recordInfo><recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource></recordInfo>\n'
        type_of_resource = '<typeOfResource>text</typeOfResource>\n'
        identifier = f"<identifier type='filename'>{self.data[2].replace('http://www.lib.utk.edu/arrowmont/Steve/', '')}</identifier>\n"
        rights = '<accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/InC/1.0/">In Copyright</accessCondition>\n'
        with open(f"{metadata_output}/{unique_id}.xml", "w") as final_xml:
            print(f"Writing file to {metadata_output}/{unique_id}.xml")
            final_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            final_xml.write(root)
            final_xml.write(title)
            final_xml.write(author)
            final_xml.write(identifier)
            final_xml.write(rights)
            final_xml.write(record_info)
            final_xml.write(type_of_resource)
            final_xml.write(subject)
            final_xml.write('</mods>')
        return


if __name__ == "__main__":
    my_set = Set("/home/mark/metadata/Arrowmont/original_data/csvs/historical_essarys.csv")
    my_set.process_records()