$(document).ready(function() {
        $("[class^=finance_goal]").each(function() {
                $(this).mouseover(function() {
                        $(this).addClass("highlight");
                    });

                $(this).mouseout(function() {
                        $(this).removeClass("highlight");
                    });
                
            });
});