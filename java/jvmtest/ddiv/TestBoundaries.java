package ddiv;

class TestBoundaries extends Ddiv {
    public static void main(String[] args) {
        boolean ok = true;
        ok &= ddiv( Double.MAX_VALUE,  Double.MAX_VALUE,  1.0);
        ok &= ddiv( Double.MAX_VALUE, -Double.MAX_VALUE, -1.0);
        ok &= ddiv(-Double.MAX_VALUE,  Double.MAX_VALUE, -1.0);
        ok &= ddiv(-Double.MAX_VALUE, -Double.MAX_VALUE,  1.0);
        ok &= ddiv( Double.MIN_VALUE,  Double.MIN_VALUE,  1.0);
        ok &= ddiv(-Double.MIN_VALUE,  Double.MIN_VALUE, -1.0);
        ok &= ddiv( Double.MIN_VALUE, -Double.MIN_VALUE, -1.0);
        ok &= ddiv(-Double.MIN_VALUE, -Double.MIN_VALUE,  1.0);
        exit(ok);
    }
}