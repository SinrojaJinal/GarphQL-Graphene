import datetime
from graphene import Schema, ObjectType, Date, Time
import json

class Query(ObjectType):
    one_week_from = Date(required=True, date_input=Date(required=True))

    def resolve_one_week_from(root, info, date_input):
        assert date_input == datetime.date(2006, 1, 2)
        return date_input + datetime.timedelta(weeks=1)

schema = Schema(query=Query)

results = schema.execute("""
    query {
        oneWeekFrom(dateInput: "2006-01-02")
    }
""")

assert results.data == {"oneWeekFrom": "2006-01-09"}
items = dict(results.data.items())
print(json.dumps(items,indent=4))



