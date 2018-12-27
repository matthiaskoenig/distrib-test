"""
Reading information from distrib examples.
"""
import libsbml


def example1():
    """ Reading distrib information.

    :return:
    """
    doc = libsbml.readSBMLFromFile('examples/distrib_example1.xml')  # type: libsbml.Model
    print(doc)
    model = doc.getModel()  # type: libsbml.Model
    for f in model.getListOfFunctionDefinitions():  # type: libsbml.FunctionDefinition
        print(f)
        f_dist = f.getPlugin("distrib")  # type: libsbml.DistribFunctionDefinitionPlugin
        print(f_dist)

        draw = f_dist.getDistribDrawFromDistribution()  # type: libsbml.DistribDrawFromDistribution
        print(draw)

        # get the distribution
        distribution = draw.getDistribution()  # type: libsbml.DistribDistribution
        print(distribution)
        distribution_type = distribution.getTypeCode()
        assert distribution_type == libsbml.SBML_DISTRIB_NORMALDISTRIBUTION

        # what are the distribution specific parameters?




if __name__ == "__main__":
    example1()



