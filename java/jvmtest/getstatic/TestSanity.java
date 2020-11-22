package getstatic;

class X {
    public static int x = 123;
    public static int[] a = {33, 44};
    public static Object noninit;
    public static Object obj = new Object();
    public static int f() { return 456; }
}

class Y extends X { }

class TestSanity {
    public static void main(String[] args) {
        boolean ok;
        // simple
        ok =  (123 == X.x);
        ok &= (33 == X.a[0]);
        ok &= (456 == X.f());
        ok &= (null == X.noninit);
        ok &= (null != X.obj);
        // inherited
        ok &= (123 == Y.x);
        ok &= (33 == Y.a[0]);
        ok &= (456 == Y.f());
        ok &= (null == Y.noninit);
        ok &= (null != Y.obj);
        System.exit(ok ? 0:1);
    }
}