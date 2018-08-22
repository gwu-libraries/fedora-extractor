# fedora-extractor
Extracts content from a Sufia-based repository via Solr and Fedora APIs. 

Assumes Sufia 6 objects (pre-PCDM) stored in Fedora 4.6.0 repository, indexed in Solr.  Does *not* require a live Sufia app.

`fedora_extractor.py` - Extracts content from target repository.  The result will be a set of folders, where the name of each folder is an object ID, and each folder contains the (single) file associated with the object, and `metadata.json` containing the object's metadata from Fedora.

`load_extracts.py` - Iterates through content extracted to target folder and invokes rake command to ingest into Hyrax repository. NOTE: The rake task invoked is specific to GW's scholarspace-hyrax ingest_work rake task (see https://github.com/gwu-libraries/scholarspace-hyrax/blob/master/lib/tasks/gwss.rake ).  Creates a CSV log mapping original item IDs to IDs in new repository.

`fedora2hyrax.py` - Utility to extract selected fields from Fedora metadata, and write "plain" json suitable for ingesting into GW ScholarSpace Hyrax-based repository via ingest_work rake task (see https://github.com/gwu-libraries/scholarspace-hyrax/blob/master/lib/tasks/gwss.rake)

`generate_redirects.py` - Generates Apache `Redirect` directives to redirect from old IDs to IDs as migrated into new repository.  Takes the CSV file generated by `load_extracts.py` as the single argument.  Writes to stdout; redirect as desired.

## Setup

- Within your python environment (e.g. with virtualenv), `pip install -r requirements.txt`
- `cp example.config.py config.py` , then configure the values in `config.py`
- Currently, the `ids_from_solr` method is hard-coded to retrieve the first 2000 records.  If your repository contains more than 2000 records, either increase the value of `rows=` or use pagination to get the full set of results.
