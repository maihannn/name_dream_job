# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program #2: Write a program that will ask you to input your name and your dream job. Print them in a fancy way.

# Ask for name.

name_input = input (str ("\033[0;32m" + "Enter your name: " + "\033[0;37m"))

# Ask for dream job.

dream_job_input = input (str ("\033[0;32m" + "Enter your dream job: " + "\033[0;37m"))

# Display output.

print ("\n", "\033[0;37m" + "Hi" + "\033[0;33m" + "\033[3m" + name_input, "!")
print ("\033[0;37m" + "Your dream job is to be a " + "\033[0;33m" + "\033[3m" + dream_job_input, "!")
