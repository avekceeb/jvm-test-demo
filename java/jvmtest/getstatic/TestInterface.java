package getstatic;

interface I {
    static int f() { return 876; }
}

class Z implements I {
    // the scope of the static interface method should be within the interface only
    static int f() { return 567; }
}

class TestInterface {
    public static void main(String[] args) {
        assert(876 == I.f());
        assert(567 == Z.f());
    }
}
