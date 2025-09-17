[[Pseudo-code]]

### [[Cheat Sheet]]
#### Exemples:

ALGORITHME CalculerAireCercle 
**CONSTANTS** : 
PI <- 3.14 
**VARIABLES** : 
a : FLOAT 
r : FLOAT 
essais : INTEGER <- 0 
==BEGIN ==
DO 
READ( r ) 
Essais <- essais +1 
WHILE ( r <= 0 AND essais <= 3 ) 
IF ( r <= 0 ) 
EXIT() 
ELSE 
a <- PI * r * r 
PRINT( a ) 
END_IF 
==END ==

**FUNCTION** checkAuthenticationPreconditions (user: Objet) : Bool 
h <- CURRENT_TIME 
RETURN  isActive AND ( NOT isOnHolydays AND 06:00 <= h <= 22:00) OR ( role = “Admin”)) 
END_FUNCTION 

IF (checkAuthenticationPrecondtions(user))
...
END_IF