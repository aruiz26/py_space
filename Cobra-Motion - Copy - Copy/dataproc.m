%{
Script to process cobra_demo output

%}
clear; clc; close all;
%% Data parsing from csv

% Read CSV file as a table (header will be used automatically)
T = readtable('output_03_straight21s.csv');

% Access each column by its name (from header)
t = T.t;
x  = T.x;
y  = T.y;
z  = T.z;
dx  = T.dx;
dy  = T.dy;
dz  = T.dz;
ddx  = T.ddx;
ddy  = T.ddy;
ddz  = T.ddz;
speed_t = T.speed_set;
steering_t = T.steering_set;


try
    ver = 1;
    q0 = T.q0;
    q1 = T.q1;
    q2 = T.q2;
    q3 = T.q3;

    % q is a quaternion in the format [w x y z]
    q = [q0, q1, q2, q3]; % Example quaternion
    % Euler angles [yaw, pitch, roll] in radians by default,
    % using the ZYX rotation sequence (yaw → pitch → roll)
    eul = quat2eul(q);       % Returns [yaw, pitch, roll]
    eul_deg = rad2deg(eul);  % Convert to degrees if needed
catch
    warning('Quat not added')
    ver = 1
end

%%
t1 = 1; % sim start time
t = t - t1;  % adjusting time
t1 = 0; % t1=1 was originally added to xlim, this is to adjust it

%% position
figure(1)
subplot(2,3,1)
plot(t, x)
hold on
plot(t,y)
plot(t,z)
xlabel('t'), ylabel('Pos')
legend('x', 'y', 'z')
xlim([t1,inf])
%% velocity
subplot(2,3,2)
plot(t, dx)
hold on
plot(t,dy)
plot(t,dz)
xlabel('t'), ylabel('Vel')
legend('x', 'y', 'z')
xlim([t1,inf])
%% acceleration
subplot(2,3,3)
plot(t, ddx)
hold on
plot(t,ddy)
plot(t,ddz)
xlabel('t'), ylabel('Acc')
legend('x', 'y', 'z')
xlim([t1,inf])
%% wheel steering
subplot(2,3,4)
plot(t, steering_t*180/pi)
legend('steering deg')
xlim([t1,inf])
%% wheel rotational speed
subplot(2,3,5)
plot(t, speed_t)
legend('wheel speed')
xlim([t1,inf])

%%
if ver>1
    %% rotation
    subplot(2,3,6)
    plot(t, eul_deg(:,1))
    hold on
    plot(t, eul_deg(:,2))
    plot(t, eul_deg(:,3))
    xlabel('t'), ylabel(' eul rot deg')
    % legend('yaw', 'pitch', 'roll')
    legend('pitch', 'yaw', 'roll')
    xlim([t1,inf])
end
%% resize figure
set(gcf, 'Position', [100, 100, 1800, 800]); % [x,y,width, height]
%%
figure
plot(z,x)
xlabel('z - lateral'), ylabel('x-longit')
% axis('equal')






