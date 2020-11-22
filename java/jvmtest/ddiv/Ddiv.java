package ddiv;

/*
    2.8.3. Value Set Conversion
    https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html#jvms-2.8.3
*/

class Ddiv {

    public static boolean ddiv(double x, double y, double z) {
        boolean ret;
        ret = do_extended_ddiv(x, y, z);
        ret &= do_strict_ddiv(x, y, z);
        return ret;
    }

    public static void exit(boolean verdict) {
        System.exit(verdict ? 0 : 1);
    }

    // I'm not sure if strictfp affects calculations in nested (non-strict) methods
    // so here are 2 identical methods: extendend fp and strict fp

    private static boolean do_extended_ddiv(double dividend, double divisor, double expected) {
        boolean verdict;
        double result = dividend / divisor;
        if (Double.isNaN(expected)) { // we are expecting NaN
            verdict = Double.isNaN(result);
        } else {
            verdict = (result == expected);
        }
        if (!verdict) {
            System.err.printf("Extended ddiv: Unexpected %e; Expected %e / %e = %e%n",
                result, dividend, divisor, expected);
        }
        return verdict;
    }

    public strictfp static boolean do_strict_ddiv(double dividend, double divisor, double expected) {
        boolean verdict;
        double result = dividend / divisor;
        if (Double.isNaN(expected)) {
            verdict = Double.isNaN(result);
        } else {
            verdict = (result == expected);
        }
        if (!verdict) {
            System.err.printf("Strict ddiv: Unexpected %e; Expected %e / %e = %e%n",
                result, dividend, divisor, expected);
        }
        return verdict;
    }


}