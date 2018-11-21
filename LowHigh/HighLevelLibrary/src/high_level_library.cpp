#include <high/high_level_library.hpp>
#include <low/low_level_library.hpp>

int high::get_high()
{
    return 2 * low::get_low();
}