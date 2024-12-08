import random
from .. import loader, utils

def yomayao(message):
    return message[::-1]
     
@loader.tds
class RevertMod(loader.Module):
    """Йомайо"""

    strings = {"name": "Revert"}
    
    async def revertcmd(self, message):
        """йомайо"""  
        revert001 = yomayao(message.split(" ", maxsplit=1)[-1])
        await utils.answer(message, revert001)