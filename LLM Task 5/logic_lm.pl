:- module(logic_lm, [binge_watches/2, downloads/2, shares/3]).

% Facts - Netflix Shows
netflix_show(stranger_things).
netflix_show(black_mirror).
netflix_show(bojack_horseman).
netflix_show(queen_gambit).
netflix_show(ozark).
netflix_show(schitts_creek).
netflix_show(rick_and_morty).
netflix_show(mindhunter).
netflix_show(breaking_bad).
netflix_show(the_crown).

% Facts - Popular shows
popular(stranger_things).
popular(queen_gambit).
popular(breaking_bad).
popular(the_crown).

% Rules: Binge-watches
binge_watches(karen, Show) :-
    netflix_show(Show),
    popular(Show).

% Rule - Downloads
downloads(karen, Show) :-
    binge_watches(karen, Show),
    Show \= black_mirror.

% Rule - Share
shares(karen, Show, lisa) :-
    binge_watches(karen, Show).

% Printing in NL
solve_query(Query) :-
    (   call(Query)
    ->  format('Query "~w" succeeded.~n', [Query])
    ;   format('Query "~w" failed.~n', [Query])
    ).

% Testing
test_queries :-
    solve_query(binge_watches(karen, stranger_things)),
    solve_query(downloads(karen, queen_gambit)),
    solve_query(shares(karen, queen_gambit, lisa)),
    solve_query(downloads(karen, black_mirror)),
    solve_query(binge_watches(karen, rick_and_morty)).
