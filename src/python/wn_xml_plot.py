import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from lxml import etree
import wn_xml
import plot_params as plp
import wn_utilities

def plot_single_mass_fraction_vs_property_in_files(
      files, prop, species, **keyword_parameters
    ):

    plp.set_plot_params( plt, keyword_parameters )

    if( 'legend_labels' in keyword_parameters ):
       if( len( keyword_parameters['legend_labels'] ) != len( files ) ):
          print( "Invalid legend labels for input files." )
          exit( 1 );

    fig = plt.figure()

    roots = []
    x = []
    y = []
    l = []

    for file in files:
      roots.append( etree.parse( file ).getroot() )

    for i in range( len( roots ) ):
      props = wn_xml.get_properties_in_zones( roots[i], [prop] )
      x = np.array( list( map( float, props[prop] ) ) )
      if( 'xfactor' in keyword_parameters ):
         x /= float( keyword_parameters['xfactor'] )
      m = wn_xml.get_mass_fractions_in_zones( roots[i], [species] )
      y = np.array( list( map( float, m[species] ) ) )
      if( 'legend_labels' in keyword_parameters ):
         ll, = plt.plot( x, y, label = keyword_parameters['legend_labels'][i] )
      else:
         ll, = plt.plot( x, y )
      l.append( ll )

    plp.apply_class_methods( plt, keyword_parameters )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           plt.ylabel(
             'X(' + wn_utilities.get_latex_names([species])[species] + ')'
           )

    plt.show()

def plot_mass_fractions(
      file, species, **keyword_parameters
    ):

    plp.set_plot_params( mpl, keyword_parameters )

    fig = plt.figure()

    y = []
    l = []
    latex_names = []

    root = etree.parse( file ).getroot()

    m = wn_xml.get_mass_fractions_in_zones( root, species )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
         latex_names = wn_utilities.get_latex_names(species)

    for i in range( len( species ) ):
      y = np.array( list( map( float, m[species[i]] ) ) )
      if( len( latex_names ) != 0 ):
        lab = latex_names[species[i]]
      else:
        lab = species[i]
      l.append( plt.plot( y, label = lab ) )

#    if( len( species ) != 1 ):
#      plt.legend(loc='upper right', prop={'size':14})

    if( 'ylabel' not in keyword_parameters ):
      if( len( species ) != 1 ):
        plt.ylabel( 'Mass Fraction' )
      else:
        if( len( latex_names ) == 0 ):
          plt.ylabel( 'X(' + species[0] + ')' )      
        else:
          plt.ylabel( 'X(' + latex_names[species[0]] + ')' )      

    if( 'xlabel' not in keyword_parameters ):
      plt.xlabel( 'step' )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.show()

def plot_mass_fractions_vs_property(
      file, prop, species, **keyword_parameters
    ):

    plp.set_plot_params( mpl, keyword_parameters )

    fig = plt.figure()

    x = []
    y = []
    l = []
    latex_names = []

    root = etree.parse( file ).getroot()

    props = wn_xml.get_properties_in_zones( root, [prop] )

    x = np.array( list( map( float, props[prop] ) ) )
    if( 'xfactor' in keyword_parameters ):
       x /= float( keyword_parameters['xfactor'] )

    m = wn_xml.get_mass_fractions_in_zones( root, species )

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

def plot_property(
       file, prop, **keyword_parameters
    ):

    root = etree.parse( file ).getroot()

    result = wn_xml.get_properties_in_zones( root, [prop] )

    x = np.array( map( float, result[prop] ) )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.plot( x )
    plt.show()

def plot_property_vs_property(
       file, prop1, prop2, **keyword_parameters
    ):

    root = etree.parse( file ).getroot()

    result = wn_xml.get_properties_in_zones( root, [prop1, prop2] )

    x = np.array( map( float, result[prop1] ) )
    y = np.array( map( float, result[prop2] ) )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.plot( x, y )
    plt.show()

def plot_zone_abundances_vs_nucleon_number(
       file, zone_xpath, nucleon, **keyword_parameters
    ):

    root = etree.parse( file ).getroot()

    zones = wn_xml.get_zones( root, zone_xpath )

    y = wn_xml.get_zone_abundances_vs_nucleon_number( zones[0], nucleon )

    plp.apply_class_methods( plt, keyword_parameters )

    plt.plot( y )
    plt.show()

