$(function(){
        // HTML объект Солнца
        var sun = document.getElementById('sun');
        // jQuery объект Солнца
        var $sun = $(sun);
        // Предзакатное Солнце
        var $sunsetSun = $('#sunsetSun');
        // Предзакатное небо
        var $sunsetSky = $('#sunsetSky');
        // Ночное небо
        var $nightSky = $('#nightSky');
        // Дневной луг
        var $grass = $('#grass');
        // Ночной луг
        var $nightGrass = $('#nightGrass');

        // Делаем наше Солнце перемещаемым объектом
        Drag.init(sun);

        // "Рисуем" 300 звезд в случайных позициях
        makeStars(300);

        // Начальная позиция Солнца (сбивается при вызове Drag.init() выше)
        $sun.css({
            'top': 20,
            'left': 20
        });

        // Данное событие вызывается при перемещении объекта
        sun.onDrag = function(x, y){
            // Отступ Солнца от верхней границы экрана
            var sunTop = $sun.css('top');
            // Высота расположения Солнца относительно высоты неба, в процентах
            var sunPosition = parseInt(sunTop) / (parseInt($sunsetSky.css('height')) / 100);
            // Высота расположения Солнца относительно высоты экрана, в процентах
            var sunAbsolutePosition = parseInt(sunTop) / ($(window).height() / 100);

            // Изменяем прозрачность предзакатного неба
            $sunsetSky.css('opacity', (Math.floor(sunPosition) / 100));
            // Изменяем прозрачность предзакатного Солнца
            $sunsetSun.css('opacity', (Math.floor(sunPosition) / 100));
            // Изменяем прозрачность ночного луга
            $nightGrass.css('opacity', (Math.floor(sunPosition) / 100));

            // Проверяем, что Солнце находится на высоте ниже 60% относительно нижней части экрана
            if (sunAbsolutePosition >= 40){
                // Высота, на которой начинают проявляться звезды и ночное небо
                var start = $(window).height() / 100 * 40;
                // Высота, на которой звезды имеют максимальную яркость, а ночное небо перекрывает собой все остальные
                var end = $(window).height() / 100 * 65;
                // Позиция в процентах от start до end
                var pos = (parseInt(sunTop) - parseInt(start)) / ((parseInt(end) - parseInt(start)) / 100);
                // Изменяем прозрачность ночного неба
                $nightSky.css('opacity', pos / 100);
                // Изменяем прозрачность звезд
                $('.star').css('opacity', pos / 100);
            }
            // Если Солнце находится выше 60% относительно нижней части экрана, то скрываем все звезды
            else {
                $('.star').css('opacity', 0);
            }
        }

        // Возвращает случайное число в диапазоне от start до end
        function range(start, end){
            if ((start >= 0) && (end >= 0)){
                return Math.round(Math.abs(start) + (Math.random() * (Math.abs(end) - Math.abs(start))));
            }
            else if ((start <= 0) && (end <= 0)){
                return 0 - (Math.round(Math.abs(start) + (Math.random() * (Math.abs(end) - Math.abs(start)))));
            }
            else{
                return Math.round(((start) + Math.random() * (end - start)));
            }
        }

        // Генерирует count звезд в случайных позициях
        function makeStars(count){
            for (var i=0; i<=count; i++){
                // Создаем элемент, который будет нашей звездой
                var star = $(document.createElement('div'));
                // Присваиваем ему класс star
                star.addClass('star');
                // Вносим в DOM и делам дочерним к body
                star.appendTo('#sun-block');
                // Объявляем стили
                star.css({
                    // Высота - случайное значение от 0 до 60% от высоты экрана
                    'top': range(0, parseInt($(window).height()) / 100 * 60),
                    // Отступ слева - случайное значение от 0 до текущей ширины экрана
                    'left': range(0, $(window).width())
                });
            }
        }

        var sunMove = function(sunId, offset, timeout) {
            $('#' + sunId).css({
                left: '+=' + offset.left,
                top: '+=' + offset.top
            }).get(0).onDrag();
            setTimeout(function() {
                sunMove(sunId, offset, timeout);
            }, timeout);
        }

        $(document).on('click', '#interface a', function(e){
            sunMove('sun', {left:1, top:1}, 50);
            e.preventDefault();
        });
	
	$(document).ready(function() {
	    sunMove('sun', {left:1, top:1}, 50);
            e.preventDefault();
	});
});
