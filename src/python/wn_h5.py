import h5py

def get_nuclide_data_array( file ):

    result = []
   
    # Read HDF5 file
   
    h5file = h5py.File( file,'r' )
    nuclide_data = h5file['/Nuclide Data']

    for i in range(len(nuclide_data)):
         data = {}
         data['name'] = nuclide_data[i][0]
         data['z'] = nuclide_data[i][2]
         data['a'] = nuclide_data[i][3]
         data['mass excess'] = nuclide_data[i][4]
         result.append( data )
           
    return result;
   
def get_nuclide_data_hash( file ):

    nuclide_data = get_nuclide_data_array( file )

    result = {}
   
    for i in range( len( nuclide_data ) ):
        data = {}
        data['index'] = i
        data['z'] = nuclide_data[i]['z']
        data['a'] = nuclide_data[i]['a']
        data['mass excess'] = nuclide_data[i]['mass excess']
        result[nuclide_data[i]['name']] = data 

    return result;

def get_group_zone_labels_array( file, group ):

    # Read HDF5 file

    h5file = h5py.File( file,'r' )
    zone_labels = h5file['/' + group + '/Zone Labels'] 

    result = []

    for i in range( len( zone_labels ) ):
         result.append(
            (zone_labels[i][0], zone_labels[i][1], zone_labels[i][2])
         )

    return result;

def get_group_zone_labels_hash( file, group ):

    zone_labels_array = get_group_zone_labels_array( file, group )

    result = {}

    for i in range( len( zone_labels_array ) ):
         result[zone_labels_array[i]] = i

    return result; 

def get_group_mass_fractions( file, group ):

    # Read HDF5 file

    h5file = h5py.File( file,'r' )
    return h5file['/' + group + '/Mass Fractions'];

def get_zone_nuclide_mass_fractions_in_groups( file, zone, nuclides ):

    # Read HDF5 file

    h5file = h5py.File( file,'r' )

    # Get index hash

    nuclide_hash = get_nuclide_data_hash( file )

    result = {}

    for nuclide in nuclides:
        result[nuclide] = []

    for group_name in h5file:
        if( group_name != 'Nuclide Data' ):
            zone_index = get_group_zone_labels_hash( file, group_name )
            x = get_group_mass_fractions( file, group_name ) 
            for nuclide in nuclides:
                result[nuclide].append(
                    x[zone_index[zone]][nuclide_hash[nuclide]['index']]
                )

    return result;

def get_group_zone_property_hash( file, group, zone ):

    # Read HDF5 file

    h5file = h5py.File( file,'r' )

    zone_index = get_group_zone_labels_hash( file, group )[zone]

    properties = h5file['/' + group + '/Zone Properties/' + str(zone_index)]

    result = {}

    for property in properties:
        name = ''
        if( property[1] == '0' and property[2] == '0' ):
            name = property[0]
        elif( property[1] != '0' and property[2] == '0' ):
            name = (property[0],property[1])
        else:
            name = (property[0],property[1],property[2])
        result[name] = property[3]

    return result; 
    
def get_zone_properties_in_groups( file, zone, properties ):

    # Read HDF5 file

    h5file = h5py.File( file,'r' )

    # Get output

    result = {}

    for property in properties:
        result[property] = []

    for group_name in h5file:
        if( group_name != 'Nuclide Data' ):
            p = get_group_zone_property_hash( file, group_name, zone )
            for property in properties:
                result[property].append( p[property] )

    return result;

