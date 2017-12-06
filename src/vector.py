'''
Starter code downloaded from Udacity class page.
-issue with type hints: https://stackoverflow.com/questions/36286894/name-not-defined-in-type-annotation
-Modifications by Partha Rajendra.

'''
from math import sqrt, pow

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self) -> str:
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v: 'Vector') -> bool:
        return self.coordinates == v.coordinates

    def __add__(self, v: 'Vector') -> 'Vector':
        '''
        Description: Given as input a second vector, v, output the sum of the self vector and v.
        :param v: (Vector) Second vector, that is being added to the current vector (self)
        :return: (Vector) Resultant sum vector.
        '''
        if self.dimension != v.dimension:
            raise Exception("Error in Plus operation: Vector dimensions are not equal.")
        else:
            sum_vector = [x+y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(sum_vector)

    def __sub__(self, v: 'Vector') -> 'Vector':
        '''
        Description: Given as input a second vector, v, output the difference of the self vector and v.
        :param v: (Vector) Second vector, that is being subtracted to the current vector (self)
        :return: (Vector) Resultant difference vector.
        '''
        if self.dimension != v.dimension:
            raise Exception("Error in Minus operation: Vector dimensions are not equal.")
        else:
            difference_vector = [x-y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(difference_vector)

    def __mul__(self, scalar: float) -> 'Vector':
        '''
        Description: Given as input a scalar, output the vector that results from multiplying the self vector by the scalar.
        :param scalar: (?float) Scalar value used for multiplication.
        :return: (Vector) Resultant scaled vector.
        '''
        # let's just assume we don't have to worry about checking the data type for the scalar.
        scaled_vector = [scalar*x for x in self.coordinates]
        return Vector(scaled_vector)

    def magnitude(self) -> float:
        '''
        Description: Output the magnitude of the vector.
        :return: (float) Magnitude of the vector.
        '''
        magnitude = 0
        for coordinate in self.coordinates:
            magnitude += pow(coordinate, 2)
        return sqrt(magnitude)

    def normalization(self) -> 'Vector':
        '''
        Description: Output the normalization (normalized vector) of the current vector.
        :return: (Vector) Normalized vector.
        '''
        magnitude = self.magnitude()
        return self * (1 / magnitude)



v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
# print("v1 + v2: %s" % (v1 + v2))
# print("v1 - v2: %s" % (v1 - v2))
# print(v1 == v2)
# in order to do (scalar * vector) instead of (vector * scalar), do we need to override the * operator for real numbers also?
# print("3 * v1 = %s" % (v1 * 3))

v3 = Vector([2, 3])
print("the magnitude is: %s" % v3.magnitude())
print("the normalized vector is: %s" % v3.normalization())