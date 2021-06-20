# -*- coding: utf-8 -*-
import CoolProp as cp
import numpy as np

class fluido:    
    def __init__(self, nombre_fluido):
        self.fluid = nombre_fluido
        self.k,self.rho,self.Pr,self.mu,self.nu,self.cp = np.ones((6,1))
        self._temperatura = 25
        self.propiedades()


    @property
    def temperatura(self):
        return self._temperatura
    @temperatura.setter
    def temperatura(self, value):
        self._temperatura = value
        # operaciones que quieras que se hagan
        self.propiedades()
        
    def propiedades(self):
        self.cp = cp.CoolProp.PropsSI('C','T',273+self.temperatura,'P',101.325e3,'Air')
        self.rho = cp.CoolProp.PropsSI('D','T',273+self.temperatura,'P',101.325e3,'Air')
        self.mu = cp.CoolProp.PropsSI('V','T',273+self.temperatura,'P',101.325e3,'Air')
        self.Pr = cp.CoolProp.PropsSI('Prandtl','T',273+self.temperatura,'P',101.325e3,'Air')
        self.k = cp.CoolProp.PropsSI('L','T',273+self.temperatura,'P',101.325e3,'Air')
        self.nu = self.mu/self.rho


    
        
