from evennia import DefaultObject

class Note(DefaultObject):
    """
    Oyuncuların okuyabileceği bir not kâğıdı.
    """
    def at_object_creation(self):
        self.db.desc = "Eskimiş buruşuk bir resim defteri sayfası."
        self.db.text = (
            "Bütün eylemlerini yazarak belirtebilirsin.\n"
            "Bütün gördüklerini okuyarak görebilirsin.\n"
            "Bütün konuşmalarını yazarak yapabilirsin.\n"
            "Bütün duyduklarını okuyarak duyabilirsin."
        )

    def at_read(self, caller):
        """
        Not kâğıdı okunduğunda tetiklenir.
        """
        caller.msg(self.db.text)


class CustomChest(DefaultObject):
    """
    Özel bir sandık nesnesi.
    """
    def at_object_creation(self):
        self.db.desc = "Eski bir sandık, kilidi kırık durumda."
        self.db.items = [
            "1x eski bakır kılıç",
            "1x eski yırtık tshirt",
            "1x eski yırtık elbise",
            "2x küçük kırmızı can şişesi"
        ]

    def at_open(self, caller):
        """
        Sandık açıldığında tetiklenir.
        """
        caller.msg("Sandığın içinde şunları buldun: " + ", ".join(self.db.items))
        caller.db.inventory = self.db.items  # Oyuncunun envanterine ekle