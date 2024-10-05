import Juliustools
from Juliustools import JuliusToolsAPI

api = JuliusToolsAPI("rd00DIxVubA0vf63Zjs_0IPNr_Mqnd5_WOgvNntC1kY")
api.get_status()
print(api.get_status())
api.add_content("Hello, World!", "quote")