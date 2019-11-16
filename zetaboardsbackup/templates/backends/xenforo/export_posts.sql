INSERT INTO `xf_post` (`post_id`, `thread_id`, `user_id`, `username`, `post_date`, `message`, `ip_id`, `message_state`, `attach_count`, `position`, `likes`, `like_users`, `warning_id`, `warning_message`, `last_edit_date`, `last_edit_user_id`, `edit_count`, `embed_metadata`) VALUES

{% for post in posts %}
({{ post.zeta_id }}, {{ post.thread.zeta_id }}, {{ post.user.zeta_id|default:0 }}, '{{ post.username }}', {{ post.date_posted|date:"U" }}, '{{ post.raw_post_bbcode|linebreaksbr }}', 0, 'visible', 0, 0, 0, 'a:0:{}', 0, '', 0, 0, 0, '[]'){% if not forloop.last %},{% else %};{% endif %}{% endfor %}

