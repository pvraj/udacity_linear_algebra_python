'''
Starter code downloaded from Udacity class page.
-issue with type hints: https://stackoverflow.com/questions/36286894/name-not-defined-in-type-annotation
-Modifications by Partha Rajendra.

'''
from math import sqrt, pow, acos, degrees
from decimal import Decimal, getcontext

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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

    def __mul__(self, scalar: Decimal) -> 'Vector':
        '''
        Description: Given as input a scalar, output the vector that results from multiplying the self vector by the scalar.
        :param scalar: (Decimal) Scalar value used for multiplication.
        :return: (Vector) Resultant scaled vector.
        '''
        # let's just assume we don't have to worry about checking the data type for the scalar.
        scaled_vector = [Decimal(scalar)*x for x in self.coordinates]
        return Vector(scaled_vector)

    def magnitude(self) -> Decimal:
        '''
        Description: Output the magnitude of the vector.
        :return: (Decimal) Magnitude of the vector.
        '''
        squared_sum = Decimal(0.0)
        for coordinate in self.coordinates:
            squared_sum += pow(coordinate, 2)
        return Decimal(sqrt(squared_sum))

    def normalization(self) -> 'Vector':
        '''
        Description: Output the normalization (normalized vector) of the current vector.
        :return: (Vector) Normalized vector.
        '''
        try:
            magnitude = self.magnitude()
            return self * (Decimal(1.0) / magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector.")

    def dot_product(self, w) -> Decimal:
        '''
        Description: Return the dot product of 2 vectors.
        :param w: (Vector) Vector to multiply by.
        :return: (Decimal) Dot product of 2 vectors.
        '''
        if self.dimension != w.dimension:
            raise Exception("Error in dot product operation: Vector dimensions are not equal.")
        else:
            sum_of_products = Decimal(0.0) # constant space
            for x,y in zip(self.coordinates, w.coordinates): # linear time
                sum_of_products += x*y
            return sum_of_products

    def angle(self, w) -> list:
        '''
        Description: Return the angle between 2 vectors
        :param w: (Vector) The second vector.
        :return: (list) The first element in the list is the angle in radians; the second element in the list is the quantity in degrees.
        '''
        theta_radians = acos((self.dot_product(w) / Decimal(self.magnitude() * w.magnitude())))
        return [theta_radians, degrees(theta_radians)]

    def is_parallel(self, w) -> bool:
        '''
        Description: Return whether or not 2 vectors are parallel (i.e, 3v is parallel with v, 0v, etc.).
        :param w: (Vector) The second vector.
        :return: (bool) is parallel.
        '''
        # if they are scalar multiples
        if self.dimension != w.dimension:
            raise Exception("Error is_parallel: Vector dimensions are not equal.")
        else:
            try:
                if self.is_zero_vector() or w.is_zero_vector():
                    return True

                factor = Decimal(0)
                if self.coordinates[0] == Decimal(0):
                    factor = Decimal(0)
                else:
                    factor = Decimal(w.coordinates[0] / self.coordinates[0])

                for v,w, in zip(self.coordinates, w.coordinates):
                    if (w/v) != factor:
                        return False
                return True

            except ZeroDivisionError:
                raise("ZeroDivisionError: is_parallel")

    def is_orthogonal(self, w) -> bool:
        '''
        Description: Return whether or not 2 vectors are orthogonal (i.e., the dot product is 0; this means either 1 must be a zero vector, or the vectors are at right angles).
        :param w:
        :return: is orthogonal
        '''
        if self.dimension != w.dimension:
            raise Exception("Error is_orthogonal: Vector dimensions are not equal.")
        else:
            return self.is_zero_vector() or w.is_zero_vector or (self.dot_product(w) == Decimal(0))


    def is_zero_vector(self) -> bool:
        '''
        Description: Return whether or not a vector is a zero vector (in other words, all numbers in the vector are 0).
        :return: is zero vector.
        '''
        for coordinate in self.coordinates:
            if coordinate != Decimal(0):
                return False
        return True

getcontext().prec = 7
# v1 = Vector([7.887, 4.138])
# w1 = Vector([-8.802, 6.776])
# v2 = Vector([-5.955, -4.904, -1.874])
# w2 = Vector([-4.496, -8.755, 7.103])
# print(v1.dot_product(w1))
# print(v2.dot_product(w2))

# v3 = Vector([3.183, -7.627])
# w3 = Vector([-2.668, 5.319])
# print(v3.angle(w3)[0])
# v4 = Vector([7.35, 0.221, 5.188])
# w4 = Vector([2.751, 8.259, 3.985])
# print(v4.angle(w4)[1])

v1 = Vector([-7.579, -7.88])
w1 = Vector([22.737, 23.64])
# print(v1.is_parallel(w1))
# print(v1.is_orthogonal(w1))
v2 = Vector([-2.029, 9.97, 4.172])
w2 = Vector([-9.231, -6.639, -7.245])
# print(v2.is_parallel(w2))
# print(v2.is_orthogonal(w2))
v3 = Vector([-2.328, -7.284, -1.214])
w3 = Vector([-1.821, 1.072, -2.940])
# for coordinate in v3.coordinates:
#     print(coordinate)
# print(v3)
# print(w3)
# print(v3.is_parallel(w3))
# print(v3.is_orthogonal(w3))
v4 = Vector([2.118, 4.827])
w4 = Vector([0, 0])
print(v4.is_parallel(w4))
print(v4.is_orthogonal(w4))
# v5 = Vector([0, 0, 0])
# print(v5.is_zero_vector())


