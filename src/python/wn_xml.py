def get_root( file ):
    from lxml import etree
    import wn_xml

    return etree.parse( file ).getroot()
    
def get_species_data( root ):

    # Create output

    result = []

    # Get species

    species = root.xpath( '//nuclear_data/nuclide' )

    for sp in species:
        data = {}
        data['z'] = (sp.xpath( 'z' ))[0].text
        data['a'] = (sp.xpath( 'a' ))[0].text
        result.append( data )

    return result;

def get_zones( root, zone_xpath ):
    return root.xpath( '//zone' + zone_xpath );

def get_properties_in_zone( zone ):

    result = {}

    properties = zone.xpath( 'optional_properties/property' )

    # Loop on properties

    for property in properties:
        result[property.xpath( '@name' )[0]] = property.text
   
    return result;

def get_properties_in_zones( root, properties ):

    # Imports

    from lxml import etree

    # Create properties tuple

    properties_t = {}

    for property in properties:
        if property.isalnum():
           properties_t[property] = (property,);
        else:
           properties_t[property] = (property.split(","))
           if len(properties_t[property]) > 3:
             print "\nToo many property tags (at most 2)!\n"
             exit() 

    # Create output

    dict = {}

    for property in properties:
      dict[property] = []

    # Loop on properties

    for property in properties:

        tup = properties_t[property]

        path = '//zone_data/zone/optional_properties/property'

        if len( tup ) == 1:
          path += '[@name="%s"]' % tup[0].strip()
        elif len( tup ) == 2:
          path += '[@name="%s" and @tag1="%s"]' % ( tup[0].strip(), tup[1].strip() )
        else:
          path += '[@name="%s" and @tag1="%s" and @tag2="%s"]' % ( tup[0].strip(), tup[1].strip(), tup[2].strip() )

        props = root.xpath( path )

        if len( props ) == 0:
          print "Property not found."
          return;

        for elem in props:
            dict[property].append( elem.text );

    return dict;

def get_mass_fractions_in_zones( root, species ):

    # Create output

    dict = {}

    for my_species in species:
      dict[my_species] = []

    # Loop on zones

    zones = get_zones( root, "" )

    for zone in zones:

      for my_species in species:

        data = zone.find( 'mass_fractions/nuclide[@name="%s"]/x' %  my_species )
 
        if data == None:
          dict[my_species].append( 0. )
        else:
          dict[my_species].append( data.text )

    return dict;

def get_zone( root, zone_name ):

    if len( zone_name ) == 1:
       return root.xpath( '//zone[@label1 = "%s"]' % zone_name[0] )
    elif len( zone_name ) == 2:
       return root.xpath( 'zone[@label1 = "%s" and @label2 = %s]' % \
          zone_name[0], zone_name[1] )
    elif len( zone_name ) == 3:
       return \
          root.xpath( \
            'zone[@label1 = "%s" and @label2 = %s and @label3 = %s]' % \
             zone_name[0], zone_name[1] \
          )

def get_species_data_for_zone( zone ):

    # Create output

    result = {}

    # Get species

    species = zone.xpath( 'mass_fractions/nuclide' )

    for sp in species:
        data = {}
        data['z'] = int( (sp.xpath( 'z' ))[0].text )
        data['a'] = int( (sp.xpath( 'a' ))[0].text )
        data['n'] = data['a'] - data['z']
        data['x'] = float( (sp.xpath( 'x' ))[0].text )
        result[sp.xpath( '@name' )[0]] = data

    return result;

def get_zone_abundances_vs_nucleon_number( zone, nucleon ):

    # Get species data

    sp = get_species_data_for_zone( zone )

    # Determine output array

    n = []
     
    for s in sp:
      n.append( sp[s][nucleon] )

    y = [0.] * ( max( n ) + 1 )

    for s in sp:
      y[sp[s][nucleon]] += sp[s]['x'] / sp[s]['a']

    return y; 

