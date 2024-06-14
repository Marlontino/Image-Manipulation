import subprocess

print("Running MATLAB CODE 1")
# Specify the full path to the MATLAB executable
# Adjust the path accordingly
# Specify the MATLAB script to execute
matlab_script = "matlabcode1.m"

# Specify the full path to the MATLAB executable
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'

# Run MATLAB script using the -batch flag and -nojvm to suppress the startup message
subprocess.run([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop', '-nojvm', '-batch', f"run('{matlab_script}')"])

# Your input array
input_array = ['1', '2', '3', '4', '5']
# Read values from 'data.txt'
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [int(value) for value in line.split()]
    input_array = [str(value) for value in input_array]

# Compile the C program (assuming it's saved as CProg.c)
print("Running C Program")
subprocess.run(["gcc", "CProg.c", "-o", "CProg"])

# Run the compiled C program with the input array as arguments
process = subprocess.run(["./CProg"] + input_array,\
        capture_output=True, text=True)

# Store the output of the C program in a Python variable
output_variable = process.stdout.strip()

# Print or use the stored output
#print("\nC program (add 1) output:")
#print(output_variable)

# Haskel subprocess
print("Running Haskell Program")
subprocess.run(['ghc', 'HProg.hs'])
process = subprocess.run(['./HProg'] + [str(x) for x in input_array], text=True, capture_output=True)
result = process.stdout.strip()

#print("Haskell program (subtract 1) output: ")
#print(result)

# Create haskell output file
with open('haskell_output.txt', 'w') as file:
    file.write(result)

# Prolog subprocess
print("Running Prolog Program")
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'PProg.pl'], input=prolog_input,
capture_output=True, text=True)
output_result = result.stdout.strip()

#print('Prolog code (reverse) output:')
#print(output_result)

# Create prolog output file
with open('prolog_output.txt', 'w') as file:
    file.write(output_result)


# Matlabcode 2 subprocess
print("Running MATLAB CODE 2")
# Load the matlab code
# Specify the MATLAB script to execute
matlab_script = "matlabcode2.m"

# Specify the full path to the MATLAB executable
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'

# Run MATLAB script using the -batch flag to suppress the startup message
subprocess.run([matlab_executable, '-nosplash', '-nodesktop', '-batch', f"run('{matlab_script}')"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
