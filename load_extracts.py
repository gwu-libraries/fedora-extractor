import config
from fedora2hyrax import fedora2hyrax
import json
import os
import subprocess


def load_extracts():
    import config
 
    for item_folder in os.listdir(config.data_root):
        folder_path = os.path.join(config.data_root, item_folder)
        folder_items = os.listdir(folder_path)
        print(folder_path)
        assert len(folder_items) == 2
        assert 'metadata.json' in folder_items
        folder_items.remove('metadata.json')
        attachment_file = folder_items[0]
        print(folder_path + "/" + attachment_file)
        m = open(os.path.join(folder_path, 'metadata.json'), 'r')
        m2 = open(os.path.join(folder_path, 'metadata-hyrax.json'), 'w')
	fedora_json = json.loads(m.read())
        hyrax_json = fedora2hyrax(fedora_json)
        m2.write(json.dumps(hyrax_json, indent=4, sort_keys=True))
        command = config.ingest_command.split(' ') + ['--',
                     '--manifest=%s' % os.path.join(folder_path,
                                                    'metadata-hyrax.json'),
                     '--primaryfile=%s' % os.path.join(folder_path,
                                                    attachment_file),
                     '--depositor=%s' % config.ingest_depositor,
                     '--set-item-id=%s' % item_folder]
        if config.debug_mode is False:
           print('Loading %s' % item_folder)
           output = subprocess.check_output(command, cwd=config.ingest_path)
        else:
           print(' '.join(command))


if __name__ == "__main__":
    
    load_extracts()
