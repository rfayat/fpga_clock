module fpga_clock(
  input clk ,
  input enable, // pin 87 (RPI GPIO 23)
  input reset,  // pin 89 (RPI GPIO 24)
  output syncout,  // pin 73
  output is_on, // pin 96
  output is_enabled // pin 93
  );

  parameter FREQ_CLK = 25000000;
  wire pulsePeriodique ; // True for one clk period every FREQ_CLK clk posedges

  // LED on pin 81 indicating that the FPGA is on
  assign is_on = 1;

  // LED on pin
  assign is_enabled = enable;

  // Create the frequency diviser
  Frequency_Diviser #(.FREQ_CLK(FREQ_CLK)) diviser(
    .clk(clk),
    .reset(reset),
    .pulse(pulsePeriodique)
  );

  Toggle toggle(
    .clk(clk),
    .enable(enable),
    .pulse(pulsePeriodique),
    .reset(reset),
    .out(syncout)
  );
endmodule
