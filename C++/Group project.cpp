//Ricardo Duran 
//11/12/2022
//COP2000
//In this Group Assignment i will be designing my own company that will read in the inventory text file 
// from our comapny warehouse.That will then be able to be written as an 
//and then write it as an output file if the user chooses too.
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

const int MAX = 10;
void menu();
bool readInventory(string itemNames[], double itemCost[], int itemNoShip[MAX][2]);
void displayInventory(string itemNames[], double itemCost[], int itemNoShip[MAX][2]);
void writeFile(string itemNames[], double itemCost[], int itemNoShip[MAX][2]);
void logo();

int main()
{
    string choice; // for menu choice entered by user
    // Declaration of parallel arrays
    string itemNames[MAX];
    double itemCost[MAX];
    int itemNoShip[MAX][2];
    int countItem = 0;
    for (countItem = 0; countItem < MAX; countItem++)
    {
        itemNames[countItem] = "NONE"; // denoting emptiness
        itemCost[countItem] = 0;     // denoting emptiness
    }
    do
    {
        menu();
        getline(cin, choice);    // Must be string and must use getline() in order to detect white spaces
        // Prevent strings from working, only char is allowed
        if (choice.size() !=1)
        {
            cout<<("\n Invalid Menu Item entered... must enter 1-4...\n\n ");
            return 1;
        }
        switch (choice[0])
        {
        case '1':
            readInventory(itemNames, itemCost, itemNoShip);
            break;
        case '2':
            displayInventory(itemNames, itemCost, itemNoShip);
            break;
        case '3':
            writeFile(itemNames, itemCost, itemNoShip);
            break;
        case '4':
            cout << "\nThank you for visiting ,have a great rest of your day!....\n";
            break;
        default:
            cout << "\n Invalid Menu Item entered... must enter 1-4...\n\n ";
            break;
        }

    } while (choice[0] != '4');
    return(0);
}
bool readInventory(string itemNames[], double itemCost[], int itemNoShip[MAX][2])
{
    ifstream file;     // file object
    string line;       // line variable, to keep one line of data taken from file
    int rowIndex; // for processing/handling parallel array
    file.open("AccountData.txt"); 
    if (file)
    {
        cout << "File was read succesfully...\n";
    }
    if (file.is_open())    // if file is successfully opened
    {
        rowIndex = 0;       // set index to 0
        while (getline(file, line, '\n')) // reading one line at a time from file.
        {
            unsigned position = 0; // Starting position of substring
            unsigned interval = 1; // Indicator for if substring is Name (1), Price (2), or Number/Ship (3)
            // Loop through each individual character in string
            for (unsigned i = 0; i < line.size(); ++i)
            {
                // Find the tab character so that we can split up the string.
                if (line[i] == '\t')
                {
                    unsigned length = (i - position);    // Length of broken up string.
                    string break_up = line.substr(position, length);
                    position = i;   // Update starting position to be the end of the broken up string for next call.
                    // Figure out if substring is Name (1), Price (2), or Number/Ship (3)
                    switch (interval)
                    {
                        // Name
                    case 1:
                        itemNames[rowIndex] = break_up;    // Save into Name array
                        interval = 2;                      // Next loop will save into Price array
                        break;
                        // Price
                    case 2:
                        // Must convert string to float/double to save into Cost array.
                        // std::atof conversion function ONLY accepts char*, so we get the char* from string using .c_str()
                        itemCost[rowIndex] = std::atof(break_up.c_str());  // Save into Cost array
                        interval = 3;                                  // Next loop will save into Number/Ship array
                        break;
                        // Number/Ship
                    case 3:
                        // Must convert string to integer
                        itemNoShip[rowIndex][0] = std::atoi(break_up.c_str()); // Save into Number array
                        std::string shipping = line.substr(position);          // This will get the remaining string left
                        itemNoShip[rowIndex][1] = std::atoi(shipping.c_str());  // Save into Shipping array
                        break;
                    }
                }
            }
            rowIndex++; // incresing index
        }
        file.close();
        return true;
    }
    else
    cout << "\n Error ,File was not read...\n\n"<<endl;
    exit(0);
    return false;
}
//This function is passed all three arrays and displays the content of these arrays (that is, the warehouse inventory) in a
//tabular format with the appropriate headings (see the sample output provided).
void displayInventory(string itemNames[], double itemCost[], int itemNoShip[MAX][2])
{
    cout << left << setw(20) << "Item name" << setw(7) << "Cost" << setw(12) << "No. Stock" << setw(16) << "Shipping(1-Yes 0-no)";
    for (int index = 0; index < MAX && itemCost[index] != 0; index++)
        // Displaying data in tabular form
        cout << "\n" << left << setw(20) << itemNames[index] << setw(14) << itemCost[index] << setw(23) << itemNoShip[index][0] << setw(20) << itemNoShip[index][1] << endl;
    cout << endl;
}
//This function is passed all three arrays from main and writes the data from these arrays in a tabular format to a text file //called outputInventory.txt.
void writeFile(string itemNames[], double itemCost[], int itemNoShip[MAX][2])
{
    ofstream file;    // file object
    int index;        // index numbers for parallel arrays
    file.open("outputInventory.txt");
    cout << "File written to outputinventory.txt...\n\n";// opening file for writing purpose
    for (index = 0; index < MAX && itemCost[index] != 0; index++)
    {
        // Writing data in tabular form
        file << left << setw(20) << itemNames[index] << setw(7) << itemCost[index] << setw(8) << itemNoShip[index][0] << setw(8) << itemNoShip[index][1] << "\n";
    }
    file.close();
}
void logo()//My Buisness Logo
{
    cout << "     CJ Pony Parts \n\n";
    cout << "***********************************" << endl;
    cout << "\n       _|\\_/|_, " << endl;
    cout << "     ,((\\\\``-\\\\\\_ " << endl;
    cout << "   ,(())      `))\\  " << endl;
    cout << " ,(()))       ,_ \\  " << endl;
    cout << "((())'   |        \\  " << endl;
    cout << ")))))     >.__     \\  " << endl;
    cout << "((('     /    `-. .c| " << endl;
    cout << "        /        `-`'" << endl;
    cout << endl;
    cout << "************************************" << endl;
}
void menu() //This function outputs the menu options to read , write the txt file for the Inventory.
{
    logo();
    cout << "\n 1. Read in Inventory\n";
    cout << " 2. Display Inventory\n";
    cout << " 3. Write to File\n";
    cout << " 4. Exit \n";
}


