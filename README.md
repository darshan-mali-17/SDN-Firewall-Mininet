# SDN Firewall using Mininet and POX

## Problem Statement

This project implements a Software Defined Networking (SDN) firewall using Mininet and POX controller to block malicious traffic.

## Objective

* Demonstrate controller-switch interaction
* Implement flow rules using OpenFlow
* Block specific host dynamically

## Tools Used

* Mininet
* POX Controller
* OpenFlow Protocol

## Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)

## Implementation

* Controller listens to packet_in events
* Matches source IP address
* Blocks host 10.0.0.2
* Allows normal traffic

## Test Cases

### Allowed Traffic

Command: h1 ping h3
Result: Successful communication

### Blocked Traffic

Command: h2 ping h1
Result: 100% packet loss

## Performance Analysis

### Latency

Measured using ping

### Throughput

Measured using iperf (~2–3 Mbits/sec)

## Conclusion

The SDN controller successfully controls traffic and blocks malicious hosts dynamically.

## Screenshots

Screenshots are included in this repository.
