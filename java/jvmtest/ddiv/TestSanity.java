package ddiv;

class TestSanity extends Ddiv {

    public static final double big = 1.7111111111111111111111111111111111111111111111111111e308;
    public static final double small = 1.0e-308;

    public static void main(String[] args) {
        boolean ok = true;
        ok &= ddiv(-0.0,  Double.POSITIVE_INFINITY, -0.0);
        ok &= ddiv(-0.0,  Double.POSITIVE_INFINITY,  0.0);
        ok &= ddiv(-0.0,  Double.NEGATIVE_INFINITY,  0.0);
        ok &= ddiv(-0.0,  Double.NEGATIVE_INFINITY, -0.0);
        ok &= ddiv(-0.0,  1.0,  -0.0);
        ok &= ddiv(-0.0,  1.0,  0.0);
        ok &= ddiv(big,         big, 1.0);
        ok &= ddiv(small,       1.0, small);
        // Overflow
        ok &= ddiv(1000.0 + Double.MAX_VALUE,  Double.MAX_VALUE,  1.0);
        ok &= ddiv(big + small, big, 1.0);
        exit(ok);
    }
}