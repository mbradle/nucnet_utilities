def get_latex_names( nuclide_list ):

    latex_names = {}
    for nuclide in nuclide_list:
        letters = nuclide[0].upper()
        numbers = ""
        for i in range(1,len(nuclide)):
            if nuclide[i].isalpha():
                letters += nuclide[i]
            if nuclide[i].isdigit():
                numbers += nuclide[i]
        name = r"$^{%s}\rm{%s}$" % (numbers,letters)
        latex_names[nuclide] = name

    return latex_names;

