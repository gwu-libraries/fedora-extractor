# fedora-extractor
Extracts content from a Sufia-based repository via Solr and Fedora APIs. 

Assumes Sufia 6 objects (pre-PCDM) stored in Fedora 4.6.0 repository, indexed in Solr.  Does *not* require a live Sufia app.

`fedora_extractor.py` - Extracts content from target repository.  The result will be a set of folders, where the name of each folder is an object ID, and each folder contains the (single) file associated with the object, and `metadata.json` containing the object's metadata from Fedora.

`load_extracts.py` - Iterates through content extracted to target folder and invokes rake command to ingest into Hyrax repository. NOTE: The rake task invoked is specific to GW's scholarspace-hyrax ingest_work rake task (see https://github.com/gwu-libraries/scholarspace-hyrax/blob/master/lib/tasks/gwss.rake )

`fedora2hyrax.py` - Utility to extract selected fields from Fedora metadata, and write "plain" json suitable for ingesting into Hyrax repository via ingest_work rake task (specifically, GW's scholarspace-hyrax ingest_work rake task -- see https://github.com/gwu-libraries/scholarspace-hyrax/blob/master/lib/tasks/gwss.rake)

## Setup

- Within your python environment (e.g. with virtualenv), `pip install -r requirements.txt`
- `cp example.config.py config.py` , then configure the values in `config.py`
