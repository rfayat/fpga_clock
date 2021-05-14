module Toggle(
  input clk,
  input enable,
  input pulse,
  input reset,
  output out
);
  reg toggled;

  // Toggle the output
  always @(posedge clk) begin
    if (reset) toggled <= 0;
    else if (pulse) toggled <= !toggled;
  end

  assign out = toggled & enable;
endmodule
