import json
import sys


def fedora2hyrax():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        j = json.loads(f.read())
        # print(json.dumps(j, indent=4, sort_keys=True))
        j2 = {}
        j2['title'] = j['http://purl.org/dc/terms/title'][0]['@value']
        j2['resource_type'] = j['http://purl.org/dc/terms/type'][0]['@value']
        j2['creator'] = j['http://purl.org/dc/terms/creator'][0]['@value']
        if 'http://purl.org/dc/terms/relation' in j:
            j2['keyword'] = [k['@value'] for k in j['http://purl.org/dc/terms/relation']]
        j2['description'] = j['http://purl.org/dc/terms/description'][0]['@value']
        j2['date_created'] = j['http://purl.org/dc/terms/created'][0]['@value']
        if 'http://scholarspace.library.gwu.edu/ns#gwaffiliation' in j:
            j2['gw_affiliation'] = j['http://scholarspace.library.gwu.edu/ns#gwaffiliation'][0]['@value']
        if 'http://purl.org/dc/terms/language' in j:
            j2['language'] = j['http://purl.org/dc/terms/language'][0]['@value']
        j2['rights'] = j['http://purl.org/dc/terms/rights'][0]['@value']
        print(json.dumps(j2, indent=4, sort_keys=True))


if __name__ == "__main__":
    fedora2hyrax()
