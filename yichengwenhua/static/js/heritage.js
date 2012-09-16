$("img").bind("load", function () { $(this).fadeIn(); });

$(function() {

$("#tabs").tabs();

$(".section-title").each(function() {
    try {
    $(this).click(function () {
        $(this).next().slideToggle("400", "swing");
    }); 
    }catch(e){}
});

$('#tabs').bind('tabsselect', function(event, ui) {
    var imageArea = $("#image-area");
    if (ui.index == 1 && imageArea.children().length == 0)
        //imageArea.load('get_images');
        
        $.ajax({
           url: 'get_images',
           success: function(data) {
            imageArea.hide();
            imageArea.html(data);
            //$("#image-area img").width(0);
            //$("#image-area img").height(0);
            imageArea.show();
               
            var counter = 0;
            var width = $("#image-area img").width() + 20;
            var offset = 20;
            $("#image-area img").each(function() {
                var leftOffset = counter % 4 * width + offset;
                var topOffset = Math.floor(counter / 4) * width + offset;
                $(this).animate({left: leftOffset, top: topOffset, }, 500, function(){});
              /*$(this).hover(function(){
                $(this).css("z-index", 100);
                $(this).animate({width: 180, height: 180, left: leftOffset-10, top: topOffset-10}, 200, function(){});
              }, function(){
                $(this).css("z-index", 50);
                $(this).animate({width: 160, height: 160, left: leftOffset, top: topOffset}, 200, function(){ $(this).css("z-index", 1); });
              });*/
              counter = counter + 1;
            });
           }
        });
});

$('.kwicks').kwicks({
    max : 200,
    spacing : 2,
    isVertical: true,
    //sticky: true
});
    
// Process the links to videos
$('#video-panel a').each(function() {
    try {
    var ref = $(this).attr("href");
    $(this).click(function () {
        $('#video-window').html('<embed src="' + ref + '" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>');
        $('#video-panel a').removeClass("video-selected");
        $(this).addClass("video-selected");
        $("#video-left-panel p").html("视频："+$(this).html());
    }); 
    $(this).attr("href", "javascript:;");
    }catch(e){}
});

if ($('#video-panel a').length == 0)
    $("#video-panel").html("<p>很抱歉，目前没有相关视频。</p>");

});