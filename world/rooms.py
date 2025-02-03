from evennia import create_object
from typeclasses.rooms import WelcomeRoom

def build_welcome_room():
    """
    Karşılama odasını oluşturur.
    """
    welcome_room = create_object(WelcomeRoom, key="Welcome Room")
    welcome_room.db.desc = "Burası karşılama odası. Oyuncular burada başlar."
    print("Welcome Room başarıyla oluşturuldu!")