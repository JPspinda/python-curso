try: 
    import sys
    sys.path.append('C:/Users/Ample Teleco/Desktop/python')
except ModuleNotFoundError:
    ...
import aula10

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')