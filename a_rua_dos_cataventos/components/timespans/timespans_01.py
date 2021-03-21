#!$HOME/github/my_venv/bin/python

# import os
import abjad
import muda
import abjadext.rmakers as rmakers
import collections
import pathlib

# work with timespans to generate durations that will be filled by rhythm makers

# new timespan list for aflute
# alternations must have the same lenght on each instrument
general_alternations = [[8, 4, 8]]
aflute_alternations = [
    [4, 4, 4, 6, 4],
    [4, 6, 6, 4, 2],
    [4, 6, 8, 4, 2],
    [4, 4, 4, 6, 4],

]
bclarinet_alternations = [
    [4, 4, 6, 4, 4],
    [4, 4, 6, 6, 2],
    [4, 4, 8, 6, 2],
    [4, 4, 4, 6, 4],

]

# presence of different materials
timespans_aflute = muda.timespan.AlternatingTimespans(
    n_annotations=5,  # different materials
    alternations=aflute_alternations,
    denominator=8,
    annotations=["aflute_A", "aflute_B", "aflute_C", "aflute_D", "Rests"],  # names of different materials
)
# new timespan list for bclarinet
timespans_bclarinet = muda.timespan.AlternatingTimespans(
    n_annotations=5,  # different materials
    alternations=bclarinet_alternations,
    denominator=8,
    annotations=["bclarinet_A", "bclarinet_B", "bclarinet_C", "bclarinet_D", "Rests"],  # names of different materials
)
# new timespan list for piano
timespans_piano1e3 = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=general_alternations,
    denominator=8,
    annotations=["Mat_A", "Mat_B", "Rests"],  # names of different materials
)
# new timespan list for violin
timespans_strings = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=general_alternations,
    denominator=8,
    annotations=["Mat_A", "Mat_B", "Rests"],  # names of different materials
)

instruments_timespans = [
    timespans_aflute,
    timespans_bclarinet,
    # timespans_piano1e3,
    # timespans_strings,
]

for instrument_ts1, instrument_ts2 in zip(
    instruments_timespans, instruments_timespans[1:]
):
    error_str = "Instruments timespans must have the same total duration."
    assert instrument_ts1.duration == instrument_ts2.duration, error_str

durations_aflute = timespans_aflute.AnnotatedDurations()
durations_bclarinet = timespans_bclarinet.AnnotatedDurations()
durations_piano = timespans_piano1e3.AnnotatedDurations()
durations_strings = timespans_strings.AnnotatedDurations()

coincident_offsets = []
for ts_list1, ts_list2 in zip(
    instruments_timespans, instruments_timespans[1:]
):
    for i, (span1, span2) in enumerate(zip(ts_list1, ts_list2)):
        if i == 0:
            coincident_offsets.append(abjad.Offset(0))
            if span1.stop_offset == span2.stop_offset:
                coincident_offsets.append(abjad.Offset(span1.stop_offset))
        else:
            if span1.stop_offset == span2.stop_offset:
                coincident_offsets.append(abjad.Offset(span1.stop_offset))
        if span1.annotation == "Mat_B" and span2.annotation == "Mat_B":
            if span1 <= span2:
                coincident_offsets.append(span1.start_offset)
            else:
                coincident_offsets.append(span2.start_offset)
            if span1.stop_offset > span2.stop_offset:
                coincident_offsets.append(abjad.Offset(span1.stop_offset))

coincident_offsets.sort()

permitted_meters = abjad.MeterList(
    [
        (5, 4),
        (9, 8),
        (4, 4),
        (7, 8),
        (3, 4),
        (5, 8),
        (2, 4),
        (3, 8),
        (5, 16),
        (1, 4),
        # (3, 16),
        # (1, 8),
    ]
)


# remove repeated
coincident_offsets = list(dict.fromkeys(coincident_offsets))
# counter
offset_counter = abjad.OffsetCounter(coincident_offsets)
# fit meters
fitted_meters = abjad.Meter.fit_meters(
    argument=offset_counter, meters=permitted_meters,  # maximum_run_length=1
)
# make time signatures
time_signatures = [_.implied_time_signature for _ in fitted_meters]

for i in time_signatures:
    print("Time Signature:", i)


final_list = abjad.TimespanList()
meters = []
for off1, off2 in zip(coincident_offsets, coincident_offsets[1:]):
    new_ts = abjad.AnnotatedTimespan(start_offset=off1, stop_offset=off2)
    final_list.append(new_ts)
    meters.append(abjad.Meter(new_ts.duration))


if __name__ == "__main__":
    illustrate_timespans = abjad.TimespanList()
    for list_ in instruments_timespans:
        for ts in list_:
            illustrate_timespans.append(ts)

    abjad.show(illustrate_timespans, scale=0.6, key="annotation")
    print("aflute durations:", durations_aflute)
    print("bclarinet durations:", durations_bclarinet)

    pass
