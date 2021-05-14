module fpga_clock(
  input clk ,
  input enable,
  input reset ,
  output syncout);

  parameter FREQ_CLK = 2000000;
  wire pulsePeriodique ; // True for one clk period every FREQ_CLK clk posedges

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
