import sys
import matplotlib.pyplot as plt
import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append( dir_path + '/../../src/python' )

import wn_xml
import plot_params as plp
import wn_utilities

def plot_property_vs_property(
       file, prop1, prop2, **keyword_parameters
    ):

    result = wn_xml.get_properties_in_zones( file, [prop1, prop2] )

    x = np.array( map( float, result[prop1] ) )
    y = np.array( map( float, result[prop2] ) )

    plp.set_plot_params( plt, keyword_parameters )

    plt.plot( x, y )
    plt.show()

def plot_single_mass_fraction_vs_property(
      file, prop, species, **keyword_parameters
    ):

    props = wn_xml.get_properties_in_zones( file, [prop] )
    m = wn_xml.get_mass_fractions_in_zones( file, [species] )

    x = np.array( map( float, props[prop] ) )
    y = np.array( map( float, m[species] ) )

    plp.set_plot_params( plt, keyword_parameters )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           plt.ylabel(
             'X(' + wn_utilities.get_latex_names([species])[species] + ')'
           )

    plt.plot( x, y )
    plt.show()


