ACTA_DESGLOSADA = False

# Cantidad de suplentes ademas del presidente en las autoridades de mesa
CANTIDAD_SUPLENTES = 1

# (No) Almacenar DNI en acta de Recuento:
GUARDAR_DNI = False

try:
    from msa.core.documentos.settings_local import *
except ImportError:
    pass
