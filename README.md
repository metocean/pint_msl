# MSL Pint
This repository contains a the pint unit registry (https://pint.readthedocs.io)
with additional units defined.
Additional units can be added in a straightforward manner by editing the python file pint_msl/unit_registry.py

Installation (from):
 ```
pip3 install -r path_to_root_of_repo/requirements.txt
pip3 install -e path_to_root_of_repo

```

Loading the registry:

```
from pint_msl.unit_registry import MSLUnitRegistry

ureg = MSLUnitRegistry()
```
