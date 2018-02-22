import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import wn_h5
import plot_params as plp
import wn_utilities

def plot_zone_property_vs_property(
       file, zone, prop1, prop2, **keyword_parameters
    ):

    result = wn_h5.get_zone_properties_in_groups( file, zone, [prop1, prop2] )

    if( 'xfactor' in keyword_parameters ):
       xfactor = keyword_parameters['xfactor']
    else:
       xfactor = 1

    x = np.array( map( float, result[prop1] ) ) / xfactor
    y = np.array( map( float, result[prop2] ) )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.plot( x, y )
    plt.show()

def plot_group_mass_fractions(
    file, group, species, **keyword_parameters
):

    plp.set_plot_params( mpl, keyword_parameters )

    fig = plt.figure()

    y = []
    l = []
    latex_names = []

    m = wn_h5.get_group_mass_fractions( file, group )

    nuclide_data = wn_h5.get_nuclide_data_hash( file )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           laxtex_names = wn_utilities.get_latex_names(species)

    iy = 0
    for sp in species:
      y = np.array( map( float, m[:, nuclide_data[sp]['index']] ) )
      if( len( latex_names ) != 0 ):
        lab = latex_names[sp]
      else:
        lab = sp
      l.append( plt.plot( y, label = lab ) )

    if( len( species ) != 1 ):
      plt.legend(loc='upper right', prop={'size':14})

    if( 'ylabel' not in keyword_parameters ):
      if( len( species ) != 1 ):
         plt.ylabel( 'Mass Fraction' )
      else:
         if( len( latex_names ) == 0 ):
            plt.ylabel( 'X(' + species[0] + ')' )      
         else:
            plt.ylabel( 'X(' + latex_names[species[0]] + ')' )      

    plp.apply_class_methods( plt, keyword_parameters )

    plt.show()

def plot_group_mass_fractions_vs_property(
    file, group, prop, species, **keyword_parameters
):

    plp.set_plot_params( mpl, keyword_parameters )

    fig = plt.figure()

    x = []
    y = []
    l = []
    latex_names = []

    props = wn_h5.get_group_properties_in_zones( file, group, [prop] )
    m = wn_h5.get_group_mass_fractions( file, group )

    nuclide_data = wn_h5.get_nuclide_data_hash( file )

    if( 'xfactor' in keyword_parameters ):
       xfactor = keyword_parameters['xfactor']
    else:
       xfactor = 1

    x = np.array( map( float, props[prop] ) ) / xfactor

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           laxtex_names = wn_utilities.get_latex_names(species)

    iy = 0
    for sp in species:
      y = np.array( map( float, m[:, nuclide_data[sp]['index']] ) )
      if( len( latex_names ) != 0 ):
        lab = latex_names[sp]
      else:
        lab = sp
      l.append( plt.plot( x, y, label = lab ) )

    if( len( species ) != 1 ):
      plt.legend(loc='upper right', prop={'size':14})

    if( 'ylabel' not in keyword_parameters ):
      if( len( species ) != 1 ):
         plt.ylabel( 'Mass Fraction' )
      else:
         if( len( latex_names ) == 0 ):
            plt.ylabel( 'X(' + species[0] + ')' )      
         else:
            plt.ylabel( 'X(' + latex_names[species[0]] + ')' )      

    if( 'xlabel' not in keyword_parameters ):
       plt.xlabel( prop )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.show()

def plot_zone_mass_fractions_vs_property(
      file, zone, prop, species, **keyword_parameters
    ):

    plp.set_plot_params( mpl, keyword_parameters )

    fig = plt.figure()

    x = []
    y = []
    l = []
    latex_names = []

    props = wn_h5.get_zone_properties_in_groups( file, zone, [prop] )
    m = wn_h5.get_zone_nuclide_mass_fractions_in_groups( file, zone, species )
 

    if( 'xfactor' in keyword_parameters ):
       xfactor = keyword_parameters['xfactor']
    else:
       xfactor = 1

    x = np.array( map( float, props[prop] ) ) / xfactor

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
         latex_names = wn_utilities.get_latex_names(species)

    for i in range( len( species ) ):
      y = np.array( list( map( float, m[species[i]] ) ) )
      if( len( latex_names ) != 0 ):
        lab = latex_names[species[i]]
      else:
        lab = species[i]
      l.append( plt.plot( x, y, label = lab ) )

    if( len( species ) != 1 ):
      plt.legend(loc='upper left', prop={'size':14})

    if( 'ylabel' not in keyword_parameters ):
      if( len( species ) != 1 ):
         plt.ylabel( 'Mass Fraction' )
      else:
         if( len( latex_names ) == 0 ):
            plt.ylabel( 'X(' + species[0] + ')' )      
         else:
            plt.ylabel( 'X(' + latex_names[species[0]] + ')' )      

    if( 'xlabel' not in keyword_parameters ):
       plt.xlabel( prop )
 
    plp.apply_class_methods( plt, keyword_parameters )

    plt.show()

