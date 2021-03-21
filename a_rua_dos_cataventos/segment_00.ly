% Instruments definitions
\version "2.22.0"  
\language "english" 


\context Score = "Score"

<<                      
    \context TimeSignatureContext = "Global_Context"
	{}
	
    \context Staff = "AltoFlute_Staff"  
	    \with
	    {
			instrumentName = "Alto Flute"
			shortInstrumentName = "Afl."
			midiInstrument = "flute"
	    }{}
	
    \context Staff = "BassClarinet_Staff" 
	    \with
	    {
		    instrumentName = "Bass clarinet"
		    shortInstrumentName = "BCl."
		    midiInstrument = "clarinet"		
	    }{}
    
    \context PianoStaff = "Piano_StaffGroup" 
	    \with
	    {
			instrumentName = "Piano"
			shortInstrumentName = "Pno."
		    midiInstrument = "acoustic grand"
	    }{}
    
    \context Staff = "Violin_Staff"
	    \with
	    {
		    instrumentName = "Violin"
		    shortInstrumentName = "Vl."
		    midiInstrument = "violin"
	    }{}
    
    \context Staff = "Viola_Staff" 
	    \with
	    {
		    instrumentName = "Viola"
		    shortInstrumentName = "Vla."
		    midiInstrument = "viola"
	    }{}
    
    \context Staff = "Cello_Staff" 
	    \with
	    {
			instrumentName = "Cello"
			shortInstrumentName = "Cl."
			midiInstrument = "cello"
	    }{}
    
>> 

