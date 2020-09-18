class Foo {

    private volatile int curFlag = 1;
    private final Object mutex = new Object();

    public Foo() {

    }

    public void first(Runnable printFirst) throws InterruptedException {

        synchronized (mutex) {
            while (curFlag != 1)
                mutex.wait();
            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            curFlag += 1;
            mutex.notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {

        synchronized (mutex) {
            while (curFlag != 2)
                mutex.wait();
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            curFlag += 1;
            mutex.notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {

        synchronized (mutex) {
            while (curFlag != 3)
                mutex.wait();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
        }
    }
}