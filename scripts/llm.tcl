bind pubm - "*" llm_query

proc llm_query {nick uhost hand chan text} {
 global botnick
    if {$nick == $botnick} { return }

    # Capture all output from helper
    set result [exec python3 helpers/llm_query.py $nick $text]

    # Split into lines and send each one separately
    foreach line [split $result "\n"] {
        set line [string trim $line]
        if {$line ne ""} {
            putserv "PRIVMSG $chan :$line"
        }
    }
}
