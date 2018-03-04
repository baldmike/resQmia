$(document).ready(function(){

    console.log("resQmia_app is now ready to rock.");
    $('.brand').fadeIn(2000);
    $('.login').fadeIn(3000);
    // $('.brand2').slideDown(5000)

    $('#login_button').click(function(){
        $('.brand').fadeOut(1000);
        $('.login').fadeOut(1000);
    })

    $('[data-toggle="tooltip"]').tooltip(); 
    
    var chicago_url = "http://api.openweathermap.org/data/2.5/weather?zip=60641,us&APPID=cf8903b4094a518b0d20af5a7ebe6e8b";

    $.get(chicago_url, function(weather) {
        var temp = kelToFahr(weather.main.temp);
        var conditions = weather.weather["0"].description
        $('#weather').append(temp + ", with " + conditions);
    })

    function kelToFahr (kelvins) {
        var fahr = Math.floor(kelvins * (9/5) - 459.67);
        var temp = fahr.toString();
        return "It\'s " + temp + String.fromCharCode(176) + " outside";
    }

    function theDay() {
        var d = new Date(),
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
        return days[d.getDay()]+'&nbsp &nbsp &nbsp &nbsp &nbsp'+months[d.getMonth()]+' '+d.getDate()+' '+d.getFullYear();
    }
    
    function theTime() {
        
        var t = new Date(),
        minutes = t.getMinutes().toString().length == 1 ? '0' + t.getMinutes() : t.getMinutes(),
        hours = hoursTime(),
        ampm = t.getHours() >= 12 ? 'pm' : 'am';
        hoursTime(hours);

        function hoursTime() {
            var hour = t.getHours().toString().length == 1 ? '0' + t.getHours() : t.getHours();
                if (hour > 12) {
                    hour -= 12;
                } return hour;
        }
        
        return hours + ':' + minutes + ampm
    }

    function timeOutput() {
        document.getElementById('date').innerHTML=theDay();
        document.getElementById('time').innerHTML=theTime();
    }
    // get the time every 1000 [increments of time which I believe to be milliseconds]
    setInterval(timeOutput, 1000);
    timeOutput()



    
    var microchip = $('#microchip')
    microchip.click(function(){
        $('#microchip-number').toggleClass('hidden')
        console.log('microchip hit')
    })

    var picture = $('#picture')
    picture.click(function(){
        $('#picture_box').toggleClass('hidden')
    })

    var rabiesVacTrue = $('#rabiesVacTrue')
    rabiesVacTrue.change(function(){
        $('#rabiesVacFalse').toggleClass('current-input')
        $('#rabiesVacTrue').toggleClass('current-input')
        $('#rabies_number').toggleClass("hidden")
    })

    var rabiesVacFalse = $('#rabiesVacFalse')
    rabiesVacFalse.change(function(){
        $('#rabiesVacFalse').toggleClass('current-input')
        $('#rabiesVacTrue').toggleClass('current-input')
        $('#rabies_number').toggleClass("hidden")
    })

    var da2ppVacTrue = $('#da2ppVacTrue')
    da2ppVacTrue.change(function(){
        $('#da2ppVacTrue').toggleClass('current-input')
        $('#da2ppVacFalse').toggleClass('current-input')
    })

    var da2ppVacFalse = $('#da2ppVacFalse')
    da2ppVacFalse.change(function(){
        $('#da2ppVacFalse').toggleClass('current-input')
        $('#da2ppVacTrue').toggleClass('current-input')
    })

    var leptoVacTrue = $('#leptoVacTrue')
    leptoVacTrue.change(function(){
        $('#leptoVacTrue').toggleClass('current-input')
        $('#leptoVacFalse').toggleClass('current-input')
    })

    var leptoVacFalse = $('#leptoVacFalse')
    leptoVacFalse.change(function(){
        $('#leptoVacFalse').toggleClass('current-input')
        $('#leptoVacTrue').toggleClass('current-input')
    })

    var bordVacTrue = $('#bordVacTrue')
    bordVacTrue.change(function(){
        $('#bordVacTrue').toggleClass('current-input')
        $('#bordVacFalse').toggleClass('current-input')
    })

    var bordVacFalse = $('#bordVacFalse')
    bordVacFalse.change(function(){
        $('#bordVacFalse').toggleClass('current-input')
        $('#bordVacTrue').toggleClass('current-input')
    })

    var civVacTrue = $('#civVacTrue')
    civVacTrue.change(function(){
        $('#civVacTrue').toggleClass('current-input')
        $('#civVacFalse').toggleClass('current-input')
    })

    var civVacFalse = $('#civVacFalse')
    civVacFalse.change(function(){
        $('#civVacFalse').toggleClass('current-input')
        $('#civVacTrue').toggleClass('current-input')
    })

    var heartwormPrevTrue = $('#heartwormPrevTrue')
    heartwormPrevTrue.change(function(){
        $('#heartwormPrevTrue').toggleClass('current-input')
        $('#heartwormPrevFalse').toggleClass('current-input')
    })

    var heartwormPrevFalse = $('#heartwormPrevFalse')
    heartwormPrevFalse.change(function(){
        $('#heartwormPrevFalse').toggleClass('current-input')
        $('#heartwormPrevTrue').toggleClass('current-input')
    })

    var fleaPrevTrue = $('#fleaPrevTrue')
    fleaPrevTrue.change(function(){
        $('#fleaPrevTrue').toggleClass('current-input')
        $('#fleaPrevFalse').toggleClass('current-input')
    })

    var fleaPrevFalse = $('#fleaPrevFalse')
    fleaPrevFalse.change(function(){
        $('#fleaPrevFalse').toggleClass('current-input')
        $('#fleaPrevTrue').toggleClass('current-input')
    })
    
    var heartwormTestTrue = $('#heartwormTestTrue')
    heartwormTestTrue.change(function(){
        $('#heartwormTestTrue').toggleClass('current-input')
        $('#heartwormTestFalse').toggleClass('current-input')
    })

    var heartwormTestFalse = $('#heartwormTestFalse')
    heartwormTestFalse.change(function(){
        $('#heartwormTestFalse').toggleClass('current-input')
        $('#heartwormTestTrue').toggleClass('current-input')
    })

    var fecalTestTrue = $('#fecalTestTrue')
    fecalTestTrue.change(function(){
        $('#fecalTestTrue').toggleClass('current-input')
        $('#fecalTestFalse').toggleClass('current-input')
    })

    var fecalTestFalse = $('#fecalTestFalse')
    fecalTestFalse.change(function(){
        $('#fecalTestFalse').toggleClass('current-input')
        $('#fecalTestTrue').toggleClass('current-input')
    })

    var dewormerTestTrue = $('#dewormerTestTrue')
    dewormerTestTrue.change(function(){
        $('#dewormerTestTrue').toggleClass('current-input')
        $('#dewormerTestFalse').toggleClass('current-input')
    })

    var dewormerTestFalse = $('#dewormerTestFalse')
    dewormerTestFalse.change(function(){
        $('#dewormerTestFalse').toggleClass('current-input')
        $('#dewormerTestTrue').toggleClass('current-input')
    })

       


    $('#new_rabies_button').click(function(){
        $('#new_rabies').toggleClass("hidden");
    })

    $('#new_da2pp_button').click(function(){
        $('#new_da2pp').toggleClass("hidden");
    })

    $('#new_lepto_button').click(function(){
        $('#new_lepto').toggleClass("hidden");
    })

    $('#new_bord_button').click(function(){
        $('#new_bord').toggleClass("hidden");
    })

    $('#new_civ_button').click(function(){
        $('#new_civ').toggleClass("hidden");
    })

    $('#new_heart_prev_button').click(function(){
        $('#new_heart_prev').toggleClass("hidden");
    })

    $('#new_flea_prev_button').click(function(){
        $('#new_flea_prev').toggleClass("hidden");
    })

    $('#new_heart_test_button').click(function(){
        $('#new_heart_test').toggleClass("hidden");
    })

    $('#new_fecal_test_button').click(function(){
        $('#new_fecal_test').toggleClass("hidden");
    })

    $('#new_dewormer_button').click(function(){
        $('#new_dewormer').toggleClass("hidden");
    })

    $('#new_fvrcp_button').click(function(){
        $('#new_fvrcp').toggleClass("hidden");
    })

    $('#new_revolution_button').click(function(){
        $('#new_revolution').toggleClass("hidden");
    })

    $('#new_fivfelv_button').click(function(){
        $('#new_fivfelv').toggleClass("hidden");
    })

    $('#fix_alert').click(function(){
        $('#fix_box').toggleClass("hidden")
    })

    $('#chip_alert').click(function(){
        $('#chip_box').toggleClass("hidden")
    })


    current_dog_selection = '#all_alerts'
    current_dog_button = '#show_all_alerts'
    console.log('Current dog view is', current_dog_selection)

    function toggle_selection(new_selection, existing_selection, new_button, existing_button) {
        $(existing_selection).hide()
        $(new_selection).show()
        $(existing_button).removeClass('btn-gray').addClass('btn-white')
        $(new_button).removeClass('btn-white').addClass('btn-gray')
        current_dog_button = new_button
        current_dog_selection = new_selection
        console.log('THE Current dog selection is now ', current_dog_selection)
        console.log('THE Current dog button is now ', current_dog_button)
    }

    $('#show_all_dogs').click(function(){
        a = '#all_dogs'
        c = '#show_all_dogs'
        toggle_selection(a, current_dog_selection, c, current_dog_button)
    })

    $('#show_all_alerts').click(function(){
        a = '#all_alerts'
        c = '#show_all_alerts'
        toggle_selection(a, current_dog_selection, c, current_dog_button)
        console.log('Current dog selection is now ', current_dog_selection)
    })

    $('#show_vaccines').click(function(){
        a = '#vaccines'
        c = '#show_vaccines'
        toggle_selection(a, current_dog_selection, c, current_dog_button)
        console.log('Current dog selection is now ', current_dog_selection)
    })

    $('#show_preventions').click(function(){
        a = '#preventions'
        c = '#show_preventions'
        toggle_selection(a, current_dog_selection, c, current_dog_button)
        console.log('Current dog selection is now ', current_dog_selection)
    })

    $('#show_tests').click(function(){
        a = '#tests'
        c = '#show_tests'
        toggle_selection(a, current_dog_selection, c, current_dog_button)
        console.log('Current dog selection is now ', current_dog_selection)
    })







    current_cat_selection = '#all_alerts_cat'
    current_cat_button = '#show_all_alerts_cat'
    console.log('Current cat view is', current_cat_selection)

    function toggle_selection_cat(new_selection, existing_selection, new_button, existing_button) {
        $(existing_selection).hide()
        $(new_selection).show()
        $(existing_button).removeClass('btn-gray').addClass('btn-white')
        $(new_button).removeClass('btn-white').addClass('btn-gray')
        current_cat_button = new_button
        current_cat_selection = new_selection
    }

    $('#show_all_cats').click(function(){
        a = '#all_cats'
        c = '#show_all_cats'
        toggle_selection_cat(a, current_cat_selection, c, current_cat_button)
        console.log('Current cat selection is now ', current_cat_selection)
    })

    $('#show_all_alerts_cat').click(function(){
        a = '#all_alerts_cat'
        c = '#show_all_alerts_cat'
        toggle_selection_cat(a, current_cat_selection, c, current_cat_button)
        console.log('Current cat selection is now ', current_cat_selection)
    })

    $('#show_vaccines_cat').click(function(){
        a = '#vaccines_cat'
        c = '#show_vaccines_cat'
        toggle_selection_cat(a, current_cat_selection, c, current_cat_button)
        console.log('Current cat selection is now ', current_cat_selection)
    })

    $('#show_preventions_cat').click(function(){
        a = '#preventions_cat'
        c = '#show_preventions_cat'
        toggle_selection_cat(a, current_cat_selection, c, current_cat_button)
        console.log('Current cat selection is now ', current_cat_selection)
    })

    $('#show_tests_cat').click(function(){
        a = '#tests_cat'
        c = '#show_tests_cat'
        toggle_selection_cat(a, current_cat_selection, c, current_cat_button)
        console.log('Current cat selection is now ', current_cat_selection)
    })

});