from graphene import ObjectType, String, Schema, Field
import json

class Person(ObjectType):
    full_name = String()

    
    def resolve_full_name(parent, info):
        print("in resolver full name")
        print(type(parent))
        full_name = 'Jinal sinroja'
        return f'{parent}'

class Query(ObjectType):
    me = Field(Person)

    
    def resolve_me(parent, info):
        # returns an object that represents a Person
        # print("ndlfknd")
        # n = 10
        
        name = 'payal kutana'
        return get_human(name)

def get_human(name):
    return "ross geller"

schema = Schema(query=Query)

query_string = "{ me { fullName } }"
result = schema.execute(query_string)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
