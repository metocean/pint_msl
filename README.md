# MSL Pint
This repository contains a the pint unit registery (https://pint.readthedocs.io)
with additional units defined.
Additionnal units can be added in a straightforward manner by editing the python file pint_msl/unit_registery.py

Installation (from):
 ```
pip3 install -r path_to_root_of_repo/requirements.txt
pip3 install -e path_to_root_of_repo

```

Loading the registry:

```
from pint_msl.unit_registery import MSLUnitRegistery

ureg = MSLUnitRegistery()
```
