\version "2.22.1"
\paper { indent=0 }
\header {title="New Five Cent"}
music ={
\time 4/4
\repeat volta 2 {
%
2.0.4 0.2.8( 0.0.8 0.2.8 0.3.8 0.2.8 0.0.8)
1.0.8 0.2.8 0.0.8 1.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                
2.0.8 2.2.8 2.0.8 3.5.8 3.4.8 3.5.8 2.0.4                                      
0.0.2~  0.0.2
2.0.4 0.2.8 0.0.8 0.2.8 0.3.8 0.2.8 0.0.8                                       
1.0.8 0.2.8 0.0.8 1.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                 
2.0.8 3.5.8  3.4.8 3.0.8 3.2.2                                                  
%
}                                                                                
\alternative {
{
% 
3.0.2~  3.0.2
%
}
{
%
3.0.2 3.0.4 1.0.8 2.2.8
%
}
}
\repeat volta 2 {
%
2.0.8 3.2.8 3.4.8 3.5.8 3.4.4 1.0.8 2.2.8                                       
2.0.8 3.2.8 3.4.8 3.5.8 3.4.4 1.0.8 2.2.8                                       
2.0.4 3.4.4 3.5.4 3.4.4                                                         
3.2.2  3.2.4 1.0.8 2.2.8                                                        
2.0.8 3.4.8 3.0.8 3.4.8 2.0.8 3.4.8 3.0.8 3.2.16 3.4.16                         
3.5.8 3.4.8 3.5.8 2.0.8 2.2.8 2.4.8 1.0.8 2.2.8                                 
2.0.8 3.5.8  3.4.8 3.0.8 3.2.2                                                  
%
}
\alternative {
{
%
3.0.2 3.0.4  1.0.8 2.2.8
%
}
{
%
1.0.2~ 1.0.2
%
}
}
\bar "|."
}

\score {                                                                       
\new Staff \with {                                                             
     \omit StringNumber                                                         
     }                                                                          
     {                                                                          
      \key d \major                                                             
      \numericTimeSignature                                                    
      {\transpose c d {\music}}                                               
}                                                                               
}                                                                               
\score {                                                                       
\new TabStaff \with {                                                         
    tablatureFormat = #fret-number-tablature-format-banjo                       
    stringTunings = \stringTuning <a'' d' a' d'' e''>                          
  }                                                                             
  {                                                                             
    {                                                                           
      \clef moderntab                                                          
      \numericTimeSignature                                                    
      \tabFullNotation                                                         
      {\transpose c d {\music}}                                               
    }                                                                           
  }                                                                             
\header {                                                                       
  piece = "aDADE"                                                               
}                                                                               
}                                                                               
