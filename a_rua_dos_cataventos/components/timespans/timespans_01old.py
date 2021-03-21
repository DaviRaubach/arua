#!$HOME/github/my_venv/bin/python

# import os
import abjad
import tsmakers
import muda
import abjadext.rmakers as rmakers
import collections
import evans
import pathlib

tsmakers.BoundaryTimespanMaker()
# work with timespans to generate durations that will be filled by rhythm makers

# voices names
music_specifiers = abjad.OrderedDict([(f"Voice {i+1}", None) for i in range(9)])

# segment size
target_timespan = abjad.Timespan(0, 16)

# taleas
timespan_maker = tsmakers.TaleaTimespanMaker(
    # initial_silence_talea=rmakers.Talea(counts=([13, 5, 1]), denominator=4),
    playing_talea=rmakers.Talea(counts=([4]), denominator=8),
    playing_groupings=([1, 2, 1, 2, 3]),
    silence_talea=rmakers.Talea(counts=([13, 5, 1]), denominator=4),
)

# temporary list
temp_list = timespan_maker(
    music_specifiers=music_specifiers, target_timespan=target_timespan
)

# the same algorythm generates durations for different voices using the annotation
# the list bellow contains all the timespans
the_list = muda.timespan.TimespanList()

# translate evans classes to abjad AnnotatedTimespan
for span in temp_list:
    new_span = abjad.AnnotatedTimespan(
        span.start_offset, span.stop_offset, annotation=span.voice_name,
    )
    the_list.append(new_span)

# this is a muda function that separate the timespan according to its annotation (its voice name)
separated_list = the_list.SeparateTimespansByAnnotation()

# another muda function that generates the silent timespans for each voice (the "negative", the opposite)
for timespan_list in separated_list:
    timespan_list.OppositeTimespanList()
    timespan_list.sort()

# convert to durations
durations_list = []

# the lists bellow go to materials and are used as divisions in rhythm makers
for timespan_list in separated_list:
    dur_list = timespan_list.AnnotatedDurations()
    durations_list.append(dur_list)

# new timespan list for aflute
# alternations must have the same lenght on each instrument
timespans_aflute = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=[[8, 6, 6], [12, 5, 5], [9, 7, 5],],  # presence of different materials
    denominator=8,
    annotations=["Mat_1", "Mat_2", "Rests"],  # names of different materials
)
# new timespan list for bclarinet
timespans_bclarinet = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=[[5, 6, 6], [14, 5, 5], [9, 7, 5],],  # presence of different materials
    denominator=8,
    annotations=["Mat_1", "Mat_2", "Rests"],  # names of different materials
)
# new timespan list for piano
timespans_piano1e3 = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=[[14, 5, 5], [5, 6, 6], [9, 7, 5],],  # presence of different materials
    denominator=8,
    annotations=["Mat_1", "Mat_2", "Rests"],  # names of different materials
)
# new timespan list for violin
timespans_strings = muda.timespan.AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=[[9, 7, 5], [14, 5, 5], [5, 6, 6]],  # presence of different materials
    denominator=8,
    annotations=["Mat_1", "Mat_2", "Rests"],  # names of different materials
)


instruments_timespans = [timespans_aflute, timespans_bclarinet]

for instrument_ts1, instrument_ts2 in zip(
    instruments_timespans, instruments_timespans[1:]
):
    error_str = "Instruments timespans must have the same total duration."
    assert instrument_ts1.duration == instrument_ts2.duration, error_str


durations_aflute = timespans_aflute.AnnotatedDurations()
durations_bclarinet = timespans_bclarinet.AnnotatedDurations()
durations_piano1 = timespans_piano1e3.AnnotatedDurations()
durations_piano3 = timespans_piano1e3.AnnotatedDurations()
durations_violin = timespans_strings.AnnotatedDurations()
durations_viola = timespans_strings.AnnotatedDurations()
durations_cello = timespans_strings.AnnotatedDurations()


# durations_piano1 = durations_list[2]
# durations_piano3 = durations_list[2]
# durations_violin = durations_list[3]
# durations_viola = durations_list[4]
# durations_cello = durations_list[5]


# time signatures for these timespan structures
permitted_meters = [
    # (7, 4),
    (5, 4),
    (4, 4),
    (3, 8),
    (11, 16),
    # (3, 16),
]
permitted_meters = [abjad.Meter(_) for _ in permitted_meters]

# argument = [_.duration for _ in timespans_aflute]
# print(argument)
# counter_path = f"""{pathlib.Path(__file__).parent}/segment_01_offset_counter.pdf"""
# abjad.persist.as_pdf(offset_counter, pdf_file_path=counter_path, scale=0.70)  # PDF
# abjad.io.open_file(counter_path)

# ts_lists = abjad.TimespanList([timespans_aflute, timespans_bclarinet])
# all_ts_list = abjad.TimespanList()

# for tlist in ts_lists:
#     for span in tlist:
#         all_ts_list.append(span)

# all_ts_list.sort()
final_list = abjad.TimespanList()

coincident_offsets = []
for i, (span1, span2) in enumerate(zip(timespans_aflute, timespans_bclarinet)):
    if i == 0:
        coincident_offsets.append(abjad.Offset(0))
        if span1.stop_offset == span2.stop_offset:
            coincident_offsets.append(abjad.Offset(span1.stop_offset))
    else:
        if span1.stop_offset == span2.stop_offset:
            coincident_offsets.append(abjad.Offset(span1.stop_offset))
    if span1.annotation == "Mat_2" and span2.annotation == "Mat_2":
        if span1 <= span2:
            coincident_offsets.append(span1.start_offset)
        else:
            coincident_offsets.append(span2.start_offset)
        if span1.stop_offset > span2.stop_offset:
            coincident_offsets.append(abjad.Offset(span1.stop_offset))
        # else:
        # print(span1.stop_offset)
        # print(span2.stop_offset)
        # coincident_offsets.append(abjad.Offset(span2.stop_offset))


coincident_offsets.sort()
meters = []
for off1, off2 in zip(coincident_offsets, coincident_offsets[1:]):
    new_ts = abjad.AnnotatedTimespan(start_offset=off1, stop_offset=off2)
    final_list.append(new_ts)
    meters.append(abjad.Meter(new_ts.duration))

fitted_meters = abjad.Meter.fit_meters(
    argument=final_list, meters=permitted_meters,  # maximum_run_length=1
)
time_signatures = [_.implied_time_signature for _ in fitted_meters]

print(time_signatures)

# time_signatures = [_.implied_time_signature for _ in meters]
# print(time_signatures)

# offset_counter = abjad.OffsetCounter(coincident_offsets)

# MetricAccentKernel = abjad.MetricAccentKernel
# counter = abjad.MetricAccentKernel.count_offsets(coincident_offsets)
# fitted_meters = abjad.Meter.fit_meters(
#     argument=final_list, meters=permitted_meters, maximum_run_length=1
# )
# print([_ for _ in fitted_meters])
# time_signatures = [abjad.TimeSignature(_.pair) for _ in durations_aflute]
# time_signatures = [_.implied_time_signature for _ in fitted_meters]
# print(time_signatures)

# time_signatures.append(abjad.TimeSignature((1, 8)))  # for ending skip

# bounds = abjad.math.cumulative_sums([_.duration for _ in time_signatures])
# print(bounds)


if __name__ == "__main__":
    # abjad.show(final_list, scale=0.8, key="annotation")
    pass

