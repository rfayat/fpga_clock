module Toggle(
  input in,
  input reset,
  output out
);
  reg toggled;
  /* Create a toggle.
  out changes value on each posedge of in */
  always @(posedge in) begin
    if (reset) toggled <= 0;  // set the counter to 0
    else toggled <= !toggled;
  end

  assign out = toggled;
endmodule
