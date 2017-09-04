from pint import UnitRegistry

class MSLUnitRegistery(UnitRegistry):
    def __init__(self):
        super().__init__()
        self.define('percent = 0.01 * count = pct')
        self.define('perthousand = 0.001 * count = ptshd')
        self.define('utc = count')
