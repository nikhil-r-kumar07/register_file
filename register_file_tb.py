import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_write(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units = "ns").start())
    dut.write_enable.value = 1
    dut.write_address.value = 2
    dut.write_data.value = 5
    dut.read_address_a.value = 2
    await RisingEdge(dut.clk)
    await Timer(1, units = "ns")
    assert dut.read_data_a.value == 5, "Write operation works correctly"

@cocotb.test()
async def test_address(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units = "ns").start())
    dut.write_enable.value = 1
    dut.write_address.value = 2
    dut.write_data.value = 5
    dut.read_address_a.value = 0
    await RisingEdge(dut.clk)
    await Timer(1, units = "ns")
    assert dut.read_data_a.value == 0, "Addressing works correctly"

@cocotb.test()
async def test_write_enable(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units = "ns").start())
    dut.write_enable.value = 0
    dut.write_address.value = 2
    dut.write_data.value = 5
    dut.read_address_a.value = 2
    await RisingEdge(dut.clk)
    await Timer(1, units = "ns")
    assert dut.read_data_a.value == 0, "Write enable works correctly"

@cocotb.test()
async def test_write_simultaneously(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units = "ns").start())
    dut.write_enable.value = 1
    dut.write_address.value = 2
    dut.write_data.value = 5
    await RisingEdge(dut.clk)
    dut.write_address.value = 3
    dut.write_data.value = 4
    await RisingEdge(dut.clk)
    dut.read_address_a.value = 2
    dut.read_address_b.value = 3
    await RisingEdge(dut.clk)
    await Timer(1, units = "ns")
    assert dut.read_data_a.value == 5 and dut.read_data_b.value == 4, "Write address doesn't work simultaneously"

@cocotb.test()
async def test_overwrite(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units = "ns").start())
    dut.write_enable.value = 1
    dut.write_address.value = 2
    dut.write_data.value = 5
    await RisingEdge(dut.clk)
    dut.write_address.value = 2
    dut.write_data.value = 4
    await RisingEdge(dut.clk)
    dut.read_address_a.value = 2
    await RisingEdge(dut.clk)
    await Timer(1, units = "ns")
    assert dut.read_data_a.value == 4, "Overwrite works correctly"