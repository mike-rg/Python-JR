def thausands_with_commas(i):
    """ Add commas every three decimal places in numbers of four or more
    digits, counting right to left."""
    out_of_commas = str(i)
    retval = ''

    while len(out_of_commas) // 3:
        three_last_digits = out_of_commas[-3:]
        with_comma = ',' + three_last_digits
        # delete tree_last_digits from out_of_commas and process residual
        out_of_commas = out_of_commas[:-3]

        if len(out_of_commas) == 0:
            retval = three_last_digits + retval

        else:
            retval = with_comma + retval

    # add the residual of out_of_commas
    retval = out_of_commas + retval
    return retval

if __name__ == "__main__":
    assert thausands_with_commas(1234) == '1,234'
    assert thausands_with_commas(123456789) == '123,456,789'
    assert thausands_with_commas(12) == '12'