import brewery
from brewery import ds
import sys

sources = [
	{"file": "mfccJos.csv",
	 "fields": ["speech", "Avgf0", "Avgf1", "Avgf2", "Avgf3", "Avgf4", "Avgf5", "Avgf6", "Avgf7", "Avgf8", "Avgf9", "Avgf10", "Avgf11", "Avgf12", "filename" ]},
	{"file": "vadJos.csv",
	 "fields": ["filename", "total_energy", "total_F", "total_SFM", "speech" ]} 

]

all_fields  = brewery.FieldList(["file"])

for source in sources:
	for field in source["fields"]:
		if field not in all_fields:
			all_fields.append(field)

out = ds.CSVDataTarget("vadMfccJos.csv")
out.fields = brewery.FieldList(all_fields)
out.initialize()

for source in sources:
    path = source["file"]
    
    #path = "/users/Capodit3/Documents/Sensedata/sense-os project2/" + path

    # Initialize data source: skip reading of headers - we are preparing them ourselves
    # use XLSDataSource for XLS files
    # We ignore the fields in the header, because we have set-up fields
    # previously. We need to skip the header row.

    src = ds.CSVDataSource(path,read_header=True, skip_rows=1)
    src.fields = ds.FieldList(source["fields"])
    src.initialize()

    for record in src.records():

        # Add file reference into ouput - to know where the row comes from
        record["file"] = path
        out.append(record)

    # Close the source stream
    src.finalize()