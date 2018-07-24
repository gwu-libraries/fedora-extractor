import config
import datetime
from fedora2hyrax import fedora2hyrax
import json
import os
import subprocess
from subprocess import CalledProcessError


def load_extract(item_id):
    folder_path = os.path.join(config.data_root, item_id)
    folder_items = os.listdir(folder_path)

    print(folder_path)
    if 'metadata-hyrax.json' in folder_items:
        folder_items.remove('metadata-hyrax.json')
    assert 'metadata.json' in folder_items
    assert len(folder_items) == 2
    folder_items.remove('metadata.json')
    attachment_file = folder_items[0]
    print("   " + attachment_file)

    with open(os.path.join(folder_path, 'metadata.json'), 'r') as m:
        fedora_json = json.loads(m.read())
    with open(os.path.join(folder_path, 'metadata-hyrax.json'), 'w') as m2:
        hyrax_json = fedora2hyrax(fedora_json)
        m2.write(json.dumps(hyrax_json, indent=4, sort_keys=True))

    command = config.ingest_command.split(' ') + ['--',
                 '--manifest=%s' % os.path.join(folder_path,
                                                'metadata-hyrax.json'),
                 '--primaryfile=%s' % os.path.join(folder_path,
                                                attachment_file),
                 '--depositor=%s' % config.ingest_depositor]

    if config.retain_ids is True:
        command += ['--set-item-id=%s' % item_folder]

    if config.load_as_private is True:
        command += ['--private']

    if config.debug_mode is False:
        try:
            processresult = subprocess.check_output(command, cwd=config.ingest_path,
                                                    stderr=subprocess.STDOUT)
            output = processresult.decode('utf-8')
            output_pieces = output.split('\n')
            new_id = output_pieces[-2]

            if not os.path.isfile(config.ingest_log):
                ingestlog = open(config.ingest_log, "w")
                ingestlog.write("original_id,gwssetd_id,upload_time\n")
                ingestlog.close()
            with open(config.ingest_log, "a") as ingestlog:
                now = datetime.datetime.utcnow()
                ingestlog.write("%s,%s,%s\n" % (item_id, new_id,
                                                now.isoformat()))
        except CalledProcessError as e:
            print e.output
    else:
        print(' '.join(command) + '\n')


def load_all_extracts():
    for item_folder_id in os.listdir(config.data_root):
        load_extract(item_folder_id)


if __name__ == "__main__":
    load_all_extracts()
