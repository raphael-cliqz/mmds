import argparse
import numpy

def build_args():
    parser = argparse.ArgumentParser(description='Calc powerrank.')
    parser.add_argument('-m', type=parse_matrix, help='the graph matrix', required=True)
    parser.add_argument('-b', type=float, help='beta', required=True)
    parser.add_argument('-r', type=parse_matrix, help='r', required=True)
    return parser.parse_args()


def parse_matrix(matrix):
    matrix = matrix.split(':')
    matrix = [[float(y) for y in x.split(',')] for x in matrix]
    matrix = numpy.array(matrix)
    return matrix

if __name__ == '__main__':
    args = build_args()
    m = args.m
    r = args.r.T
    b = args.b

    x1 = m.dot(b)
    num_nodes = len(x1[0])

    x2 = numpy.ones((num_nodes, num_nodes), dtype=numpy.float)
    x2 = x2.dot(1./num_nodes)
    x2 = x2.dot(1 - b)

    y = x1 + x2

    for x in xrange(1000000):
        r = y.dot(r)

    print r
