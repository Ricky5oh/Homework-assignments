//Ricardo Duran		
//11/28/2022
//COP2000
//In this Assignment i will be creating a program that will first read a file.
// Then ask the user for their username and password for account accesss.The program then validates
//to see if the information is correct and then allows them to see the information pertaining to them.
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;

void showAll(string theAccounts[5][7]);
void sortInput(string theAccounts[5][7]);
bool readFile(string theAccounts[5][7]);
bool validateUser(string theAccounts[5][7], string username, string password, int*);

int main()
{
	cout << setprecision(2) << fixed << showpoint;
	bool userGood;
	bool fileGood;
	int saveRow;
	string username;//for username entered by user
	string password;//for password entered by user 
	string accountData[5][7] = { " " };
	fileGood = readFile(accountData);
	{
		if (fileGood == true)// message letting the user know that the file was succesfully read , and they can proceed 
			cout << " File read succesfully...\n\n";
		else
		{
			cout << "the file was not read succesfully... exiting program.\n\n";//message letting the user know that there is a problem with the file.
			return 0;
		}
	}
	sortInput(accountData);
	do
	{
		username = "";
		password = "";
		cout << "Enter the following information, or press 0 to Exit..." << endl;
		cout << "Please enter your User Name >";// asking the user to enter their account access username
		cin >> username;
		if (username == "0")
		{
			cout << "\nThank You, have a nice day.\n\n";// Output message if user decides to exit the program 
			return 0;
		}
		cout << "Please Enter your User Password >";//asking the user to enter their account access password
		cin >> password;
		if (password == "0")
		{
			cout << "\nThank You, have a nice day.\n\n";//output message if user decides to exit the program 
			return 0;
		}
		userGood = validateUser(accountData, username, password, &saveRow);
		{
			if (userGood == true)
			{
				if (accountData[saveRow][5] == "A")
				{
					showAll(accountData);
				}
				else
				{//letting the user know they have sucessfully logged in , and display they're information . 
					cout << "\nWelcome Back " << accountData[saveRow][1] << "!\n";
					cout << setw(8) << left << accountData[saveRow][1];
					cout << setw(8) << left << accountData[saveRow][2];
					cout << setw(6) << left << accountData[saveRow][4];
					cout << setw(4) << left << accountData[saveRow][5];
					cout << setw(15) << left << accountData[saveRow][6];
					cout << endl << endl;
				}
			}
			else
			{//displays a message letting the user know they account information does not match.
				cout << "\nUsername and password do not match ...Please try again ...\n" << endl;
			}
		}
	} while (password != "0" || username != "0");
	return 0;
}
void showAll(string theAccounts[5][7])
{
	ofstream outputFile;//file object
	outputFile.open("sortedBackup.txt");//outputs data from the main into a txt file named sortedBackup.txt.
	int row = 5;//num of rows
	cout << "\n";
	for (int index = 0; index < row; index++)
	{
		cout << setw(20) << right << theAccounts[index][0];
		cout << setw(8) << right << theAccounts[index][1];
		cout << setw(8) << right << theAccounts[index][2];
		cout << setw(10) << right << theAccounts[index][3];
		cout << setw(6) << right << theAccounts[index][4];
		cout << setw(4) << right << theAccounts[index][5];
		cout << setw(15) << right << theAccounts[index][6];
		cout << endl;
		outputFile << setw(20) << right << theAccounts[index][0];
		outputFile << setw(8) << right << theAccounts[index][1];
		outputFile << setw(8) << right << theAccounts[index][2];
		outputFile << setw(10) << right << theAccounts[index][3];
		outputFile << setw(6) << right << theAccounts[index][4];
		outputFile << setw(4) << right << theAccounts[index][5];
		outputFile << setw(15) << right << theAccounts[index][6];
		outputFile << endl;
	}
	cout << "Backup file completed ....\n " << endl;//stating the backup file was created
	outputFile.close();
}
void sortInput(string theAccounts[5][7])
{//this function sorts the account data and 
	bool sorted = false;
	string temp;
	while (!sorted) {
		sorted = true;
		for (int index = 0; index < 4; ++index) {
			if (theAccounts[index][2] > theAccounts[index + 1][2]) {
				sorted = false;
				for (int last = 0; last < 7; ++last) {
					temp = theAccounts[index][last];
					theAccounts[index][last] = theAccounts[index + 1][last];
					theAccounts[index + 1][last] = temp;
				}
			}
		}
	}
}
bool readFile(string theAccounts[5][7]) //this function is used to read the user file .
{
	bool fileRead = false;
	int row = 5;//num of rows
	int col = 7;//num of columns
	ifstream inputFile;//ifstream object/inputFile stream object 
	inputFile.open("AccountData.txt");//the open member function opens the text file and links it with 
	//the input file to read data from the AccountData.txt file
	if (inputFile) // if file is successfully opened
	{
		fileRead = true;
		for (int index = 0; index < row; index++)
			for (int index2 = 0; index2 < col; index2++)
				inputFile >> theAccounts[index][index2];
	}
	inputFile.close();//To close the txt file 
	return fileRead;
}
bool validateUser(string theAccounts[5][7], string username, string password, int* saveRow)
{
	//Search for matching accts and pass and if it cant to return false
	bool passed = false;
	int user = 0;
	int pass = 3;
	int row = 0;
	for (int row = 0; row <= 4; row++)
	{
		if ((username == theAccounts[row][user]) && (password == theAccounts[row][pass]))
		{
			passed = true;
			*saveRow = row;
		}
	}
	return passed;
}