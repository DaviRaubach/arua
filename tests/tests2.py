import abjad


class AnnotatedDuration(abjad.Duration):
    def __init__(self, annotation):
        self.annotation = annotation


dur = AnnotatedDuration((3, 8))
dur.annotation = "note"
print(dur.annotation)


staff = abjad.Staff("c'1 d'1 c'1. d'1. c'1. d'1. ")
abjad.hairpin("p < f", staff[:])
abjad.override(staff).dynamic_line_spanner.staff_padding = 3

durations = [(3, 4), (4, 4), (5, 4)]
result = abjad.mutate.split(staff[:], durations, cyclic=True,)
abjad.f(result)

meters = [abjad.Meter(_) for _ in durations]

result2 = abjad.select(staff).leaves()
result2 = result2.group_by

# for measure, time_sig in zip(result2, meters):
#     print(measure)
# abjad.Meter.rewrite_meter(measure, time_sig)


# time_signatures = []
# for item in in_time_signatures:
#     time_signatures.append(abjad.Meter(item))
# abjad.mutate().split(music, in_time_signature, cyclic=True)
# # selection
# abjad.Meter.rewrite_meter(music[:], time_signatures)
# selector = abjad.select(music).leaves()
# measures = selector.group_by_measure()
# for time, measure in zip(time_signatures, measures):
#     abjad.mutate(measure).rewrite_meter(time)

