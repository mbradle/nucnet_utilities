;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;  This file was originally written by Bradley S. Meyer and Michael J. Bojazi.
;
;  This is free software; you can redistribute it and/or modify it
;  under the terms of the GNU General Public License as published by
;  the Free Software Foundation; either version 3 of the License, or
;  (at your option) any later version.
;  but WITHOUT ANY WARRANTY; without even the implied warranty of
;  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;  GNU General Public License for more details.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;+
; :Description:
;    IDL function to retrieve one or more properties for all groups in a given 
;    zone from a standard multi-zone hdf5 output file
;
; :Params:
;    file = the name of the input file
;    zone = a three-element vector identifying the zone
;    property = an array of strings, each string 
;               (in the form 'name,tag_1 (optional),tag_2 (optional)') 
;               containing the name of the property to be retrieved and 
;               optional tag specifiers, or a string of 
;               the name and optional tag specifiers if only a single property 
;               is to be retrieved (see examples below)
;
; :Returns:
;    a string of the value of one property for the zone in all groups; or a 
;    two-dimensional array for the zone containing strings of the values of 
;    multiple properties in all groups, the first dimension corresponding to 
;    each property and the second dimension corresponding to each group 
;
; :Example:
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], ['time,0
;    ,0','zone mass,0,0','groups,0,0'] )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], ['time',
;    'zone mass,0,0','groups,0'] )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], ['time,0
;    ,0','zone mass,0'] )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], ['time,0
;    ','groups,0,0'] )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], ['time',
;    'zone mass','groups'] )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], 'time,0,
;    0' )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], 'time,0'
;     )
;    IDL>print, h5_get_zone_properties_in_groups( 'my_file.h5', [1,0,0], 'time' )
;-

function h5_get_zone_properties_in_groups, file, zone, property

s = h5_get_group_names( file )

property_array = make_array( n_elements( property ), 1, value = '' )

for n = 0, n_elements( s ) - 1 do begin
  prop = h5_get_group_zone_properties( file, s[n], zone, property )
  property_array = [[property_array],[prop]]
endfor

return, property_array[0:n_elements( property ) - 1,1:n_elements( s ) -1]

end
