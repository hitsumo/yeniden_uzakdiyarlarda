from evennia import DefaultRoom
from evennia.utils import delay

class OpeningRoom(DefaultRoom):
    """
    Oyunun açılış odası.
    """
    def at_object_receive(self, obj, source_location):
        """
        Oyuncu odaya girdiğinde tetiklenir.
        """
        if obj.has_account:  # Oyuncuysa
            self.msg_contents("|cMerhaba!|n Yeniden Uzak Diyarlarda oyununa hoş geldiniz.")
            delay(2, self.msg_contents, "Bu oyun yazı tabanlı olup Evennia sistemi kullanılarak oluşturulmuştur.")
            delay(4, self.msg_contents, "|gHazırım|n yazarak oyuna başlayabilirsin.")


class WelcomeRoom(DefaultRoom):
    """
    Oyuncunun oyuna başladığı karşılama odası.
    """
    def at_object_receive(self, obj, source_location):
        """
        Oyuncu odaya girdiğinde tetiklenir.
        """
        if obj.has_account:  # Oyuncuysa
            self.msg_contents("Bir geçitten yere düşerek dışarı çıktın. Geçit gümbürtüyle kapandı.")
            delay(2, self.msg_contents, "Etrafına bakınıyorsun. Sonra bir ses duydun:")
            delay(3, self.msg_contents, '"Merhaba Oyuncu! Artık buradasın."')
            delay(8, self.msg_contents, "Bu odada yapabileceğin temel eylemler ile ilgili bilgi alacağın bir eşya var. "
                                         "Bu eşya tahta masanın üzerindeki not kâğıdı.")
            delay(10, self.msg_contents, "Şu iki ipucunu veriyorum sana: 'Bak' ve 'Oku.'")
            delay(12, self.msg_contents, "Ardından gürültülü bir kahkaha duyuyorsun.")


class TrainingRoom(DefaultRoom):
    """
    Eğitim odası.
    """
    def at_object_receive(self, obj, source_location):
        if obj.has_account:  # Oyuncuysa
            self.msg_contents("Mahmud: Merhaba! Görüyorum ki Karşılama Salonundan geldin. "
                              "Ben Mahmud. Sana temel eğitim vereceğim.")