#include <iostream>
#include <map>

using namespace std;

// Circular list of cups.
struct cup
{
    cup(int v) : label(v), next(this) {}

    const int label = 0;
    cup* next = 0;
};

// Quick finder of the cup with the given label.
// Since we never delete cups, this lookup table is stable.
struct cup_finder
{
    map<int, cup*> cup_by_value;
};

// Add a cup with the given label after the given cup,
// maintaining the circular list. Works even if the
// after-cup is null, to create the first cup.
// Add it to the cup finder, too.
cup* add_cup_after(cup* after, cup_finder& f, int label)
{
    auto new_cup = new cup(label);
    if (after)
    {
        new_cup->next = after->next;
        after->next = new_cup;
    }
    f.cup_by_value[label] = new_cup;
    return new_cup;
}

// Remove the three cups after the given one and return them.
// Note: the removed cups form a simple list, not a circular one.
cup* cut_next_three(cup* current)
{
    auto first = current->next;
    auto last = current->next->next->next;
    current->next = last->next;
    last->next = nullptr;
    return first;
}

// Reduce label by one, with wrap around if zero or less.
int previous_label(int label, int max_label)
{
    return label == 1 ? max_label : label - 1;
}

// Verify if a label is in the linked list of cups.
// Note: linked list is not circular.
bool is_label_in(cup* cup, const int label)
{
    for(; cup; cup = cup->next)
        if (label == cup->label)
            return true;
    return false;
}

// Insert the non-circular list of cups after the given cup
// which is in a circular list. Keep the resulting list circular.
void insert_after(cup* after, cup* picked)
{
    auto last = after->next;
    after->next = picked;

    while (picked->next)
        picked = picked->next;

    picked->next = last;
}

// Execute a single crab game move.
void crab_move(cup* current, cup_finder& finder, int max_label)
{
    auto picked_cups = cut_next_three(current);
    int destination_label = previous_label(current->label, max_label);
    while (is_label_in(picked_cups, destination_label))
        destination_label = previous_label(destination_label, max_label);
    auto destination_cup = finder.cup_by_value[destination_label];
    insert_after(destination_cup, picked_cups);
}

void part_1()
{
    cup_finder finder;

    //auto current = add_cup_after(nullptr, finder, 3);
    auto current = add_cup_after(nullptr, finder, 4);
    auto last = current;
    //for (int label : { 8, 9, 1, 2, 5, 4, 6, 7})
    for (int label : { 9, 6, 1, 3, 8, 5, 2, 7 })
        last = add_cup_after(last, finder, label);

    const int max_label = 9;

    for (int i = 0; i < 100; ++i)
    {
        crab_move(current, finder, max_label);
        current = current->next;
    }

    auto cup_to_print = finder.cup_by_value[1];
    for (int i = 0; i < max_label - 1; ++i)
    {
        cup_to_print = cup_to_print->next;
        cout << cup_to_print->label;
    }

    cout << endl;

}

void part_2()
{
    cup_finder finder;

    //auto current = add_cup_after(nullptr, finder, 3);
    auto current = add_cup_after(nullptr, finder, 4);
    auto last = current;
    //for (int label : { 8, 9, 1, 2, 5, 4, 6, 7})
    for (int label : { 9, 6, 1, 3, 8, 5, 2, 7 })
        last = add_cup_after(last, finder, label);

    for (int label = 10; label <= 1000000; ++label)
        last = add_cup_after(last, finder, label);

    const int max_label = 1000000;

    for (int i = 0; i < 10000000; ++i)
    {
        crab_move(current, finder, max_label);
        current = current->next;
    }

    auto one_cup = finder.cup_by_value[1];
    const long long label_1 = one_cup->next->label;
    const long long label_2 = one_cup->next->next->label;

    cout << label_1 * label_2 << endl;
}

int main()
{
    part_1();
    part_2();
}

