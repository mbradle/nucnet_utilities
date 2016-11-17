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
;    IDL function to retrieve the mass fraction of one or more species for all 
;    groups in a given zone from a standard multi-zone hdf5 output file
;
; :Params:
;    file = the name of the input file
;    zone = a three-element vector identifying the zone
;    species = the name of the species (more than one as an array)
;
; :Returns:
;    a double of the mass fraction of one species for the zone in all groups; or 
;    a two-dimensional array for the zone containing doubles of the mass 
;    fractions of multiple species in all groups, the first dimension 
;    corresponding to each species and the second dimension corresponding to 
;    each group 
;
; :Example:
;    IDL>print, h5_get_zone_mass_fractions_in_groups( 'my_file.h5', [1,0,0], 'mg2
;    4' )
;    IDL>print, h5_get_zone_mass_fractions_in_groups( 'my_file.h5', [1,0,0], ['mg
;    24','mg25','mg26'] )
;-

function h5_get_zone_mass_fractions_in_groups, file, zone, species

x_array = make_array( n_elements( species ), 1, value = 0. )

s = h5_get_group_names( file )

for n = 0, n_elements( s ) - 1 do begin
  x = h5_get_group_zone_species_mass_fractions( file, s[n], zone, species )
  x_array = [[x_array],[x]]
endfor

return, x_array[0:n_elements( species ) - 1,1:n_elements( s ) - 1]

end
