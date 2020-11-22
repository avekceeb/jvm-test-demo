package getstatic;

class TestBigConstantPool {
    public static void main(String[] args) {
        boolean ok = (300 == Bulk.dummy300);
        System.exit(ok ? 0:1);
    }
}