\version "2.22.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\context Score = "Score" %! muda.Score()
<<                       %! muda.Score()
    \context TimeSignatureContext = "Global_Context"
    {
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 5/4 %! muda.Score.MakeSkips()
        s1 * 5/4
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 5/4 %! muda.Score.MakeSkips()
        s1 * 5/4
        \time 3/4 %! muda.Score.MakeSkips()
        s1 * 3/4
        \time 1/4 %! muda.Score.MakeSkips()
        s1 * 1/4
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 5/4 %! muda.Score.MakeSkips()
        s1 * 5/4
        \time 4/4 %! muda.Score.MakeSkips()
        s1 * 1
        \time 1/4 %! muda.Score.MakeSkips()
        s1 * 1/4
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
        \time 5/4 %! muda.Score.MakeSkips()
        s1 * 5/4
        \time 2/4 %! muda.Score.MakeSkips()
        s1 * 1/2
    }
    \context Staff = "AltoFlute_Staff" %! muda.score.instrument()
    {                                  %! muda.score.instrument()
        \context Voice = "AltoFlute_Voice_1" %! muda.score.instrument()
        {                                    %! muda.score.instrument()
            g8 %! aflute_A
            r8 %! aflute_A
            r4 %! aflute_A
            \times 2/3 { %! aflute_B
                e'8 %! aflute_B
                r8 %! aflute_B
                r8 %! aflute_B
                f'8 %! aflute_B
                r8 %! aflute_B
                e'8 %! aflute_B
            } %! aflute_B
            \times 4/7 { %! aflute_C
                d'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
                [ %! aflute_C
                d'8 %! aflute_C
                ] %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
            } %! aflute_C
            \tweak text #tuplet-number::calc-fraction-text %! aflute_D
            \times 3/4 {                                   %! aflute_D
                c'8 %! aflute_D
                r8 %! aflute_D
                r8 %! aflute_D
                bf8 %! aflute_D
                r8 %! aflute_D
                c'8 %! aflute_D
                [ %! aflute_D
                bf8 %! aflute_D
                ] %! aflute_D
                r8 %! aflute_D
            } %! aflute_D
            r2 %! Rests
            g8 %! aflute_A
            r8 %! aflute_A
            r4 %! aflute_A
            \tweak text #tuplet-number::calc-fraction-text %! aflute_B
            \times 3/4 {                                   %! aflute_B
                e'8 %! aflute_B
                r8 %! aflute_B
                r8 %! aflute_B
                f'8 %! aflute_B
                r8 %! aflute_B
                e'8 %! aflute_B
                [ %! aflute_B
                f'8 %! aflute_B
                ] %! aflute_B
                r8 %! aflute_B
            } %! aflute_B
            \times 2/3 {
                d'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
                [ %! aflute_C
                d'8 %! aflute_C
                ] %! aflute_C
                r8 %! aflute_C
            }
            \times 2/3 {
                e'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
            }
            \times 2/3 { %! aflute_D
                c'8 %! aflute_D
                r8 %! aflute_D
                r8 %! aflute_D
                bf8 %! aflute_D
                r8 %! aflute_D
                c'8 %! aflute_D
            } %! aflute_D
            r4 %! Rests
            g8 %! aflute_A
            r8 %! aflute_A
            r4 %! aflute_A
            \tweak text #tuplet-number::calc-fraction-text %! aflute_B
            \times 3/4 {                                   %! aflute_B
                e'8 %! aflute_B
                r8 %! aflute_B
                r8 %! aflute_B
                f'8 %! aflute_B
                r8 %! aflute_B
                e'8 %! aflute_B
                [ %! aflute_B
                f'8 %! aflute_B
                ] %! aflute_B
                r8 %! aflute_B
            } %! aflute_B
            \times 8/11 {
                d'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
                [ %! aflute_C
                d'8 %! aflute_C
                ] %! aflute_C
                r16
            }
            \times 8/11 {
                r16
                e'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
                d'8 %! aflute_C
                [ %! aflute_C
                e'8 %! aflute_C
                ] %! aflute_C
            }
            \times 2/3 { %! aflute_D
                c'8 %! aflute_D
                r8 %! aflute_D
                r8 %! aflute_D
                bf8 %! aflute_D
                r8 %! aflute_D
                c'8 %! aflute_D
            } %! aflute_D
            r4 %! Rests
            g8 %! aflute_A
            r8 %! aflute_A
            r4 %! aflute_A
            \times 2/3 { %! aflute_B
                e'8 %! aflute_B
                r8 %! aflute_B
                r8 %! aflute_B
                f'8 %! aflute_B
                r8 %! aflute_B
                e'8 %! aflute_B
            } %! aflute_B
            \times 4/7 { %! aflute_C
                d'8 %! aflute_C
                r8 %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
                [ %! aflute_C
                d'8 %! aflute_C
                ] %! aflute_C
                r8 %! aflute_C
                e'8 %! aflute_C
            } %! aflute_C
            \tweak text #tuplet-number::calc-fraction-text %! aflute_D
            \times 3/4 {                                   %! aflute_D
                c'8 %! aflute_D
                r8 %! aflute_D
                r8 %! aflute_D
                bf8 %! aflute_D
                r8 %! aflute_D
                c'8 %! aflute_D
                [ %! aflute_D
                bf8 %! aflute_D
                ] %! aflute_D
                r8 %! aflute_D
            } %! aflute_D
            r2 %! Rests
        } %! muda.score.instrument()
    } %! muda.score.instrument()
    \context Staff = "BassClarinet_Staff" %! muda.score.instrument()
    {                                     %! muda.score.instrument()
        \context Voice = "BassClarinet_Voice_1" %! muda.score.instrument()
        {                                       %! muda.score.instrument()
            \times 2/3 { %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                d8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
            } %! bclarinet_A
            \times 2/3 { %! bclarinet_B
                r8 %! bclarinet_B
                d,8 %! bclarinet_B
                r8 %! bclarinet_B
                r8 %! bclarinet_B
                f,8 %! bclarinet_B
                r8 %! bclarinet_B
            } %! bclarinet_B
            \tweak text #tuplet-number::calc-fraction-text %! bclarinet_C
            \times 6/11 {                                  %! bclarinet_C
                g,8 %! bclarinet_C
                [ %! bclarinet_C
                a,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                g,8 %! bclarinet_C
                r8 %! bclarinet_C
                a,8 %! bclarinet_C
                [ %! bclarinet_C
                g,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                a,8 %! bclarinet_C
            } %! bclarinet_C
            \times 2/3 { %! bclarinet_D
                c8 %! bclarinet_D
                r8 %! bclarinet_D
                e8 %! bclarinet_D
                r8 %! bclarinet_D
                r8 %! bclarinet_D
                c8 %! bclarinet_D
            } %! bclarinet_D
            r2 %! Rests
            \times 2/3 { %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                d8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
            } %! bclarinet_A
            \times 2/3 { %! bclarinet_B
                r8 %! bclarinet_B
                d,8 %! bclarinet_B
                r8 %! bclarinet_B
                r8 %! bclarinet_B
                f,8 %! bclarinet_B
                r8 %! bclarinet_B
            } %! bclarinet_B
            \tweak text #tuplet-number::calc-fraction-text %! bclarinet_C
            \times 6/11 {                                  %! bclarinet_C
                g,8 %! bclarinet_C
                [ %! bclarinet_C
                a,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                g,8 %! bclarinet_C
                r8 %! bclarinet_C
                a,8 %! bclarinet_C
                [ %! bclarinet_C
                g,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                a,8 %! bclarinet_C
            } %! bclarinet_C
            \tweak text #tuplet-number::calc-fraction-text %! bclarinet_D
            \times 3/4 {                                   %! bclarinet_D
                c8 %! bclarinet_D
                r8 %! bclarinet_D
                e8 %! bclarinet_D
                r8 %! bclarinet_D
                r8 %! bclarinet_D
                c8 %! bclarinet_D
                [ %! bclarinet_D
                e8 %! bclarinet_D
                ] %! bclarinet_D
                r8 %! bclarinet_D
            } %! bclarinet_D
            r4 %! Rests
            \times 2/3 { %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                d8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
            } %! bclarinet_A
            \times 2/3 { %! bclarinet_B
                r8 %! bclarinet_B
                d,8 %! bclarinet_B
                r8 %! bclarinet_B
                r8 %! bclarinet_B
                f,8 %! bclarinet_B
                r8 %! bclarinet_B
            } %! bclarinet_B
            \times 8/13 {
                g,8 %! bclarinet_C
                [ %! bclarinet_C
                a,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                g,8 %! bclarinet_C
                r8 %! bclarinet_C
                a,8 %! bclarinet_C
                [ %! bclarinet_C
                g,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r16.
            }
            \times 8/13 {
                r32
                a,8 %! bclarinet_C
                r8 %! bclarinet_C
                g,8 %! bclarinet_C
            }
            \tweak text #tuplet-number::calc-fraction-text %! bclarinet_D
            \times 3/4 {                                   %! bclarinet_D
                c8 %! bclarinet_D
                r8 %! bclarinet_D
                e8 %! bclarinet_D
                r8 %! bclarinet_D
                r8 %! bclarinet_D
                c8 %! bclarinet_D
                [ %! bclarinet_D
                e8 %! bclarinet_D
                ] %! bclarinet_D
                r8 %! bclarinet_D
            } %! bclarinet_D
            r4 %! Rests
            \times 2/3 { %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
                d8 %! bclarinet_A
                r8 %! bclarinet_A
                r8 %! bclarinet_A
            } %! bclarinet_A
            \times 2/3 { %! bclarinet_B
                r8 %! bclarinet_B
                d,8 %! bclarinet_B
                r8 %! bclarinet_B
                r8 %! bclarinet_B
                f,8 %! bclarinet_B
                r8 %! bclarinet_B
            } %! bclarinet_B
            \times 4/5 { %! bclarinet_C
                g,8 %! bclarinet_C
                [ %! bclarinet_C
                a,8 %! bclarinet_C
                ] %! bclarinet_C
                r8 %! bclarinet_C
                r8 %! bclarinet_C
                g,8 %! bclarinet_C
            } %! bclarinet_C
            \tweak text #tuplet-number::calc-fraction-text %! bclarinet_D
            \times 3/4 {                                   %! bclarinet_D
                c8 %! bclarinet_D
                r8 %! bclarinet_D
                e8 %! bclarinet_D
                r8 %! bclarinet_D
                r8 %! bclarinet_D
                c8 %! bclarinet_D
                [ %! bclarinet_D
                e8 %! bclarinet_D
                ] %! bclarinet_D
                r8 %! bclarinet_D
            } %! bclarinet_D
            r2 %! Rests
        } %! muda.score.instrument()
    } %! muda.score.instrument()
    \context PianoStaff = "Piano_StaffGroup" %! muda.score.instrument()
    <<                                       %! muda.score.instrument()
        \context Staff = "Piano_Staff_1" %! muda.score.instrument()
        {                                %! muda.score.instrument()
            \context Voice = "Piano_Voice_1" %! muda.score.instrument()
            {                                %! muda.score.instrument()
            } %! muda.score.instrument()
            \context Voice = "Piano_Voice_2" %! muda.score.instrument()
            {                                %! muda.score.instrument()
            } %! muda.score.instrument()
        } %! muda.score.instrument()
        \context Staff = "Piano_Staff_2" %! muda.score.instrument()
        <<                               %! muda.score.instrument()
            \context Voice = "Piano_Voice_3" %! muda.score.instrument()
            {                                %! muda.score.instrument()
            } %! muda.score.instrument()
            \context Voice = "Piano_Voice_4" %! muda.score.instrument()
            {                                %! muda.score.instrument()
            } %! muda.score.instrument()
        >> %! muda.score.instrument()
    >> %! muda.score.instrument()
    \context Staff = "Violin_Staff" %! muda.score.instrument()
    {                               %! muda.score.instrument()
        \context Voice = "Violin_Voice_1" %! muda.score.instrument()
        {                                 %! muda.score.instrument()
        } %! muda.score.instrument()
    } %! muda.score.instrument()
    \context Staff = "Viola_Staff" %! muda.score.instrument()
    {                              %! muda.score.instrument()
        \context Voice = "Viola_Voice_1" %! muda.score.instrument()
        {                                %! muda.score.instrument()
        } %! muda.score.instrument()
    } %! muda.score.instrument()
    \context Staff = "Cello_Staff" %! muda.score.instrument()
    {                              %! muda.score.instrument()
        \context Voice = "Cello_Voice_1" %! muda.score.instrument()
        {                                %! muda.score.instrument()
        } %! muda.score.instrument()
    } %! muda.score.instrument()
>> %! muda.Score()