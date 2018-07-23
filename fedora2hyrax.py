import json
import sys

# Fedora to Hyrax mapping
f2h = {
    # Hyrax: Fedora
    'title': 'http://purl.org/dc/terms/title',
    'resource_type': 'http://purl.org/dc/terms/type',
    'creator': 'http://purl.org/dc/terms/creator',
    'keyword': 'http://purl.org/dc/terms/relation',
    'description': 'http://purl.org/dc/terms/description',
    'date_created': 'http://purl.org/dc/terms/created',
    'gw_affiliation': 'http://scholarspace.library.gwu.edu/ns#gwaffiliation',
    'language': 'http://purl.org/dc/terms/language',
    'license': 'http://purl.org/dc/terms/rights'
}


def fedora2hyrax(j):
    j2 = {}
    for fed, hyr in f2h.items():
        if hyr in j:
            j2[fed] = [k['@value'] for k in j[hyr]]
    return(j2)


if __name__ == "__main__":
    fedora_json_file = sys.argv[1]
    with open(fedora_json_file, 'r') as f:
        fedora_json = json.loads(f.read())
        # print("FEDORA:")
        # print(json.dumps(fedora_json, indent=4, sort_keys=True))
        hyrax_json = fedora2hyrax(fedora_json)
        # print("HYRAX:")
        print(json.dumps(hyrax_json, indent=4, sort_keys=True))
