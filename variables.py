import graphene
import json

class Query(graphene.ObjectType):
    name = graphene.String(n=graphene.String(default_value = 'Jinal'))

    def resolve_name(self, info, n):
        return f'Hello {n}'

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    query($name : String!){
        name(n : $name)
    }
    ''',
    variables = {'name' : 'payal'},
)

items = dict(result.data.items())
print(json.dumps(items,indent=4))