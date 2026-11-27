# PSEUDOCODE Hasan Ismail
Type: Pseudocode  \
Method: register_participant(pid) in Event class  \
Student: Hasan Ismail

## `register_participant(pid)` Pseudocode

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
