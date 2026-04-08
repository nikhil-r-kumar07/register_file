TOPLEVEL_LANG = verilog
VERILOG_SOURCES = register_file.sv
TOPLEVEL = register_file
MODULE = register_file_tb
SIM = icarus
include $(shell cocotb-config --makefiles)/Makefile.sim