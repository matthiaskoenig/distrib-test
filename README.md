# Installation
To run distrib simulations we need a libsbml version supporting distrib
and a simulator which can handle the distrib information.


# install libsbml-experimental


    cd ../../test/distrib/

    cmake -DENABLE_DISTRIB=ON \
    -DENABLE_COMP=ON -DWITH_PYTHON=ON \
    -DPYTHON_USE_DYNAMIC_LOOKUP:BOOL=ON \
    -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python3.6 \
    -DPYTHON_EXECUTABLE=/usr/bin/python3.6  \
    -DLIBSBML_USE_LEGACY_MATH=ON \
    ../../svn/libsbml-experimental/

    make
    make binding_python_lib


# create virtualenv and copy libsbml into site-packages




# comments of distrib

f_dist.getDistribDrawFromDistribution()
should be
f_dist.getDrawFromDistribution();
same for
setDrawFromDistribution;

Rename:
DistribInput -> DistributionInput
makes it much clearer

How to get the actual type of the distribution?
Do I have to check against all the type codes?


## problems with examples

### example2
```
Error: Invalid SBML:
line 23: (10219 [Error]) The number of arguments used in a call to a function defined by a <functionDefinition> must equal the number of arguments accepted by that function, or in other words, the number of <bvar> elements inside the <lambda> element of the function definition.
Reference: L3V1 Section 4.3.4
 The formula 'distribution()' in the math element of the <initialAssignment> uses the function 'distribution' which requires a different number of arguments than the number supplied.
```


### example5
```
Warning: Global parameter, 'Z' missing value and missing init assignment and assignment rule!, defaulting value to 0.0.
Warning: This probably is NOT what you want with global parameter 'Z'.
RuntimeError: Global parameter 'Z' missing value and missing init assignment and assignment rule!
```

### example7
```
Warning: Global parameter, 'gender' missing value and missing init assignment and assignment rule!, defaulting value to 0.0.
Warning: This probably is NOT what you want with global parameter 'gender'.
RuntimeError: Global parameter 'gender' missing value and missing init assignment and assignment rule!
```