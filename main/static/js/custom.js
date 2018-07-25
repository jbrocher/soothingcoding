$(document).ready(function () {
  ModalDetails.init()
  AOS.init()

  $('.fa-angle-down').on('click', function () {

    if ($(this).hasClass('fa-rotate-180')) {

      setTimeout(function () {
        $(window).trigger('resize.px.parallax')
      }, 201)

      setTimeout(function () {
        $('.contact-information').addClass('h-100')
      }, 500)
      $(this).removeClass('fa-rotate-180')
    } else {

      setTimeout(function () {
        $(window).trigger('resize.px.parallax')
      }, 101)
      var height = $('.contact-information').height()

      $('.contact-information').removeClass('h-100')
      var height = $('.contact-information').height(height)

      $(this).addClass('fa-rotate-180')
    }
  })
})
