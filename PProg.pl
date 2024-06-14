% Rule to reverse list
reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).

% Main rule to perform sequence of operations
main :-
    read(List),
    reverse_list(List, Reversed),
    print_list(Reversed),
    nl. % Add a new line at the end

% Predicate to print list
print_list([]).
print_list([X]) :-
    write(X).
print_list([Head|Tail]) :-
    write(Head),
    write(' '), % Add a space after each element
    print_list(Tail).

% Entry point
:- initialization(main, main).
