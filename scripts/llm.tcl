bind pubm - "*" llm_query

proc llm_query {nick uhost hand chan text} {
    if {$nick == "EGGDROP-BOT-NAME"} { return } # Set your eggdrop bot's name.

    # Capture all output from helper
    set result [exec python3 helpers/llm_query.py $text]

    # Split into lines and send each one separately
    foreach line [split $result "\n"] {
        set line [string trim $line]
        if {$line ne ""} {
            putserv "PRIVMSG $chan :$line"
        }
    }
}
