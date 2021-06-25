$(document).ready(function(){
    // muestra el submenu principal
    let timer;
    $('#deptos').hover(
        function(){
            $('.submenu-1').css("display","block");
        },
        function(){
            timer = setTimeout(() => {
                $('.submenu-1').css("display","none");
            }, 300);
        }
    );
    $(".submenu-1").hover(
        function(){
            clearTimeout(timer);
        }
    );
    
    // FUNCNIONES HOVER PARA LA FLECHA
    $('.pape').hover(
        function(){
            $('.f1').css("display","inline-block");
            $('.submenu-2').css("display","block");
        },
        function(){
            $('.f1').css("display","none");
            $('.submenu-2').css("display","none");
        }
    );
    $('.ropa').hover(
        function(){
            $('.f2').css("display","inline-block");
            $('.submenu-3').css("display","block");
        },
        function(){
            $('.f2').css("display","none");
            $('.submenu-3').css("display","none");
        }
    );
    $('.acce').hover(
        function(){
            $('.f3').css("display","inline-block");
            $('.submenu-4').css("display","block");
        },
        function(){
            $('.f3').css("display","none");
            $('.submenu-4').css("display","none");
        }
    );

    animacionCanvas();
});

function mostrarcate(cata){
    var categoria = cata;
    console.log(categoria);
    if(categoria == "repo"){
        $('#reposteria-cata').css("display","block");
    }
}

function animacionCanvas(){
    // Obtenemos una referencia al canvas
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    // Generamos las coordenadas iniciales
    x = 0;
    y = 0;
    // Los frames seran renderizados por este intervalo
    // aproximadamente a 24 frames por segundo (fps)
    setInterval(function() {
        // Limpiamos el canvas, eliminando el contenido
        // desde el punto (0, 0) al punto (200, 200)
        ctx.clearRect(0, 0, 200, 200);    
        // Generamos nuevas coordenadas
        // Que basicamente representan un desplazamiento lineal
        x = x >= 100 ? 0 : x + 1;
        y = y >= 100 ? 0 : y + 1;
        // Y dibujamos nuevamente
        ctx.fillRect(x, y, 100, 100);
    }, 1000 / 60);
}
