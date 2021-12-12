# uri para conectar python con nuestro cluster de mongo atlas
PYDEVOPS_URI = 'mongodb+srv://jns:dev23@sandbox.em4zt.mongodb.net/pydevops?retryWrites=true&w=majority'

PYDEVOPS_KEYS = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price',
                 'amenities']
PYDEVOPS_VALUE_TYPES = [str, str, str, int, str, str, str, int, int, list]
