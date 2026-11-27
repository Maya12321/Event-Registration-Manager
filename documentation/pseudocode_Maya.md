# PSEUDOCODE Maya Chehab
__Type:__ Pseudocode  \
__Method:__ `search_participants()` in `EventManager` class  \
__Student:__ Maya Chehab

```text
FUNCTION search_participants(pid):
    IF pid IS IN participants THEN
        name <- participants[pid]
        confirmed <- empty list
        waiting_list <- empty list

        FOR EACH event IN events.values DO
            IF pid IS IN event.confirmed THEN
                APPEND event TO confirmed
            END IF

            IF pid IS IN event.waiting_list THEN
                APPEND event TO waiting_list
            END IF
        END FOR

        PRINT "Participant: " + name + " (" + pid + ")"

        IF confirmed IS EMPTY AND waiting_list IS EMPTY THEN
            PRINT "Participant isn't registered in any event."
        END IF

        IF confirmed IS NOT EMPTY THEN
            PRINT "Confirmed Events:"
            FOR EACH event IN confirmed DO
                PRINT event.event_id + " - " + event.name
            END FOR
        END IF

        IF waiting_list IS NOT EMPTY THEN
            PRINT "Waiting List:"
            FOR EACH event IN waiting_list DO
                PRINT event.event_id + " - " + event.name
            END FOR
        END IF
    ELSE
        PRINT "Participant ID not found."
    END IF

END FUNCTION
```
