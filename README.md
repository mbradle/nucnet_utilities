# nucnet_utilities

This is a set of plotting utilities for output from NucNet Tools.  To use,
clone the repository .  Then set the PYTHONPATH environment variable.  If
you cloned the repository to /home/xxx/nucnet_utilities, where xxx = your user name, type

     export PYTHONPATH=/home/xxx/nucnet_utilities/src/python

Then, in a directory with an output xml file called my_output.xml
from NucNet Tools, open python and type, for example:

     >>>import wn_xml_plot as wp

     >>>wp.plot_mass_fractions_vs_property( 'my_output.xml', 'time', ['h1','he4'] )

You can include keywords:

    xscale='linear' or 'log'
    yscale='linear' or 'log'
    xlim=[a,b] where a and b are the range of the x axis
    ylim=[a,b] where a and b are the range of the y axis
    xlabel='some text' which is the label of the x axis
    ylabel='some text' which is the label of the y axis
    
Thus, for example, you can type

    >>>import wn_xml_plot as wp
    >>>wp.plot_mass_fractions_vs_property( 'my_output.xml', 'time', ['h1','he4'], xscale = 'log', xlim = [1.e-3,10], xlabel = 'time (s)', ylabel = 'Mass Fraction' )
    
 Another plotting function plots a property versus a property.  Thus, one could type
 
     >>>wp.plot_property_vs_property( 'my_output.xml', 'time', 't9', xscale = 'log', xlim = [1.e-3,10], xlabel = 'time (s)', ylabel = '$T_9$' )
