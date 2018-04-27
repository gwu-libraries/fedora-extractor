# fedora-extractor
Extracts content from a Sufia-based repository via Solr and Fedora APIs.

Assumes Sufia 6 objects (pre-PCDM) stored in Fedora 4.6.0 repository, indexed in Solr.  Does *not* require a live Sufia app.

`fedora_extractor.py` - Extracts content from target repository

`load_extracts.py` - Iterates through content extracted to target folder and invokes rake command to ingest into new repository

`fedora2hyrax.py` - Utility to extract selected fields from Fedora metadata, and write "plain" json for ingesting into Hyrax repository via ingest_work rake task
