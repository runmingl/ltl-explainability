module acacia (clk, cancel, go, req, grant);
input clk, cancel, go, req;
output grant;
wire grant;
reg [0:0] state;

assign grant = (state == 0);

initial begin 
 	state = 0;
end

always @(posedge clk)
	case(state)
	1 : begin
		if (!cancel && !go && !req) state = 0;
		if (!cancel && !go && req) state = 0;
		if (!cancel && go && !req) state = 0;
		if (!cancel && go && req) state = 0;
		if (cancel && !go && !req) state = 0;
		if (cancel && !go && req) state = 0;
		if (cancel && go && !req) state = 0;
		if (cancel && go && req) state = 0;
	end
	0 : begin
		if (!cancel && !go && !req) state = 1;
		if (!cancel && !go && req) state = 1;
		if (!cancel && go && !req) state = 1;
		if (!cancel && go && req) state = 1;
		if (cancel && !go && !req) state = 1;
		if (cancel && !go && req) state = 1;
		if (cancel && go && !req) state = 1;
		if (cancel && go && req) state = 1;
	end
	endcase

endmodule
