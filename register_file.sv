module register_file(
    input logic clk,
    input logic areset,
    input logic write_enable,
    input logic [1:0] write_address,
    input logic [3:0] write_data,
    input logic [1:0] read_address_a,
    input logic [1:0] read_address_b,
    output logic [3:0] read_data_a,
    output logic [3:0] read_data_b
);

    logic [3:0] registers [4];

    always_ff @(posedge clk or posedge areset) begin
        if (areset) begin
            registers[0] <= 4'b0000;
            registers[1] <= 4'b0000;
            registers[2] <= 4'b0000;
            registers[3] <= 4'b0000;
        end else if (write_enable) begin
            registers[write_address] <= write_data;
        end
    end

    always_comb begin
        read_data_a = registers[read_address_a];
        read_data_b = registers[read_address_b];
    end
endmodule