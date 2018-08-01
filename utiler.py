import json

def save_to_local_json(fname, data):
    data_json = json.dumps(data, indent=4)
    f = open('./data/%s' % fname, 'w')
    f.write(data_json)
    f.close()
