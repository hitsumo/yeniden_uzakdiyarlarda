from evennia import DefaultCharacter
from commands.command import CmdOpenChest, CmdTalk  # Özel komutları içe aktarıyoruz

class Character(DefaultCharacter):
    """
    Oyuncu karakteri için temel sınıf.
    Bu sınıf, oyuncuların varsayılan davranışlarını ve komut setlerini tanımlar.
    """

    def at_object_creation(self):
        """
        Oyuncu karakteri oluşturulduğunda tetiklenir.
        Burada oyuncuya özel komutlar eklenir.
        """
        # Özel komutları oyuncunun komut setine ekliyoruz
        self.cmdset.add(CmdOpenChest)
        self.cmdset.add(CmdTalk)

        # Oyuncunun başlangıç özelliklerini tanımlayabilirsiniz
        self.db.gold = 0  # Oyuncunun başlangıç altını
        self.db.inventory = []  # Oyuncunun başlangıç envanteri

    def at_after_move(self, source_location):
        """
        Oyuncu bir yerden başka bir yere hareket ettiğinde tetiklenir.
        """
        self.msg(f"Yeni bir yere geldin: {self.location.key}")
        if self.location.db.desc:
            self.msg(self.location.db.desc)

    def at_say(self, message, **kwargs):
        """
        Oyuncu bir şey söylediğinde tetiklenir.
        """
        self.msg(f"Sen söyledin: {message}")