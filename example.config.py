solr_url = "http://path/to/my/solr/index"
fedora_url = "http://path/to/fedora/repo"
fedora_user = "fedoraUser"
fedora_pwd = "fedoraPassword"

data_root = "/path/to/my/data"
ingest_log = "/path/to/ingestlog.csv"

# GW ScholarSpace ingest configuration
ingest_path = "/opt/scholarspace/scholarspace-hyrax"
ingest_command = "rake RAILS_ENV=production gwss:ingest_work"
ingest_depositor = "openaccess@gwu.edu"

# Flags
retain_ids = False
load_as_private = True
debug_mode = False  # Behaves like a dry run, but DOES generate metadata-hyrax.json
