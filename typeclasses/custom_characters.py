from evennia import DefaultCharacter

class Mahmud(DefaultCharacter):
    """
    Eğitim veren bir NPC.
    """
    def at_object_creation(self):
        self.db.desc = "Yaşlı bir adam, sana eğitim vermek için burada."
        self.db.quest = "5 kurtçuk öldür."
        self.db.quest_complete = False

    def talk(self, caller):
        """
        Mahmud ile konuşma.
        """
        if not caller.db.took_items:
            caller.msg("Mahmud: Sandıktaki eşyaları al ve tekrar yanıma gel.")
        elif not self.db.quest_complete:
            caller.msg("Mahmud: İlk görevin, dışarıdaki 5 kurtçuğu öldürmek. Kabul ediyor musun?")
            caller.msg("Mahmud: Eğer kabul ediyorsan 'Evet' yaz.")
        else:
            caller.msg("Mahmud: Görevi tamamladın! İşte ödülün: 10 altın sikke.")
            caller.db.gold += 10  # Oyuncuya altın ekle