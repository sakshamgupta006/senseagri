
$(window).scroll(function(){
console.log('asd');
			var wScroll = $(this).scrollTop();

			$('.logo').css({
				'transform' : 'translate(0px,'+ wScroll/2 +'%)'
			});
console.log('sdsad');

		if(wScroll >  $('.content').offset().top-($(window).height()/1.2)) {

			$('.content div').each(function(i){
						setTimeout(function(){
						$('.content div').eq(i).addClass('is-showing');
					},150 * (i+1));
					});

		}

		if(wScroll >  $('.container').offset().top-($(window).height()/1.5))  {
			console.log('hi');

			$('.container div ').each(function(i){
						
				setTimeout(function(){
						$('.container .div').eq(i).addClass('is-show');
					},150 * (i+1));
					});
		}

});