package getstatic;


class Bad {
    private static boolean disaster = ((String) null).endsWith("x");
    public static boolean x;
    public static boolean f() { return false; }
}


class TestExceptionInInit {
    public static void main(String[] args) {
        boolean ok = false;
        // Check NPE changed to Init error in getstatic
        // https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-5.html#jvms-5.5
        // Getting field:
        try {
            ok = Bad.x;
        } catch (ExceptionInInitializerError e) {
            ok = true;
        } finally {
            if (!ok) {
                System.out.println("No exception during getting static field");
                System.exit(1);
            }
        }
        ok = false;
        // Getting method:
        try {
            ok = Bad.f();
        } catch (ExceptionInInitializerError e) {
            ok = true;
        } catch (NoClassDefFoundError e) {
            // see JSE Spec 5.5.5:
            // If the Class object for C is in an erroneous state, then initialization is not possible.
            // Release LC and throw a NoClassDefFoundError.
            ok = true;
        } finally {
            if (!ok) {
                System.out.println("No exception during getting static method");
                System.exit(2);
            }
        }
    }
}