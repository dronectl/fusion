# -*- coding: utf-8 -*-
"""
Propeller
=========

Copyright © 2022 dronectl. All rights reserved.
"""

class Propeller:

    @property
    def pitch(self) -> float:
        """
        Propeller blade pitch (mm)

        :return: propeller blade pitch (mm)
        :rtype: float
        """
        return self.__pitch
    
    @pitch.setter
    def pitch(self, pitch: float) -> None:
        """
        Propeller blade pitch (mm)

        :return: propeller blade pitch (mm)
        :rtype: float
        """
        self.__pitch = pitch
  
    @property
    def blades(self) -> int:
        """
        Number of propeller blades

        :return: number of propeller blades
        :rtype: int
        """
        return self.__blades
    
    @blades.setter
    def blades(self, blades: int) -> None:
        """
        Number of propeller blades

        :param blades: number of propeller blades
        :type blades: int
        """
        self.__blades = blades

    @property
    def diameter(self) -> float:
        """
        Propeller blade diameter (mm) 

        :return: Propeller blade diameter (mm)
        :rtype: float
        """
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: float) -> None:
        """
        Propeller blade diameter (mm)

        :param diameter: propeller blade diameter (mm)
        :type diameter: float
        """
        self.__diameter = diameter