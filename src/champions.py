from sklearn import preprocessing
import pandas as pd


class ChampionData:
    """Storage and methods for transforming champion representations.

    Each champion has unique traits that make it fitted towards certain playstyles.
    This is where a database of those traits will live and be transformed into machine data.
    """

    """
    Example:
        Given Blue: Tryndamere, Viego, Zoe, Jhin, Leona
        Given Red: Jax, Xin Zhao, Viktor, Jinx, Thresh

        Blue Vector: <......., Tryndamere :yup:, .....> + (<Attack, Split, Siege, Protect, Catch> / 5)

        Inputs to Machine:
            Blue Vector: length 160
            Red Vector: length 160
    """
    pass
