$(document).ready(function() {
  $("[class^=finance_goal]").each(function() {
    $(this).mouseover(function() {
      $(this).addClass("highlight");
    });

    $(this).mouseout(function() {
      $(this).removeClass("highlight");
    });

    var end_val = $(this).find(".goal_end").html();
    $(this).find(".goal_progress").css("width", end_val);
  });
});