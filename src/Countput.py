# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Dec 14, 2018

@author: Erik Pohl
"""
from collections import Counter, OrderedDict



class Countput(Counter):
    """ Extend Counter with some output methods """
    
    def return_topn_as_list_of_strings(
            self,
            *,
            n=None,
            delimiter=' ',
            prefix='',
            suffix='',
            header=None
    ):
        """
        Return the top n of the counter object
        as a list of strings
        using parameter hints for formatting
        """
        headless_horseman = [
            prefix + delimiter.join(
                [
                    str(
                        frequency_data
                    )
                    for frequency_data
                    in frequency_tuple
                ]
            ) + suffix
            for frequency_tuple
            in self.most_common(n)
        ]
        return [header] + headless_horseman if header else headless_horseman

    def formatted_topn_output(
            self,
            *,
            n=None,
            delimiter=' ',
            prefix='',
            suffix='',
            header=None
    ):
        """
        Output to stdout the top n 
        of the counter object
        using parameter hints for formatting
        """
        if header:
            print(header)
        [
            print(
                prefix + delimiter.join(
                    [
                        str(
                            frequency_data
                        )
                        for frequency_data
                        in frequency_tuple
                    ]
                ) + suffix
            )
            for frequency_tuple
            in self.most_common(n)
        ]

    def return_as_dict(self, frequency=None):
        """
        Return the Counter results
        as a dictionary 
        using an optional frequency parameter
        to limit results
        """

        from src.version_compare import version_compare
        # do something different for versions of Python
        # where the dictionary is not automatically ordered
        vc = version_compare()
        # adding to an ordered dict takes 75% more time
        return_dictionary = {} if vc.current_version_greater_than_or_equal_than("3.7.1") else OrderedDict()
        return_dictionary.update(
            {
                frequency_tuple[0]: frequency_tuple[1]
                for frequency_tuple
                in self.most_common()
                if frequency_tuple[1] == (frequency_tuple[1] if frequency is None else frequency)
            }
        )
        return dict(return_dictionary)

        
