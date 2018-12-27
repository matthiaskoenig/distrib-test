"""
Simulating a distrib model with libroadrunner.

Sampling from the distribution.
Draw from distribution happens in either InitialAssignment or EventAssignments.
This is a function definition.
"""
import warnings
import libsbml
import roadrunner
import pandas as pd
import numpy as np


class DistribSimulator(object):
    """ Simulator for distrib models. """

    def __init__(self, doc, rr):
        """

        :param doc: SBMLDocument
        :param rr: roadrunner model for SBMLDocument
        """
        self.doc = doc  # type: libsbml.SBMLDocument
        self.rr = rr
        self._parse_distrib()

    @staticmethod
    def from_path(path):
        """ Initiate from given path.

        :param path:
        :return:
        """
        print("# Loading SBML document")
        doc = libsbml.readSBMLFromFile(path)  # type: libsbml.SBMLDocument

        # strip distrib and load in roadrunner
        doc_rr = doc.clone()
        print("# Loading RoadRunner model")
        config = libsbml.ConversionProperties()
        if config != None:
            config.addOption('stripPackage')
            config.addOption('package', 'distrib')
            status = doc_rr.convert(config)
            if status != libsbml.LIBSBML_OPERATION_SUCCESS:
                # Handle error somehow.
                print('Error: unable to strip the Distrib package.')
                print('LibSBML returned error: ' + libsbml.OperationReturnValue_toString(status).strip())

        sbml_str = libsbml.writeSBMLToString(doc_rr)
        rr = roadrunner.RoadRunner(sbml_str)

        return DistribSimulator(doc, rr)

    def sample(self, draw, size):
        """ Sample from given distribution.

        :param draw:
        :return:
        """
        # Necessary to map the parameters of libsbml distrib to the numpy parameters for random sampling


        type_code = None

        # -------------------------------
        # ContinousUnivariateDistribution
        # -------------------------------
        if type_code == libsbml.SBML_DISTRIB_NORMALDISTRIBUTION:
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal
            loc = None
            scale = None
            size = None
            data = np.random.normal(loc, scale, size)

        elif type_code == libsbml.SBML_DISTRIB_UNIFORMDISTRIBUTION:
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html#numpy.random.uniform


            low = None
            high = None
            data = np.random.uniform(low, high)

        elif type_code == libsbml.SBML_DISTRIB_LOGNORMALDISTRIBUTION:
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.lognormal.html#numpy.random.lognormal
            mean = None
            sigma = None
            size = None
            data = np.random.lognormal(mean, sigma, size)

        else:
            warnings.warn("Distribution is not supported: " + type_code + " (" + type(draw) + ")")
        # compare the


    def _parse_distrib(self):
        """ Parses the distrib information on the model.

        The information will be used for sampling.
        """
        print("# parse_distrib")
        print(self.doc)
        model = self.doc.getModel()  # type: libsbml.Model

        # ---------------------------
        # parse drawFromDistribution
        # ---------------------------
        print("\n# parse draw")
        for f in model.getListOfFunctionDefinitions():  # type: libsbml.FunctionDefinition
            f_dist = f.getPlugin("distrib")  # type: libsbml.DistribFunctionDefinitionPlugin
            if f_dist and f_dist.isSetDistribDrawFromDistribution():

                print(f_dist)

                draw = f_dist.getDistribDrawFromDistribution()  # type: libsbml.DistribDrawFromDistribution
                print(draw)

                # get the distribution
                distribution = draw.getDistribution()  # type: libsbml.DistribDistribution
                print(distribution)

                # distribution types
                distribution_type = distribution.getTypeCode()
                assert distribution_type == libsbml.SBML_DISTRIB_NORMALDISTRIBUTION
                print(distribution_type)

                # get the inputs
                for distrib_input in draw.getListOfDistribInputs():
                    id = distrib_input.getId()
                    index = distrib_input.getIndex()
                    print(id, index)

        # ------------------------
        # parse uncertainty
        # ------------------------
        print("\n# parse uncertainty")
        for element in model.getListOfAllElements():
            el_dist = model.getPlugin("distrib")  # type: libsbml.DistribSBasePlugin
            if (el_dist is not None) and (el_dist.isSetDistribUncertainty()):
                print("Element with uncertainty: " + el_dist)






        # model.removeFunctionDefinition()


    def simulate(self, start, end, points=None, steps=None, repeats=1):
        """ Run a distrib simulation.

        Using the distrib information to sample.

        :param start:
        :param end:
        :param points:
        :param steps:
        :param repeats:
        :return: list of results (list of pandas DataFrames)
        """

        # load an SBML model

        results = []
        for k in range(repeats):
            # TODO: sample from draws

            # No events with draws defined.

            # TODO: set the parameters and initial conditions from given values.


            # simulate
            s = self.rr.simulate(start=start, end=end, points=points, steps=steps)  # roadrunner.Nam
            df = pd.DataFrame(s, columns=s.colnames)

            results.append(df)

        return results



def example1():
    path = './examples/distrib_example1.xml'
    simulator = DistribSimulator.from_path(path)
    results = simulator.simulate(start=0, end=10, steps=10)
    print(results)


def examples():
    """ Run all examples. """
    for k in range(1, 9):
        path = './examples/distrib_example{}.xml'.format(k)
        print("-"*80)
        print(path)
        print("-" * 80)

        # if k in [2, 5, 7]:
        #    continue


        simulator = DistribSimulator.from_path(path)
        results = simulator.simulate(start=0, end=10, steps=10)
        print(results)





if __name__ == "__main__":
    # example1()
    examples()
