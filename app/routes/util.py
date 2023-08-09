from flask import abort, make_response

fields_dict = {
    "title": str,
    "description": str,
    "image": str
}

id_dict = {
    "emote_id":int
}


#validate id in any model
def validate_object(cls, object_id):
    try:
        object_id = int(object_id)
    except ValueError:
        error_message = {"error": f"Invalid {cls.__name__.lower()} ID: expected int, recieved '{object_id}' of type {type(object_id).__name__}"}
        abort(make_response(error_message, 400))

    obj = cls.query.get(object_id)

    if not obj:
        error_message = {"error": f"{cls.__name__.lower()} not found with ID: {object_id}"}
        abort(make_response(error_message, 404))

    return obj


# Validation field and type
def validate_fields(request_data, fields_dict):
    validation_errors = []

    for field, expected_type in fields_dict.items():
        value = request_data.get(field)
        
        if not value:
            validation_errors.append((field, f"Missing field"))
        else:
            if not isinstance(value, expected_type):
                validation_errors.append((field, f"Invalid type: expected {expected_type.__name__}, recieved '{value}' of type {type(value).__name__}"))
        
    if validation_errors:
        error_message = "Validation errors:"
        for error in validation_errors:
            error_message += f"\n- {error}"
        raise ValueError(validation_errors)