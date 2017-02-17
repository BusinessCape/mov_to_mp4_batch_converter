#!/usr/bin/env python3


#cd /tmp/serv/sec/web/tmp/vids/batch2
#for x in *; do echo "https://familyape.com/tmp/vids/batch2/"$x; done;

from pycloak import shellutils
import sh, sys

inputs = {
   #'DSC_5747.MOV' : 'Hack1_income_vs_assets.mp4',
   #'DSC_5748.MOV' : 'Hack2_habits.mp4',
   #'DSC_5751.MOV' : 'Hack3_revocable_living_trust.mp4',
   #'DSC_5752.MOV' : 'Hack4_bigfoot.mp4',
   'DSC_5754.MOV' : 'Hack5_401K_help.mp4',
   #'DSC_5755.MOV' : 'Hack6_cost_segregation.mp4',
   #'DSC_5756.MOV' : 'Hack7_tax_14_day.mp4',
   'DSC_5758.MOV' : 'Hack8_kiddie_tax.mp4',
   #'DSC_5759.MOV' : 'Hack9_medicaid_nursing_home.mp4'
}


bad = False
for in_name in inputs:
   if not shellutils.file_exists(in_name):
      bad = True
      print(in_name)

if bad:
   sys.exit()

def print_out(line):
   #print(line)
   pass

convert_cmd = sh.Command('./convert.sh')

for in_name in inputs:
   out_name = inputs[in_name]

   print('doing: ' + out_name)
   print(convert_cmd(in_name, out_name, _out=print_out, _tty_in=True, _bg=False))


