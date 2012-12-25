(function(window, document, undefined) {
	"use strict"

	var okButton = document.getElementById("okButton"),
		autoButton = document.getElementById("autoButton"),
		locateButton = document.getElementById("locateButton"),
		leftText = document.getElementById("leftText"),
		topText = document.getElementById("topText"),
		fish = document.getElementById("fish"),
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
			fish.style.left = left + "px";
			fish.style.top = top + "px";
			setTimeout(interval, 100);
		
	};
	var GetPosition=function(){
		  $.getJSON("cgi-bin/makeJSON.py", function(data) {
        		left=data.x;
			right=data.y;
			leftText.value = left;
			topText.value = top;
			fish.style.left = left + "px";
			fish.style.top = top + "px";
			setTimeout(GetPosition, 1000);
		  });
	};

	okButton.addEventListener("click", function() {
		fish.style.left = leftText.value + "px";
		fish.style.top = topText.value + "px";
	}, false);
	
	autoButton.addEventListener("click", function() {
		top = 0;
		left = 0;
		interval();
	}, false);
	
	locateButton.addEventListener("click", function() {
		top = 0;
		left = 0;
		GetPosition();
	}, false);
})(window, document);
