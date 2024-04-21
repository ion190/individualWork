#include <iostream>

int main(int argc, char* argv[]) {

    std::string stagiul_cotizare = argv[1];
    std::string venitul_mediu_lunar = argv[2];

    int stagiul = std::stoi(stagiul_cotizare);
    double venitul_mediu = std::stod(venitul_mediu_lunar);

    double pensia;
    double rataAcumulare = 1.35 / 100;
    pensia = rataAcumulare * stagiul * venitul_mediu;

    std::cout << "Pensia: " << pensia << std::endl;

    return 0;
}
