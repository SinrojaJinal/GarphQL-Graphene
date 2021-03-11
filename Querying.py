# Context
import graphene
from graphene import ObjectType, String, Schema,ID
import json

class Query(ObjectType):
    name = String()

    def resolve_name(root, info):
        return info.context.get('name')

schema = Schema(Query)
result = schema.execute('{ name }', context={'name': 'Ross'})
assert result.data['name'] == 'Syrus' # for debugging purpose
# if name is not equal to Syrus then it will raise an Assertation error


items = dict(result.data.items())
print(json.dumps(itmes, indent=4))