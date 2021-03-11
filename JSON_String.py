from graphene import Schema, ObjectType, JSONString, String
import json

class Query(ObjectType):
    update_json_key = JSONString(
        required=True,
        json_input=JSONString(required=True),
        key=String(required=True),
        value=String(required=True)
    )

    def resolve_update_json_key(root, info, json_input, key, value):
        assert json_input == {"name": "Jane"}
        json_input[key] = value
        return json_input

schema = Schema(query=Query)

results = schema.execute("""
    query {
        updateJsonKey(jsonInput: "{\\"name\\": \\"Jane\\"}", key: "name", value: "Beth")
    }
""")

assert results.data == {"updateJsonKey": "{\"name\": \"Beth\"}"}

items = dict(results.data.items())
print(json.dumps(items, indent=4))