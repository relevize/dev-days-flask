from flask import Blueprint

from ..models.Log import Log
from ..models.CrewMember import CrewMember
from ..extensions import db

bp = Blueprint('seed', __name__, url_prefix="/seed")

@bp.route("/", methods=["GET"])
def seed_database():
    """
    DELETE EXISTING DATA
    """
    Log.query.delete()
    CrewMember.query.delete()


    """
    PLANT NEW DATA
    """
    def create_crew_member(name, rank):
        new_crew_member = CrewMember(name=name, rank=rank)
        db.session.add(new_crew_member)

    create_crew_member("Tsuki", "captain")
    create_crew_member("Bradward Boimler", "ensign")
    create_crew_member("Data", "lieutenant_commander")

    def create_log(log_entry, crew_member_id, redacted=False):
        new_log = Log(log_entry=log_entry, crew_member_id=crew_member_id, redacted=redacted)
        db.session.add(new_log)

    create_log("the stars are in the sky, why can i not swat?", 1)
    create_log("Mewwoooowwwww", 1, True)
    create_log("If this was actually happening, they'd send the Enterprise. But, you know. Artistic license.", 2)
    create_log("Ahhh!!!!", 2, True)
    create_log("It is a beard Geordi, a fine, full, dignified beard.", 3)
    create_log("I am an android.", 3)


    db.session.commit()

    return "SEEDED", 200
