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

    mpl.rc('font', family='serif', serif='cm10')

    mpl.rc('text', usetex=True)
    mpl.rc('font', family='serif')

    if( 'legend_labels' in keyword_parameters ):
       if( len( keyword_parameters['legend_labels'] ) != len( files ) ):
          print "Invalid legend labels for input files."
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
      x = np.array( map( float, props[prop] ) )
      if( 'xfactor' in keyword_parameters ):
         x /= float( keyword_parameters['xfactor'] )
      m = wn_xml.get_mass_fractions_in_zones( roots[i], [species] )
      y = np.array( map( float, m[species] ) )
      if( 'legend_labels' in keyword_parameters ):
         ll, = plt.plot( x, y, label = keyword_parameters['legend_labels'][i] )
      else:
         ll, = plt.plot( x, y )
      l.append( ll )

    if( 'legend_labels' in keyword_parameters ):
       plt.legend(loc='upper right', prop={'size':14})

    plp.set_plot_params( plt, keyword_parameters )

    if( 'use_latex_names' in keyword_parameters ):
       if( keyword_parameters['use_latex_names'] == 'yes' ):
           plt.ylabel(
             'X(' + wn_utilities.get_latex_names([species])[species] + ')'
           )

    plt.show()

