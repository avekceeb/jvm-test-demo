package ddiv;

class TestZero extends Ddiv {
    public static void main(String[] args) {
        boolean ok = true;
        ok &= ddiv( 3.14,  0.0, Double.POSITIVE_INFINITY);
        ok &= ddiv(-3.14, -0.0, Double.POSITIVE_INFINITY);
        ok &= ddiv(-3.14,  0.0, Double.NEGATIVE_INFINITY);
        ok &= ddiv( 3.14, -0.0, Double.NEGATIVE_INFINITY);
        ok &= ddiv( 1000.0 + Double.MAX_VALUE,  Double.MAX_VALUE,  1.0);
        ok &= ddiv( -0.0,  1.0,  -0.0);
        ok &= ddiv( -0.0,  1.0,  0.0);
        exit(ok);
    }
}