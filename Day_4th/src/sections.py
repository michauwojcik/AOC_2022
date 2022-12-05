

class CommonSectionsFinder:
    """
    CommonSectionsFinders allows to compare different elves' sections 
    and find sections which are planned to be cleand twice.

    """

    def __init__(self, sections_ranges: list):
        self.sections_ranges = sections_ranges


    def count_common_sections(self, sections_pairs_sets: list):
        """
        Counts the number of section which are fully covered by other elf's sections.

        Args:
            sections_pairs_sets (list): _description_

        Returns:
            _type_: _description_
        """
        fully_covered_sections = list(filter(lambda pair: self.check_two_sets(pair[0], pair[1]), sections_pairs_sets))
        return len(fully_covered_sections)


    @staticmethod
    def check_two_sets(s1: set, s2: set):
        """
        Checks whether *s1* is a subset of *s2* OR *s2* is a subset of *s1*
        if above conditions is satisfied returns True.
        """

        return (s1 <= s2) | (s2 <= s1)


    def get_sections_sets_pairs(self):
        """
        Gets *sections_ranges* (e.g. [['2-4', '6-8'], ['2-3', '4-5']])
        and converts it into pairs of sections sets (e.g. [({2,3,4}, {6,7,8}), ({2,3}, {4,5})]))

        Returns:
            (list): list of pairs, where each pair is two sets of sections' ranges
        """

        sections_sets_pairs = map(lambda x: (self.get_sections_range(x[0]), self.get_sections_range(x[1])), self.sections_ranges)
        return list(sections_sets_pairs)

    
    def get_sections_range(self, sections: str):
        """
        Returns representaion of given *sections* as a set of sections

        Args:
            sections (str): given sections range (e.g.: '1-2', '3-6', etc.)

        Returns:
            range: a set of sections (e.g. {1,2}, {3,4,5,6}, etc.)
        """

        section_range_start = int(sections[0])
        section_range_end = int(sections[-1]) + 1

        return {section for section in range(section_range_start, section_range_end)}
