def post_parameter(model_classl):
    return {
        'name': 'mountain',
        'description': 'new mountain information',
        'required': True,
        'dataType': model_classl.__name__,
        'paramType': 'body'
    }
