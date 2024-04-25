class Te:
    def __init__(self):
        """
        Funcion constructora de la clase, los métodos son estáticos por lo que no se ingresan valores aqui.

        Equivalencias
        ----------
        sabor : int
            Sabor del te representado en un numero.
            1 - te negro
            2 - te verde
            3 - infusion de hierbas

        formato : int
            Tamaño de la porcion del te representado en un numero.
            1 - 300 gr
            2 - 500 gr
        """

    @staticmethod
    def texto_sabor(sabor: int) -> str:
        """
        Esta función tiene como objetivo transformar el valor numerico del te a texto.

        Parameters
        ----------
        sabor : int
            Sabor del te representado en un numero.

        Returns
        -------
        str
            Retorna el valor string del sabor del te.
        """
        if sabor == 1:
            return "Té negro"

        elif sabor == 2:
            return "Té verde"

        elif sabor == 3:
            return "Infusión de hierbas"

    @staticmethod
    def tiempo_preparacion(sabor: int) -> int:
        """
        Esta función tiene como objetivo determinar el tiempo de preparacion del te en funcion de su sabor.

        Parameters
        ----------
        sabor : int
            Sabor del te representado en un numero.

        Returns
        -------
        int
            Retorna los minutos de preparacion del te en minutos.
        """
        if sabor == 1:
            return 3

        elif sabor == 2:
            return 5

        elif sabor == 3:
            return 6

    @staticmethod
    def recomendacion(sabor: int) -> str:
        """
        Esta función tiene como objetivo determinar la recomendacion para el consumo del te en funcion de su sabor.

        Parameters
        ----------
        sabor : int
            Sabor del te representado en un numero.

        Returns
        -------
        str
            Retorna la recomendacion de consumo.
        """
        if sabor == 1:
            return "Se recomienda consumirlo al desayuno"

        elif sabor == 2:
            return "Se recomienda consumirlo al medio día"

        elif sabor == 3:
            return "Se recomienda consumirlo al atardecer"

    @staticmethod
    def precio(formato: int) -> int:
        """
        Esta función tiene como objetivo determinar el precio del te en funcion de su sabor.

        Parameters
        ----------
        formato : int
            Tamaño de la porcion del te representado en un numero.

        Returns
        -------
        int
            Retorna el costo del te.
        """
        if formato == 1:
            return 3000

        elif formato == 2:
            return 5000
