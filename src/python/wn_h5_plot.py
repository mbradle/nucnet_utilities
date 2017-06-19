import matplotlib.pyplot as plt
import numpy as np

import wn_h5
import plot_params as plp

def plot_zone_property_vs_property(
       file, zone, prop1, prop2, **keyword_parameters
    ):

    result = wn_h5.get_zone_properties_in_groups( file, zone, [prop1, prop2] )

    if( 'xfactor' in keyword_parameters ):
       xfactor = keyword_parameters['xfactor']
    else:
       xfactor = 1

    if( 'yfactor' in keyword_parameters ):
       yfactor = keyword_parameters['yfactor']
    else:
       yfactor = 1

    x = np.array( map( float, result[prop1] ) ) / xfactor
    y = np.array( map( float, result[prop2] ) ) / yfactor

    plp.set_plot_params( plt, keyword_parameters )

    plt.plot( x, y )
    plt.show()

def plot_single_mass_fraction_vs_property(
      file, zone, prop, species, **keyword_parameters
    ):

    props = wn_h5.get_zone_properties_in_groups( file, zone, [prop] )
    m = wn_h5.get_zone_nuclide_mass_fractions_in_groups( file, zone, [species] )

    if( 'xfactor' in keyword_parameters ):
       xfactor = keyword_parameters['xfactor']
    else:
       xfactor = 1

    x = np.array( map( float, props[prop] ) ) / xfactor
    y = np.array( map( float, m[species] ) )

    plp.set_plot_params( plt, keyword_parameters )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           plt.ylabel(
             'X(' + wn_utilities.get_latex_names([species])[species] + ')'
           )

    plt.plot( x, y )
    plt.show()

def plot_group_mass_fractions_vs_property(
    file, group, prop, species, **keyword_parameters
):

   props = wn_h5.get_group_properties_in_zones( file, group, [prop] )
   m = wn_h5.get_group_mass_fractions( file, group )

   nuclide_data = wn_h5.get_nuclide_data_hash( file )

   if( 'xfactor' in keyword_parameters ):
      xfactor = keyword_parameters['xfactor']
   else:
      xfactor = 1

   x = np.array( map( float, props[prop] ) ) / xfactor

   plp.set_plot_params( plt, keyword_parameters )

   names = wn_utilities.get_latex_names(species)

   for sp in species:
     print x
     y = np.array( map( float, m[:, nuclide_data[sp]['index']] ) )
     print y
     plt.plot( x, y, label = names[sp] )

   legend = plt.legend( loc='upper center', shadow=True )

   plt.show()
