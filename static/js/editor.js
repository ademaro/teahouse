jQuery(document).ready(function() {
    jQuery("#id_text").wymeditor({ // assuming content is field name with TextField.
        updateSelector: "input:submit", //without this line and next line, you will be able to see editor but content will not be passed through POST.
        updateEvent:    "click"
    });
});
