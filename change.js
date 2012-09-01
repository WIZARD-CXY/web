(function(window, document, undefined) {
	"use strict"

	var okButton = document.getElementById("okButton"),
		autoButton = document.getElementById("autoButton"),
		leftText = document.getElementById("leftText"),
		topText = document.getElementById("topText"),
		heart = document.getElementById("heart"),
		top = 0,
		left = 0;

	
	var interval = function() {
		
                   if(top<=100)
                   {                 
                          left+=8;
                          top=100;   
                   }
                   if(left>=1000)
                   {
                      left=1000;
                      top+=5;
                   }
                   if(top>=700)
                   {
                      left-=8;
                      top=700;
                   }
                   if(left<=300)
                   {
                      left=300;
                      top-=5;
                   }
			leftText.value = left;
			topText.value = top;
			heart.style.left = left + "px";
			heart.style.top = top + "px";
			setTimeout(interval, 100);
		
	};

	okButton.addEventListener("click", function() {
		heart.style.left = leftText.value + "px";
		heart.style.top = topText.value + "px";
	}, false);
	
	autoButton.addEventListener("click", function() {
		top = 0;
		left = 0;
		interval();
	}, false);
	
})(window, document);
