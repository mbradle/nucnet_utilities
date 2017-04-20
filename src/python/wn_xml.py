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

    zones = root.xpath( '//zone' )

    for zone in zones:

      for my_species in species:

        data = zone.find( 'mass_fractions/nuclide[@name="%s"]/x' %  my_species )
 
        if data == None:
          dict[my_species].append( 0. )
        else:
          dict[my_species].append( data.text )

    return dict;

def get_mass_fractions_for_zone( root, zone_name ):

    # Create output

    dict = {}

    # Get species

    z = root.xpath( '//nuclide_data/nuclide/z' )

    for my_z in z:
       print my_z

    return;

