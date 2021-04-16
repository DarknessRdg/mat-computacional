# function
# minQuadradosLinear(x, y)
# {
#     let[Ex, Ey, Exy, Ex2] = [0, 0, 0, 0];
#
# for (let i in x)
# {
#     Ex += x[i];
# Ey += y[i];
# Exy += x[i] * y[i];
# Ex2 += x[i] ** 2;
# }
#
# const
# n = x.length;
#
# const
# a = (n * Exy - Ex * Ey) / (n * Ex2 - Math.pow(Ex, 2));
#
# const
# b = (Ex2 * Ey - Exy * Ex) / (n * Ex2 - Math.pow(Ex, 2));
#
# return [a, b]
# }
# https://pastebin.com/LviQS4Q8
