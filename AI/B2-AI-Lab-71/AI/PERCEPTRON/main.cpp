# include <bits/stdc++.h>
using namespace std;

int signum(double value){
    return value > 0 ? 1 : -1;
}

double calculateNet(vector<double> w, vector<double> x){
    double sum = 0;
    for(int i=0;i<w.size();i++){
        sum += w[i] * x[i];
        // cout << "The sum is ::";
        // cout << sum << endl;
    }
    // cout << "The net is ::" << sum << endl;

    return sum;

}


int main(){

    double c = 1;
    int size = 0, dimension = 0;
    // cout << "Enter the number of inputs::";
    cin >> size;
    // cout << "Enter the dimesion of the data::";
    cin >> dimension;
    // vector<vector<int>> v = take_input(size, dimension);
    vector<vector<double>> v(size, vector<double>(dimension, 0));
    double data;
    for(int i=0;i<size;i++){
        for(int j=0;j<dimension;j++){
            cin >> data;
            v[i][j] = data;
        }
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<dimension;j++){
            cout << v[i][j] << " ";
        }
        cout << endl;
    }

    // cout << "Enter the initial w_i::";
    vector<double> w_i(dimension, 0);
    for(int i=0;i<dimension;i++){
        cin >> data;
        w_i[i] = data;
    }

    vector<double> y(size, 0);

    // cout << "Enter the actual labels::";
    double ans;
    for(int i=0;i<size;i++){
        cin >> ans;
        y[i] = ans;
    }

    int epoch = 1000;
    double error = DBL_MAX;

    for(auto x : y){
        cout << x << " ";
    }


    vector<double> _error;

    int cycle = 0;
    while(error != 0){
        double e = 0;
        double row = 0;
        for(int j=0;j<size;j++){
            vector<double> input(dimension, 0);
            for(int j=0;j<dimension;j++){
                input[j] = v[row][j];
            }
            cout << endl;
            cout << "This is the input::";
            for(auto x : input){
                cout << x << " ";
            }
            double net = calculateNet(w_i, input);
            int o = signum(net);
            cout << "o is ::" << o <<  endl;
            cout << "y is ::" << y[row] << endl;
            e += (y[row] - o);

            cout << "e is " << e << endl;
            
            vector <double> w(dimension, 0);

            double constant = c * (y[row] - o);
            for(int k=0;k<dimension;k++){
                w[k] = constant * input[k];
                cout << w[k];
            }
            vector<double> _w_i(dimension, 0);
            cout << "This is w_i::";
            for(int p=0;p<dimension;p++){
                _w_i[p] = w[p] + w_i[p];

                cout << _w_i[p] << " ";
            }

            cout << "This is the constant::" << constant << endl;
            cout << "This is w_i::";
            for(auto x : _w_i){
                cout << x << " ";
            }
            w_i = _w_i;
            row ++;



        }
        cycle ++;
        cout << endl;
        cout << "-------------------------------------------------"<< endl;

        error = e;
        _error.push_back(error);
        cout << error << endl;
        cout << "-------------------------------------------------"<< endl;


    }

    cout << "The error is " << error << endl;

    for(auto x : w_i){
        cout << x << " ";
    }

    cout << endl;

    for(auto x : _error){
        cout << x << endl;
    }



    
    return 0;
}
