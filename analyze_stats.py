# Python script to parse and analyze gem5 statistics
import re

# File path to stats.txt
stats_file = "m5out/stats.txt"

ipc = 0
total_cycles = 0
total_insts = 0

with open(stats_file, "r") as file:
    for line in file:
        # Find the IPC
        if "system.cpu.ipc" in line:
            ipc = float(line.split()[1])
            print(f"Instruction  Per Cycle (IPC): {ipc}")

        # Find the total cycles
        if "system.cpu.numCycles" in line:
            total_cycles = int(line.split()[1])
            print(f"Number of Cycles: {total_cycles}")
        # Find the total instructions
        if "system.cpu.instsIssued" in line:
            total_insts = int(line.split()[1])
            print(f"Total Number of Instructions {total_insts}")

# Calculate latency in cycles
if total_insts > 0:
    latency = total_cycles / total_insts
else:
    latency = None

# Output results
print(f"Instruction Throughput (IPC): {ipc}")
print(f"Instruction Latency (Cycles per Instruction): {latency}")
