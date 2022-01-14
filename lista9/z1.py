import numpy as np

#	x + 2y + 3z - 2t - u = 6
#	3x + 5y + 5z - 3t - 9u = 2
#	2x + 3y + 2z + 0t - 8u = -5
#	2x + 6y + 7z - 5t + u = 17
#	x + 2y + 6z - 4t - 10u = 12

a = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
b = np.array([6,2,-5,17,12])

val = np.linalg.solve(a,b)

print('Układ równań :')
print('x + 2y + 3z - 2t - u = 6 \n3x + 5y + 5z - 3t - 9u = 2 \n2x + 3y + 2z - 8u = -5 \n2x + 6y + 7z - 5t + u = 17 \nx + 2y + 6z - 4t - 10u = 12 \n')
print('x = '+str(val[0])+'\ty = '+str(val[1])+'\tz = '+str(val[2])+'\tt = '+str(val[3])+'\tu = '+str(val[4]))
