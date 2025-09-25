[[Algorithme]]

## Deviner le nombre

```
Algorithm GuessTheNumber  
VARIABLES:  
  targetNumber: INT  
  attempt: INT  
  
CONSTANTS:  
  MIN <- 1  
  MAX <- 1000  
  
BEGIN  
  targetNumber <- RANDOM(MIN,MAX)    // Nombre à deviner  
  DO  
    READ(attempt)  
    IF attempt > targetNumber  
       PRINT("trop grand")  
    ELSIF attempt < targetNumber  
       PRINT("trop petit")  
    ELSE  
       PRINT("gagné")  
    END_IF  
  WHILE attempt <> targetNumber  
END
```

## Spotify

![[Spotify - Problématiques.pdf]]
