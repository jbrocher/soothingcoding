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
  $('.contact-form__btn').on('click', function () {
    var relatedInputId = $(this).attr('for')
    $('#' + relatedInputId).prop('checked', true)

  })
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
})
