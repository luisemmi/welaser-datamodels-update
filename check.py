import geojson
import json
import os
import re

for root, dirs, files in os.walk("."):
    for file in sorted(filter(lambda f: f.endswith('.json'), files)):
        path = os.path.join(root, file)
        if "package" not in path and "renovate" not in path:
            print(path)
            with open(path) as f:
                entity = json.load(f)
                # all entities should have a type and an id
                assert "id" in entity
                assert " " not in entity["id"], {"id": entity["id"]}
                assert "type" in entity
                assert " " not in entity["type"], {"id": entity["id"], "type": entity["type"]}
                regexp = re.compile(r'\(|\)')
                for key, value in entity.items():
                    assert not key.startswith(" ") and not key.endswith(" "), {"id": entity["id"], key: value}
                    assert not str(value).startswith(" ") and not str(value).endswith(" "), {"id": entity["id"], key: value}
                    assert not regexp.search(str(value)), {"id": entity["id"], key: value}
                #if "Task" in path:
                #    assert "actualLocation" in entity, f"Entity: {path}"
                if "location" in entity:
                    assert geojson.loads(json.dumps(entity["location"])).is_valid
                if "controlledProperty" in entity:
                    known_properties = set(["heartbeat", "temperature", "humidity", "image", "timestamp"])
                    difference = set(entity["controlledProperty"]).difference(known_properties)
                    assert (len(difference) == 0), "Unknown properties: " + str(difference)
