from math import exp, log, sqrt, tan


def cot(x):
    return tan(x)**-1


# Bessel functions from http://mhtlab.uwaterloo.ca/old/courses/me3532/js/bessel.html


def I0(x):
    ax = abs(x)
    if ax < 3.75:
        y  = (x / 3.75)**2
        ans = 1 + y * (3.5156229 + y * (3.0899424 + y * (1.2067492 + y * (0.2659732 + y * (0.360768E-1 + y * 0.45813e-2)))))
    else:
        try:
            y = 3.75 / ax
            ans  = 0.39894228 + y * (0.1328592E-1 + y * (0.225319E-2 + y * (-0.157565E-2 + y * (0.916281E-2 + y * (-0.2057706E-1 + y * (0.2635537E-1 + y * (-0.1647633E-1 +y * 0.392377E-2)))))))
            ans *= exp(ax) / sqrt(ax)
        except OverflowError:
            ans = float('inf')
    return ans


def I1(x):
    ax = abs(x)
    if ax < 3.75:
        y  = (x / 3.75)**2
        ans = ax * (0.5 + y * (0.87890594 + y * (0.51498869 + y * (0.15084934 + y * (0.2658733E-1 + y * (0.301532E-2 + y * 0.32411E-3))))))
    else:
        try:
            y = 3.75 / ax
            ans  = 0.2282967E-1 + y * (-0.2895312E-1 + y * (0.1787654E-1 - y * 0.420059E-2))
            ans  = (0.39894228 + y * (-0.3988024E-1 + y * (-0.362018E-2 + y * (0.163801E-2 + y * (-0.1031555E-1 + y * ans)))))
            ans *= exp(ax) / sqrt(ax)
        except OverflowError:
            ans = float('inf')
    return -ans if x < 0 else ans


def K0(x):
    if x <= 2:
        y = x**2 / 4
        ans = -log(x/2) * I0(x) - 0.57721566 + 0.42278420 * y + 0.23069756 * y**2 + 0.03488590 * y**3 + 0.00262698 * y**4 + 0.00010750 * y**5 + 0.00000740 * y**6
    else:
        try:
            y = 2 / x
            ans  = 1.25331414 + y * (-0.7832358E-1 + y * (0.2189568E-1 + y * (-0.1062446E-1 + y * (0.587872E-2 + y * (-0.251540E-2 + y * 0.53208E-3)))))
            ans *= exp(-x) / sqrt(x)
        except OverflowError:
            ans = float('inf')
    return ans


def K1(x):
    if x <= 2:
        y = x**2 / 4
        ans = log(x/2) * I1(x) + 1/x * (1 + y * (0.15443144 + y * (-0.67278579 + y * (-0.18156897 + y * (-0.1919402E-1 + y * (-0.110404E-2 + y * (-0.4686E-4)))))))
    else:
        try:
            y = 2 / x
            ans  = 1.25331414 + y * (0.23498619 + y * (-0.3655620E-1 + y * (0.1504268E-1 + y * (-0.780353E-2 + y * (0.325614E-2 + y * (-0.68245E-3))))))
            ans *= exp(-x) / sqrt(x)
        except OverflowError:
            ans = float('inf')
    return ans
