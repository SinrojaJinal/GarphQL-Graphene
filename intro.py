from graphene import ObjectType, String, Schema
import json

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)

result = schema.execute(
    '''
    {
        hello($name)
        goodbye
    }
    ''',
    variables = {'name' : 'Payal'}
)

items = dict(result.data.items())
print(json.dumps(items,indent=4))