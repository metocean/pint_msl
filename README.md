# Pint extra definitions
This repository contains a files with the extra units definition need to run the pint unit parser (https://pint.readthedocs.io) on our system.
The definitions can be loaded in a piece of python code the following way:

```
import pint.UnitRegistery

ureg = UnitRegistery
ureg.load_defintitions('/path/pint_extra_definitions.txt')
```
