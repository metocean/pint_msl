from pint import UnitRegistry

class MSLUnitRegistry(UnitRegistry):
    def __init__(self):
        super(MSLUnitRegistry, self).__init__()
        self.define('percent = 0.01 * count = pct')
        self.define('perthousand = 0.001 * count = ptshd')
        self.define('utc = count')
        seff.define('okta = 0.125 * count')