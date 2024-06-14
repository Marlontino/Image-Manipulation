% Read grayscale img
img = imread('mickey.png');

% Specify target size
targetSize = [128, 128];
% Resize img
img = imresize(img, targetSize);
% Reshape to 1d array
img_1d = reshape(img, 1, []);

% write the data to a file
dlmwrite('input.txt', img_1d, 'delimiter', ' ');
