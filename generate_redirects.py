import csv
import sys

new_server_id = "https://scholarspace-etds.library.gwu.edu"

# Generate Apache redirects
def generate_redirects(id_map_file):
    with open(id_map_file, 'r') as mapfile:
        reader = csv.DictReader(mapfile)
        for row in reader:
            print("Redirect /files/%s %s/work/%s" % 
              (row['original_id'], new_server_id, row['gwssetd_id']))


if __name__ == "__main__":
    id_map_file = sys.argv[1]
    generate_redirects(id_map_file)
