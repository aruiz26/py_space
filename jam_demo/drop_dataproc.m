clear; clc; close all;

% Read CSV file as a table (header will be used automatically)
T = readtable('output.csv');

% Access each column by its name (from header)
t     = T.t;
x  = T.x;
y  = T.y;
z  = T.z;
dx  = T.dx;
dy  = T.dy;
dz  = T.dz;
ddx  = T.ddx;
ddy  = T.ddy;
ddz  = T.ddz;


%%
figure(1)
plot(t, ddy)
xlabel('t'), ylabel('ddy')

%%
figure(11)
plot(t,ddx, '--', 'DisplayName','ddx')
hold on
plot(t,ddy, 'DisplayName','ddy')
plot(t,ddz, 'DisplayName','ddz')
legend
%%

dlim = 0.005
ddydif = diff(ddy);
ind0 = find(ddy>ddy(1e3)*0.9, 1)
indf = 55000
inds = [ind0:indf];


figure(1)
hold on
yyaxis('right')
plot(t(2:end),ddydif, '--', 'DisplayName','diff')
legend
%%
t = t(inds);
ddy = ddy(inds);
%% spectral analysis
fs = 1/(t(2)-t(1)); % sampling frequency
n = length(t);
f = (0:n-1)*(fs/n);     % frequency range

ddyf = fft(ddy);
power = abs(ddyf).^2/n;  

y0 = fftshift(ddyf);
f0 = (-n/2:n/2-1)*(fs/n); % 0-centered frequency range
power0 = abs(y0).^2/n;    % 0-centered power

f2 = figure(2); clf(f2);
plot(f0,power0); xlabel('Freq'); ylabel('power')
xlim([0, 80])

%%
figure
meanfreq(ddy, fs)


