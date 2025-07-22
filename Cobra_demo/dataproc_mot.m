%{
Script to process cobra_demo output

%}
clear; clc; close all;
%% Data parsing from csv

% Read CSV file as a table (header will be used automatically)
T = readtable('output_06_straight21s_60rpm_SandySoil_edit.csv');
figTitle = 'Cobra CSM - Sandy Soil - 60rpm';

% Access each column by its name (from header)
t = T.t;
T_FR = T.motFRTor;
T_RR = -T.motRRTor;
T_FL = T.motFLTor;
T_RL = -T.motRLTor;
vx = T.dx;
q1 = T.q1;
ax = T.ddx;
%%
R = 0.25
w1 = 60*(2*pi/60)
Rw1 = R*w1

S = 1 - (vx/Rw1);
%% plot
f1 = figure(1); clf(f1)

plot(t,T_FR);
hold on
plot(t,T_RR);
plot(t,T_FL);
plot(t,T_RL);

grid minor, box on
legend('FR', 'RR', 'FL', 'RL')

ylim([-5, 30])
xlabel('Time(s)')
ylabel('Motor Torque (Nm)')
title(figTitle)
%%
f2 = figure(2); clf(f2)
% subplot(211)
% plot(t, w1)
% 
% subplot(212)
plot(t,S)
ylim([0 1])
ylabel('Slip Ratio')
xlabel('Time(s)')
%%
f3 = figure(3); clf(f3)

plot(t,ax)
% ylim([0 1])
grid minor; box on;
ylabel('Slip Ratio')
xlabel('Time(s)')

%%
F = 220 % newtos
r = 0.075 % approx 10cm
T = F*r
