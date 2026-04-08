# Register File
An array of registers that can be read and written. Reading does not destroy the data in the register.
## How It Works
Given an input of an address and data to write, a corresponding register can be overwritten. Writing is not synchronous.
Given an input of an address to read, a corresponding register can be read without destroying the data. Up to two addresses can be read. 
## Features
- Always flip flop block for sequential logic (updating written addresses)
- Always combinational block for combinational logic (reading addresses)
- Asynchronous Reset
- Verified with self-checking cocotb testbenches
## Files
- `register_file.sv` - RTL Design
- `register_file_tb.py` - Python cocotb testbench
- `Makefile` - cocotb simulation build
## How to Simulate
``` bash
make
```
## Tools
Icarus verilog, cocotb
## Status
Simulated and verified