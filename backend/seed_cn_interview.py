from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "Computer Networks"


QUESTIONS = [
    # =========================================================
    # EASY — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the OSI model? Name its seven layers."
        ),
        "expected_answer": (
            "The OSI (Open Systems Interconnection) model is a "
            "conceptual framework that standardizes network "
            "communication into seven layers. From bottom to top they "
            "are Physical, Data Link, Network, Transport, Session, "
            "Presentation, and Application. Each layer provides "
            "services to the layer above and relies on the layer below."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "TCP vs UDP -- key differences?"
        ),
        "expected_answer": (
            "TCP is connection-oriented, provides reliable in-order "
            "delivery with acknowledgments and retransmissions, and "
            "includes flow and congestion control. UDP is "
            "connectionless, provides best-effort delivery with no "
            "guarantees of ordering or reliability, and has lower "
            "overhead. TCP is used for web, email, and file transfer; "
            "UDP is used for DNS, streaming, and real-time applications."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is an IP address? IPv4 vs IPv6?"
        ),
        "expected_answer": (
            "An IP address is a numerical label assigned to each "
            "device on a network for identification and routing. IPv4 "
            "uses 32-bit addresses (about 4.3 billion addresses) in "
            "dotted-decimal notation. IPv6 uses 128-bit addresses in "
            "hexadecimal colon notation, providing a vastly larger "
            "address space and built-in features like simplified "
            "headers and IPsec support."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is DNS, and why is it needed?"
        ),
        "expected_answer": (
            "DNS (Domain Name System) translates human-readable domain "
            "names like example.com into IP addresses that computers "
            "use to route traffic. Without DNS, users would have to "
            "remember numeric IP addresses. DNS is a hierarchical, "
            "distributed system using root servers, TLD servers, and "
            "authoritative servers."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Hub vs switch vs router?"
        ),
        "expected_answer": (
            "A hub broadcasts incoming data to all ports (Layer 1, "
            "physical layer). A switch forwards data only to the "
            "specific port associated with the destination MAC address "
            "(Layer 2, data link layer). A router forwards packets "
            "between different networks based on IP addresses (Layer 3, "
            "network layer) and makes routing decisions."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the TCP three-way handshake?"
        ),
        "expected_answer": (
            "The three-way handshake establishes a TCP connection. The "
            "client sends a SYN segment, the server responds with "
            "SYN-ACK, and the client replies with ACK. After this "
            "exchange, both sides have synchronized sequence numbers "
            "and the connection is established for bidirectional data "
            "transfer."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "HTTP vs HTTPS?"
        ),
        "expected_answer": (
            "HTTP (HyperText Transfer Protocol) transmits data in "
            "plaintext, making it vulnerable to eavesdropping and "
            "tampering. HTTPS adds TLS/SSL encryption on top of HTTP, "
            "providing confidentiality, integrity, and server "
            "authentication via digital certificates. HTTPS uses "
            "port 443 by default instead of HTTP's port 80."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a MAC address?"
        ),
        "expected_answer": (
            "A MAC (Media Access Control) address is a 48-bit hardware "
            "identifier assigned to a network interface card by the "
            "manufacturer. It operates at the data link layer (Layer 2) "
            "and is used for local network communication within the "
            "same broadcast domain. MAC addresses are typically "
            "represented as six pairs of hexadecimal digits."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a LAN, WAN, and MAN?"
        ),
        "expected_answer": (
            "A LAN (Local Area Network) covers a small area like a "
            "building or campus with high speed and low latency. A "
            "MAN (Metropolitan Area Network) spans a city or metro "
            "area. A WAN (Wide Area Network) covers large geographical "
            "distances, connecting LANs across cities or countries, "
            "typically with lower speed and higher latency than a LAN."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a firewall?"
        ),
        "expected_answer": (
            "A firewall is a network security device or software that "
            "monitors and controls incoming and outgoing network "
            "traffic based on predefined security rules. It establishes "
            "a barrier between a trusted internal network and untrusted "
            "external networks, blocking unauthorized access while "
            "permitting legitimate traffic."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a port number, and why is it needed?"
        ),
        "expected_answer": (
            "A port number is a 16-bit integer (0-65535) that "
            "identifies a specific application or service on a host. "
            "It allows multiple services to share the same IP address "
            "by differentiating traffic. Well-known ports include 80 "
            "for HTTP, 443 for HTTPS, 22 for SSH, and 53 for DNS."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a static and "
            "dynamic IP address?"
        ),
        "expected_answer": (
            "A static IP address is manually assigned and does not "
            "change, making it suitable for servers and network "
            "devices that need a permanent address. A dynamic IP "
            "address is assigned automatically by a DHCP server and "
            "may change over time, which is more efficient for "
            "networks with many transient clients."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is bandwidth vs latency?"
        ),
        "expected_answer": (
            "Bandwidth is the maximum rate of data transfer across a "
            "network link, measured in bits per second. Latency is the "
            "time it takes for a packet to travel from source to "
            "destination, measured in milliseconds. High bandwidth "
            "means more data can flow at once; low latency means "
            "faster response times. Both affect user-perceived "
            "performance."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the purpose of the ARP protocol?"
        ),
        "expected_answer": (
            "ARP (Address Resolution Protocol) maps a known IP address "
            "to the corresponding MAC address on a local network. When "
            "a device needs to send a frame to an IP address on the "
            "same subnet, it broadcasts an ARP request; the device "
            "with that IP replies with its MAC address, which is then "
            "cached for future use."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a proxy server?"
        ),
        "expected_answer": (
            "A proxy server is an intermediary that sits between a "
            "client and a destination server. It forwards requests on "
            "behalf of clients, providing benefits such as caching, "
            "anonymity, content filtering, and access control. Proxies "
            "can operate at different layers and may handle HTTP, "
            "SOCKS, or other protocols."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between unicast, multicast, "
            "and broadcast?"
        ),
        "expected_answer": (
            "Unicast sends data from one sender to one specific "
            "receiver. Multicast sends data from one sender to a "
            "group of interested receivers. Broadcast sends data from "
            "one sender to all devices on the network. Unicast is "
            "the most common; multicast is used for streaming and "
            "routing protocols; broadcast is limited to local "
            "network segments."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a VPN, and why is it used?"
        ),
        "expected_answer": (
            "A VPN (Virtual Private Network) creates an encrypted "
            "tunnel over a public network (typically the internet) to "
            "securely connect remote users or sites to a private "
            "network. It provides confidentiality, data integrity, "
            "and can mask the user's IP address. VPNs are commonly "
            "used for remote work and bypassing geographic restrictions."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between HTTP GET and POST?"
        ),
        "expected_answer": (
            "GET requests data from a server and appends parameters "
            "in the URL query string; it is idempotent and cacheable. "
            "POST submits data to a server in the request body, "
            "typically to create or modify a resource; it is not "
            "idempotent by default and is not cached. GET should not "
            "be used for sensitive data because parameters are visible "
            "in the URL."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a subnet mask?"
        ),
        "expected_answer": (
            "A subnet mask is a 32-bit number that separates the "
            "network portion of an IP address from the host portion. "
            "It determines which part of the address identifies the "
            "network and which part identifies the specific host. "
            "For example, 255.255.255.0 (/24) means the first 24 bits "
            "are the network and the last 8 bits are the host."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a domain name and a URL?"
        ),
        "expected_answer": (
            "A domain name is the human-readable name of a website, "
            "such as example.com. A URL (Uniform Resource Locator) is "
            "the full web address that includes the protocol, domain "
            "name, port, path, and optional query parameters, such as "
            "https://example.com/page?id=1. The domain name is one "
            "component of a URL."
        ),
    },

    # =========================================================
    # MEDIUM — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain DNS resolution step by step."
        ),
        "expected_answer": (
            "When a client queries a domain name, it first checks its "
            "local cache and hosts file. If not found, it sends a "
            "recursive query to its configured DNS resolver. The "
            "resolver queries the root name servers to find the TLD "
            "server, then the TLD server to find the authoritative "
            "name server, and finally the authoritative server to get "
            "the IP address. Each answer may be cached with a TTL. "
            "The resolver returns the IP to the client."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Flow control vs congestion control in TCP?"
        ),
        "expected_answer": (
            "Flow control prevents a fast sender from overwhelming a "
            "slow receiver by using a receive window (rwnd) advertised "
            "by the receiver. Congestion control prevents the sender "
            "from overwhelming the network by maintaining a congestion "
            "window (cwnd) that responds to packet loss and delay "
            "signals. The effective sending rate is limited by the "
            "minimum of rwnd and cwnd."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain subnetting with a worked example."
        ),
        "expected_answer": (
            "Subnetting divides a network into smaller sub-networks. "
            "For example, a /24 network 192.168.1.0/24 has 256 "
            "addresses. Splitting it into two /25 subnets gives "
            "192.168.1.0/25 (hosts .1-.126) and 192.168.1.128/25 "
            "(hosts .129-.254), each with 126 usable hosts. The extra "
            "subnet bit borrows from the host portion, doubling the "
            "number of networks while halving the hosts per network."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is NAT, and why is it needed?"
        ),
        "expected_answer": (
            "NAT (Network Address Translation) maps private IP "
            "addresses to one or more public IP addresses at a router "
            "or gateway. It was introduced to conserve the limited "
            "IPv4 address space by allowing multiple devices on a "
            "private network to share a single public IP. NAT also "
            "provides a basic layer of security by hiding internal "
            "network structure from external hosts."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Symmetric vs asymmetric encryption -- role in TLS?"
        ),
        "expected_answer": (
            "Symmetric encryption uses the same key for encryption and "
            "decryption and is fast (e.g. AES). Asymmetric encryption "
            "uses a public-private key pair and is slower but solves "
            "the key distribution problem (e.g. RSA, ECDHE). In TLS, "
            "asymmetric encryption is used during the handshake to "
            "securely exchange or derive a shared session key, which "
            "is then used for symmetric encryption of the actual data "
            "for performance."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are sockets, and how does client-server "
            "communication use them?"
        ),
        "expected_answer": (
            "A socket is an endpoint for network communication, "
            "identified by an IP address and port number. In "
            "client-server communication, the server creates a socket, "
            "binds it to an address and port, and listens for "
            "connections. The client creates a socket and connects to "
            "the server's address. Once connected, both sides can send "
            "and receive data through their sockets."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Layer 4 vs Layer 7 load balancing?"
        ),
        "expected_answer": (
            "Layer 4 (transport) load balancing makes routing decisions "
            "based on IP addresses and TCP/UDP port numbers without "
            "inspecting the payload, offering lower latency and higher "
            "throughput. Layer 7 (application) load balancing inspects "
            "the application-layer content (e.g. HTTP headers, URL "
            "paths, cookies) and can make more intelligent routing "
            "decisions like content-based routing, SSL termination, "
            "and header manipulation, but with more processing "
            "overhead."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the difference between a stateful and "
            "stateless firewall."
        ),
        "expected_answer": (
            "A stateless firewall filters packets individually based "
            "on static rules (source/destination IP, port, protocol) "
            "without tracking connection state. A stateful firewall "
            "tracks the state of active connections and allows return "
            "traffic that belongs to an established session, providing "
            "better security because it can distinguish legitimate "
            "return traffic from unsolicited inbound packets."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is HTTP keep-alive, and how does it "
            "improve performance?"
        ),
        "expected_answer": (
            "HTTP keep-alive (persistent connections) reuses a single "
            "TCP connection for multiple HTTP request-response pairs "
            "instead of opening a new connection for each request. "
            "This eliminates the overhead of repeated TCP three-way "
            "handshakes and slow-start phases, reducing latency and "
            "server resource consumption. It is the default behavior "
            "in HTTP/1.1."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how ping and traceroute work."
        ),
        "expected_answer": (
            "ping sends ICMP Echo Request packets to a destination "
            "and measures the round-trip time from the Echo Reply, "
            "checking reachability and latency. traceroute sends "
            "packets with incrementally increasing TTL values; each "
            "router along the path decrements the TTL and sends back "
            "an ICMP Time Exceeded message when TTL reaches zero, "
            "revealing each hop and its latency on the route to the "
            "destination."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between TCP's fast retransmit "
            "and timeout-based retransmission?"
        ),
        "expected_answer": (
            "Timeout-based retransmission waits for a retransmission "
            "timeout (RTO) to expire before resending a lost segment, "
            "which can introduce significant delay. Fast retransmit "
            "triggers retransmission after receiving three duplicate "
            "ACKs for the same segment, indicating a likely loss "
            "without waiting for the timeout. Fast retransmit enables "
            "quicker recovery and is paired with fast recovery to "
            "avoid reducing the congestion window as aggressively."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the concept of a VLAN and why it's used."
        ),
        "expected_answer": (
            "A VLAN (Virtual LAN) logically segments a physical "
            "network into separate broadcast domains at Layer 2, "
            "even across different physical switches. Devices on "
            "different VLANs cannot communicate directly without a "
            "router (inter-VLAN routing). VLANs improve security by "
            "isolating traffic, reduce broadcast traffic, and simplify "
            "network management by grouping devices logically rather "
            "than physically."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the role of a DHCP server?"
        ),
        "expected_answer": (
            "A DHCP (Dynamic Host Configuration Protocol) server "
            "automatically assigns IP addresses and network "
            "configuration (subnet mask, default gateway, DNS servers) "
            "to devices on a network. It uses a four-step process: "
            "Discover, Offer, Request, Acknowledge (DORA). DHCP "
            "simplifies network administration by eliminating the "
            "need for manual IP assignment and manages address reuse "
            "through leases."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how HTTPS certificate validation works "
            "(chain of trust)."
        ),
        "expected_answer": (
            "When a client connects via HTTPS, the server presents "
            "its certificate. The client verifies the certificate's "
            "signature against the issuing Certificate Authority (CA). "
            "If the CA is not directly trusted, the client follows the "
            "chain of intermediate CAs up to a root CA in its trust "
            "store. The client also checks that the certificate is not "
            "expired, not revoked (via CRL or OCSP), and that the "
            "domain name matches."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between forward and "
            "reverse proxies?"
        ),
        "expected_answer": (
            "A forward proxy sits in front of clients and forwards "
            "their requests to the internet, providing anonymity, "
            "caching, and access control for clients. A reverse proxy "
            "sits in front of servers and forwards incoming requests "
            "from the internet to backend servers, providing load "
            "balancing, SSL termination, caching, and security for "
            "the servers."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how QUIC differs from TCP for modern "
            "web transport."
        ),
        "expected_answer": (
            "QUIC is a transport protocol built on top of UDP that "
            "integrates TLS 1.3 encryption directly, reducing "
            "connection setup to a single round trip (or zero for "
            "resumed connections). Unlike TCP, QUIC supports "
            "multiplexed streams without head-of-line blocking, so "
            "a lost packet in one stream does not stall others. QUIC "
            "also supports connection migration across network changes "
            "using connection IDs rather than IP/port tuples."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is head-of-line blocking, and how does "
            "HTTP/2 address it?"
        ),
        "expected_answer": (
            "Head-of-line (HOL) blocking occurs when the first item "
            "in a queue blocks all subsequent items. In HTTP/1.1, a "
            "slow response blocks later requests on the same "
            "connection. HTTP/2 addresses this at the application "
            "layer by multiplexing multiple streams over a single TCP "
            "connection, allowing responses to interleave. However, "
            "TCP-level HOL blocking remains because a lost TCP segment "
            "stalls all streams until it is retransmitted."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how routing protocols like OSPF differ "
            "from static routing."
        ),
        "expected_answer": (
            "Static routing uses manually configured fixed routes that "
            "do not adapt to network changes, making it simple but "
            "unsuitable for large or dynamic networks. OSPF (Open "
            "Shortest Path First) is a dynamic link-state routing "
            "protocol that automatically discovers neighbors, "
            "exchanges topology information, and computes shortest "
            "paths using Dijkstra's algorithm. OSPF adapts to link "
            "failures and topology changes without manual intervention."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between a session and a cookie?"
        ),
        "expected_answer": (
            "A cookie is a small piece of data stored on the client's "
            "browser and sent with every subsequent request to the same "
            "server. A session is server-side state associated with a "
            "client, typically identified by a session ID stored in a "
            "cookie. Cookies persist across browser restarts if given "
            "an expiry; sessions typically expire after a period of "
            "inactivity or when the server clears them."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how a CDN caches and serves content "
            "closer to users."
        ),
        "expected_answer": (
            "A CDN (Content Delivery Network) is a geographically "
            "distributed network of edge servers that cache content "
            "close to end users. When a user requests content, DNS "
            "directs the request to the nearest edge server. If the "
            "edge has a cached copy, it serves it directly with low "
            "latency. On a cache miss, the edge fetches from the "
            "origin server, caches the response, and serves the user. "
            "Cache headers (Cache-Control, TTL) control freshness."
        ),
    },

    # =========================================================
    # HARD — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain TCP congestion control (slow start, "
            "congestion avoidance, fast recovery)."
        ),
        "expected_answer": (
            "TCP congestion control regulates the sending rate to "
            "avoid overwhelming the network. Slow start begins with "
            "a small congestion window (cwnd) and doubles it each RTT "
            "until it reaches the slow-start threshold (ssthresh). "
            "Congestion avoidance then increases cwnd linearly by one "
            "segment per RTT. On detecting loss via three duplicate "
            "ACKs, fast recovery halves cwnd and ssthresh, retransmits "
            "the lost segment, and inflates cwnd for each additional "
            "duplicate ACK received, transitioning back to congestion "
            "avoidance once the loss is acknowledged. Timeout loss "
            "resets cwnd to one segment and re-enters slow start."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Walk through the full TLS handshake including "
            "key exchange."
        ),
        "expected_answer": (
            "In TLS 1.2, the client sends ClientHello (supported "
            "cipher suites, random). The server responds with "
            "ServerHello (chosen suite, random), its certificate, and "
            "ServerKeyExchange (e.g. ECDHE parameters). The client "
            "verifies the certificate chain, generates a premaster "
            "secret (or derives it via ECDHE), and sends "
            "ClientKeyExchange. Both sides derive the master secret "
            "from the premaster and randoms, compute session keys, "
            "exchange ChangeCipherSpec, and send Finished messages "
            "encrypted with the new keys. TLS 1.3 simplifies this to "
            "one round trip by sending key shares in the ClientHello."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does BGP work, and why is it critical to "
            "internet routing?"
        ),
        "expected_answer": (
            "BGP (Border Gateway Protocol) is the path-vector protocol "
            "that exchanges routing information between autonomous "
            "systems (ASes) on the internet. Each BGP speaker "
            "advertises reachable IP prefixes along with the AS path. "
            "Route selection considers policies, AS path length, and "
            "attributes like local preference and MED. BGP is critical "
            "because it is the glue that connects ISPs, cloud "
            "providers, and enterprise networks, determining how "
            "traffic flows across the global internet. BGP "
            "misconfigurations or hijacks can cause widespread outages."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does a CDN handle cache invalidation at scale?"
        ),
        "expected_answer": (
            "CDNs use a combination of TTL-based expiration, explicit "
            "purge APIs, and surrogate keys (tags) for grouped "
            "invalidation. When content changes, the origin can issue "
            "a purge request that propagates to edge nodes. Surrogate "
            "keys allow invalidating all objects associated with a "
            "logical entity in one operation. Soft purging marks "
            "content as stale and serves it while revalidating in the "
            "background. At scale, eventual consistency is accepted "
            "because propagating purges to thousands of edge nodes "
            "takes finite time."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "WebSockets vs long-polling -- trade-offs for "
            "real-time systems?"
        ),
        "expected_answer": (
            "Long-polling holds an HTTP request open until the server "
            "has data, then the client immediately sends a new request. "
            "It works through standard HTTP infrastructure but wastes "
            "connections and adds latency on each reconnect. WebSockets "
            "upgrade an HTTP connection to a persistent, full-duplex "
            "channel with very low overhead per message. WebSockets "
            "are better for high-frequency, bidirectional communication "
            "but require WebSocket-aware proxies and load balancers. "
            "Long-polling is simpler to deploy behind restrictive "
            "firewalls."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How do distributed systems handle network partitions "
            "(CAP theorem in practice)?"
        ),
        "expected_answer": (
            "During a network partition, a system must choose between "
            "consistency and availability. CP systems (e.g. ZooKeeper, "
            "etcd) reject or block requests on the minority side to "
            "preserve consistency. AP systems (e.g. Cassandra, DynamoDB "
            "in certain configurations) continue serving requests on "
            "both sides, accepting the risk of divergent data that "
            "must be reconciled later. In practice, most systems are "
            "tunable: operators choose consistency levels per operation "
            "rather than making a global CAP choice."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how consistent hashing helps distribute "
            "load across servers in a networked system."
        ),
        "expected_answer": (
            "Consistent hashing maps both servers and request keys "
            "onto a hash ring. Each request is routed to the first "
            "server encountered clockwise on the ring. Adding or "
            "removing a server only remaps the keys between the "
            "affected server and its predecessor, minimizing "
            "redistribution. Virtual nodes (multiple positions per "
            "server) improve balance. This is widely used in "
            "distributed caches, CDNs, and load balancers to achieve "
            "even distribution with minimal disruption during scaling."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does DNS load balancing differ from a "
            "hardware load balancer?"
        ),
        "expected_answer": (
            "DNS load balancing distributes traffic by returning "
            "different IP addresses for the same domain, often using "
            "round-robin or geographic policies. It is simple and "
            "scales well but has limitations: DNS responses are cached "
            "for the TTL, so failover is slow, and it cannot consider "
            "server health or current load. A hardware (or software) "
            "load balancer operates at Layer 4 or 7 in the data path, "
            "can perform real-time health checks, route based on "
            "current load, and remove failed servers immediately."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how QUIC/HTTP3 reduces connection setup "
            "latency versus TCP+TLS."
        ),
        "expected_answer": (
            "TCP+TLS 1.2 requires a three-way TCP handshake plus a "
            "two-round-trip TLS handshake (three total round trips, "
            "or two with TLS 1.3). QUIC merges transport and "
            "cryptographic handshakes into a single round trip using "
            "TLS 1.3 integrated into the protocol. For previously "
            "connected servers, QUIC supports 0-RTT resumption, "
            "allowing data to be sent with the first packet. Since "
            "QUIC runs over UDP, it also avoids kernel-level TCP "
            "overhead and OS-level HOL blocking."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design a globally distributed rate "
            "limiter across data centers?"
        ),
        "expected_answer": (
            "A globally distributed rate limiter can use a local "
            "token bucket per data center with periodic synchronization "
            "of usage counts via a shared store (e.g. Redis with "
            "replication). Each data center enforces a local limit as "
            "a fraction of the global limit and asynchronously reports "
            "usage. A sliding window approach with eventual consistency "
            "accepts minor over-admission during sync intervals. For "
            "strict limits, a centralized coordination service or "
            "consensus protocol is needed, trading latency for "
            "accuracy."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how anycast routing is used by CDNs "
            "and DNS providers."
        ),
        "expected_answer": (
            "Anycast assigns the same IP address to multiple servers "
            "in different geographic locations. BGP routing directs "
            "each client's packets to the nearest (topologically "
            "closest) server based on the routing table. CDNs and DNS "
            "providers use anycast to automatically route users to the "
            "closest edge server without application-layer redirection. "
            "It also provides natural DDoS resilience because attack "
            "traffic is distributed across all anycast nodes rather "
            "than concentrated at one."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does packet fragmentation and reassembly work, "
            "and what problems can it cause (e.g., MTU mismatch)?"
        ),
        "expected_answer": (
            "When a packet exceeds a link's MTU (Maximum Transmission "
            "Unit), it must be fragmented into smaller pieces that fit. "
            "Each fragment carries offset information so the "
            "destination can reassemble the original packet. Problems "
            "include reassembly overhead, out-of-order fragments, "
            "increased loss probability (losing one fragment discards "
            "the entire packet), and security issues (fragmentation "
            "attacks). Path MTU Discovery is used to avoid "
            "fragmentation by setting the Don't Fragment flag and "
            "adjusting the sending size based on ICMP feedback."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how a Service Mesh (e.g., Istio) manages "
            "traffic between microservices."
        ),
        "expected_answer": (
            "A service mesh deploys a sidecar proxy (e.g. Envoy) "
            "alongside each service instance. All inter-service "
            "traffic passes through the proxy, which handles load "
            "balancing, retries, timeouts, circuit breaking, mutual "
            "TLS, and observability (metrics, tracing, logging) "
            "without application code changes. A control plane (e.g. "
            "Istio's istiod) configures the sidecar proxies "
            "dynamically. This separates networking concerns from "
            "business logic but adds latency and resource overhead "
            "from the extra network hop."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you debug intermittent packet loss "
            "in a production network?"
        ),
        "expected_answer": (
            "Start by verifying the scope: use ping and mtr/traceroute "
            "from multiple sources to isolate which hop or segment is "
            "dropping packets. Check interface error counters (CRC "
            "errors, drops, overruns) on switches and routers via SNMP "
            "or CLI. Examine buffer utilization and queue depths for "
            "congestion. Use packet captures (tcpdump, Wireshark) at "
            "both ends to confirm which packets are lost. Check for "
            "MTU mismatches, duplex mismatches, or faulty cables. "
            "Correlate with time-of-day traffic patterns and review "
            "firewall/ACL logs for inadvertent drops."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how mutual TLS (mTLS) is used for "
            "service-to-service authentication."
        ),
        "expected_answer": (
            "In standard TLS, only the server presents a certificate. "
            "In mutual TLS, the client also presents a certificate "
            "that the server validates, authenticating both parties. "
            "Each service is provisioned with its own certificate and "
            "private key, typically managed by a certificate authority "
            "internal to the organization. mTLS ensures that only "
            "authorized services can communicate, providing identity "
            "verification, encryption, and integrity for east-west "
            "traffic in microservice architectures."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How does multi-path TCP or connection multiplexing "
            "improve throughput?"
        ),
        "expected_answer": (
            "Multi-path TCP (MPTCP) allows a single TCP connection to "
            "use multiple network paths (e.g. WiFi and cellular) "
            "simultaneously. It splits data across subflows, each on "
            "a different path, and reassembles them at the receiver. "
            "This increases aggregate throughput, improves resilience "
            "to single-path failures, and enables seamless connection "
            "migration. Connection multiplexing at the application "
            "layer (e.g. HTTP/2 streams) similarly improves throughput "
            "by sending multiple logical streams over one connection, "
            "reducing connection overhead."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how DDoS mitigation systems detect and "
            "absorb attack traffic."
        ),
        "expected_answer": (
            "DDoS mitigation systems use traffic profiling to "
            "establish baselines and detect anomalies (e.g. sudden "
            "spikes in packet rate, unusual geographic sources). "
            "Detection techniques include rate analysis, protocol "
            "anomaly detection, and machine learning models. "
            "Mitigation involves scrubbing traffic through specialized "
            "hardware or software that filters malicious packets while "
            "passing legitimate traffic. Techniques include SYN "
            "cookies, rate limiting, IP reputation filtering, and "
            "anycast-based dispersion. Large-scale providers absorb "
            "volumetric attacks by distributing traffic across many "
            "PoPs."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design a network architecture for "
            "a low-latency real-time multiplayer game?"
        ),
        "expected_answer": (
            "Use UDP-based transport for game state updates to avoid "
            "TCP retransmission delays. Deploy game servers in regions "
            "close to players using edge locations. Implement client-side "
            "prediction and server reconciliation to mask network "
            "latency. Use a tick-rate model where the server simulates "
            "the game state at a fixed rate and sends authoritative "
            "snapshots. Employ delta compression to minimize packet "
            "size. A matchmaking service should group players by "
            "proximity to minimize round-trip times. DDoS protection "
            "and IP obfuscation are critical for game servers."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how software-defined networking (SDN) "
            "decouples the control and data planes."
        ),
        "expected_answer": (
            "In traditional networking, each switch or router contains "
            "both a control plane (routing decisions) and a data plane "
            "(packet forwarding). SDN separates these: a centralized "
            "controller maintains the network-wide view and pushes "
            "forwarding rules to the switches via protocols like "
            "OpenFlow. The switches become simple forwarding devices. "
            "This centralization enables programmable, dynamic network "
            "management, easier policy enforcement, and faster "
            "innovation, but introduces a single point of failure "
            "that must be addressed with controller redundancy."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe how you'd design cross-region failover "
            "for a globally available API."
        ),
        "expected_answer": (
            "Deploy the API in multiple regions with independent "
            "infrastructure. Use DNS-based or anycast-based global "
            "load balancing with health checks to route traffic to "
            "healthy regions. Database replication (synchronous for "
            "critical data, asynchronous for high throughput) keeps "
            "data available in each region. On failure, health checks "
            "detect the outage and DNS or the global load balancer "
            "redirects traffic to a surviving region. Stateless "
            "services and externalized session state (e.g. in Redis) "
            "enable seamless failover. Regular chaos engineering "
            "exercises validate the failover path."
        ),
    },
]


def seed_cn_questions() -> None:
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
                    "Computer Networks interview questions "
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
                f"Computer Networks topic already contains "
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
        print("COMPUTER NETWORKS INTERVIEW QUESTION BANK CREATED")
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
    seed_cn_questions()
