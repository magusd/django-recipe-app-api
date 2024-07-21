# https://pypi.org/project/warlock/
# https://aisaastemplate.com/tools/django-model-generator/
import json
from jinja2 import Template

schema = None
with open("fhir.schema.json", "r") as f:
    schema = json.loads(f.read())

file_template = """
from django.db import models

{{models}}

"""



# https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types

# Field

# AutoField
# BigAutoField
# BigIntegerField
# BinaryField
# BooleanField
# CharField
# DateField
# DateTimeField
# DecimalField
# DurationField
# EmailField
# FileField
# FilePathField
# FloatField
# GeneratedField
# GenericIPAddressField
# ImageField
# IntegerField
# JSONField
# PositiveBigIntegerField
# PositiveIntegerField
# PositiveSmallIntegerField
# SlugField
# SmallAutoField
# SmallIntegerField
# TextField
# TimeField
# URLField
# UUIDField

# Relationship

# ForeignKey
# ManyToManyField
# OneToOneField

template = """
class {{class_name}}(models.Model):
    \"\"\"autogenarated fhir model\"\"\"
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
"""

print(schema.keys())
print(schema["definitions"].keys())

print(schema["definitions"]["id"])

types = ['no type', 'string', 'boolean', 'number', 'object']

models = []
for entity, entity_schema in schema["definitions"].items():
    # print("----------")
    if "type" not in entity_schema:
        #no type, auxiliary/collection
        continue

    if entity_schema["type"] != "object":
        print('not object', entity_schema["type"], entity)
        continue

    # print(entity_schema["type"], entity)


    # if entity in skip:
    #     continue

    # print(entity, json.dumps(entity_schema))
    # data = {
    #     "class_name": entity,
    #     "descritpion": entity_schema["description"],
    # }

    # j2_template = Template(template)
    # print(j2_template.render(data))




print(types)



