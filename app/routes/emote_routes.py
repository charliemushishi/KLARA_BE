from flask import Blueprint,request,jsonify,abort,make_response
from app import db
from app.models.emotes import Emote
from app.routes.util import validate_fields, fields_dict, validate_object
#from functools import wraps
# from app.auth import requires_auth, check_auth

emotes_bp = Blueprint("emotes", __name__, url_prefix="/emotes")

#all emotes
@emotes_bp.route("", methods=["GET"])
def get_all_emotes():
    #filter id
    #emote_id = request.args.get("emote_id")  
    emote_query = Emote.query
    
    #future filter
    #if emote_id:
    #    emote_query = emote_query.filter_by(emote_id=emote_id)

    emotes = emote_query.all()

    emote_response = [emote.to_dict() for emote in emotes]
    return jsonify(emote_response)


#one emote
@emotes_bp.route("/<emote_id>", methods=["GET"])
def get_one_emote(emote_id):
    emote = validate_object(Emote,emote_id)
    return jsonify({"emote":emote.to_dict()})
    

#upload emote
@emotes_bp.route("", methods=["POST"])
def create_emote():
    request_body = request.get_json()

    try:
        validate_fields(request_body, fields_dict)

        new_emote = Emote.from_dict(request_body)
        db.session.add(new_emote)
        db.session.commit()
        response_body = {"emote":new_emote.to_dict()}
        return jsonify(response_body),201

    except ValueError as validation_error:
        error_list = validation_error.args[0] 
        error_messages = {field: message for field, message in error_list}
        return abort(make_response({"error": error_messages}, 400)) 

    except Exception as error:
        print(error)
        return abort(make_response({"error":"NNNOOOOOOPE didnt create new emote"},500))


#remove emote
@emotes_bp.route("/<emote_id>", methods=["DELETE"])
#@requires_auth  # Apply authentication to this route
def remove_one_emote(emote_id):
    #auth = request.authorization  # Access the authentication credentials
    
    #if auth and check_auth(auth.username, auth.password):
    emote = validate_object(Emote,emote_id)
    db.session.delete(emote)
    db.session.commit()
    return jsonify({"details":f"Emote {emote_id} successfully deleted"}), 200
    # else:
    #     return jsonify({"error": "Incorrect password"}), 401


#state for VIEWPORT
current_emote = {
    "title":"",
    "image":"",
    "description":""
    }

@emotes_bp.route("/currentemote", methods=["POST"])
def save_current_emote():
    request_body = request.get_json()

    try:
        global current_emote
        current_emote = {
            "title": request_body.get("title", ""),
            "image": request_body.get("image", ""),
            "description": request_body.get("description", "")
        }

        response_data = {
            "details": "Current emote saved successfully",
            "emote": current_emote
        }
        return jsonify(response_data), 200

    except Exception as error:
        print(error)
        return abort(make_response({"error": "Failed to save current emote"}, 500))


# @emotes_bp.route("/currentemote", methods=["POST"])
# def save_current_emote():
#     request_body = request.get_json()
#     global current_emote
#     current_emote = {
#         "title": request_body.get("title", ""),
#         "image": request_body.get("image", ""),
#         "description": request_body.get("description", "")
#     }
    
#     return jsonify({"details": f"Current emote saved succesfully, {current_emote}"}),200


@emotes_bp.route("/currentemote", methods=["GET"])
def get_current_emote():
    return jsonify({"emote": current_emote}), 200
#end of viewport state


#update emote
@emotes_bp.route("/<emote_id>/<field>", methods=["PUT"])
def update_emote(emote_id, field):

    emote = validate_object(Emote,emote_id)
    # field = request.path.split("/")[-1]
    request_body = request.get_json()

    field_actions = {
        "title":Emote.title,
        "description":Emote.description,
        "image":Emote.image
    }

    if field in field_actions:
        expected_type = fields_dict.get(field)  
        field_value = request_body.get(field)  
        # Validate the field_info dictionary
    try:
        validate_fields({field: field_value}, {field: expected_type})


        setattr(emote, field, field_value)
        db.session.commit()
        response_body = {"Emote":emote.to_dict()}
        return jsonify(response_body),201
    except ValueError as validation_error:
        error_list = validation_error.args[0] 
        error_messages = {field: message for field, message in error_list}
        return abort(make_response({"error": error_messages}, 400)) 

    except Exception as e:
        return abort(make_response({"error":"NNNOOOOOOPE didnt UPDATE the emote"},500)) 

    


    

