
#include <iostream>
#include <fstream>
#include <string>
#include <Eigen/Dense>
#include <vector>
#include <list>

using namespace std;
using namespace Eigen;

#define MAXBUFSIZE  ((int) 1e6)

MatrixXd readMatrix(const char *filename)
{
  int cols = 0, rows = 0;
  double buff[MAXBUFSIZE];

  // Read numbers from file into buffer.
  ifstream infile;
  infile.open(filename);
  while (! infile.eof())
      {
      string line;
      getline(infile, line);

      int temp_cols = 0;
      stringstream stream(line);
      while(! stream.eof())
          stream >> buff[cols*rows+temp_cols++];

      if (temp_cols == 0)
          continue;

      if (cols == 0)
          cols = temp_cols;

      rows++;
      }

  infile.close();

  rows--;

  // Populate matrix with numbers.
  MatrixXd result(rows,cols);
  for (int i = 0; i < rows; i++)
      for (int j = 0; j < cols; j++)
          result(i,j) = buff[ cols*i+j ];

  return result;
}


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
  MatrixXd A = readMatrix("in/A.txt");
  RowVectorXd x = readVector("in/x.txt");
  
  RowVectorXd z;
  z = A*x.transpose();
}