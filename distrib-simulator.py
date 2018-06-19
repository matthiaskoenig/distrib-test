"""
Simulating a distrib model with libroadrunner.

Sampling from the distribution.
"""
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
        self.parse_distrib()


    def from_path(self, path):
        """ Initiate from given path.

        :param path:
        :return:
        """
        doc = libsbml.readSBMLFromFile(path)  # type: libsbml.SBMLDocument
        rr = roadrunner.RoadRunner(path)
        return DistribSimulator(doc, rr)


    def parse_distrib(self):
        """ Parses the distrib information on the model.

        The information will be used for sampling.
        """
        print(doc)
        model = doc.getModel()  # type: libsbml.Model

        # parse the distributions
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
        rr = roadrunner.RoadRunner("mymodel.xml")
        results = []


        # simulate
        s = rr.simulate(start=start, end=end, points=points, steps=steps)
        df = pd.DataFrame()



        rr.plot()



def example1():
    path = './examples/distrib_example1.xml'
    simulator = DistribSimulator.from_path(path)
    results =



if __name__ == "__main__":
    example1()

