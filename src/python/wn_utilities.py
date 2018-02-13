def get_latex_names( nuclides ):

    latex_names = {}
    for nuclide in nuclides:
        if len( nuclide ) != 1 or nuclide[0] != 'n':
          letters = nuclide[0].upper()
        else:
          letters = nuclide[0]
        numbers = ""
        for i in range(1,len(nuclide)):
            if nuclide[i].isalpha():
                letters += nuclide[i]
            if nuclide[i].isdigit():
                numbers += nuclide[i]
        name = r"$^{%s}\rm{%s}$" % (numbers,letters)
        latex_names[nuclide] = name

    return latex_names;

