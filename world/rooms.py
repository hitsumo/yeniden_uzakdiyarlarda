from evennia import create_object
from typeclasses.custom_rooms import WelcomeRoom, TrainingRoom
from typeclasses.custom_objects import Note, CustomChest
from typeclasses.custom_characters import Mahmud

def build_game():
    # Karşılama Odası
    welcome_room = create_object(WelcomeRoom, key="Karşılama Odası")
    welcome_room.db.desc = "Bir geçitten yere düşerek dışarı çıktın. Geçit gümbürtüyle kapandı."

    # Not Kâğıdını ekle
    note = create_object(Note, key="Not Kâğıdı", location=welcome_room)

    # Eğitim Odası
    training_room = create_object(TrainingRoom, key="Eğitim Odası")
    training_room.db.desc = "Oda neredeyse diğer odayla aynı. Bir kişi ve bir sandık dışında farklı bir şey yok."

    # Mahmud'u ekle
    mahmud = create_object(Mahmud, key="Mahmud", location=training_room)

    # Sandığı ekle
    chest = create_object(CustomChest, key="Sandık", location=training_room)

    # Odaları bağla
    welcome_room.db.exits = {"doğu": training_room}
    training_room.db.exits = {"batı": welcome_room}