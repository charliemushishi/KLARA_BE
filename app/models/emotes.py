from app import db 

class Emote(db.Model):
    emote_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    #fav connect
    favorites = db.relationship('Favorites', backref='emote', lazy=True)

#format method in
    def to_dict(self):
        emote_as_dict = {}
        emote_as_dict["id"] = self.emote_id
        emote_as_dict["title"] = self.title
        emote_as_dict["description"] = self.description
        emote_as_dict["image"] = self.image
        return emote_as_dict

#new object out
    @classmethod
    def from_dict(cls, emote_data):
        new_emote = Emote(title=emote_data["title"],
                        description=emote_data["description"],
                        image=emote_data["image"])
        return new_emote

#favorites table 1 to many
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emote_id = db.Column(db.Integer, db.ForeignKey('emote.emote_id'), nullable=False)

    