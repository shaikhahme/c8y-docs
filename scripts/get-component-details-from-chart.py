import json
from _datetime import datetime

output = []
with open("../data/buildartifact.json") as json_file:
    artifact_options_list = json.load(json_file).get('options')
    artifact_list = [build_artifact['option'] for build_artifact in artifact_options_list]
with open("../temp/temp-heml.json") as json_file:
    components_list = list(json.load(json_file).values())
for component in components_list:
    if component.get('component_name') in artifact_list and component.get('zones').get('c8y-ops-zone-1').get(
            'updated_at') is not None:
        name = (component.get('component_name'))
        version = (component.get('zones').get('c8y-ops-zone-1').get('desired_version'))
        date = str(component.get('zones').get('c8y-ops-zone-1').get('updated_at'))
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d')
        component = {'component_name': name, 'component_version': version, 'component_update_date': date}
        if component not in output:
            output.append(component)

with open('../temp/output.json', 'w') as output_file:
    json.dump(output, output_file)
