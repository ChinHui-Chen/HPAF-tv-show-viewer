#!/usr/bin/env python
import sys

prev_tvshow   = "  "                #initialize previous tv show to blank string
count_viewers = 0 
is_selected   = False
line_cnt      = 0                   #count input lines

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    curr_tvshow = key_value[0]      #key is first item in list, indexed by 0
    value_in    = key_value[1]      #value is 2nd item

    # for output
    if curr_tvshow != prev_tvshow and line_cnt>1 :
        if( is_selected ):
            print( '%s %d' % (prev_tvshow, count_viewers) )             
        prev_tvshow = curr_tvshow   #set up previous tv show for the next set of input lines
        is_selected = False
        count_viewers = 0

    if ( value_in.isdigit() ): 
        count_viewers = count_viewers + int(value_in)
    if ( value_in == "ABC" ):
	is_selected = True

# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------
if is_selected:
    print( '%s %d' % (prev_tvshow, count_viewers) )             

