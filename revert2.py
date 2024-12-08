import random
from .. import loader, utils

def yomayao(message):
    return message[::-1]
     
@loader.tds
class RevertMod(loader.Module):
    """Revert"""

    strings = {"name": "Revert"}
    
    async def revertcmd(self, message):
        """перевернуть строку наоборот"""  
        revert001 = yomayao(message.text.split(" ", maxsplit=1)[-1])
        await utils.answer(message, revert001)