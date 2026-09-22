from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "Operating Systems"


QUESTIONS = [
    # =========================================================
    # EASY — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between a process and a thread?"
        ),
        "expected_answer": (
            "A process is an independent execution unit with its own "
            "memory address space, file descriptors, and resources. A "
            "thread is a lightweight unit of execution within a process "
            "that shares the process's memory and resources. Creating "
            "and switching between threads is cheaper than between "
            "processes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a deadlock, and its four necessary conditions?"
        ),
        "expected_answer": (
            "A deadlock is a situation where two or more processes are "
            "permanently blocked because each is waiting for a resource "
            "held by another. The four necessary conditions are mutual "
            "exclusion (resources cannot be shared), hold and wait (a "
            "process holds resources while waiting for others), no "
            "preemption (resources cannot be forcibly taken), and "
            "circular wait (a cycle of processes exists where each "
            "waits on the next)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Multitasking vs multiprogramming vs multithreading?"
        ),
        "expected_answer": (
            "Multiprogramming keeps multiple programs in memory so "
            "the CPU is never idle when one program waits for I/O. "
            "Multitasking extends this by rapidly switching between "
            "processes (time-sharing) to give each the illusion of "
            "exclusive CPU access. Multithreading runs multiple threads "
            "within a single process, allowing concurrent execution of "
            "different parts of the same program."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is virtual memory, and why is it used?"
        ),
        "expected_answer": (
            "Virtual memory is a memory management technique that "
            "gives each process the illusion of a large, contiguous "
            "address space by mapping virtual addresses to physical "
            "memory or disk (swap space). It allows programs larger "
            "than physical RAM to run, provides process isolation, and "
            "simplifies memory allocation."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Paging vs segmentation?"
        ),
        "expected_answer": (
            "Paging divides memory into fixed-size blocks called pages "
            "(virtual) and frames (physical), eliminating external "
            "fragmentation but potentially causing internal "
            "fragmentation. Segmentation divides memory into "
            "variable-size segments based on logical units like "
            "functions or data structures, reflecting the program's "
            "logical view but susceptible to external fragmentation."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a context switch?"
        ),
        "expected_answer": (
            "A context switch is the process of saving the state "
            "(registers, program counter, stack pointer) of the "
            "currently running process or thread and restoring the "
            "state of the next one to be executed. Context switches "
            "have overhead because they involve saving and loading "
            "state and may flush caches and TLB entries."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What are the states of a process?"
        ),
        "expected_answer": (
            "The main process states are New (being created), Ready "
            "(waiting to be assigned to a CPU), Running (instructions "
            "are being executed), Waiting/Blocked (waiting for an "
            "event or I/O), and Terminated (finished execution). The "
            "OS scheduler moves processes between these states."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a kernel and an "
            "operating system?"
        ),
        "expected_answer": (
            "The kernel is the core component of the OS that manages "
            "hardware resources, memory, process scheduling, and "
            "system calls. The operating system is the full package "
            "that includes the kernel plus system utilities, libraries, "
            "shells, file managers, and user-facing services."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a system call?"
        ),
        "expected_answer": (
            "A system call is the programmatic interface through which "
            "a user-space application requests a service from the "
            "kernel, such as file I/O, process creation, or memory "
            "allocation. It triggers a transition from user mode to "
            "kernel mode so the kernel can execute the privileged "
            "operation safely."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between logical and "
            "physical addresses?"
        ),
        "expected_answer": (
            "A logical (virtual) address is generated by the CPU "
            "during program execution and is what the process sees. "
            "A physical address refers to the actual location in "
            "hardware RAM. The Memory Management Unit (MMU) translates "
            "logical addresses to physical addresses at runtime using "
            "page tables."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is fragmentation (internal vs external)?"
        ),
        "expected_answer": (
            "Internal fragmentation is wasted space within an allocated "
            "block when the allocated block is larger than the requested "
            "size. External fragmentation is wasted space between "
            "allocated blocks, where the total free memory is "
            "sufficient but not contiguous enough to satisfy a request. "
            "Paging eliminates external fragmentation; compaction can "
            "also help."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the role of an interrupt in an OS?"
        ),
        "expected_answer": (
            "An interrupt is a signal to the CPU that an event "
            "requiring attention has occurred, such as I/O completion, "
            "a timer tick, or a hardware error. The CPU pauses its "
            "current task, saves its state, and executes an interrupt "
            "handler (ISR) to process the event before resuming the "
            "interrupted task."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a file system, and why is it needed?"
        ),
        "expected_answer": (
            "A file system organizes and controls how data is stored "
            "on and retrieved from a storage device. It provides a "
            "hierarchical structure of files and directories, manages "
            "metadata (names, permissions, timestamps), and handles "
            "allocation and deallocation of storage blocks. Without "
            "it, data would be an unstructured blob on disk."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a program and a process?"
        ),
        "expected_answer": (
            "A program is a passive entity, a file of instructions "
            "stored on disk. A process is an active entity, an "
            "instance of a program being executed with its own "
            "allocated memory, registers, and program counter. "
            "Multiple processes can be running instances of the "
            "same program."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is multiprocessing?"
        ),
        "expected_answer": (
            "Multiprocessing is the use of two or more CPUs (or CPU "
            "cores) within a single computer system to execute multiple "
            "processes simultaneously. It provides true parallelism, "
            "improving throughput and fault tolerance compared to "
            "single-processor systems."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the purpose of a scheduler?"
        ),
        "expected_answer": (
            "A scheduler is the OS component that decides which "
            "process or thread gets CPU time and for how long. The "
            "long-term scheduler controls admission to the ready "
            "queue, the short-term scheduler selects the next process "
            "to run, and the medium-term scheduler handles swapping "
            "processes in and out of memory."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is swapping in an OS?"
        ),
        "expected_answer": (
            "Swapping is the process of moving an entire process from "
            "main memory to a backing store (swap space on disk) and "
            "back again. It frees up physical memory for other "
            "processes when RAM is scarce but introduces significant "
            "latency because disk access is much slower than memory "
            "access."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a bootloader "
            "and a kernel?"
        ),
        "expected_answer": (
            "A bootloader is a small program that runs when the "
            "computer starts and is responsible for loading the kernel "
            "into memory and transferring control to it. The kernel is "
            "the core of the OS that manages hardware and system "
            "resources after it has been loaded. Examples of bootloaders "
            "include GRUB and the Windows Boot Manager."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is thread synchronization, and why is it needed?"
        ),
        "expected_answer": (
            "Thread synchronization is the coordination of concurrent "
            "threads to ensure correct and predictable behavior when "
            "they access shared resources. Without synchronization, "
            "race conditions can cause data corruption and "
            "unpredictable results. Common mechanisms include mutexes, "
            "semaphores, and condition variables."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a monolithic and "
            "layered OS structure?"
        ),
        "expected_answer": (
            "A monolithic OS runs the entire operating system as a "
            "single program in kernel space, offering high performance "
            "but making the code harder to maintain and debug. A "
            "layered OS is divided into hierarchical layers where each "
            "layer only interacts with its immediate neighbors, "
            "improving modularity and maintainability at the cost of "
            "some performance overhead from inter-layer calls."
        ),
    },

    # =========================================================
    # MEDIUM — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Preemptive vs non-preemptive scheduling with "
            "algorithm examples."
        ),
        "expected_answer": (
            "In preemptive scheduling, the OS can forcibly remove a "
            "running process from the CPU (e.g. when a higher-priority "
            "process arrives or a time quantum expires). Examples "
            "include Round Robin and Preemptive SJF. In non-preemptive "
            "scheduling, a running process keeps the CPU until it "
            "voluntarily yields, blocks, or finishes. Examples include "
            "FCFS and non-preemptive SJF. Preemptive scheduling "
            "provides better responsiveness but has higher context "
            "switch overhead."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a semaphore vs a mutex?"
        ),
        "expected_answer": (
            "A mutex is a binary lock that provides mutual exclusion: "
            "only the thread that locked it can unlock it. A semaphore "
            "is a signaling mechanism with a counter that can be "
            "greater than one, allowing a specified number of threads "
            "to access a resource concurrently. A binary semaphore "
            "behaves similarly to a mutex but does not enforce ownership."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the producer-consumer problem and its solution."
        ),
        "expected_answer": (
            "The producer-consumer problem involves two types of "
            "processes sharing a bounded buffer: producers add items "
            "and consumers remove them. The challenge is preventing "
            "producers from adding to a full buffer and consumers from "
            "removing from an empty buffer. A classic solution uses two "
            "counting semaphores (one tracking empty slots, one tracking "
            "full slots) and a mutex for mutual exclusion on buffer "
            "access."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is thrashing, and how is it avoided?"
        ),
        "expected_answer": (
            "Thrashing occurs when the system spends most of its time "
            "swapping pages in and out of memory rather than executing "
            "useful work, typically because too many processes are "
            "competing for too little physical memory. It can be "
            "avoided by reducing the degree of multiprogramming, "
            "using the working set model to allocate sufficient frames "
            "per process, or employing page fault frequency monitoring "
            "to adjust allocations."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Compare FCFS, SJF, Round Robin, and Priority Scheduling."
        ),
        "expected_answer": (
            "FCFS (First-Come, First-Served) is simple but suffers "
            "from the convoy effect where short jobs wait behind long "
            "ones. SJF (Shortest Job First) minimizes average waiting "
            "time but requires knowing burst times in advance. Round "
            "Robin assigns a fixed time quantum and cycles through "
            "processes, providing good responsiveness but potentially "
            "high turnaround time. Priority Scheduling runs the "
            "highest-priority process first but can cause starvation "
            "of low-priority processes, mitigated by aging."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a page fault, and what happens when one occurs?"
        ),
        "expected_answer": (
            "A page fault occurs when a process accesses a virtual "
            "page that is not currently mapped to a physical frame in "
            "memory. The OS traps the fault, locates the page on disk "
            "(swap or file system), finds or frees a physical frame "
            "(possibly evicting another page using a replacement "
            "algorithm), loads the page into the frame, updates the "
            "page table, and restarts the interrupted instruction."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain IPC mechanisms: pipes, message queues, "
            "shared memory."
        ),
        "expected_answer": (
            "Pipes provide a unidirectional byte stream between "
            "related processes (or bidirectional via two pipes). "
            "Message queues allow processes to send and receive "
            "discrete messages via a kernel-managed queue with "
            "message boundaries preserved. Shared memory maps the "
            "same physical memory into multiple processes' address "
            "spaces for the fastest IPC but requires explicit "
            "synchronization (e.g. semaphores) to avoid race conditions."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the dining philosophers problem, "
            "and how is it solved?"
        ),
        "expected_answer": (
            "Five philosophers sit around a table with five forks; "
            "each needs two forks to eat. If all pick up their left "
            "fork simultaneously, deadlock occurs. Solutions include "
            "limiting the number of philosophers allowed to sit (using "
            "a semaphore), imposing an ordering on fork acquisition "
            "(e.g. always pick up the lower-numbered fork first), or "
            "using an arbitrator that grants permission to pick up "
            "both forks."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the difference between a hard link and "
            "a symbolic link."
        ),
        "expected_answer": (
            "A hard link is an additional directory entry pointing to "
            "the same inode as the original file; deleting the original "
            "does not affect the hard link because the inode still has "
            "a reference. A symbolic (soft) link is a separate file "
            "that contains the path to the target; it breaks if the "
            "target is moved or deleted. Hard links cannot span file "
            "systems or link to directories (on most systems), while "
            "symbolic links can."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a race condition, and how do you prevent it?"
        ),
        "expected_answer": (
            "A race condition occurs when the outcome of a computation "
            "depends on the unpredictable order in which concurrent "
            "threads or processes execute, leading to incorrect results. "
            "Prevention involves using synchronization primitives such "
            "as mutexes, semaphores, or atomic operations to ensure "
            "that critical sections are accessed by only one thread "
            "at a time."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the readers-writers problem and its solutions."
        ),
        "expected_answer": (
            "The readers-writers problem involves concurrent access "
            "to a shared resource where multiple readers can read "
            "simultaneously but writers need exclusive access. The "
            "first readers-writers solution gives priority to readers "
            "(writers may starve). The second gives priority to writers "
            "(readers may starve). A fair solution uses a queue or "
            "turnstile to serve requests in order, preventing "
            "starvation of either group."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is demand paging, and how does it improve efficiency?"
        ),
        "expected_answer": (
            "Demand paging loads pages into memory only when they are "
            "accessed (on demand) rather than loading the entire "
            "process at startup. This reduces initial load time and "
            "memory usage because pages that are never accessed are "
            "never loaded. A page fault triggers loading of the needed "
            "page from disk."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the difference between spinlocks and "
            "blocking locks."
        ),
        "expected_answer": (
            "A spinlock continuously checks (busy-waits) in a loop "
            "until the lock becomes available, consuming CPU cycles "
            "but avoiding the overhead of a context switch. A blocking "
            "lock puts the waiting thread to sleep and wakes it when "
            "the lock is released, saving CPU but incurring context "
            "switch overhead. Spinlocks are preferred for very short "
            "critical sections on multi-core systems; blocking locks "
            "are better when the wait time may be long."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a zombie process vs an orphan process?"
        ),
        "expected_answer": (
            "A zombie process has finished execution but still has an "
            "entry in the process table because its parent has not yet "
            "called wait() to read its exit status. An orphan process "
            "is a running process whose parent has terminated; it is "
            "adopted by the init/systemd process (PID 1), which "
            "eventually reaps it. Zombies consume a process table "
            "slot; too many can exhaust the table."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how the OS handles multi-level page tables."
        ),
        "expected_answer": (
            "A multi-level page table breaks the virtual address into "
            "multiple index fields, each used to look up a table at "
            "the next level. For example, a two-level scheme uses the "
            "top bits to index a page directory, which points to a "
            "second-level page table, which contains the physical "
            "frame number. This saves memory because second-level "
            "tables are only allocated for virtual address ranges "
            "actually in use, unlike a flat page table that must cover "
            "the entire address space."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the working set model in memory management?"
        ),
        "expected_answer": (
            "The working set of a process is the set of pages it has "
            "referenced within a recent time window. The working set "
            "model allocates enough physical frames to hold each "
            "process's working set, preventing thrashing. If the total "
            "working set size of all processes exceeds available "
            "memory, some processes must be suspended to free frames."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain disk scheduling algorithms "
            "(FCFS, SCAN, C-SCAN)."
        ),
        "expected_answer": (
            "FCFS processes disk I/O requests in arrival order, which "
            "is fair but may cause excessive head movement. SCAN "
            "(elevator algorithm) moves the head in one direction, "
            "servicing all requests along the way, then reverses "
            "direction. C-SCAN is a variant that moves in one "
            "direction only and jumps back to the beginning after "
            "reaching the end, providing more uniform wait times "
            "across the disk."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between user-level and "
            "kernel-level threads?"
        ),
        "expected_answer": (
            "User-level threads are managed entirely by a user-space "
            "library without kernel awareness, making creation and "
            "switching very fast but unable to take advantage of "
            "multiple CPUs. Kernel-level threads are managed by the "
            "OS kernel, allowing true parallelism on multi-core "
            "systems but with higher creation and switching overhead. "
            "Most modern systems use kernel threads or a hybrid model."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how caching (LRU, LFU) works at the OS level."
        ),
        "expected_answer": (
            "The OS maintains caches (e.g. page cache, buffer cache) "
            "to keep frequently accessed disk data in memory. LRU "
            "(Least Recently Used) evicts the page that has not been "
            "accessed for the longest time, exploiting temporal "
            "locality. LFU (Least Frequently Used) evicts the page "
            "with the fewest accesses. LRU is more common in practice "
            "because it adapts well to changing access patterns."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is copy-on-write, and where is it used?"
        ),
        "expected_answer": (
            "Copy-on-write (COW) is an optimization where multiple "
            "processes share the same physical pages until one of them "
            "tries to write. At that point, the OS creates a private "
            "copy of the modified page for the writing process. COW "
            "is heavily used in fork() to avoid duplicating the entire "
            "address space of the parent process immediately and in "
            "file systems to implement efficient snapshots."
        ),
    },

    # =========================================================
    # HARD — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the Banker's Algorithm for deadlock "
            "avoidance with an example."
        ),
        "expected_answer": (
            "The Banker's Algorithm prevents deadlock by simulating "
            "resource allocation before granting a request. It "
            "maintains matrices of maximum demand, current allocation, "
            "and remaining need for each process. When a process "
            "requests resources, the algorithm tentatively grants them "
            "and checks whether the resulting state is safe (i.e. "
            "there exists at least one ordering in which all processes "
            "can finish). If safe, the request is granted; otherwise, "
            "the process must wait. The algorithm requires advance "
            "knowledge of maximum resource needs."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does address translation work with a TLB "
            "and multi-level page tables?"
        ),
        "expected_answer": (
            "The CPU first checks the TLB (Translation Lookaside "
            "Buffer), a fast cache of recent virtual-to-physical "
            "translations. On a TLB hit, the physical address is "
            "returned immediately. On a miss, the hardware or OS "
            "walks the multi-level page table (e.g. PGD -> PUD -> "
            "PMD -> PTE on x86-64) to find the mapping, loads it into "
            "the TLB, and retries. TLB misses are expensive because "
            "each level requires a memory access, which is why keeping "
            "a high TLB hit rate is critical for performance."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Compare monolithic, microkernel, and hybrid "
            "kernel architectures."
        ),
        "expected_answer": (
            "A monolithic kernel runs all OS services (file systems, "
            "drivers, networking) in kernel space, offering high "
            "performance but a large attack surface and harder "
            "debugging. A microkernel runs only essential services "
            "(IPC, scheduling, basic memory management) in kernel "
            "space and the rest in user space, improving modularity "
            "and fault isolation at the cost of IPC overhead. A hybrid "
            "kernel (e.g. Windows NT, macOS XNU) combines both "
            "approaches, running some services in kernel space for "
            "performance while keeping others in user space for "
            "modularity."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain copy-on-write in fork() and why it's efficient."
        ),
        "expected_answer": (
            "When fork() creates a child process, instead of copying "
            "all parent memory, both processes share the same physical "
            "pages marked as read-only. When either process writes to "
            "a page, a page fault occurs, the OS allocates a new "
            "physical frame, copies the contents, and maps the new "
            "frame to the writing process. This avoids copying pages "
            "that are never modified, which is especially efficient "
            "when fork() is immediately followed by exec(), since "
            "exec() replaces the entire address space anyway."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is priority inversion, and how does priority "
            "inheritance solve it?"
        ),
        "expected_answer": (
            "Priority inversion occurs when a high-priority task is "
            "blocked waiting for a resource held by a low-priority "
            "task, while a medium-priority task preempts the low-priority "
            "task, effectively delaying the high-priority task "
            "indefinitely. Priority inheritance solves this by "
            "temporarily boosting the low-priority task's priority to "
            "that of the highest-priority task waiting on it, so it "
            "can finish quickly and release the resource. The Mars "
            "Pathfinder incident is a famous real-world example."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does the Linux Completely Fair Scheduler (CFS) work?"
        ),
        "expected_answer": (
            "CFS models an ideal multitasking processor where each "
            "runnable task receives an equal share of CPU time. It "
            "tracks each task's virtual runtime (vruntime), which "
            "advances more slowly for high-priority (low nice value) "
            "tasks. Tasks are stored in a red-black tree sorted by "
            "vruntime, and the scheduler always picks the task with "
            "the smallest vruntime. This ensures fairness because "
            "tasks that have used less CPU time are preferentially "
            "scheduled."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how NUMA architectures affect OS "
            "scheduling decisions."
        ),
        "expected_answer": (
            "In NUMA (Non-Uniform Memory Access) architectures, each "
            "CPU socket has local memory that it can access faster "
            "than remote memory attached to another socket. The OS "
            "scheduler tries to keep a process on CPUs within the same "
            "NUMA node as its allocated memory to minimize remote "
            "memory access latency. Memory allocation policies (e.g. "
            "local, interleave) and NUMA-aware scheduling are critical "
            "for performance on multi-socket servers."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does an OS implement memory-mapped files, "
            "and what are their use cases?"
        ),
        "expected_answer": (
            "The OS maps a file's contents directly into the process's "
            "virtual address space using the mmap system call. Reads "
            "and writes to the mapped region translate to reads and "
            "writes of the file through the page cache, with page "
            "faults loading pages on demand. Use cases include "
            "efficient random-access I/O on large files, shared "
            "memory between processes via mapping the same file, "
            "loading shared libraries, and implementing memory-mapped "
            "databases."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how a modern OS handles TLB shootdown "
            "in multi-core systems."
        ),
        "expected_answer": (
            "When one core modifies a page table entry (e.g. unmaps a "
            "page), the TLBs on other cores that may have cached the "
            "old mapping must be invalidated. The modifying core sends "
            "an inter-processor interrupt (IPI) to the affected cores, "
            "requesting them to flush the relevant TLB entries. The "
            "initiating core typically waits for acknowledgment from "
            "all target cores before proceeding. TLB shootdowns are "
            "expensive due to IPI latency and can be a scalability "
            "bottleneck on many-core systems."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design a lock-free data structure, "
            "and what hardware primitives (CAS) does it rely on?"
        ),
        "expected_answer": (
            "Lock-free data structures use atomic hardware instructions "
            "like Compare-And-Swap (CAS) instead of locks. CAS "
            "atomically compares a memory location to an expected "
            "value and, only if they match, writes a new value. A "
            "lock-free algorithm typically reads the current state, "
            "computes the desired next state, and uses CAS to attempt "
            "the update in a retry loop. At least one thread always "
            "makes progress, preventing deadlock. Challenges include "
            "the ABA problem (solved with tagged pointers or hazard "
            "pointers) and memory ordering (addressed with appropriate "
            "memory barriers)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how journaling file systems recover "
            "from crashes."
        ),
        "expected_answer": (
            "A journaling file system records pending changes to a "
            "journal (log) before applying them to the file system's "
            "main data structures. If a crash occurs, the journal is "
            "replayed on mount to complete or discard uncommitted "
            "operations, restoring consistency without a full file "
            "system check. Metadata-only journaling (e.g. ext4 default) "
            "journals only structural changes; full journaling also "
            "journals data, providing stronger guarantees but at a "
            "performance cost."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does the OS scheduler balance real-time and "
            "normal processes (e.g., Linux SCHED_FIFO vs "
            "SCHED_OTHER)?"
        ),
        "expected_answer": (
            "Linux uses multiple scheduling classes with strict "
            "priority ordering. Real-time classes (SCHED_FIFO, "
            "SCHED_RR) have higher priority than the normal class "
            "(SCHED_OTHER, which uses CFS). SCHED_FIFO runs a task "
            "until it blocks or a higher-priority task preempts it. "
            "SCHED_RR is similar but adds time slicing among equal-priority "
            "real-time tasks. Normal tasks only run when no real-time "
            "tasks are runnable. Misconfigured real-time tasks can "
            "starve normal tasks entirely."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how containers achieve isolation using "
            "namespaces and cgroups."
        ),
        "expected_answer": (
            "Linux namespaces provide isolation of system resources so "
            "each container has its own view of process IDs (PID "
            "namespace), network interfaces (net namespace), mount "
            "points, hostnames, users, and IPC. Cgroups (control "
            "groups) limit and account for resource usage such as CPU, "
            "memory, disk I/O, and network bandwidth. Together, "
            "namespaces provide the illusion of an isolated system "
            "while cgroups prevent any single container from monopolizing "
            "host resources, all without the overhead of full "
            "hardware virtualization."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is false sharing in multi-threaded programs, "
            "and how do you avoid it?"
        ),
        "expected_answer": (
            "False sharing occurs when threads on different cores "
            "modify variables that reside on the same CPU cache line. "
            "Even though the variables are logically independent, "
            "writing to one invalidates the entire cache line on other "
            "cores, causing constant cache coherence traffic and "
            "significant performance degradation. It is avoided by "
            "padding or aligning frequently written variables to "
            "separate cache lines (typically 64 bytes on x86), using "
            "compiler or language attributes like alignas or "
            "@Contended in Java."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how virtual machines differ from containers "
            "at the OS level."
        ),
        "expected_answer": (
            "Virtual machines run a full guest OS on emulated or "
            "paravirtualized hardware managed by a hypervisor, "
            "providing strong isolation because each VM has its own "
            "kernel. Containers share the host kernel and use "
            "namespaces and cgroups for isolation, making them much "
            "lighter (faster startup, lower memory overhead) but with "
            "a weaker isolation boundary. VMs are preferred when "
            "running untrusted workloads or different OS kernels; "
            "containers are preferred for lightweight, homogeneous "
            "deployments."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does an OS handle out-of-memory (OOM) situations, "
            "and what is the OOM killer's selection strategy?"
        ),
        "expected_answer": (
            "When the system cannot free enough memory through "
            "reclaiming caches and swapping, the Linux OOM killer "
            "selects a process to terminate based on an oom_score that "
            "factors in the process's memory usage, nice value, and "
            "runtime. Processes using the most memory get the highest "
            "scores. The oom_score_adj tunable lets administrators "
            "protect critical processes (e.g. set to -1000 to make "
            "them unkillable). The OOM killer is a last resort; proper "
            "memory limits via cgroups and monitoring should prevent "
            "reaching this state."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how RCU (Read-Copy-Update) is used in "
            "the Linux kernel for synchronization."
        ),
        "expected_answer": (
            "RCU is a synchronization mechanism optimized for "
            "read-heavy workloads. Readers access shared data without "
            "acquiring any lock and are protected from seeing "
            "inconsistent state. Writers create a new version of the "
            "data, publish it atomically (via pointer swap), and defer "
            "freeing the old version until all pre-existing readers "
            "have finished (a grace period). This provides extremely "
            "low overhead for readers at the cost of slightly delayed "
            "memory reclamation and more complex update logic."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design an OS-level scheduler for "
            "a real-time embedded system?"
        ),
        "expected_answer": (
            "A real-time scheduler must guarantee that tasks meet "
            "their deadlines. It uses fixed-priority scheduling (Rate "
            "Monotonic for periodic tasks) or dynamic-priority "
            "scheduling (Earliest Deadline First). The system must "
            "perform schedulability analysis to ensure all tasks can "
            "meet deadlines under worst-case conditions. Interrupts "
            "must have bounded latency, kernel preemption must be "
            "supported, and priority inheritance is needed to handle "
            "priority inversion. Hardware timer resolution and "
            "deterministic memory allocation are also critical."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how memory compaction and paging interact "
            "to reduce external fragmentation."
        ),
        "expected_answer": (
            "Paging eliminates external fragmentation at the page "
            "level because any free physical frame can be mapped to "
            "any virtual page. However, fragmentation can still occur "
            "at larger granularities (e.g. when the kernel needs "
            "contiguous physical pages for DMA or huge pages). Memory "
            "compaction (used in the Linux buddy allocator) migrates "
            "movable pages to consolidate free blocks into larger "
            "contiguous regions. This is triggered when an allocation "
            "for a high-order (multi-page) block fails due to "
            "scattered free frames."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe how a hypervisor manages CPU and memory "
            "virtualization for guest OSes."
        ),
        "expected_answer": (
            "A Type 1 hypervisor (e.g. KVM, ESXi) runs directly on "
            "hardware and uses hardware virtualization extensions "
            "(Intel VT-x, AMD-V) to trap sensitive guest instructions "
            "without binary translation. The hypervisor schedules "
            "virtual CPUs onto physical CPUs and manages VMCS/VMCB "
            "structures for guest state. For memory, it maintains a "
            "second level of address translation (Extended Page Tables "
            "/ Nested Paging) that maps guest-physical addresses to "
            "host-physical addresses. Memory can be overcommitted "
            "using techniques like ballooning, KSM (Kernel Same-page "
            "Merging), and transparent huge pages."
        ),
    },
]


def seed_os_questions() -> None:
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
                    "Operating Systems interview questions "
                    "covering fundamentals, intermediate "
                    "concepts, and advanced topics."
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
                f"Operating Systems topic already contains "
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
        print("OPERATING SYSTEMS INTERVIEW QUESTION BANK CREATED")
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
    seed_os_questions()
