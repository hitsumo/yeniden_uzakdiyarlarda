from evennia import Command

class CmdOpenChest(Command):
    """
    Sandığı açmak için bir komut.
    Kullanım:
        open chest
    """
    key = "open chest"

    def func(self):
        chest = self.caller.search("Sandık")
        if not chest:
            self.caller.msg("Burada açılacak bir sandık yok.")
            return
        chest.at_open(self.caller)


class CmdTalk(Command):
    """
    Mahmud ile konuşmak için bir komut.
    Kullanım:
        talk mahmud
    """
    key = "talk mahmud"

    def func(self):
        mahmud = self.caller.search("Mahmud")
        if not mahmud:
            self.caller.msg("Burada konuşacak kimse yok.")
            return
        mahmud.talk(self.caller)