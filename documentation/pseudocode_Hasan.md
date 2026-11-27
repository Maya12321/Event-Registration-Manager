# PSEUDOCODE Hasan Ismail
__Type:__ Pseudocode  \
__Method:__ `register_participant(pid)` in `Event` class  \
__Student:__ Hasan Ismail

```text
FUNCTION register_participant(pid)

    IF pid is in confirmed or waiting_list THEN
        RETURN False, "Error: Already registered."
    END IF

    IF len(confirmed) < capacity THEN
        add pid to confirmed
        RETURN True, "Success: Added to confirmed seats."
    ELSE:
        add pid to waiting_list
        RETURN True, "Notice: Added to waiting list."
    END IF

END FUNCTION
```
