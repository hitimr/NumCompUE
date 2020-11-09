
#include <iostream>
#include <fstream>
#include <string>
#include <Eigen/Dense>
#include <vector>
#include <list>

using namespace std;
using namespace Eigen;


RowVectorXd readVector(const char *filename)
{
    ifstream infile;
    infile.open(filename);
    list<string> val_list;

    while (! infile.eof())
    {
        string line;
        getline(infile, line);
        val_list.push_back(line);

    }
    val_list.pop_back();

    RowVectorXd vec(val_list.size());
    int i = 0;
    for(auto itr=val_list.begin(); itr!=val_list.end(); itr++)
    {
        vec[i] = stof(*itr);
        i++;
    }

    return vec;
}



int main()
{
  RowVectorXd x = readVector("in/x.txt");
  RowVectorXd y = readVector("in/y.txt");
  float z= x*y.transpose();
  z += 1; // to make the warning disappear
}