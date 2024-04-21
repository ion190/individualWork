#include <iostream>

int main(int argc, char* argv[]) {

    std::string stagiul_cotizare = argv[1];
    std::string venitul_mediu_lunar = argv[2];
    std::string stagiul_potential = argv[3];
    std::string salariul_mediu_lunar = argv[4];


    std::cout << "Stagiul cotizare: " << stagiul_cotizare << std::endl;
    std::cout << "Venitul mediu lunar: " << venitul_mediu_lunar << std::endl;
    std::cout << "Stagiul potential: " << stagiul_potential << std::endl;
    std::cout << "Stagiul mediu lunar: " << salariul_mediu_lunar << std::endl;

    return 0;
}
