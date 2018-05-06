var agente = navigator.userAgent.toLowerCase()

function carruselImagenes()
{
	var slider = document.querySelector('.slider'),
		n = 0,
		imagenes = new Array(
			'images/s1.jpg',
			'images/s2.jpg',
			'images/s3.jpg',
			'images/p10.jpg',
			'images/p11.jpg',
			'images/p12.jpg',
			'images/p7.jpg',
			'images/p6.jpg'
		)

		function opacidad(valor)
		{
			slider.style.opacity = valor/100
			console.log(slider.style.opacity)
			
		}

		function fadeIn()
		{
			for(var i=0; i <= 100; i++)
			{
			        opacidad(i)
				setTimeout((function (i){
					return function (){
						opacidad(i)
					}
				})(i), i*10)
			}
		}
		

		function fadeOut(callback)
		{
			for(var i=100; i>0; i--)
			{

				setTimeout((function (i){
					return function (){

						opacidad(i)
						if(i==0)
						{
							slider.style.backgroundImage = 'url(' + imagenes[n] + ')'
							n++

							if(n==imagenes.length)
							{
								n=0
							}

							callback()
						}
						
					}
				})(100-i), i*10)
			}
		}

		reproducirSlider = function () { fadeOut(fadeIn) }

		setInterval(reproducirSlider, 8000)
}
if(agente.search(/edge|msie|firefox/) > -1)
{
	carruselImagenes()
	alert('No estoy en Chrome')
}
else
{
	alert('Estoy en Chrome')	
}