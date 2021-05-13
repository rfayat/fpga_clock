module Frequency_Diviser(
  input clk ,
  input reset ,
  output pulse
);
  /* Create a frequency divider.
  Pulse is set to True for one clk period every FREQ_CLK periods of clk */
  parameter FREQ_CLK = 50000000; // Clock frequency

  function integer Size (input integer in);
    // Return the number of bits necessary to represent in
    for (Size=0; in>0; Size=Size+1) in = in >> 1;
  endfunction

  // Assign a counter with same size as FREQ_CLK - 1
  reg [Size(FREQ_CLK - 1) - 1:0] cpt;

  // On each positive edge of clk increment the counter cpt
  // And reset it to the 0 when we reach FREQ_CLK
  always @(posedge clk) begin
    if (reset)
      cpt <= 0;  // set the counter to 0
    else
      // Reset the counter if we reached FreQ_CLK
      if (cpt == FREQ_CLK - 1) cpt <= 0;
      // else increment the counter
      else cpt <= cpt + 1;
  end

  // True on one edge of each FREQ_CLK clk positive edges
  assign pulse = cpt==FREQ_CLK - 1;

endmodule
