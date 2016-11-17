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
;    IDL function to retrieve the number of steps from a standard multi-zone 
;    hdf5 output file
;
; :Params:
;    file = the name of the input file
;
; :Returns:
;    a long integer of the number of steps    
;    
; :Example:
;    IDL>print, h5_get_number_of_steps( 'my_file.h5' )
;-

function h5_get_number_of_steps, file

file_id = h5f_open( file )
n_steps = h5g_get_nmembers( file_id, '/' )
h5f_close, file_id

return, n_steps - 1 ; number of steps is number of groups minus 1

end
