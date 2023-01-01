module acacia (clk, r0, r1, r2, a0, a1, a2);
input clk, r0, r1, r2;
output a0, a1, a2;
wire a0, a1, a2;
reg [3:0] state;

assign a0 = (state == 10 || state == 4 || state == 5);
assign a1 = (state == 2 || state == 7 || state == 9);
assign a2 = (state == 0 || state == 1 || state == 3 || state == 6);

initial begin 
 	state = 8;
end

always @(posedge clk)
	case(state)
	8 : begin
		if (!r0 && !r1 && !r2) state = 8;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 9;
		if (!r0 && r1 && r2) state = 0;
		if (r0 && !r1 && !r2) state = 4;
		if (r0 && !r1 && r2) state = 3;
		if (r0 && r1 && !r2) state = 2;
		if (r0 && r1 && r2) state = 6;
	end
	1 : begin
		if (!r0 && !r1 && !r2) state = 1;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 0;
		if (!r0 && r1 && r2) state = 0;
		if (r0 && !r1 && !r2) state = 3;
		if (r0 && !r1 && r2) state = 3;
		if (r0 && r1 && !r2) state = 2;
		if (r0 && r1 && r2) state = 2;
	end
	0 : begin
		if (!r0 && !r1 && !r2) state = 7;
		if (!r0 && !r1 && r2) state = 7;
		if (!r0 && r1 && !r2) state = 7;
		if (!r0 && r1 && r2) state = 7;
		if (r0 && !r1 && !r2) state = 2;
		if (r0 && !r1 && r2) state = 2;
		if (r0 && r1 && !r2) state = 2;
		if (r0 && r1 && r2) state = 2;
	end
	6 : begin
		if (!r0 && !r1 && !r2) state = 2;
		if (!r0 && !r1 && r2) state = 2;
		if (!r0 && r1 && !r2) state = 2;
		if (!r0 && r1 && r2) state = 2;
		if (r0 && !r1 && !r2) state = 2;
		if (r0 && !r1 && r2) state = 2;
		if (r0 && r1 && !r2) state = 2;
		if (r0 && r1 && r2) state = 2;
	end
	3 : begin
		if (!r0 && !r1 && !r2) state = 10;
		if (!r0 && !r1 && r2) state = 10;
		if (!r0 && r1 && !r2) state = 5;
		if (!r0 && r1 && r2) state = 5;
		if (r0 && !r1 && !r2) state = 10;
		if (r0 && !r1 && r2) state = 10;
		if (r0 && r1 && !r2) state = 5;
		if (r0 && r1 && r2) state = 5;
	end
	7 : begin
		if (!r0 && !r1 && !r2) state = 1;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 1;
		if (!r0 && r1 && r2) state = 1;
		if (r0 && !r1 && !r2) state = 3;
		if (r0 && !r1 && r2) state = 3;
		if (r0 && r1 && !r2) state = 3;
		if (r0 && r1 && r2) state = 3;
	end
	2 : begin
		if (!r0 && !r1 && !r2) state = 5;
		if (!r0 && !r1 && r2) state = 10;
		if (!r0 && r1 && !r2) state = 5;
		if (!r0 && r1 && r2) state = 10;
		if (r0 && !r1 && !r2) state = 5;
		if (r0 && !r1 && r2) state = 10;
		if (r0 && r1 && !r2) state = 5;
		if (r0 && r1 && r2) state = 10;
	end
	10 : begin
		if (!r0 && !r1 && !r2) state = 1;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 0;
		if (!r0 && r1 && r2) state = 0;
		if (r0 && !r1 && !r2) state = 1;
		if (r0 && !r1 && r2) state = 1;
		if (r0 && r1 && !r2) state = 0;
		if (r0 && r1 && r2) state = 0;
	end
	5 : begin
		if (!r0 && !r1 && !r2) state = 9;
		if (!r0 && !r1 && r2) state = 7;
		if (!r0 && r1 && !r2) state = 9;
		if (!r0 && r1 && r2) state = 7;
		if (r0 && !r1 && !r2) state = 9;
		if (r0 && !r1 && r2) state = 7;
		if (r0 && r1 && !r2) state = 9;
		if (r0 && r1 && r2) state = 7;
	end
	9 : begin
		if (!r0 && !r1 && !r2) state = 9;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 9;
		if (!r0 && r1 && r2) state = 1;
		if (r0 && !r1 && !r2) state = 2;
		if (r0 && !r1 && r2) state = 3;
		if (r0 && r1 && !r2) state = 2;
		if (r0 && r1 && r2) state = 3;
	end
	4 : begin
		if (!r0 && !r1 && !r2) state = 4;
		if (!r0 && !r1 && r2) state = 1;
		if (!r0 && r1 && !r2) state = 9;
		if (!r0 && r1 && r2) state = 0;
		if (r0 && !r1 && !r2) state = 4;
		if (r0 && !r1 && r2) state = 1;
		if (r0 && r1 && !r2) state = 9;
		if (r0 && r1 && r2) state = 0;
	end
	endcase

endmodule
