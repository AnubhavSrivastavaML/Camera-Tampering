



 This Repository provide script to check if camera is tampered or not using live feed.
 
 This script can easily run  on small hardware such as Raspberry pi with real time streaming.
 
 Algorithm : 
 
 Image :
 
................................................................................. 

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................

.		.		.		.		.		.	

.		.		.		.		.		.	

.................................................................................


Steps:

	Image is divided into nxn matrix randomly.
	
	For each divided image random subimages are stored as template.
	
	For each iteration the templates are matched and checked for and change.
	
	If the change if greater than certain threshold value a alert can be generated.
	
	Please Check the for differebt parameter usage.
