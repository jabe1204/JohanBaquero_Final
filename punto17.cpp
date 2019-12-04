#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

void ecuacion(int nx, int nt, string name);

double tmax = 0.5;
double xi = 0.0;
double xf = 2.0;
double dx = 0.01;      
double dt = 0.01;
int Nx = 2/0.01; /*(xf-xi)/dx*/	
int Nt = tmax/dt;

int main () 
{
	ecuacion(Nx,Nt,"datos.dat");
	return 0;
}

void ecuacion(int nx, int nt, string name)
{
    ofstream outfile;
    outfile.open(name);
    
	double M[nt+1][nx+1];
	double x;
    for(int i=0; i<=nx; i++)
    {
        /*Condiciones iniciales*/
        x=i*dx;
        M[0][i]=exp(-0.5*((x-1)*(x-1))/(0.25*0.25));
    }
    
        for(int i=1 ;i < nt; i++)
        {
            for(int j = 1; j < nx; j++)
            {
                M[i+1][j] = M[i-1][j] - M[i][j]*(M[i][j+1] - M[i][j-1])*(dt/dx);
            }  
        }
    
    /*Imprime los datos en un archivo .dat*/
    for(int i = 0; i<nt;i++)
    {
        for(int j = 0; j<nx;j++)
        {
            outfile<<M[i][j]<<"\t";
        }
        outfile<<endl;
    }
    outfile.close();
}