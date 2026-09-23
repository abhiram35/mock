from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "Python"


QUESTIONS = [
    # =========================================================
    # EASY — 10 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is Python, and what are its key features?"
        ),
        "expected_answer": (
            "Python is a high-level, interpreted, general-purpose "
            "programming language. Key features include dynamic typing, "
            "being interpreted rather than compiled ahead of time, support "
            "for procedural, object-oriented, and functional programming, "
            "automatic memory management through garbage collection, and "
            "a large standard library."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a list and a tuple?"
        ),
        "expected_answer": (
            "A list is mutable and is defined using square brackets. "
            "A tuple is immutable and is defined using parentheses. "
            "Tuples are generally faster and use less memory, and a tuple "
            "can be used as a dictionary key if all its elements are "
            "hashable, whereas a list cannot."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are Python's built-in data types?"
        ),
        "expected_answer": (
            "Python's built-in data types include numeric types such as "
            "int, float, and complex; sequence types such as str, list, "
            "tuple, and range; mapping type dict; set types set and "
            "frozenset; boolean bool; and NoneType."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between == and is?"
        ),
        "expected_answer": (
            "The == operator checks value equality, meaning whether two "
            "objects contain the same data. The is operator checks identity "
            "equality, meaning whether two references point to the same "
            "object in memory."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is indentation and why does Python rely on it?"
        ),
        "expected_answer": (
            "Python uses whitespace indentation instead of braces to define "
            "code blocks such as loops, functions, and conditionals. "
            "Indentation is part of Python's syntax and enforces readable "
            "and consistently formatted code."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a variable in Python, and how is it different "
            "from variables in statically typed languages?"
        ),
        "expected_answer": (
            "A Python variable is a name bound to an object and does not "
            "have a fixed type declared upfront. The type belongs to the "
            "object rather than the variable name, so the same variable "
            "can be rebound to objects of different types."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are mutable and immutable objects? Give examples."
        ),
        "expected_answer": (
            "Mutable objects can be changed after creation, such as lists, "
            "dictionaries, and sets. Immutable objects cannot be changed "
            "after creation, such as integers, floats, strings, tuples, "
            "and frozensets. Modifying an immutable object creates a new "
            "object."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between str and repr?"
        ),
        "expected_answer": (
            "str() returns a human-readable informal string representation "
            "intended mainly for end users. repr() returns an unambiguous "
            "formal representation intended mainly for developers and "
            "debugging, ideally one that can recreate the object."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are Python namespaces?"
        ),
        "expected_answer": (
            "A namespace is a mapping from names to objects used to avoid "
            "naming conflicts. Python has built-in, global, and local "
            "namespaces, organized through the LEGB lookup rule: Local, "
            "Enclosing, Global, and Built-in."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is PEP 8?"
        ),
        "expected_answer": (
            "PEP 8 is Python's official style guide. It covers naming "
            "conventions, indentation, line length, formatting, and other "
            "coding practices that help keep Python code consistent and "
            "readable."
        ),
    },


    # =========================================================
    # MEDIUM — 14 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between deep copy and shallow copy?"
        ),
        "expected_answer": (
            "A shallow copy creates a new outer object but keeps references "
            "to the same nested objects as the original. A deep copy "
            "recursively copies nested objects, making the copied structure "
            "independent of the original. Python provides copy.copy() for "
            "shallow copying and copy.deepcopy() for deep copying."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are *args and **kwargs?"
        ),
        "expected_answer": (
            "*args collects extra positional arguments into a tuple, while "
            "**kwargs collects extra keyword arguments into a dictionary. "
            "They allow functions to accept a variable number of arguments."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a decorator in Python?"
        ),
        "expected_answer": (
            "A decorator is a function that takes another function or class "
            "as input and extends or modifies its behavior without permanently "
            "changing its source code. Decorators are commonly applied using "
            "the @decorator_name syntax and rely on Python functions being "
            "first-class objects."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between a generator and a normal function?"
        ),
        "expected_answer": (
            "A normal function uses return to produce a value and then exits. "
            "A generator function uses yield to produce values lazily, "
            "pausing its execution state between calls. It returns a "
            "generator object that can be iterated without storing the entire "
            "sequence in memory."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between an iterator and an iterable?"
        ),
        "expected_answer": (
            "An iterable is an object capable of returning its members one "
            "at a time and typically implements __iter__. An iterator is an "
            "object with a __next__ method that produces the next value and "
            "raises StopIteration when exhausted. An iterator can be obtained "
            "from an iterable using iter()."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is list comprehension, and why is it preferred over loops?"
        ),
        "expected_answer": (
            "List comprehension is concise syntax for creating lists using "
            "an expression, an iterable, and optionally a condition. It is "
            "generally faster than an equivalent simple for loop and is more "
            "readable for straightforward transformations and filtering."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the Global Interpreter Lock (GIL)?"
        ),
        "expected_answer": (
            "The GIL is a mutex in CPython that allows only one thread to "
            "execute Python bytecode at a time. It simplifies memory "
            "management but limits true parallelism for CPU-bound "
            "multithreaded programs. Multiprocessing is generally better "
            "for CPU-bound work, while threading can still help with "
            "I/O-bound work."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between @staticmethod, "
            "@classmethod, and an instance method?"
        ),
        "expected_answer": (
            "An instance method takes self and operates on a particular "
            "object instance. A class method takes cls and operates on the "
            "class itself, allowing access to class state. A static method "
            "takes neither self nor cls and behaves like a regular function "
            "logically grouped inside the class namespace."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is exception handling, and how is it done in Python?"
        ),
        "expected_answer": (
            "Exception handling manages runtime errors using try and except "
            "blocks. Python also provides else, which runs when no exception "
            "occurs, and finally, which runs regardless of whether an "
            "exception occurs and is commonly used for cleanup. Custom "
            "exceptions can be created by subclassing Exception."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a context manager, and what does the with statement do?"
        ),
        "expected_answer": (
            "A context manager manages the setup and teardown of resources "
            "such as files and locks. It commonly implements __enter__ and "
            "__exit__. The with statement automatically calls the cleanup "
            "logic even when an exception occurs."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between __init__ and __new__?"
        ),
        "expected_answer": (
            "__new__ is called first and is responsible for creating and "
            "returning a new instance. __init__ is called afterward to "
            "initialize the already-created instance. Overriding __new__ "
            "is relatively uncommon and is mainly useful for immutable "
            "types or patterns such as singletons."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is monkey patching?"
        ),
        "expected_answer": (
            "Monkey patching is dynamically modifying or extending a class "
            "or module at runtime, such as replacing a method without "
            "changing the original source code. It can be powerful but may "
            "make software harder to understand, debug, and maintain."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain Python's memory management model."
        ),
        "expected_answer": (
            "Python manages memory using a private heap where objects are "
            "allocated. Reference counting is the primary mechanism for "
            "tracking object lifetimes, and objects are normally deallocated "
            "when their reference count reaches zero. A cyclic garbage "
            "collector supplements reference counting by detecting and "
            "cleaning reference cycles."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are Python's magic or dunder methods? Give examples."
        ),
        "expected_answer": (
            "Magic or dunder methods are special methods surrounded by "
            "double underscores that allow objects to integrate with "
            "Python's built-in syntax and operations. Examples include "
            "__init__, __str__, __repr__, __len__, __eq__, and __add__."
        ),
    },


    # =========================================================
    # HARD — 11 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the difference between multithreading, "
            "multiprocessing, and asyncio in Python?"
        ),
        "expected_answer": (
            "Multithreading uses multiple threads sharing memory and is "
            "effective for I/O-bound work but is limited by the GIL for "
            "CPU-bound Python bytecode. Multiprocessing uses separate "
            "processes with separate interpreters and memory spaces, "
            "bypassing the GIL and making it suitable for CPU-bound "
            "parallelism, but with higher memory and communication costs. "
            "asyncio provides single-threaded cooperative concurrency using "
            "an event loop and async/await, making it efficient for high "
            "volumes of I/O-bound work when the code supports non-blocking "
            "operations."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the Method Resolution Order (MRO) and how Python "
            "resolves multiple inheritance."
        ),
        "expected_answer": (
            "MRO defines the order in which Python searches base classes "
            "when looking for methods or attributes. Python uses the C3 "
            "linearization algorithm to create a consistent and monotonic "
            "order even with complex multiple inheritance and diamond "
            "structures. The MRO can be inspected using ClassName.__mro__ "
            "or ClassName.mro()."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What are metaclasses in Python?"
        ),
        "expected_answer": (
            "A metaclass is the class of a class. It defines how classes "
            "themselves are constructed, just as normal classes define how "
            "their instances are constructed. By default, Python classes "
            "are instances of type. Custom metaclasses can control class "
            "creation, enforce rules, or implement patterns such as "
            "automatic registration."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What are descriptors, and how do property, staticmethod, "
            "and classmethod relate to them?"
        ),
        "expected_answer": (
            "A descriptor is an object implementing one or more of "
            "__get__, __set__, or __delete__, allowing it to customize "
            "attribute access. property, staticmethod, and classmethod "
            "use the descriptor protocol internally. Descriptors are used "
            "for attribute access, validation, computed properties, and "
            "other low-level behavior."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the difference between is, ==, and hash() in the "
            "context of custom objects, and how do __eq__ and __hash__ interact?"
        ),
        "expected_answer": (
            "is compares object identity, while == performs value "
            "comparison and can call a custom __eq__ implementation. "
            "Objects used as dictionary keys or set elements must be "
            "hashable. If two objects are considered equal by __eq__, "
            "they must have the same hash value. If __eq__ is overridden "
            "without a consistent __hash__, Python normally makes the "
            "object unhashable by setting __hash__ to None."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain closures in Python and how they relate to Python's "
            "scoping rules."
        ),
        "expected_answer": (
            "A closure occurs when a nested function captures and remembers "
            "variables from an enclosing function's scope even after the "
            "outer function has finished executing. This works because "
            "Python functions retain references to their enclosing lexical "
            "scope. Closures are commonly used in decorators and factory "
            "functions and are related to Python's LEGB scoping rules."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the difference between copy.deepcopy, pickling, "
            "and __reduce__ for object serialization?"
        ),
        "expected_answer": (
            "deepcopy recursively duplicates an object in memory using "
            "the copy module and can use __deepcopy__ when defined. "
            "Pickling serializes an object into a byte stream for storage "
            "or transfer and can reconstruct it later. deepcopy and "
            "pickle can rely on __reduce__ or __reduce_ex__, as well as "
            "__getstate__ and __setstate__, to determine how custom "
            "objects should be reconstructed."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does Python's garbage collector handle reference cycles, "
            "and what role do __del__ and weak references play?"
        ),
        "expected_answer": (
            "Reference counting alone cannot free objects involved in "
            "reference cycles because their reference counts never reach "
            "zero. Python's cyclic garbage collector periodically detects "
            "and collects unreachable cycles. __del__ methods historically "
            "complicated cycle collection, while weakref provides references "
            "that do not increase reference counts and can help prevent "
            "unwanted object retention."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the difference between __slots__ and a regular class, "
            "and what are the trade-offs?"
        ),
        "expected_answer": (
            "Regular Python instances normally store attributes in a "
            "per-instance __dict__, allowing dynamic attribute addition "
            "but using more memory. __slots__ restricts instances to a "
            "fixed set of attributes and can reduce memory usage and "
            "improve attribute access performance. The trade-offs include "
            "losing dynamic attribute assignment and additional complexity "
            "with multiple inheritance."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how Python coroutines and the asyncio event loop "
            "actually work under the hood."
        ),
        "expected_answer": (
            "A coroutine created with async def can suspend at await points "
            "and return control to the event loop. The event loop maintains "
            "tasks and callbacks and repeatedly resumes ready tasks based "
            "on I/O readiness notifications from the operating system. "
            "This allows many concurrent I/O-bound operations to run on a "
            "single thread without traditional thread-based preemption."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is duck typing, and how does it relate to Python's "
            "dynamic type system?"
        ),
        "expected_answer": (
            "Duck typing means an object's suitability for an operation "
            "depends on whether it provides the required methods or "
            "attributes rather than on its explicit class or inheritance "
            "hierarchy. This reflects Python's dynamic typing philosophy. "
            "For example, any object implementing the required iteration "
            "protocol can be used in a for loop regardless of its class."
        ),
    },


    # =========================================================
    # EASY — 10 ADDITIONAL QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the walrus operator (:=) in Python, and when "
            "would you use it?"
        ),
        "expected_answer": (
            "The walrus operator, introduced in Python 3.8, is an "
            "assignment expression that assigns a value to a variable "
            "as part of a larger expression. It is useful for avoiding "
            "redundant computations, such as assigning the result of a "
            "function call inside a while-loop condition or an if-statement "
            "so the value can be tested and used without calling the "
            "function twice."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "How do f-strings work in Python, and what advantages "
            "do they have over older formatting methods?"
        ),
        "expected_answer": (
            "F-strings, introduced in Python 3.6, embed expressions "
            "inside string literals using curly braces prefixed with f. "
            "They are evaluated at runtime and are generally faster than "
            "str.format() or percent formatting because the parsing is "
            "done at compile time. They also support format specifiers, "
            "arbitrary expressions, and, since Python 3.12, multi-line "
            "expressions and nested quotes more flexibly."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the purpose of the enumerate() function?"
        ),
        "expected_answer": (
            "enumerate() wraps an iterable and yields tuples of an "
            "index and the corresponding element. It accepts an optional "
            "start parameter to change the initial index value. It is "
            "preferred over manually maintaining a counter variable "
            "inside a for loop because it is more readable and less "
            "error-prone."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What does the zip() function do, and what happens "
            "when the iterables have different lengths?"
        ),
        "expected_answer": (
            "zip() takes two or more iterables and returns an iterator "
            "of tuples, pairing elements by position. By default it "
            "stops at the shortest iterable. itertools.zip_longest can "
            "be used to continue until the longest iterable is exhausted, "
            "filling missing values with a specified fill value. In "
            "Python 3.10+, zip also accepts a strict=True argument that "
            "raises ValueError if lengths differ."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a dataclass in Python, and how does it differ "
            "from a regular class?"
        ),
        "expected_answer": (
            "A dataclass, provided by the dataclasses module since "
            "Python 3.7, automatically generates __init__, __repr__, "
            "and __eq__ methods based on annotated class fields. It "
            "reduces boilerplate for classes that primarily hold data. "
            "Unlike a regular class, fields are declared with type "
            "annotations and default values, and additional features "
            "like frozen instances and field ordering can be enabled "
            "through decorator parameters."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are type hints in Python, and are they enforced "
            "at runtime?"
        ),
        "expected_answer": (
            "Type hints are optional annotations that indicate the "
            "expected types of function parameters, return values, and "
            "variables. They are not enforced at runtime by CPython; "
            "they serve as documentation and are used by external tools "
            "such as mypy, Pyright, and IDEs for static analysis, "
            "autocompletion, and catching type errors before execution."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is structural pattern matching (match/case) "
            "in Python?"
        ),
        "expected_answer": (
            "Structural pattern matching, introduced in Python 3.10, "
            "allows matching a subject value against a series of "
            "patterns using match and case statements. Patterns can "
            "destructure sequences, mappings, and objects. It is more "
            "expressive than chained if/elif blocks for complex "
            "branching because it supports guards, wildcards, OR "
            "patterns, and capture variables."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the itertools module, and name three commonly "
            "used functions from it?"
        ),
        "expected_answer": (
            "itertools is a standard-library module providing fast, "
            "memory-efficient iterator building blocks. Commonly used "
            "functions include chain (concatenates iterables), islice "
            "(lazily slices an iterator), and product (computes the "
            "Cartesian product). Others like combinations, permutations, "
            "and groupby are also widely used."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What does functools.lru_cache do, and when should "
            "you use it?"
        ),
        "expected_answer": (
            "functools.lru_cache is a decorator that memoizes the "
            "results of a function, caching the most recent calls up "
            "to a configurable maxsize. It is useful for expensive "
            "pure functions with hashable arguments, such as recursive "
            "computations. cache_info() can be used to monitor hit and "
            "miss rates, and cache_clear() resets the cache."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the __all__ variable in a Python module?"
        ),
        "expected_answer": (
            "__all__ is a list of strings that defines the public "
            "API of a module. When a consumer uses 'from module import *', "
            "only names listed in __all__ are imported. It does not "
            "prevent direct import of unlisted names; it only controls "
            "the wildcard import behavior and serves as documentation "
            "of the module's intended public interface."
        ),
    },


    # =========================================================
    # MEDIUM — 6 ADDITIONAL QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How does __slots__ affect memory usage and attribute "
            "access compared to a regular instance __dict__?"
        ),
        "expected_answer": (
            "When __slots__ is defined, Python stores instance "
            "attributes in a fixed-size array of slot descriptors "
            "instead of a per-instance __dict__. This eliminates the "
            "hash-table overhead of a dict, reducing memory per instance "
            "significantly when many instances exist. Attribute access "
            "through slot descriptors can also be slightly faster. The "
            "trade-off is that instances cannot have arbitrary dynamic "
            "attributes unless __dict__ is explicitly included in "
            "__slots__."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the descriptor protocol and the difference "
            "between data descriptors and non-data descriptors."
        ),
        "expected_answer": (
            "A descriptor is an object that defines __get__, __set__, "
            "or __delete__. A data descriptor defines at least __set__ "
            "or __delete__ in addition to __get__, while a non-data "
            "descriptor defines only __get__. Data descriptors take "
            "priority over instance __dict__ entries during attribute "
            "lookup, whereas non-data descriptors are overridden by "
            "instance __dict__ entries. Functions are non-data descriptors "
            "whose __get__ returns a bound method."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How does super() work in Python, and why is it "
            "preferred over calling a parent class directly?"
        ),
        "expected_answer": (
            "super() returns a proxy object that delegates attribute "
            "lookups to the next class in the Method Resolution Order "
            "rather than hardcoding a specific parent class. This is "
            "essential for cooperative multiple inheritance because it "
            "ensures every class in the MRO is called exactly once. "
            "Calling a parent class directly by name breaks this chain "
            "and can cause classes in the MRO to be skipped or called "
            "multiple times."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are pytest fixtures, and how do they differ from "
            "setUp/tearDown in unittest?"
        ),
        "expected_answer": (
            "Pytest fixtures are functions decorated with @pytest.fixture "
            "that supply reusable setup and teardown logic to tests via "
            "dependency injection. Tests request fixtures by name in "
            "their parameter list. Unlike unittest's setUp/tearDown, "
            "fixtures support scoping (function, class, module, session), "
            "parameterization, and composability through fixture chaining, "
            "which makes test setup more modular and explicit."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are the practical trade-offs between multiprocessing "
            "and threading for CPU-bound work in Python?"
        ),
        "expected_answer": (
            "Threading in CPython is limited by the GIL, which prevents "
            "true parallel execution of Python bytecode, making it "
            "unsuitable for CPU-bound parallelism. Multiprocessing "
            "spawns separate OS processes, each with its own interpreter "
            "and GIL, enabling true parallelism but incurring higher "
            "memory overhead and inter-process communication costs via "
            "pickling. For CPU-bound work, multiprocessing or "
            "ProcessPoolExecutor is generally preferred."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is an Abstract Base Class (ABC) in Python, and "
            "how does it enforce interface contracts?"
        ),
        "expected_answer": (
            "An ABC, created by subclassing abc.ABC or using "
            "ABCMeta as a metaclass, defines an interface by marking "
            "methods with @abstractmethod. Any concrete subclass must "
            "implement all abstract methods or it cannot be instantiated. "
            "ABCs also support virtual subclassing via register(), "
            "allowing unrelated classes to be recognized as subclasses "
            "without inheriting implementation."
        ),
    },


    # =========================================================
    # HARD — 9 ADDITIONAL QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain Python's import system: what happens internally "
            "when you write 'import foo'?"
        ),
        "expected_answer": (
            "Python first checks sys.modules for a cached module object. "
            "If not found, it iterates through the finders in "
            "sys.meta_path (typically BuiltinImporter, FrozenImporter, "
            "and PathFinder). The finder returns a module spec, which "
            "contains a loader. The loader creates the module object, "
            "adds it to sys.modules, and then executes the module's "
            "code in the module's namespace. This two-phase "
            "create-then-exec approach prevents infinite recursion "
            "in circular imports."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What are weak references, and how does the weakref "
            "module help prevent memory leaks?"
        ),
        "expected_answer": (
            "A weak reference refers to an object without increasing "
            "its reference count, so the object can be garbage collected "
            "when no strong references remain. The weakref module "
            "provides ref, proxy, and WeakValueDictionary, among "
            "others. Weak references are useful for caches, observer "
            "patterns, and parent-child object graphs where you want "
            "to avoid preventing garbage collection of objects that "
            "are otherwise unreachable."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe the C3 linearization algorithm and explain "
            "why Python chose it over depth-first or breadth-first "
            "MRO strategies."
        ),
        "expected_answer": (
            "C3 linearization produces a monotonic, consistent method "
            "resolution order by merging the linearizations of parent "
            "classes while preserving local precedence order and the "
            "ordering of the parents list. Unlike naive depth-first "
            "search, C3 avoids violating monotonicity in diamond "
            "inheritance hierarchies and raises TypeError when a "
            "consistent ordering is impossible. Python adopted C3 in "
            "version 2.3 to fix inconsistencies in the earlier MRO "
            "algorithm for new-style classes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does asyncio schedule and run tasks, and what is "
            "the difference between asyncio.create_task, "
            "asyncio.ensure_future, and awaiting a coroutine directly?"
        ),
        "expected_answer": (
            "asyncio.create_task wraps a coroutine into a Task and "
            "schedules it on the running event loop immediately, "
            "allowing concurrent execution. ensure_future is a more "
            "general version that also accepts Futures. Awaiting a "
            "coroutine directly runs it inline without creating a "
            "Task, so no concurrency occurs — the caller suspends "
            "until the coroutine completes. Using create_task is the "
            "preferred way to run coroutines concurrently within a "
            "single event loop."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you profile memory usage in a Python "
            "application, and what tools are available?"
        ),
        "expected_answer": (
            "tracemalloc, built into the standard library, tracks "
            "memory allocations and can produce snapshots showing "
            "per-file and per-line allocation statistics. objgraph "
            "visualizes object reference graphs and helps find leaks. "
            "memory_profiler provides line-by-line memory usage via "
            "the @profile decorator. sys.getsizeof gives the size of "
            "a single object but does not account for referenced "
            "objects, so recursive measurement or pympler.asizeof "
            "is needed for deep sizes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What are typing.Protocol and typing.Generic, and how "
            "do they enable structural subtyping and parameterized "
            "types in Python?"
        ),
        "expected_answer": (
            "typing.Generic allows defining classes parameterized by "
            "type variables, enabling type-safe containers and "
            "algorithms without runtime overhead. typing.Protocol, "
            "introduced in Python 3.8, enables structural subtyping: "
            "a class satisfies a Protocol if it has the required "
            "attributes and method signatures, without needing to "
            "explicitly inherit from it. This bridges duck typing and "
            "static type checking, letting tools like mypy verify "
            "structural compatibility at analysis time."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the free-threaded (no-GIL) build introduced "
            "experimentally in CPython 3.13, and what challenges "
            "does removing the GIL present?"
        ),
        "expected_answer": (
            "CPython 3.13 offers an experimental free-threaded build "
            "that disables the GIL, allowing multiple threads to "
            "execute Python bytecode in parallel. This required "
            "replacing the GIL with fine-grained per-object locking, "
            "biased reference counting, and making the memory allocator "
            "thread-safe. Challenges include potential thread-safety "
            "bugs in existing C extensions that assumed the GIL, "
            "possible single-threaded performance regressions, and "
            "the need for library authors to audit and test their "
            "code for true thread safety."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the difference between a virtual environment, "
            "a venv, a conda environment, and a Docker container "
            "for Python dependency isolation."
        ),
        "expected_answer": (
            "A venv (created via python -m venv) isolates Python "
            "packages by creating a lightweight directory with its "
            "own site-packages and a symlink or copy of the Python "
            "binary, but shares the system's OS-level libraries. "
            "Conda environments isolate both Python and native C "
            "libraries, making them suitable for scientific packages "
            "with complex compiled dependencies. Docker containers "
            "provide full OS-level isolation, packaging the entire "
            "filesystem, libraries, and runtime. The trade-off is "
            "increasing isolation versus increasing resource overhead "
            "and complexity."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is functools.singledispatch, and how does it "
            "enable function overloading in Python?"
        ),
        "expected_answer": (
            "functools.singledispatch is a decorator that transforms "
            "a function into a single-dispatch generic function, "
            "dispatching on the type of the first argument. Overloaded "
            "implementations are registered with @function.register "
            "for specific types. At call time, the dispatcher looks "
            "up the most specific registered implementation in the "
            "MRO of the argument's type. It provides a clean "
            "alternative to isinstance chains and supports adding "
            "new type handlers without modifying the original function."
        ),
    },
]


def seed_python_questions() -> None:
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
                    "Python programming language interview "
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
                f"Python topic already contains "
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
        print("PYTHON INTERVIEW QUESTION BANK CREATED")
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
    seed_python_questions()