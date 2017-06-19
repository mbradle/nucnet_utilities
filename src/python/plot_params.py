def set_plot_params( plt, keyword_params ):

    if( 'xscale' in keyword_params ):
      plt.xscale( keyword_params['xscale'] )

    if( 'yscale' in keyword_params ):
      plt.yscale( keyword_params['yscale'] )

    if( 'xlim' in keyword_params ):
      plt.xlim( keyword_params['xlim'] )

    if( 'ylim' in keyword_params ):
      plt.ylim( keyword_params['ylim'] )

    if( 'xlabel' in keyword_params ):
      plt.xlabel( keyword_params['xlabel'] )

    if( 'ylabel' in keyword_params ):
      plt.ylabel( keyword_params['ylabel'] )

    if( 'thickness' in keyword_params ):
      plt.rcParams['axes.linewidth'] = float(keyword_params['thickness'])
      plt.rcParams['lines.linewidth'] = float(keyword_params['thickness'])

    if( 'font_size' in keyword_params ):
      plt.rcParams.update( {'font.size': int( keyword_params['font_size'] ) } )
