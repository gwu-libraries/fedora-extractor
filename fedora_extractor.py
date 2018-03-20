import json
import os
import requests
import shutil
import solr


def extract_fedora_objects(ids, fedora_url, fedora_user, fedora_pwd):
    for id in ids[0:20]:
        print("%s --> %s" % (id, id_to_path(id)))
        rurl = fedora_url + "/" + id_to_path(id)
        r = requests.get(rurl, auth=(fedora_user, fedora_pwd),
                         headers={"Accept":"application/ld+json"})
        j = json.loads(r.content)
 
        filepath = config.data_root + "/" + id
        os.mkdir(filepath)

        with open(filepath + "/metadata.json", 'w') as metadata_file:
            metadata_file.write(json.dumps(j[0], indent=4, sort_keys=True))

        furl = rurl + "/content/fcr:metadata"
        r = requests.get(furl, auth=(fedora_user, fedora_pwd),
                         headers={"Accept":"application/ld+json"})
        j = json.loads(r.content)
        filename = j[0]["http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#filename"][0]["@value"]
        print('Filename = %s' % filename)
        fileurl = rurl + "/content"
        r = requests.get(fileurl, auth=(fedora_user, fedora_pwd), stream=True)
        with open(filepath + "/" + filename, 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r

def ids_from_solr(solr_url):
    s = solr.SolrConnection(solr_url)
    query = "+has_model_ssim:GenericFile"
    solr_response = s.query(query, fl="id", rows=2000)
    ids = [r['id'] for r in solr_response]
    for id in ids:
        print(id)
    return ids


def id_to_path(id):
    return "%s/%s/%s/%s/%s" % (id[0:2], id[2:4], id[4:6], id[6:8], id)


if __name__ == "__main__":
    import config
    
    print('Retrieving ids from solr index...')
    solr_ids = ids_from_solr(config.solr_url)
    print()
    print('Extracting Fedora objects...')
    extract_fedora_objects(solr_ids,
                           config.fedora_url,
                           config.fedora_user,
                           config.fedora_pwd)
