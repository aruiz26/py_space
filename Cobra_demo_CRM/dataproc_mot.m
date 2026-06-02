%{
Script to process cobra_demo output

%}
clear; clc; close all;
%% Data parsing from csv

% Read CSV file as a table (header will be used automatically)
T = readtable('output_03_curve_20deg_5s_50rpm_Sand.csv');
% figTitle = 'Cobra CSM - Sandy Soil - 60rpm';
%%
% Access each column by its name (from header)
t = T.t;
T_FR = T.motFRTor;
T_RR = -T.motRRTor;
T_FL = T.motFLTor;
T_RL = -T.motRLTor;
vx = T.dx;
vy = T.dy;
q1 = T.q1;
ax = T.ddx;

% steering servo torques
T_FR_steer = T.servFRTor;
T_RR_steer = T.servRRTor;
T_FL_steer = -T.servFLTor;
T_RL_steer = -T.servRLTor;


%%
R = 0.25
% w1 = 60*(2*pi/60)
% Rw1 = R*w1

w1 = zeros(size(t));
for i = 1:length(t)
    w1(i) = rotvel(t(i));
end

Rw1 = R*w1;

vel = sqrt(vx.^2+vy.^2);

S = 1 - (vel/Rw1);
%% conversion
% (1)N*m = (10.197162129779)kg*cm
% 1 kgf·cm = 0.0980665 N·m

%% plot of driving torque motor
figure
plot(t,T_FR);
hold on
plot(t,T_RR);
plot(t,T_FL);
plot(t,T_RL);

grid minor, box on
legend('FR', 'RR', 'FL', 'RL')

% ylim([-5, 30])
xlim([0, t(end)])
xlabel('Time(s)')
ylabel('Motor Torque (Nm)')
title('Wheel Motor Torque')
%% plot of servo steering torque 
figure
nm2kg = 10.197
% nm2kg = 1
plot(t,T_FR_steer*nm2kg);
hold on
plot(t,T_RR_steer*nm2kg);
plot(t,T_FL_steer*nm2kg);
plot(t,T_RL_steer*nm2kg);

grid minor, box on
legend('FR', 'RR', 'FL', 'RL')

% ylim([-5, 30])
xlim([0, t(end)])

xlabel('Time(s)')
ylabel('Motor Torque (kg-cm)')
title('Steering Servo Torque (1N*m=10.2kg*cm)')

%% Slip Ratio
figure
% subplot(211)
% plot(t, w1)
% 
% subplot(212)
plot(t,S)
ylim([0 1])
xlim([0, t(end)])

ylabel('Slip Ratio')
xlabel('Time(s)')
grid minor
box on
%% acceleration in x direction
figure

plot(t,ax)
% ylim([0 1])
xlim([0, t(end)])
grid minor; box on;
ylabel('acc_x (m/s/s)')
xlabel('Time(s)')

%%
F = 220 % newtos
r = 0.075 % approx 10cm
Tor = F*r

%%
function w = rotvel(t)

full_speed = 50*(1/60)*(2*pi);
if(t<0.5)
    w = 0
elseif(t>=0.5 & t<1)
    w = full_speed*(t-0.5)/0.5;
else
    w = full_speed;
end

end