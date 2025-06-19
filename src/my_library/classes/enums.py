from enum import StrEnum


class BaseEnum(StrEnum):
    @classmethod
    def value_list(cls):
        return [e.value for e in cls]

class FictionLabel(BaseEnum):
    SCI_FI = 'Sciene-Fiction'
    HORROR = 'Horror'
    FANTASY = 'Fantasy'
    HISTORY = 'Historisch'
    HUMOR = 'Humor'
    DRAMA = 'Drama'


class NonFictionLabel(BaseEnum):
    POLITIK = 'Politik'
    RELIGION = 'Religion'
    PSYCHOLOGIE = 'Psychologie'
    SOZIOLOGIE = 'Soziologie'
    NATURWISSENSCHAFT = 'Naturwissenschaft'
    MEDIZIN = 'Medizin'


class Genre(BaseEnum):
    ROMAN = 'Roman'
    SACHBUCH = 'Sachbuch'
    BILDBAND = 'Bildband'

