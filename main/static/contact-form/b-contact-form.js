// using jQuery
function getCookie (name) {
  var cookieValue = null
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(' ')
    console.log(cookies)
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i])
      // Does this cookie string begin with the name we want?
      console.log(cookie)

      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

// this is the id of the form
$(document).ready(function () {
  $('#contactForm').submit(function (e) {
    e.preventDefault() // avoid to execute the actual submit of the form.

    var csrftoken = getCookie('csrftoken')
    var form = $(this)
    var url = form.attr('action') // the script where you handle the form input.
    var data = $('#contactForm').serialize()
    $.ajax({
      type: 'POST',
      url: url,
      headers: {'X-CSRFToken': csrftoken},
      data: data, // serializes the form's elements.
      success: function (data) {
        $('#successModal').modal({
          keyboard: false
        })
      }
    })
  })

  $('.b-contact-form__radio').on('click', function(e){
    e.preventDefault()
    $(this).addClass('b-button--clicked')
    $(this).parent().parent().find('.b-contact-form__radio').removeClass('b-button--clicked')
    $(this).parent().trigger('click')
  })


  $('.b-contact-form__collapse-toggle').on('click', function () {

    if ($(this).hasClass('fa-rotate-180')) {

      $(this).removeClass('fa-rotate-180')
      $('.contact-form').css('height', '600px')

    } else {

      $(this).addClass('fa-rotate-180')
      $('.contact-form').css('height', '100%')

    }
  })

  $('#id_project_desc').on('keydown', function (e){
    if(e.key != "Backspace"){
      $('#contact-form__contact-info').collapse('show')
      if (!$('.b-contact-form__collapse-toggle').hasClass('fa-rotate-180')){
        $('.b-contact-form__collapse-toggle').trigger('click')

      }
    }
  })
})


//activating the tooltips :
$('i').tooltip()
