/* DirectChat()
 * ===============
 * Toggles the state of the control sidebar
 *
 * @Usage: $('#my-chat-box').directChat()
 *         or add [data-widget="direct-chat"] to the trigger
 */
+function ($) {
  'use strict';

  var DataKey = 'lte.directchat';

  var Selector = {
    data: '[data-widget="chat-pane-toggle"]',
    box : '.direct-chat'
  };

  var ClassName = {
    open: 'direct-chat-contacts-open'
  };

  // DirectChat Class Definition
  // ===========================
  var DirectChat = function (element) {
    this.element = element;
  };

  DirectChat.prototype.toggle = function ($trigger) {
    $trigger.parents(Selector.box).first().toggleClass(ClassName.open);
  };

  // Plugin Definition
  // =================
  function Plugin(option) {
    return this.each(function () {
      var $this = $(this);
      var data  = $this.data(DataKey);

      if (!data) {
        $this.data(DataKey, (data = new DirectChat($this)));
      }

      if (typeof option == 'string') data.toggle($this);
    });
  }

  var old = $.fn.directChat;

  $.fn.directChat             = Plugin;
  $.fn.directChat.Constructor = DirectChat;

  // No Conflict Mode
  // ================
  $.fn.directChat.noConflict = function () {
    $.fn.directChat = old;
    return this;
  };

  // DirectChat Data API
  // ===================
  $(document).on('click', Selector.data, function (event) {
    if (event) event.preventDefault();
    Plugin.call($(this), 'toggle');
  });
  var text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
          '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
          '{message}' +
          '</div>';

  function scrolltoend() {
      $('#board').stop().animate({
          scrollTop: $('#board')[0].scrollHeight
      }, 800);
  }

  function send(sender, receiver, message) {
      $.post('/api/messages', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
          console.log(data);
          var box = text_box.replace('{sender}', "You");
          box = box.replace('{message}', message);
          $('#board').append(box);
          scrolltoend();
      })
  }

  function receive() {
      $.get('/api/messages/'+ sender_id + '/' + receiver_id, function (data) {
          console.log(data);
          if (data.length !== 0)
          {
              for(var i=0;i<data.length;i++) {
                  console.log(data[i]);
                  var box = text_box.replace('{sender}', data[i].sender);
                  box = box.replace('{message}', data[i].message);
                  box = box.replace('right', 'left');
                  $('#board').append(box);
                  scrolltoend();
              }
          }
      })
  }

  function register(username, password) {
      $.post('/api/users', '{"username": "'+ username +'", "password": "'+ password +'"}',
          function (data) {
          console.log(data);
          window.location = '/';
          }).fail(function (response) {
              $('#id_username').addClass('invalid');
          })
  }

}(jQuery);
