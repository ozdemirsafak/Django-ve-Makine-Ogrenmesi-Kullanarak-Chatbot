
const universite =  $("#universite");
universite.change(function(){
    $(".bolum").css({"display":"none"});
    const selectOption = $(this).children('option:selected');
    const bolum = selectOption.attr("data-name");
    $("#"+bolum+"_bolum").css({"display":"block"});
});



