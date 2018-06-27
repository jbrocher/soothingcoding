var ModalDetails = (function () {
  return {
    init: function () {
      $('.modal-details').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var title = button.data('title')
        var list = button.data('list')
        var value = button.data('value')

        var modal = $(this)
        modal.find('.modal-title').text(title)
        modal.find('.modal-details__value').text(value)
        modal.find('.modal-details__tech').text(list.tech)
        modal.find('.modal-details__time').text(list.time)
        modal.find('.modal-details__cost').text(list.cost)

      })
    }
  }

})()
