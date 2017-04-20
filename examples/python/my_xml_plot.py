import sys
import matplotlib.pyplot as plt
import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append( dir_path + '/../../src/python' )

from lxml import etree
import wn_xml
import plot_params as plp
import wn_utilities

def plot_property_vs_property(
       file, prop1, prop2, **keyword_parameters
    ):

    root = etree.parse( file ).getroot()

    result = wn_xml.get_properties_in_zones( root, [prop1, prop2] )

    x = np.array( map( float, result[prop1] ) )
    y = np.array( map( float, result[prop2] ) )

    plp.set_plot_params( plt, keyword_parameters )

    plt.plot( x, y )
    plt.show()

def plot_single_mass_fraction_vs_property(
      file, prop, species, **keyword_parameters
    ):

    root = etree.parse( file ).getroot()

    props = wn_xml.get_properties_in_zones( root, [prop] )
    m = wn_xml.get_mass_fractions_in_zones( root, species )

    x = np.array( map( float, props[prop] ) )

    if( 'xfactor' in keyword_parameters ):
      x /= float( keyword_parameters['xfactor'] )

    plp.set_plot_params( plt, keyword_parameters )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           plt.ylabel(
             'X(' + wn_utilities.get_latex_names([species])[species] + ')'
           )

    for my_species in species:
      y = np.array( map( float, m[my_species] ) )
      plt.plot( x, y )

    plt.show()

