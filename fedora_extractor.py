import config
import json
import os
import requests
import shutil
import solr
import urllib


def extract_fedora_objects(ids, fedora_url, fedora_user, fedora_pwd):
    for id in ids:
        print("%s --> %s" % (id, id_to_path(id)))
        rurl = fedora_url + "/" + id_to_path(id)
        r = requests.get(rurl, auth=(fedora_user, fedora_pwd),
                         headers={"Accept": "application/ld+json"})
        j = r.json()
        for member in j[0]['http://pcdm.org/models#hasMember']:
            print(member['@id'])
            r_member = requests.get(member['@id'],
                                    auth=(fedora_user, fedora_pwd),
                                    headers={"Accept": "application/ld+json"})
            j = r_member.json()
            for f in j[0]['http://pcdm.org/models#hasFile']:
                r_file = requests.get(f['@id']+'/fcr:metadata',
                                      auth=(fedora_user, fedora_pwd),
                                      headers={"Accept": "application/ld+json"})
                j = r_file.json()
                mType = j[0]['http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#hasMimeType']
                if mType[0]['@value'] == 'application/pdf':
                    print('found PDF')
                    fileurl = f['@id']
                    filename = j[0]["http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#filename"][0]["@value"]
                    r_download = requests.get(fileurl, auth=(fedora_user, fedora_pwd), stream=True)
                    with open(filename, 'wb') as out_file:
                        shutil.copyfileobj(r_download.raw, out_file)                        
                # else do nothing
"""
        filepath = config.data_root + "/" + id
        if not config.debug_mode:
            os.mkdir(filepath)

        if not config.debug_mode:
            with open(filepath + "/metadata.json", 'w') as metadata_file:
                metadata_file.write(json.dumps(j[0], indent=4, sort_keys=True))

        furl = rurl + "/content/fcr:metadata"
        r = requests.get(furl, auth=(fedora_user, fedora_pwd),
                         headers={"Accept":"application/ld+json"})
        j = r.json()
        filename = j[0]["http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#filename"][0]["@value"]
        print('Filename = %s' % filename)
        fileurl = rurl + "/content"
        r = requests.get(fileurl, auth=(fedora_user, fedora_pwd), stream=True)
        if not config.debug_mode:
            with open(filepath + "/" + urllib.parse.unquote(filename),
                      'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
        del r
"""


def ids_from_solr(solr_url):
    s = solr.SolrConnection(solr_url)
    ids = []
    for model_type in ['GwWork', 'GwEtd']:
      query = "+has_model_ssim:" + model_type
      solr_response = s.query(query, fl="id", rows=12000)
      ids += [r['id'] for r in solr_response]

    for id in ids:
        print(id)
    return ids


def id_to_path(id):
    return "%s/%s/%s/%s/%s" % (id[0:2], id[2:4], id[4:6], id[6:8], id)


if __name__ == "__main__":
    print('Retrieving ids from solr index...')
    # solr_ids = ids_from_solr(config.solr_url)
    solr_ids = ['gb19f602j']
    print()
    print('Extracting Fedora objects...')
    extract_fedora_objects(solr_ids,
                           config.fedora_url,
                           config.fedora_user,
                           config.fedora_pwd)
