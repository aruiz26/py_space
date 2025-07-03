clear; clc; close all;

% Read CSV file as a table (header will be used automatically)
T = readtable('output.csv');

% Access each column by its name (from header)
t     = T.t;
val1  = T.x;
val2  = T.y;
val3  = T.z;
val4  = T.dx;
val5  = T.dy;
val6  = T.dz;
val7  = T.ddx;
val8  = T.ddy;
val9  = T.ddz;


%%
figure(1)
plot(t, val8)
xlabel('t'), ylabel('ddy')