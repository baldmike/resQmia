$(document).ready(function(){
    
    console.log("resQmia_app is now ready to rock.");
    $('.brand').fadeIn(2000);
    $('.login').fadeIn(2000);

    $('#login_button').click(function(){
        $('.brand').fadeOut(1000);
        $('.login').fadeOut(1000);
    })

    // function theDay() {
    //     var d = new Date(),
    //     months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    //     days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    //     return days[d.getDay()]+'&nbsp &nbsp &nbsp &nbsp &nbsp'+months[d.getMonth()]+' '+d.getDate()+' '+d.getFullYear();
    // }
    
    // function theTime() {
        
    //     var t = new Date(),
    //     minutes = t.getMinutes().toString().length == 1 ? '0' + t.getMinutes() : t.getMinutes(),
    //     hours = hoursTime(),
    //     ampm = t.getHours() >= 12 ? 'pm' : 'am';
    //     hoursTime(hours);

    //     function hoursTime() {
    //         var hour = t.getHours().toString().length == 1 ? '0' + t.getHours() : t.getHours();
    //             if (hour > 12) {
    //                 hour -= 12;
    //             } return hour;
    //     }
        
    //     return hours + ':' + minutes + ampm
    // }

    // function timeOutput() {
    //     document.getElementById('date').innerHTML=theDay();
    //     document.getElementById('time').innerHTML=theTime();
    // }
    // // get the time every 1000 [increments of time which I believe to be milliseconds]
    // setInterval(timeOutput, 1000);

    function newDogName() {
        new_rescue_name = document.getElementById('#new_rescue_name').value;
        console.log(new_rescue_name)
    
        document.getElementById('#current_rescue_name').innerHTML=new_rescue_name;
        return new_rescue_name;
    }
    
    var microchip = $('#microchip')
    microchip.click(function(){
        $('#microchip-number').toggleClass('hidden')
    })

    $("#show_vacs").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#vaccinations").offset().top
        }, 1500);
        var new_rescue_name = $('#new_rescue_name').val()
        $('#current_rescue_name').html(new_rescue_name + "!");
    });

    $("#show_prevs").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#preventions").offset().top
        }, 1400);
    });

    var rabiesVacTrue = $('#rabiesVacTrue')
    rabiesVacTrue.change(function(){
        $('#rabiesVacFalse').toggleClass('rabies-form')
        $('#rabiesVacTrue').toggleClass('rabies-form')
        $('#rabies_number').toggleClass("hidden")
    })

    var rabiesVacFalse = $('#rabiesVacFalse')
    rabiesVacFalse.change(function(){
        $('#rabiesVacFalse').toggleClass('rabies-form')
        $('#rabiesVacTrue').toggleClass('rabies-form')
        $('#rabies_number').toggleClass("hidden")
    })

    var da2ppVacTrue = $('#da2ppVacTrue')
    da2ppVacTrue.change(function(){
        $('#da2ppVacTrue').toggleClass('purple-form')
        $('#da2ppVacFalse').toggleClass('purple-form')
    })

    var da2ppVacFalse = $('#da2ppVacFalse')
    da2ppVacFalse.change(function(){
        $('#da2ppVacFalse').toggleClass('purple-form')
        $('#da2ppVacTrue').toggleClass('purple-form')
    })

    var leptoVacTrue = $('#leptoVacTrue')
    leptoVacTrue.change(function(){
        $('#leptoVacTrue').toggleClass('orange-form')
        $('#leptoVacFalse').toggleClass('orange-form')
    })

    var leptoVacFalse = $('#leptoVacFalse')
    leptoVacFalse.change(function(){
        $('#leptoVacFalse').toggleClass('orange-form')
        $('#leptoVacTrue').toggleClass('orange-form')
    })

    var bordVacTrue = $('#bordVacTrue')
    bordVacTrue.change(function(){
        $('#bordVacTrue').toggleClass('blue-form')
        $('#bordVacFalse').toggleClass('blue-form')
    })

    var bordVacFalse = $('#bordVacFalse')
    bordVacFalse.change(function(){
        $('#bordVacFalse').toggleClass('blue-form')
        $('#bordVacTrue').toggleClass('blue-form')
    })

    var civVacTrue = $('#civVacTrue')
    civVacTrue.change(function(){
        $('#civVacTrue').toggleClass('pink-form')
        $('#civVacFalse').toggleClass('pink-form')
    })

    var civVacFalse = $('#civVacFalse')
    civVacFalse.change(function(){
        $('#civVacFalse').toggleClass('pink-form')
        $('#civVacTrue').toggleClass('pink-form')
    })

    var heartwormPrevTrue = $('#heartwormPrevTrue')
    heartwormPrevTrue.change(function(){
        $('#heartwormPrevTrue').toggleClass('heartworm-prev-form')
        $('#heartwormPrevFalse').toggleClass('heartworm-prev-form')
    })

    var heartwormPrevFalse = $('#heartwormPrevFalse')
    heartwormPrevFalse.change(function(){
        $('#heartwormPrevFalse').toggleClass('heartworm-prev-form')
        $('#heartwormPrevTrue').toggleClass('heartworm-prev-form')
    })

    var fleaPrevTrue = $('#fleaPrevTrue')
    fleaPrevTrue.change(function(){
        $('#fleaPrevTrue').toggleClass('flea-prev-form')
        $('#fleaPrevFalse').toggleClass('flea-prev-form')
    })

    var fleaPrevFalse = $('#fleaPrevFalse')
    fleaPrevFalse.change(function(){
        $('#fleaPrevFalse').toggleClass('flea-prev-form')
        $('#fleaPrevTrue').toggleClass('flea-prev-form')
    })
    
    var heartwormTestTrue = $('#heartwormTestTrue')
    heartwormTestTrue.change(function(){
        $('#heartwormTestTrue').toggleClass('heartworm-test-form')
        $('#heartwormTestFalse').toggleClass('heartworm-test-form')
    })

    var heartwormTestFalse = $('#heartwormTestFalse')
    heartwormTestFalse.change(function(){
        $('#heartwormTestFalse').toggleClass('heartworm-test-form')
        $('#heartwormTestTrue').toggleClass('heartworm-test-form')
    })

    var fecalTestTrue = $('#fecalTestTrue')
    fecalTestTrue.change(function(){
        $('#fecalTestTrue').toggleClass('fecal-test-form')
        $('#fecalTestFalse').toggleClass('fecal-test-form')
    })

    var fecalTestFalse = $('#fecalTestFalse')
    fecalTestFalse.change(function(){
        $('#fecalTestFalse').toggleClass('fecal-test-form')
        $('#fecalTestTrue').toggleClass('fecal-test-form')
    })

    var dewormerTestTrue = $('#dewormerTestTrue')
    dewormerTestTrue.change(function(){
        $('#dewormerTestTrue').toggleClass('dewormer-test-form')
        $('#dewormerTestFalse').toggleClass('dewormer-test-form')
    })

    var dewormerTestFalse = $('#dewormerTestFalse')
    dewormerTestFalse.change(function(){
        $('#dewormerTestFalse').toggleClass('dewormer-test-form')
        $('#dewormerTestTrue').toggleClass('dewormer-test-form')
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

// CAT ONLY BELOW **********************

    var fvrcpVacTrue = $('#fvrcpVacTrue')
    fvrcpVacTrue.change(function(){
        $('#fvrcpVacFalse').toggleClass('fvrcp-form')
        $('#fvrcpVacTrue').toggleClass('fvrcp-form')
    })

    var fvrcpVacFalse = $('#fvrcpVacFalse')
    fvrcpVacFalse.change(function(){
        $('#fvrcpVacFalse').toggleClass('fvrcp-form')
        $('#fvrcpVacTrue').toggleClass('fvrcp-form')
    })

    var fivfelvTestTrue = $('#fivfelvTestTrue')
    fivfelvTestTrue.change(function(){
        $('#fivfelvTestTrue').toggleClass('fivfelv-test-form')
        $('#fivfelvTestFalse').toggleClass('fivfelv-test-form')
    })

    var fivfelvTestFalse = $('#fivfelvTestFalse')
    fivfelvTestFalse.change(function(){
        $('#fivfelvTestFalse').toggleClass('fivfelv-test-form')
        $('#fivfelvTestTrue').toggleClass('fivfelv-test-form')
    })

    var revolutionPrevTrue = $('#revolutionPrevTrue')
    revolutionPrevTrue.change(function(){
        $('#revolutionPrevTrue').toggleClass('revolution-prev-form')
        $('#revolutionPrevFalse').toggleClass('revolution-prev-form')
    })

    var revolutionPrevFalse = $('#revolutionPrevFalse')
    revolutionPrevFalse.change(function(){
        $('#revolutionPrevFalse').toggleClass('revolution-prev-form')
        $('#revolutionPrevTrue').toggleClass('revolution-prev-form')
    })



    function newCatName() {
        new_rescue_name = document.getElementById('#new_rescue_name').value;
        console.log(new_rescue_name)

        document.getElementById('#current_rescue_name').innerHTML=new_rescue_name;
        return new_rescue_name;
    }



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
        console.log('FIX BUTTON FIX')
        $('#fix_box').toggleClass("hidden")
    })

    $('#chip_alert').click(function(){
        console.log('chip BUTTON chip')
        $('#chip_box').toggleClass("hidden")
    })




});