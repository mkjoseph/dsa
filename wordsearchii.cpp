#include <iostream>
#include <string>

int main() {
    std::string date, time, office, name;

    std::cout << "Enter the date: ";
    std::getline(std::cin, date);

    std::cout << "Enter the time: ";
    std::getline(std::cin, time);

    std::cout << "Enter the office: ";
    std::getline(std::cin, office);

    std::cout << "Enter the name: ";
    std::getline(std::cin, name);

    std::cout << "Appointment details:\n";
    std::cout << "Date: " << date << "\n";
    std::cout << "Time: " << time << "\n";
    std::cout << "Office: " << office << "\n";
    std::cout << "Name: " << name << "\n";

    return 0;
}
