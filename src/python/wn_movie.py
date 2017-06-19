import matplotlib as mpl
mpl.use("Agg")
import wn_utilities as wu
import wn_h5
import numpy as np
import matplotlib.pyplot as plt
import plot_params as plp

def movie_mass_fractions_vs_property(
    file, movie_name, prop, species, **keyword_parameters
):

  import matplotlib.animation as manimation

  FFMpegWriter = manimation.writers['ffmpeg']
  metadata = dict(title='Movie Test', artist='Matplotlib',
                  comment='Movie support!')

  if( 'fps' in keyword_parameters ):
     fps = keyword_parameters['fps']
  else:
     fps = 15

  writer = FFMpegWriter( fps=fps, metadata=metadata )

  ts_factor = {'yr': 3.15e7, 'kyr': 3.15e10, 'Myr': 3.15e13}

  fig = plt.figure()

  groups = wn_h5.get_iterable_groups( file )

  nuclide_data = wn_h5.get_nuclide_data_hash( file )

  plp.set_plot_params( plt, keyword_parameters )

  names = wu.get_latex_names(species)

  l = {}
  for name in names:
     l[name], = plt.plot( [], [], label = name )

  legend = plt.legend( loc='upper center', shadow=True )

  with writer.saving(fig, movie_name, 200 ):
     for group in groups:
        m = wn_h5.get_group_mass_fractions( file, group )

        t = wn_h5.get_group_properties_in_zones( file, group, ['time'] )
        tt = float( t['time'][0] )
        title_str = "time (s) = %7.2e" % tt
        if( 'time_scale' in keyword_parameters ):
            title_str = \
               "time (" + keyword_parameters['time_scale'] + ") = %7.2e" \
               % (tt / ts_factor[keyword_parameters['time_scale']] )
 
        plt.title( title_str )

        if prop == '':
           x = np.linspace( 0, len( m[:,0] ) - 1, len( m[:,0] ) )
        else:
           props = wn_h5.get_group_properties_in_zones( file, group, [prop] )
           if( 'xfactor' in keyword_parameters ):
             xfactor = keyword_parameters['xfactor']
           else:
             xfactor = 1
           x = np.array( map( float, props[prop] ) ) / xfactor

        for sp in species:
           y = np.array( map( float, m[:, nuclide_data[sp]['index']] ) )
           l[sp].set_data( x, y )

        writer.grab_frame()
