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
