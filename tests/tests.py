import os
import abjad
import tsmakers

print(os.path.dirname(__file__))

print("   ")
file_name = os.path.basename(__file__)
file_name = os.path.splitext(file_name)[0]
illust_path = "../../a_rua_dos_cataventos/segments/illustrations"
new_file = illust_path+"/"+str(file_name)+".ly"
print(new_file)

                

container = abjad.Container("c''4 d''8 e''16 e''32 e''4 e''4 e''4")
meters = [(3, 4), (4, 4), (5, 4)]
meters = [abjad.Meter(_) for _ in meters]


argument = [(0, 4), (4, 4), (8, 4), (12, 4), (16, 4)]
for meter in abjad.Meter.fit_meters(container, meters):
    print(meter.implied_time_signature)
    
    
    
    
# for staff in score:
#     for container in staff:
#         leaf = abjad.get.leaf(container, 0)
#         time_signature = abjad.get.indicator(leaf, abjad.TimeSignature)
#         abjad.Meter.rewrite_meter(container[:], time_signature)
#
#
abjad.f(container)
                        