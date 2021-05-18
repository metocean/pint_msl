# MSL Pint
This package provides a [Pint](https://pint.readthedocs.io/) unit registry 
with a few additional units defined that we regularly use at MetOcean Solutions.
Units can be added in a straightforward manner by adding define() calls to [./pint_msl/unit_registry.py](./pint_msl/unit_registry.py).

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
