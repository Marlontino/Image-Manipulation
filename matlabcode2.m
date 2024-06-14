% Read the output variables from the files
output_variable1 = fileread('input.txt');
output_variable2 = fileread('c_output.txt');
output_variable3 = fileread('haskell_output.txt');  % Update the filename
output_variable4 = fileread('prolog_output.txt');   % Update the filename

% Convert string to numeric array
output_array1 = uint8(str2num(output_variable1));
output_array2 = uint8(str2num(output_variable2));
output_array3 = uint8(str2num(output_variable3));  % Add conversion for Haskell output
output_array4 = uint8(str2num(output_variable4));  % Add conversion for Prolog output

% Resize the images to the original size (256x256)
resized_matrix1 = reshape(output_array1, 128, 128);
resized_matrix2 = reshape(output_array2, 128, 128);
resized_matrix3 = reshape(output_array3, 128, 128);  % Resize Haskell output
resized_matrix4 = reshape(output_array4, 128, 128);  % Resize Prolog output

% Display all images on the same figure with subplots
figure;

% Subplot 1: Original Image
subplot(2, 2, 1);
imshow(resized_matrix1);
title('Original Image');

% Subplot 2: Black & White Image from c_output.txt
subplot(2, 2, 2);
imshow(resized_matrix2);
title('Black & White Image from C Program');

% Subplot 3: Image from Haskell output
subplot(2, 2, 3);
imshow(resized_matrix3);
title('Color Flipped Image from Haskell');

% Subplot 4: Image from Prolog output
subplot(2, 2, 4);
imshow(resized_matrix4);
title('Rotated Image from Prolog');

pause(10);


