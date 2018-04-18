import json
import sys

# Fedora to Hyrax mapping
f2h = {
    'title': 'http://purl.org/dc/terms/title',
    'resource_type': 'http://purl.org/dc/terms/type',
    'creator': 'http://purl.org/dc/terms/creator',
    'keyword': 'http://purl.org/dc/terms/relation',
    'description': 'http://purl.org/dc/terms/description',
    'date_created': 'http://purl.org/dc/terms/created',
    'gw_affiliation': 'http://scholarspace.library.gwu.edu/ns#gwaffiliation',
    'language': 'http://purl.org/dc/terms/language',
    'rights': 'http://purl.org/dc/terms/rights'
}


def fedora2hyrax():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        j = json.loads(f.read())
        # print(json.dumps(j, indent=4, sort_keys=True))
        j2 = {}
        for fed, hyr in f2h.items():
            if hyr in j:
                j2[fed] = [k['@value'] for k in j[hyr]]
        print(json.dumps(j2, indent=4, sort_keys=True))


if __name__ == "__main__":
    fedora2hyrax()
