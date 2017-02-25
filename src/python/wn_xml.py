def get_properties_in_zones( file, properties ):

    # Imports

    from lxml import etree
    
    # Parse the file and get the root

    root = etree.parse( file ).getroot()

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

    # Loop on zones

    zones = root.xpath( '//zone' )

    for zone in zones:

      for property in properties:

        tup = properties_t[property]

        if len( tup ) == 1:
          data = zone.xpath( './/property[@name="%s"]' %  tup[0] )
        elif len( tup ) == 2:
          data = zone.xpath(
              './/property[@name="%s" and @tag1="%s"]' %
              tup[0], tup[1]
            )
        else:
          data = zone.xpath(
            './/property[@name="%s" and @tag1="%s" and @tag2="%s"]' %
              tup[0], tup[1], tup[2]
          )

        for node in data:
          dict[property].append( node.text )
      
    return dict;

def get_mass_fractions_in_zones( file, species ):

    # Imports

    from lxml import etree
    
    # Parse file

    root = etree.parse( file ).getroot()
    
    # Create output

    dict = {}

    for my_species in species:
      dict[my_species] = []

    # Loop on zones

    zones = root.xpath( '//zone' )

    for zone in zones:

      for my_species in species:

        data = zone.xpath( './/nuclide[@name="%s"]/x' %  my_species )

        if len( data ) == 0:
          dict[my_species].append( 0. )
        else:
          dict[my_species].append( data[0].text )

    return dict;

