import argparse
import numpy

def build_args():
    parser = argparse.ArgumentParser(description='Calc powerrank.')
    parser.add_argument('-m', help='the graph matrix', required=True)
    parser.add_argument('-b', type=float, help='beta', required=True)
    parser.add_argument('-r', help='r', required=True)
    return parser.parse_args()


def parse_matrix(matrix):
    matrix = matrix.split(':')
    matrix = [[float(y) for y in x.split(',')] for x in matrix]
    matrix = numpy.array(matrix)
    return matrix

if __name__ == '__main__':
    args = build_args()
    m = parse_matrix(args.m)
    r = parse_matrix(args.r).T
    b = args.b

    x1 = m.dot(b)
    num_nodes = float(len(x1[0]))
    x2 = numpy.array([[1 / num_nodes for x in range(int(num_nodes))]
                       for x in range(int(num_nodes))])
    x2 = x2.dot(0.3)
    y = x1 + x2

    for x in xrange(1000000):
        r = y.dot(r)

    print r
