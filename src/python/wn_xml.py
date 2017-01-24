def get_properties_in_zones( file, properties ):

    # Imports

    from xml.dom.minidom import parse
    import xml.dom.minidom
    
    # Open XML document using minidom parser

    DOMTree = xml.dom.minidom.parse( file )
    collection = DOMTree.documentElement

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

    # Get all the zones in the collection

    zones = collection.getElementsByTagName("zone")
    
    # Assign data for each zone

    for zone in zones:
    
        # Get property lists

        props = zone.getElementsByTagName("property")
    
        prop_dict = {}

        for prop in props:
            prop_dict[prop.getAttribute("name")] = prop

        for property in properties:
            tup = properties_t[property]
            if( tup[0] in prop_dict ):
               prop = prop_dict[tup[0]]
               if( len( tup ) == 1 ):
                  dict[property].append( prop.firstChild.data )
               elif( len( tup  ) == 2 ):
                  if(
                      prop.hasAttribute("tag1") and
                      prop.getAttribute("tag1") == tup[1]
                    ):
                     dict[property].append( prop.firstChild.data )
               else:
                  if(
                      prop.hasAttribute("tag1") and 
                      prop.getAttribute("tag1") == tup[1] and
                      prop.hasAttribute("tag2") and 
                      prop.getAttribute("tag2") == tup[2]
                  ):
                     dict[property].append( prop.firstChild.data )
                  
    return dict;

def get_mass_fractions_in_zones( file, species ):

    # Imports

    from xml.dom.minidom import parse
    import xml.dom.minidom
    
    # Open XML document using minidom parser

    DOMTree = xml.dom.minidom.parse( file )
    collection = DOMTree.documentElement
    
    # Create output

    dict = {}

    for my_species in species:
      dict[my_species] = []

    # Get all the zones in the collection

    zones = collection.getElementsByTagName("zone")
    
    # Assign data for each zone

    for zone in zones:
    
        # Get species mass fractions.  If the species is not present,
        # the abundance is set to zero for this zone.

        zone_nuclides = zone.getElementsByTagName("nuclide")

        nuclides = {}

        for nuclide in zone_nuclides:
          nuclides[nuclide.getAttribute("name")] = nuclide

        for my_species in species:
            if my_species in nuclides:
                dict[my_species].append( 
                  nuclides[
                     my_species
                  ].getElementsByTagName("x")[0].firstChild.data
                )
            else:
                dict[my_species].append( 0. )
            
    return dict;

