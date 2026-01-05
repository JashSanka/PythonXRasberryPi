from electric import Electric
from petrol import Petrol

class Hybrid(Petrol,Electric):

    pass

nissan = Hybrid()
nissan.can_charge
nissan.engine_size

