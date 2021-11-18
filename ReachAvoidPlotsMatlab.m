% This is getting the trajectory. Each state is the row of the matrix
P = readmatrix('treact20120.out.txt');

% This plots
plot(P(1:length(P),1), P(1:length(P),2), 'LineWidth', 2)
hold on
plot(P(1:length(P),6), P(1:length(P),7), 'LineWidth', 2)
%xlim([4 10])
%ylim([0 28])

% This plots a circle
circleout = circle(8.5, 25, 2, 'g')

xlim([4 10])
ylim([0 28])
% This plots a line
% plot([10.5,10.5], [min(ylim()),max(ylim())], 'k')
% plot([6.5,6.5], [min(ylim()),max(ylim())], 'y--')
% plot([2.5,2.5], [min(ylim()),max(ylim())], 'k')


% plot([6.5,6.5],[0,30], 'y--')
% hold on
% plot([4.5,4.5],[0,30], 'k')
% hold on
% plot([8.5,8.5],[0,30], 'k')

%plot(8.5, 25, '.r', 'MarkerSize',40)



%% One-Player One-Obstacle Time-Consistent
% This is getting the trajectory. Each state is the row of the matrix
P = readmatrix('1player1obs_timeconsistent_radius4.5_41.txt');

% Define obstacle parameters
obstacle_x = 6.5;
obstacle_y = 15.0;
obs = 4.5;

% Define target parameters
target_x = 6.5;
target_y = 35.0;
target_radius = 2.0;

% Define closest point for iteration k
iter_4 = 31;
iter_26 = 21;
iter_31 = 18;
iter_34 = 17;
iter_37 = 16;
iter_42 = 14;

% This plots
figure(6)
%plot( P(1:length(P),1)', P(1:length(P),2)' , 'LineWidth', 2)
%hold on
%xlim([4 10])
%ylim([0 28])

% This plots the obstacle and target, respectively
circleout = circle(obstacle_x, obstacle_y, obs, 'r')
circleout = circle(target_x, target_y, target_radius, 'g')

hold on
plot( P(1:length(P),1)', P(1:length(P),2)' , 'b', 'LineWidth', 2)

%
circleempty = emptycircle(P(5,1), P(5,2), 2, 'b')
circleempty = emptycircle(P(iter_42,1), P(iter_42,2), 2, 'b')
circleempty = emptycircle(P(length(P),1), P(length(P),2), 2, 'b')

% This plots cirlces along the trajectory

xlim([-2 20])
ylim([-10 40])
hold off




%% Pinch-point
M = readmatrix('1player1obs_pinchpoint_radius4.5_2.txt');

% Define obstacle parameters
obstacle_x = 6.5;
obstacle_y = 15.0;
obs = 4.5;

% Define target parameters
target_x = 4.5;
target_y = 35.0;
target_radius = 2.0;


figure(9)
% This plots the obstacle and target, respectively
circleout = circle(obstacle_x, obstacle_y, obs, 'k')
circleout = circle(target_x, target_y, target_radius, 'm')

hold on
plot( M(1:length(M),1)', M(1:length(M),2)' , 'b', 'LineWidth', 2)

%
circleempty = emptycircle(M(5,1), M(5,2), 2, 'b')
circleempty = emptycircle(M(37,1), M(37,2), 2, 'b')
circleempty = emptycircle(M(length(M),1), M(length(M),2), 2, 'b')

% xlim([-10 20])
% ylim([-10 100])
hold off





%% Time-Consistent Loopty Loop
%%% Pinch-point
%file_list_raw = fileread('frames.txt')
file_list_raw = fileread('frames1.txt')
file_list = strsplit(file_list_raw)
file_list{1}


for i = 1:size(file_list,2)-1
M = readmatrix(file_list{i});
%M = readmatrix('1player1obs_timeconsistent_radius4.5_looparound_0.txt');

% Define obstacle parameters
obstacle_x = 6.5;
obstacle_y = 15.0;
obs = 4.5;

% Define target parameters
target_x = 6.5;
target_y = 35.0;
target_radius = 2.0;


figure(8)
% This plots the obstacle and target, respectively
circleout = circle(obstacle_x, obstacle_y, obs, 'k')
circleout = circle(target_x, target_y, target_radius, 'm')

hold on
plot( M(1:length(M),1)', M(1:length(M),2)' , 'b', 'LineWidth', 2)
axis off

%
%circleempty = emptycircle(M(5,1), M(5,2), 2, 'b')
%circleempty = emptycircle(M(35,1), M(35,2), 2, 'b')
%circleempty = emptycircle(M(length(M),1), M(length(M),2), 2, 'b')

%xlim([-15 40])
%ylim([-10 100])
saveas(gcf,strcat('trial', int2str(i),'.png'))
hold off
clf
end





%% One-Player Multiple-Obstacles
%%% Pinch-point
%file_list_raw = fileread('frames.txt')
file_list_raw = fileread('frames2.txt')
file_list = strsplit(file_list_raw)
file_list{1}


for i = 1:size(file_list,2)-1
M = readmatrix(file_list{i});
%M = readmatrix('1player1obs_timeconsistent_radius4.5_looparound_0.txt');

% Define obstacle parameters
obstacle_x1 = 6.5;
obstacle_y1 = 15.0;
obs1 = 4.5;

obstacle_x2 = 0.0;
obstacle_y2 = 20.0;
obs2 = 1.5;

obstacle_x3 = 12.0;
obstacle_y3 = 24.0;
obs3 = 4.0;

% Define target parameters
target_x = 6.5;
target_y = 35.0;
target_radius = 2.0;


figure(8)
% This plots the obstacle and target, respectively
circleout = circle(obstacle_x1, obstacle_y1, obs1, 'k')
circleout = circle(obstacle_x2, obstacle_y2, obs2, 'k')
circleout = circle(obstacle_x3, obstacle_y3, obs3, 'k')
circleout = circle(target_x, target_y, target_radius, 'm')

hold on
plot( M(1:length(M),1)', M(1:length(M),2)' , 'b', 'LineWidth', 2)
axis off

%
%circleempty = emptycircle(M(5,1), M(5,2), 2, 'b')
%circleempty = emptycircle(M(35,1), M(35,2), 2, 'b')
%circleempty = emptycircle(M(length(M),1), M(length(M),2), 2, 'b')

%xlim([-15 40])
%ylim([-10 100])
saveas(gcf,strcat('trial', int2str(i),'.png'))
hold off
clf
end




%% Pinch-point
file_list_raw = fileread('frames.txt')
%file_list_raw = fileread('frames2.txt')
file_list = strsplit(file_list_raw)
file_list{1}


for i = 1:size(file_list,2)-1
M = readmatrix(file_list{i});
%M = readmatrix('1player1obs_timeconsistent_radius4.5_looparound_0.txt');

% Define obstacle parameters
obstacle_x1 = 6.5;
obstacle_y1 = 15.0;
obs1 = 4.5;

% Define target parameters
target_x = 6.5;
target_y = 35.0;
target_radius = 2.0;


figure(8)
% This plots the obstacle and target, respectively
circleout = circle(obstacle_x1, obstacle_y1, obs1, 'k')
circleout = circle(target_x, target_y, target_radius, 'm')

hold on
plot( M(1:length(M),1)', M(1:length(M),2)' , 'b', 'LineWidth', 2)
axis off

%
%circleempty = emptycircle(M(5,1), M(5,2), 2, 'b')
%circleempty = emptycircle(M(35,1), M(35,2), 2, 'b')
%circleempty = emptycircle(M(length(M),1), M(length(M),2), 2, 'b')

%xlim([-15 40])
%ylim([-10 100])
saveas(gcf,strcat('trial', int2str(i),'.png'))
hold off
clf
end