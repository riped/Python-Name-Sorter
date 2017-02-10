#===============================================================================
# Sean Corrigan 2017
# ICS 3U1
# Name Groups Program
# PC MAC: D0:50:99:A9:9B:31
#===============================================================================

# import libraries
import os  # Needed for clearing the terminal in a clear manner
import sys  # Needed for seemless restarts
#########

os.system('clear')  # clearterm
name = raw_input('PRESS ENTER YOUR NAME:' "\n" )  # wait by asking to press enter to continue
os.system('clear')  # clearterm

# Start the program here

print 'Welcome', name.title()
numberofstudents = raw_input ('Please enter the number of names you wish to sort (Must be an even number from 1 to 10): ') # ask for number of students

try:  # Try to convert to a int. if not restart
		numberofstudents = int(numberofstudents)  # Define numberofstudents as interger
except ValueError:  # If it isn't a whole number then
	print("That's not a whole number")  # Tell user that is not a number
	wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
	os.execl(sys.executable, sys.executable, *sys.argv)  # restart program
	
if numberofstudents < 0:  # Make sure that the amount of students isn't a negative 
		
		print ("Stop, Please. Don't Break me any more")  # Beg for them to stop
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program
	
if numberofstudents > 10:  # when there are more then 10 students to sort
		os.system('clear')  # clearterm
		print 'Can only make 5 groups of 10 students'  # display that only make 5 groups with a total of 10 students
		wait = raw_input('PRESS ENTER TO RESTART')  # wait by asking to press enter to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program

if numberofstudents % 2 == 0:  # check if number of students is odd or even

	# sorting then asking for students names
	if numberofstudents == 2:  # when there are 2 students	
	
		os.system('clear')  # clearterm
		name1 = raw_input('First Students Name: ')  # ask for first students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name1sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name2 = raw_input('Second Students Name: ')  # ask for second students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name2sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		wait = raw_input('GROUPS CREATED, PRESS ENTER')  # wait for return on ENTER
		os.system('clear')  # clearterm
		print 'Groups are as follows:'  # list groups title wait for enter key
		print 'Group 1:', name1, name1sn, "and", name2, name2sn  # list group 1
		print ' '  # Space to clean up
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program


	elif numberofstudents == 4:  # when there are 4 students

		os.system('clear')  # clearterm
		name1 = raw_input('First Students Name: ')  # ask for first students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name1sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name2 = raw_input('Second Students Name: ')  # ask for second students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name2sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name3 = raw_input('Third Students Name: ')  # ask for third students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name3sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name4 = raw_input('Fourth Students Name: ')  # ask for fourth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name4sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		wait = raw_input('2 GROUPS CREATED, PRESS ENTER')  # display that groups are created and to press enter to continue
		os.system('clear')  # clearterm
		print 'Groups are as follows:'  # list groups title wait for enter key
		print 'Group 1:', name1, name1sn, "and", name3, name3sn  # list group 1
		print 'Group 2:', name4, name4sn, "and", name2, name2sn  # list group 2
		print ' '  # Space to clean up
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program

	elif numberofstudents == 6:  # when there are 6 students

		os.system('clear')  # clearterm
		name1 = raw_input('First Students Name: ')  # ask for first students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name1sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name2 = raw_input('Second Students Name: ')  # ask for second students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name2sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name3 = raw_input('Third Students Name: ')  # ask for third students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name3sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name4 = raw_input('Fourth Students Name: ')  # ask for fourth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name4sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name5 = raw_input('Fifth Students Name: ')  # ask for fifth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name5sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name6 = raw_input('Sixth Students Name: ')  # ask for sixth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name6sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		
		wait = raw_input('3 GROUPS CREATED, PRESS ENTER')  # display that groups are created and to press enter to continue
		os.system('clear')  # clearterm
		print 'Groups are as follows:'  # list groups
		print 'Group 1:', name1, name1sn, "and", name5, name5sn  # list group 1
		print 'Group 2:', name4, name4sn, "and", name2, name2sn  # list group 2
		print 'Group 3:', name3, name3sn, "and", name6, name6sn  # list group 3
		print ' '  # Space to clean up
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program

	elif numberofstudents == 8:  # when there are 8 students

		os.system('clear')  # clearterm
		name1 = raw_input('First Students Name: ')  # ask for first students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name1sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name2 = raw_input('Second Students Name: ')  # ask for second students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name2sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name3 = raw_input('Third Students Name: ')  # ask for third students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name3sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name4 = raw_input('Fourth Students Name: ')  # ask for fourth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name4sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name5 = raw_input('Fifth Students Name: ')  # ask for fifth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name5sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name6 = raw_input('Sixth Students Name: ')  # ask for sixth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name6sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name7 = raw_input('Seventh Students Name: ')  # ask for seventh students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name7sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name8 = raw_input('Eighth Students Name: ')  # ask for eighth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name8sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		
		wait = raw_input('4 GROUPS CREATED, PRESS ENTER')  # display that groups are created and to press enter to continue
		os.system('clear')  # clearterm
		print 'Groups are as follows:'  # list groups
		print 'Group 1:', name1, name1sn, "and", name8, name8sn  # list group 1
		print 'Group 2:', name7, name7sn, "and", name2, name2sn  # list group 2
		print 'Group 3:', name3, name3sn, "and", name6, name6sn # list group 3
		print 'Group 4:', name5, name5sn, "and", name4, name4sn  # list group 4
		print ' '  # Space to clean up
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program

	elif numberofstudents == 10:  # when there are 10 students
		
		os.system('clear')  # clearterm
		name1 = raw_input('First Students Name: ')  # ask for first students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name1sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name2 = raw_input('Second Students Name: ')  # ask for second students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name2sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name3 = raw_input('Third Students Name: ')  # ask for third students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name3sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name4 = raw_input('Fourth Students Name: ')  # ask for fourth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name4sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name5 = raw_input('Fifth Students Name: ')  # ask for fifth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name5sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name6 = raw_input('Sixth Students Name: ')  # ask for sixth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name6sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name7 = raw_input('Seventh Students Name: ')  # ask for seventh students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name7sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name8 = raw_input('Eighth Students Name: ')  # ask for eighth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name8sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name9 = raw_input('Nineth Students Name: ')  # ask for nineth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name9sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		name10 = raw_input('Tenth Students Name: ')  # ask for tenth students names
		print 'Please enter the last 3 digits of the students BC Number.'
		name10sn = raw_input('Last 3 digits of BC: ')  # ask for student number
		os.system('clear')  # clearterm
		
		
		wait = raw_input('5 GROUPS CREATED, PRESS ENTER')  # display that groups are created and to press enter to continue
		os.system('clear')  # clearterm
		print 'Groups are as follows:'  # list groups
		print 'Group 1:', name1, name1sn, "and", name10, name10sn  # list group 1
		print 'Group 2:', name9, name9sn, "and", name2, name2sn  # list group 2
		print 'Group 3:', name3, name3sn, "and", name8, name8sn  # list group 3
		print 'Group 4:', name7, name7sn, "and", name4, name4sn  # list group 4
		print 'Group 5:', name5, name5sn, "and", name6, name6sn  # list group 5
		print ' '  # Space to clean up
		wait = raw_input('PRESS ENTER TO RESTART')  # Ask to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program
	

else:
		print 'Sorry you have an uneven amount of students'  # display that there is an uneven amount of students so no equal amount of groups can be made
		wait = raw_input('PRESS ENTER TO RESTART')  # wait by asking to press enter to continue
		os.execl(sys.executable, sys.executable, *sys.argv)  # restart program
