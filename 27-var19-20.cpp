#include <fstream>
#include <iostream>
#include <limits>
#include <vector>

ssize_t mod(ssize_t a, ssize_t b)
{
    auto c = a % b;

    return c < 0 ? c + b : c;
}

void var19()
{
    std::ifstream fin("/home/vaskozlov/CLionProjects/ege/19-27A.txt");
    ssize_t n = 0, R = 0;

    fin >> n >> R;

    std::vector<ssize_t> data(n);

    for (auto &elem : data) {
        fin >> elem;
    }

    const ssize_t first = n / 2 + n % 2;
    const ssize_t second = n / 2;

    size_t pos = 0;
    ssize_t min_s = std::numeric_limits<ssize_t>::max();

    for (ssize_t begin = 0; begin != n; ++begin) {
        ssize_t s = 0;

        for (ssize_t j = 0; j != first; ++j) {
            auto i = begin + j;
            auto signals = data[mod(i, n)];
            auto distance = R * j;
            s += signals * (distance * distance);
        }

        for (ssize_t j = 0; j != second; ++j) {
            auto i = begin - j - 1;
            auto signals = data[mod(i, n)];
            auto distance = R * (j + 1);
            s += signals * (distance * distance);
        }

        if (s < min_s) {
            min_s = s;
            pos = begin;
        }
    }

    std::cout << pos + 1 << std::endl;
}

void var20()
{
    std::ifstream fin("/home/vaskozlov/CLionProjects/ege/20-27A.txt");
    size_t n = 0;
    fin >> n;

    std::vector<size_t> data(n);

    for (auto &elem : data) {
        fin >> elem;
    }

    size_t counter = 0;

    for (size_t begin = 0; begin != n; ++begin) {
        size_t p = 1;

        for (size_t end = begin; end != n; ++end) {
            p *= data[end];
            counter += static_cast<size_t>(p % 524288 != 0);
        }
    }

    std::cout << counter << std::endl;
}

int main()
{
    var19();
    return 0;
}
