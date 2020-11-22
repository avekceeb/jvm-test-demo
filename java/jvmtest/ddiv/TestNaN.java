package ddiv;

class TestNaN extends Ddiv {
    public static void main(String[] args) {
        boolean ok = true;
        ok &= ddiv( Double.NaN, 3.14,       Double.NaN);
        ok &= ddiv( 3.14,       Double.NaN, Double.NaN);
        ok &= ddiv( Double.NaN, Double.NaN, Double.NaN);
        exit(ok);
    }
}