from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "Java"


QUESTIONS = [
    # =========================================================
    # EASY — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between JDK, JRE, and JVM?"
        ),
        "expected_answer": (
            "The JDK (Java Development Kit) is a superset that includes "
            "the JRE plus development tools such as the compiler (javac) "
            "and debugger. The JRE (Java Runtime Environment) provides "
            "the libraries and the JVM needed to run Java applications. "
            "The JVM (Java Virtual Machine) is the component that "
            "actually executes Java bytecode on the host platform."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between == and .equals()?"
        ),
        "expected_answer": (
            "The == operator compares object references, checking whether "
            "two variables point to the same object in memory. The "
            ".equals() method compares the logical content or value of "
            "two objects and can be overridden to define custom equality "
            "semantics."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between ArrayList and LinkedList?"
        ),
        "expected_answer": (
            "ArrayList is backed by a dynamic array, providing O(1) "
            "random access but O(n) insertions and deletions in the "
            "middle. LinkedList is a doubly-linked list that provides "
            "O(1) insertions and deletions at known positions but O(n) "
            "random access. ArrayList is generally preferred unless "
            "frequent insertions or removals at arbitrary positions "
            "are required."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are the four pillars of OOP?"
        ),
        "expected_answer": (
            "The four pillars are encapsulation, which bundles data and "
            "methods and restricts direct access; abstraction, which "
            "hides implementation details and exposes only essential "
            "behavior; inheritance, which allows a class to derive "
            "from another class; and polymorphism, which lets the same "
            "method call behave differently depending on the object's "
            "actual type."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between overloading and overriding?"
        ),
        "expected_answer": (
            "Overloading means defining multiple methods with the same "
            "name but different parameter lists within the same class; "
            "it is resolved at compile time. Overriding means a subclass "
            "provides its own implementation of a method already defined "
            "in its superclass with the same signature; it is resolved "
            "at runtime through dynamic dispatch."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are Java access modifiers?"
        ),
        "expected_answer": (
            "Java has four access levels. public makes a member "
            "accessible everywhere. protected makes it accessible "
            "within the same package and by subclasses. Default "
            "(package-private, no keyword) restricts access to the "
            "same package. private restricts access to the declaring "
            "class only."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between String, StringBuilder, StringBuffer?"
        ),
        "expected_answer": (
            "String is immutable; every modification creates a new "
            "object. StringBuilder is mutable and not thread-safe, "
            "making it the fastest option for single-threaded string "
            "manipulation. StringBuffer is mutable and thread-safe "
            "because its methods are synchronized, but this adds "
            "overhead compared to StringBuilder."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a constructor? Can it be overloaded?"
        ),
        "expected_answer": (
            "A constructor is a special method called when an object "
            "is created to initialize its state. It has the same name "
            "as the class and no return type. Yes, constructors can be "
            "overloaded by defining multiple constructors with different "
            "parameter lists, and one constructor can call another using "
            "this()."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the static keyword used for?"
        ),
        "expected_answer": (
            "The static keyword makes a member belong to the class "
            "rather than to any particular instance. Static fields are "
            "shared across all instances, static methods can be called "
            "without creating an object, and static blocks run once "
            "when the class is loaded."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between an array and an ArrayList?"
        ),
        "expected_answer": (
            "An array has a fixed size set at creation and can hold "
            "both primitives and objects. An ArrayList is a resizable "
            "collection from the Collections Framework that can only "
            "hold objects (primitives are autoboxed). ArrayList provides "
            "convenience methods like add, remove, and contains that "
            "arrays do not have."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is exception handling, and why is it needed?"
        ),
        "expected_answer": (
            "Exception handling is a mechanism to detect and respond "
            "to runtime errors so the program can recover or fail "
            "gracefully instead of crashing. Java uses try, catch, "
            "finally, throw, and throws to manage exceptions and "
            "separate error-handling logic from normal control flow."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the final keyword and its three uses "
            "(variable, method, class)?"
        ),
        "expected_answer": (
            "A final variable cannot be reassigned once initialized, "
            "making it effectively a constant. A final method cannot "
            "be overridden by subclasses. A final class cannot be "
            "extended at all, which is useful for security or design "
            "reasons, as seen with the String class."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a package in Java?"
        ),
        "expected_answer": (
            "A package is a namespace that groups related classes and "
            "interfaces, helping to avoid naming conflicts and organize "
            "code logically. Packages also provide access control, since "
            "default (package-private) members are only accessible within "
            "the same package."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between break and continue?"
        ),
        "expected_answer": (
            "break immediately exits the enclosing loop or switch "
            "statement entirely. continue skips the rest of the current "
            "iteration and jumps to the next iteration of the loop. "
            "Both can be used with labels to target outer loops in "
            "nested structures."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is type casting in Java (implicit vs explicit)?"
        ),
        "expected_answer": (
            "Implicit casting (widening) happens automatically when "
            "converting a smaller type to a larger type, such as int "
            "to long, with no data loss. Explicit casting (narrowing) "
            "requires the programmer to specify the target type in "
            "parentheses, such as (int) from a double, and may result "
            "in data loss or overflow."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the this keyword used for?"
        ),
        "expected_answer": (
            "The this keyword refers to the current object instance. "
            "It is used to disambiguate between instance variables and "
            "parameters with the same name, to call other constructors "
            "in the same class via this(), and to pass the current "
            "object as an argument to another method."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a wrapper class? Give examples."
        ),
        "expected_answer": (
            "A wrapper class wraps a primitive type into an object so "
            "it can be used where objects are required, such as in "
            "collections. Examples include Integer for int, Double for "
            "double, Character for char, and Boolean for boolean. Java "
            "performs autoboxing and unboxing to convert between "
            "primitives and their wrappers automatically."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between throw and throws?"
        ),
        "expected_answer": (
            "throw is used inside a method body to explicitly raise "
            "an exception object. throws is used in a method signature "
            "to declare that the method may propagate one or more "
            "checked exceptions to its caller, requiring the caller "
            "to handle or further declare them."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a Java interface?"
        ),
        "expected_answer": (
            "An interface is a reference type that defines a contract "
            "of abstract methods that implementing classes must provide. "
            "Since Java 8, interfaces can also contain default methods "
            "with implementations and static methods. A class can "
            "implement multiple interfaces, enabling a form of multiple "
            "inheritance of behavior."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the entry point of a Java program "
            "(main method signature)?"
        ),
        "expected_answer": (
            "The entry point is public static void main(String[] args). "
            "It must be public so the JVM can access it, static so it "
            "can be called without creating an instance, void because "
            "it does not return a value, and it accepts a String array "
            "for command-line arguments."
        ),
    },

    # =========================================================
    # MEDIUM — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How does HashMap work internally?"
        ),
        "expected_answer": (
            "HashMap stores key-value pairs in an array of buckets. "
            "The key's hashCode() determines the bucket index. When "
            "multiple keys hash to the same bucket (collision), they "
            "are stored in a linked list, which converts to a balanced "
            "tree (red-black tree) when the list exceeds a threshold "
            "(default 8) in Java 8+. On a get or put, the key's hash "
            "is computed, the correct bucket is located, and equals() "
            "is used to find the exact entry."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Difference between abstract class and interface "
            "-- when to use which?"
        ),
        "expected_answer": (
            "An abstract class can have constructors, instance fields, "
            "and a mix of abstract and concrete methods, but a class "
            "can only extend one. An interface defines a contract and "
            "supports multiple inheritance of type. Use an abstract "
            "class when you need shared state or partial implementation "
            "across related classes. Use an interface when unrelated "
            "classes need to share a capability or when you need "
            "multiple inheritance."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Checked vs. unchecked exceptions with examples?"
        ),
        "expected_answer": (
            "Checked exceptions extend Exception (but not "
            "RuntimeException) and must be caught or declared in the "
            "method signature; examples include IOException and "
            "SQLException. Unchecked exceptions extend RuntimeException "
            "and do not require explicit handling; examples include "
            "NullPointerException and ArrayIndexOutOfBoundsException. "
            "Checked exceptions represent recoverable conditions, "
            "while unchecked exceptions usually indicate programming "
            "errors."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How does Java garbage collection decide what to collect?"
        ),
        "expected_answer": (
            "The garbage collector identifies objects that are no longer "
            "reachable from any GC root (such as static fields, local "
            "variables on active threads, and JNI references). "
            "Unreachable objects are eligible for collection. Modern "
            "collectors use a generational approach, dividing the heap "
            "into young and old generations so that short-lived objects "
            "can be collected quickly and cheaply."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "volatile vs synchronized -- what's the difference?"
        ),
        "expected_answer": (
            "volatile guarantees visibility: reads and writes to a "
            "volatile variable are always done from main memory, so "
            "all threads see the latest value. However, it does not "
            "provide atomicity for compound operations. synchronized "
            "provides both visibility and mutual exclusion, ensuring "
            "that only one thread executes a synchronized block at a "
            "time. Use volatile for simple flags and synchronized for "
            "compound operations that need atomicity."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the try-with-resources statement."
        ),
        "expected_answer": (
            "try-with-resources, introduced in Java 7, automatically "
            "closes resources that implement AutoCloseable when the "
            "try block exits, whether normally or via an exception. "
            "This eliminates the need for explicit finally blocks for "
            "resource cleanup and helps prevent resource leaks. "
            "Multiple resources can be declared in a single statement, "
            "and suppressed exceptions are tracked automatically."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are functional interfaces and lambda expressions?"
        ),
        "expected_answer": (
            "A functional interface is an interface with exactly one "
            "abstract method, such as Runnable, Callable, or Comparator. "
            "A lambda expression is a concise anonymous function that "
            "can be used wherever a functional interface is expected. "
            "The @FunctionalInterface annotation is optional but helps "
            "the compiler enforce the single-abstract-method constraint."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the Java Collections Framework hierarchy."
        ),
        "expected_answer": (
            "The framework is rooted in the Iterable and Collection "
            "interfaces. Collection has three main sub-interfaces: "
            "List (ordered, allows duplicates, e.g. ArrayList, "
            "LinkedList), Set (no duplicates, e.g. HashSet, TreeSet), "
            "and Queue (FIFO or priority-based, e.g. PriorityQueue, "
            "ArrayDeque). Map is a separate hierarchy (e.g. HashMap, "
            "TreeMap) that stores key-value pairs and does not extend "
            "Collection."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between HashMap, "
            "LinkedHashMap, and TreeMap?"
        ),
        "expected_answer": (
            "HashMap provides O(1) average-case get/put but does not "
            "guarantee any iteration order. LinkedHashMap maintains "
            "insertion order (or optionally access order) while "
            "preserving HashMap's O(1) performance. TreeMap keeps "
            "entries sorted by key using a red-black tree, providing "
            "O(log n) operations and supporting range queries via the "
            "NavigableMap interface."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between Comparable and Comparator?"
        ),
        "expected_answer": (
            "Comparable is implemented by the class itself and defines "
            "a single natural ordering via compareTo(). Comparator is "
            "a separate object that defines an external ordering via "
            "compare(), allowing multiple different sort orders without "
            "modifying the original class. Comparator is often used as "
            "a lambda or anonymous class passed to sort methods."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain method overriding rules with respect to "
            "access modifiers and exceptions."
        ),
        "expected_answer": (
            "An overriding method must have the same name and parameter "
            "list as the superclass method. Its access modifier must be "
            "the same or less restrictive (e.g. protected can become "
            "public but not private). It cannot throw broader checked "
            "exceptions than the overridden method declares, though it "
            "may throw fewer or narrower checked exceptions and any "
            "unchecked exceptions."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a deadlock in Java multithreading, "
            "and how do you avoid it?"
        ),
        "expected_answer": (
            "A deadlock occurs when two or more threads each hold a "
            "lock the other needs, so none can proceed. Common "
            "avoidance strategies include always acquiring locks in a "
            "consistent global order, using tryLock with timeouts from "
            "java.util.concurrent.locks, reducing lock scope, and "
            "preferring higher-level concurrency utilities over raw "
            "synchronized blocks."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between Runnable and Callable?"
        ),
        "expected_answer": (
            "Runnable's run() method returns void and cannot throw "
            "checked exceptions. Callable's call() method returns a "
            "result of a parameterized type and can throw checked "
            "exceptions. Callable is typically submitted to an "
            "ExecutorService, which returns a Future that can be used "
            "to retrieve the result or handle exceptions."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the Java equals() and hashCode() contract."
        ),
        "expected_answer": (
            "If two objects are equal according to equals(), they must "
            "return the same hashCode(). If hashCode() values differ, "
            "the objects must not be equal. Violating this contract "
            "breaks hash-based collections like HashMap and HashSet, "
            "because objects may be placed in the wrong bucket and "
            "become unretrievable."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between fail-fast and "
            "fail-safe iterators?"
        ),
        "expected_answer": (
            "Fail-fast iterators (e.g. those from ArrayList, HashMap) "
            "throw ConcurrentModificationException if the collection "
            "is structurally modified during iteration. Fail-safe "
            "iterators (e.g. those from ConcurrentHashMap, "
            "CopyOnWriteArrayList) work on a snapshot or allow "
            "concurrent modification without throwing an exception, "
            "though they may not reflect the very latest changes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are Java Streams, and how do map() "
            "and filter() work?"
        ),
        "expected_answer": (
            "Streams provide a functional-style pipeline for processing "
            "sequences of elements. filter() takes a predicate and "
            "returns a stream containing only elements that match. "
            "map() takes a function and returns a stream where each "
            "element has been transformed. Both are intermediate "
            "operations that are lazy and only execute when a terminal "
            "operation (e.g. collect, forEach) is invoked."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the Singleton design pattern and its "
            "thread-safe implementation."
        ),
        "expected_answer": (
            "Singleton ensures a class has only one instance and "
            "provides a global access point to it. A simple lazy "
            "implementation is not thread-safe. Thread-safe approaches "
            "include eager initialization, double-checked locking with "
            "a volatile field, a static inner holder class that "
            "leverages class-loading guarantees, or using an enum with "
            "a single constant."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is dependency injection, and how does Spring use it?"
        ),
        "expected_answer": (
            "Dependency injection is a design pattern where an object's "
            "dependencies are supplied externally rather than created "
            "internally, promoting loose coupling and testability. "
            "Spring's IoC container manages beans and injects "
            "dependencies via constructor injection, setter injection, "
            "or field injection using annotations like @Autowired, "
            "@Component, and @Service."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between ExecutorService "
            "and creating raw Thread objects?"
        ),
        "expected_answer": (
            "Creating raw Thread objects for every task is expensive "
            "because each thread consumes OS resources and must be "
            "managed manually. ExecutorService manages a thread pool, "
            "reuses threads, and provides features like task submission "
            "via submit/invokeAll, Future-based result retrieval, and "
            "graceful shutdown, leading to more efficient and "
            "maintainable concurrent code."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain autoboxing and unboxing with a pitfall example."
        ),
        "expected_answer": (
            "Autoboxing is the automatic conversion of a primitive to "
            "its wrapper class (e.g. int to Integer), and unboxing is "
            "the reverse. A common pitfall is unboxing a null wrapper: "
            "for example, an Integer variable set to null will throw a "
            "NullPointerException when unboxed to int. Another pitfall "
            "is using == to compare Integer objects outside the cached "
            "range (-128 to 127), where two equal values may not be "
            "reference-equal."
        ),
    },

    # =========================================================
    # HARD — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the Java Memory Model and visibility "
            "guarantees across threads."
        ),
        "expected_answer": (
            "The Java Memory Model (JMM) defines how threads interact "
            "through memory and what behaviors are allowed by the "
            "compiler, JIT, and hardware. It specifies happens-before "
            "relationships that guarantee visibility: for example, an "
            "unlock on a monitor happens-before a subsequent lock on "
            "the same monitor, a write to a volatile field happens-before "
            "a subsequent read of that field, and thread start/join "
            "establish ordering. Without these relationships, threads "
            "may see stale or reordered values due to CPU caches and "
            "instruction reordering."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does ConcurrentHashMap achieve thread safety "
            "internally?"
        ),
        "expected_answer": (
            "In Java 8+, ConcurrentHashMap uses a combination of CAS "
            "(compare-and-swap) operations and fine-grained synchronized "
            "blocks on individual bins (buckets) rather than locking "
            "the entire map. Reads are typically lock-free. When a bin "
            "is being modified, only that bin is locked. The internal "
            "structure uses an array of nodes that can grow into "
            "linked lists or red-black trees for collision handling, "
            "similar to HashMap but with per-bin synchronization."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain JVM class loading and the parent "
            "delegation model."
        ),
        "expected_answer": (
            "When a class is needed, the JVM delegates loading to the "
            "classloader hierarchy. The bootstrap classloader loads "
            "core Java classes, the platform (extension) classloader "
            "loads platform-specific classes, and the application "
            "classloader loads user classes from the classpath. Each "
            "classloader first delegates to its parent before "
            "attempting to load the class itself. This parent-delegation "
            "model prevents duplicate class definitions and ensures "
            "core classes cannot be overridden by user code."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Difference between CompletableFuture and Future, "
            "with chaining examples."
        ),
        "expected_answer": (
            "Future represents the result of an asynchronous computation "
            "but only supports blocking retrieval via get(). "
            "CompletableFuture extends Future with a rich fluent API "
            "for non-blocking composition: thenApply for transforming "
            "results, thenCompose for chaining dependent async stages, "
            "thenCombine for combining two independent futures, and "
            "exceptionally or handle for error recovery. This enables "
            "building complex async pipelines without blocking threads."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does JIT compilation work, and how does it differ "
            "from interpretation?"
        ),
        "expected_answer": (
            "The JVM initially interprets bytecode instruction by "
            "instruction. The JIT (Just-In-Time) compiler identifies "
            "hot methods that are called frequently and compiles them "
            "to optimized native machine code at runtime. JIT applies "
            "optimizations like inlining, loop unrolling, and dead-code "
            "elimination that an ahead-of-time compiler cannot do as "
            "effectively because the JIT has runtime profiling data. "
            "The result is near-native performance for hot paths while "
            "keeping the portability of bytecode."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Design a thread-safe Singleton without using "
            "synchronized on every call."
        ),
        "expected_answer": (
            "One approach is the initialization-on-demand holder idiom: "
            "a private static inner class holds the singleton instance. "
            "The JVM guarantees thread-safe, lazy class initialization, "
            "so the instance is created only when the holder class is "
            "first accessed, without explicit synchronization. Another "
            "approach is double-checked locking with a volatile field, "
            "where the synchronized block is entered only when the "
            "instance is null. The enum singleton approach also works "
            "because the JVM guarantees enum instances are created "
            "exactly once."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the internal working of the String pool "
            "and intern()."
        ),
        "expected_answer": (
            "The String pool is a special area in the heap (moved from "
            "PermGen to the main heap in Java 7) that stores unique "
            "String literals. When a literal like \"hello\" appears in "
            "code, the JVM checks the pool and reuses an existing "
            "instance if one matches. intern() explicitly adds a String "
            "to the pool or returns the existing pooled reference. This "
            "saves memory when many identical strings exist but can "
            "cause overhead if used excessively because the pool is "
            "backed by a hash table that must be searched."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you detect and fix a memory leak "
            "in a Java application?"
        ),
        "expected_answer": (
            "Detection starts with monitoring heap usage via JVM flags, "
            "JMX, or tools like VisualVM and JConsole. If the old "
            "generation keeps growing, a heap dump can be taken using "
            "jmap or -XX:+HeapDumpOnOutOfMemoryError and analyzed with "
            "Eclipse MAT or similar tools to find retained object trees. "
            "Common causes include static collections that accumulate "
            "entries, listeners or callbacks never deregistered, "
            "unclosed resources, and classloader leaks. Fixes involve "
            "removing stale references, using weak references where "
            "appropriate, and ensuring proper resource cleanup."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the differences between G1, CMS, and "
            "ZGC garbage collectors."
        ),
        "expected_answer": (
            "CMS (Concurrent Mark-Sweep) minimizes pause times by "
            "performing most marking concurrently but suffers from "
            "fragmentation and is deprecated since Java 9. G1 "
            "(Garbage-First) divides the heap into regions, collects "
            "regions with the most garbage first, and compacts "
            "incrementally, targeting configurable pause-time goals. "
            "ZGC is a low-latency collector that performs almost all "
            "work concurrently using colored pointers and load barriers, "
            "keeping pause times under a few milliseconds regardless "
            "of heap size. G1 is the default in modern JDKs; ZGC is "
            "preferred when sub-millisecond pauses are critical."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does the ForkJoinPool and work-stealing "
            "algorithm work?"
        ),
        "expected_answer": (
            "ForkJoinPool is designed for recursive divide-and-conquer "
            "tasks. A task forks (splits) into subtasks that are pushed "
            "onto the submitting thread's deque. Each worker thread "
            "processes its own deque in LIFO order for cache locality. "
            "When a worker's deque is empty, it steals tasks from "
            "another worker's deque in FIFO order. This work-stealing "
            "approach balances load dynamically without centralized "
            "scheduling. The common ForkJoinPool also backs parallel "
            "streams."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how Spring Boot's auto-configuration "
            "works under the hood."
        ),
        "expected_answer": (
            "Spring Boot uses @EnableAutoConfiguration (via "
            "@SpringBootApplication) which triggers the loading of "
            "auto-configuration classes listed in "
            "META-INF/spring/org.springframework.boot.autoconfigure."
            "AutoConfiguration.imports (or spring.factories in older "
            "versions). Each auto-configuration class uses conditional "
            "annotations like @ConditionalOnClass, @ConditionalOnBean, "
            "and @ConditionalOnProperty to decide whether to create "
            "beans. This allows Spring Boot to configure sensible "
            "defaults based on what is on the classpath while still "
            "letting the developer override any bean."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design a rate limiter using Java "
            "concurrency utilities?"
        ),
        "expected_answer": (
            "A token-bucket approach works well: maintain a counter "
            "of available tokens protected by a ReentrantLock or "
            "AtomicInteger. A scheduled thread or ScheduledExecutorService "
            "replenishes tokens at a fixed rate. Each request attempts "
            "to acquire a token; if none are available, the request is "
            "rejected or queued. For distributed scenarios, the token "
            "state would be stored in an external store like Redis. "
            "Alternatively, a sliding-window counter using "
            "ConcurrentHashMap with timestamp keys can track request "
            "counts per window."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the difference between heap and off-heap memory, "
            "and when you'd use ByteBuffer.allocateDirect."
        ),
        "expected_answer": (
            "Heap memory is managed by the JVM garbage collector and "
            "is where most Java objects live. Off-heap (direct) memory "
            "is allocated outside the JVM heap via the OS and is not "
            "subject to GC pauses. ByteBuffer.allocateDirect creates "
            "an off-heap buffer that avoids the overhead of copying "
            "data between the Java heap and native I/O buffers, making "
            "it faster for large or long-lived I/O operations like "
            "network and file channel transfers. The trade-off is that "
            "allocation and deallocation of direct buffers are slower "
            "than heap buffers, and memory leaks are possible if "
            "buffers are not released."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does synchronized interact with the JVM's "
            "monitor lock and object header?"
        ),
        "expected_answer": (
            "Every Java object has a header that includes a mark word "
            "used for locking. When a thread enters a synchronized "
            "block, the JVM attempts biased locking (one thread uses "
            "the lock repeatedly with near-zero overhead). If contention "
            "occurs, it escalates to a thin (lightweight) lock using "
            "CAS on the mark word. Under heavy contention, it inflates "
            "to a heavyweight monitor backed by an OS mutex. The "
            "monitor tracks the owning thread, an entry count for "
            "reentrancy, and a wait set for threads that called wait()."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how you'd design an LRU cache in Java "
            "from scratch."
        ),
        "expected_answer": (
            "An LRU cache combines a HashMap for O(1) key lookup with "
            "a doubly-linked list for O(1) recency tracking. On a get "
            "or put, the accessed node is moved to the head of the "
            "list. When the cache exceeds capacity, the tail node "
            "(least recently used) is evicted and removed from the map. "
            "Java's LinkedHashMap with accessOrder=true and an "
            "overridden removeEldestEntry provides a simpler built-in "
            "alternative. For thread safety, wrap operations in a "
            "ReentrantLock or use a ConcurrentHashMap-based approach."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is a ClassLoader leak, and how does it "
            "happen in application servers?"
        ),
        "expected_answer": (
            "A ClassLoader leak occurs when a classloader and all the "
            "classes it loaded cannot be garbage collected because "
            "something outside the classloader still holds a strong "
            "reference to an object from one of those classes. In "
            "application servers, redeploying a web application creates "
            "a new classloader, but if the old one is retained via "
            "static fields, thread-local variables, JDBC drivers "
            "registered with DriverManager, or shutdown hooks, the "
            "entire set of loaded classes and their static data remain "
            "in memory, causing PermGen or metaspace exhaustion."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the differences between pessimistic and "
            "optimistic locking in a Java-based service."
        ),
        "expected_answer": (
            "Pessimistic locking acquires a database or application "
            "lock before reading data, preventing other transactions "
            "from modifying it until the lock is released (e.g. SELECT "
            "FOR UPDATE). Optimistic locking does not lock the row; "
            "instead, it reads a version or timestamp and checks it at "
            "update time. If the version has changed, the update fails "
            "and the application retries. Optimistic locking offers "
            "better throughput under low contention, while pessimistic "
            "locking is safer under high contention but can cause "
            "blocking and deadlocks."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How do you handle backpressure in reactive Java "
            "(Project Reactor / RxJava)?"
        ),
        "expected_answer": (
            "Backpressure is the mechanism by which a slow consumer "
            "signals a fast producer to limit the rate of emission. "
            "In Project Reactor, Flux implements the Reactive Streams "
            "Subscription interface where the subscriber requests a "
            "specific number of items. Strategies for handling excess "
            "items include onBackpressureBuffer (buffer until consumed), "
            "onBackpressureDrop (discard excess), and "
            "onBackpressureLatest (keep only the most recent). Choosing "
            "the right strategy depends on whether data loss is "
            "acceptable and on memory constraints."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how Java's Optional should (and shouldn't) "
            "be used in API design."
        ),
        "expected_answer": (
            "Optional should be used as a return type to explicitly "
            "signal that a method may not produce a result, replacing "
            "null returns and reducing NullPointerException risk. It "
            "should not be used as a method parameter, a field type, "
            "or in collections, because it adds unnecessary wrapping "
            "and is not serializable. Prefer methods like map, "
            "flatMap, orElse, and orElseThrow over calling get() "
            "directly, which defeats the purpose of using Optional."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Design a thread pool from scratch and explain "
            "queueing/rejection policies."
        ),
        "expected_answer": (
            "A custom thread pool maintains a fixed set of worker "
            "threads that pull tasks from a shared BlockingQueue. When "
            "a task is submitted, it is enqueued; if the queue is full "
            "and all threads are busy, a rejection policy kicks in. "
            "Common policies include AbortPolicy (throw an exception), "
            "CallerRunsPolicy (execute the task in the submitter's "
            "thread), DiscardPolicy (silently drop the task), and "
            "DiscardOldestPolicy (drop the oldest queued task). Workers "
            "loop, taking tasks from the queue and executing them, and "
            "should handle interruption for graceful shutdown."
        ),
    },
]


def seed_java_questions() -> None:
    db = SessionLocal()

    try:
        topic = (
            db.query(Topic)
            .filter(Topic.name == TOPIC_NAME)
            .first()
        )

        if not topic:
            topic = Topic(
                name=TOPIC_NAME,
                description=(
                    "Java programming language interview "
                    "questions covering fundamentals, "
                    "intermediate concepts, and advanced topics."
                ),
                is_active=True,
            )

            db.add(topic)
            db.commit()
            db.refresh(topic)

            print(
                f"Created topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        else:
            print(
                f"Using existing topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        existing_count = (
            db.query(Question)
            .filter(Question.topic_id == topic.id)
            .count()
        )

        if existing_count >= len(QUESTIONS):
            print(
                f"Java topic already contains "
                f"{existing_count} question(s)."
            )
            print(
                "No questions were inserted to avoid duplicates."
            )
            return

        questions = [
            Question(
                topic_id=topic.id,
                difficulty=item["difficulty"],
                question_text=item["question_text"],
                expected_answer=item["expected_answer"],
            )
            for item in QUESTIONS
        ]

        db.add_all(questions)
        db.commit()

        print()
        print("=" * 60)
        print("JAVA INTERVIEW QUESTION BANK CREATED")
        print("=" * 60)
        print(f"Topic ID       : {topic.id}")
        print(f"Topic          : {topic.name}")
        print(f"Total questions: {len(questions)}")
        print(
            "Easy           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.EASY)}"
        )
        print(
            "Medium         : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.MEDIUM)}"
        )
        print(
            "Hard           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.HARD)}"
        )
        print("=" * 60)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_java_questions()
